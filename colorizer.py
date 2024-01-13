# Modules
import numpy
import cv2
import os


# Colorize function
def colorize_image(image_path):
    mod_pro = r"model/colorizer/colorization_deploy_v2.prototxt"
    mod_pts = r"model/colorizer/pts_in_hull.npy"
    mod_caf = r"model/colorizer/colorization_release_v2.caffemodel"

    # Load the Model
    net = cv2.dnn.readNetFromCaffe(mod_pro, mod_caf)
    pts = numpy.load(mod_pts)

    # Load centers for ab channel quantization used for re-balancing.
    class8 = net.getLayerId("class8_ab")
    conv8 = net.getLayerId("conv8_313_rh")
    pts = pts.transpose().reshape(2, 313, 1, 1)
    net.getLayer(class8).blobs = [pts.astype("float32")]
    net.getLayer(conv8).blobs = [numpy.full([1, 313], 2.606, dtype="float32")]

    # Load the input image
    image = cv2.imread(image_path)
    scaled = image.astype("float32") / 255.0
    lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)

    # Resize
    resized = cv2.resize(lab, (224, 224))
    cap_l = cv2.split(resized)[0]
    cap_l -= 50

    # Colorize
    net.setInput(cv2.dnn.blobFromImage(cap_l))
    ab = net.forward()[0, :, :, :].transpose((1, 2, 0))
    ab = cv2.resize(ab, (image.shape[1], image.shape[0]))
    cap_l = cv2.split(lab)[0]
    colorized = numpy.concatenate((cap_l[:, :, numpy.newaxis], ab), axis=2)
    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
    colorized = numpy.clip(colorized, 0, 1)
    colorized = (255 * colorized).astype("uint8")
    cv2.waitKey(0)

    # Output
    file_name, file_extension = os.path.splitext(os.path.split(image_path)[1])
    output_path = os.path.split(image_path)[0] + "/" + file_name + "_ProPixel_AI_Col" + file_extension
    cv2.imwrite(output_path, colorized)

    return output_path

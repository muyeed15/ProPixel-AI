# Modules
import cv2
import numpy
import os
import onnxruntime


# Remove background
def remove_background(image_path):
    # Model
    model_path = r"model/remover/isnet-general-use.onnx"

    # Output
    file_name, file_extension = os.path.splitext(os.path.split(image_path)[1])
    output_path = os.path.split(image_path)[0] + "/" + file_name + "_ProPixel_AI_RmBg" + ".png"

    # Load image
    original_image = cv2.imread(image_path)

    # Resize image to match the model input size
    input_size = (1024, 1024)
    image = cv2.resize(original_image, input_size)

    # Normalize image
    image = image / 255.0
    image = image.astype(numpy.float32)

    # Load the U-2-Net model using onnxruntime
    session = onnxruntime.InferenceSession(model_path)

    # Prepare input tensor
    input_name = session.get_inputs()[0].name
    input_data = numpy.expand_dims(image.transpose(2, 0, 1), axis=0)

    # Run inference
    output_name = session.get_outputs()[0].name
    result = session.run([output_name], {input_name: input_data})[0][0][0]

    # Threshold the result to get a binary mask
    mask = (result > 0.5).astype(numpy.uint8)

    # Resize mask to original image size
    mask = cv2.resize(mask, (original_image.shape[1], original_image.shape[0]))

    # Create an alpha channel with the mask
    alpha_channel = numpy.ones_like(mask) * 255

    # Merge the original image with the alpha channel
    result_image = cv2.merge([original_image, alpha_channel[:, :, numpy.newaxis]])

    # Apply the mask to the alpha channel
    result_image[:, :, 3] = mask * 255

    # Save the result with transparency
    cv2.imwrite(output_path, result_image)

    return output_path

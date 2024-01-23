# Remove background
def remove_background(image_path):
    # Modules
    import cv2
    import numpy
    import os
    import onnxruntime


    # Config folder
    if os.path.exists("config") == False:
        os.makedirs("config")
    
    # Model
    model_path = r"model/remover/isnet-general-use.onnx"

    # Output
    file_name, file_extension = os.path.splitext(os.path.split(image_path)[1])
    output_path = os.path.split(image_path)[0] + "/" + file_name + "_ProPixel_AI_RemBG" + ".png"

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

    # Add feather effect to the edges
    try:
        ed_data = int(open(r"config/edge.ini", "r").read())
        if ed_data not in [1, 2, 3]:
            ed_data = 2
    except:
        open(r"config/edge.ini", "w").write(str(2))
        ed_data = 2
    
    # Ensure it is a positive odd number    
    if ed_data == 1:
        feather_amount = 1
    elif ed_data == 2:
        feather_amount = 17
    elif ed_data == 3:
        feather_amount = 35
    
    result_image[:, :, 3] = cv2.GaussianBlur(result_image[:, :, 3], (feather_amount, feather_amount), 0)

    # Save the result with transparency
    cv2.imwrite(output_path, result_image)

    return output_path

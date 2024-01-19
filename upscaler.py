# Modules
import torch
from PIL import Image
from RealESRGAN import RealESRGAN
import os
import shutil


# Upscale function
def upscale_image(image_path):
    # Config folder
    if os.path.exists("config") == False:
        os.makedirs("config")
    
    # Create cache folder
    os.makedirs("cache")

    def resize_image(input_path):
        # Open the image file
        original_image = Image.open(input_path)

        # Get the original width and height
        original_width, original_height = original_image.size

        # Calculate the new dimensions while preserving the original aspect ratio
        max_pixels = 512
        ratio = min(max_pixels / original_width, max_pixels / original_height)
        new_width = int(original_width * ratio)
        new_height = int(original_height * ratio)

        # Resize the image
        resized_image = original_image.resize((new_width, new_height))

        # Save the resized image
        resized_image.save(fr"cache/{os.path.split(image_path)[1]}")
        
        return original_width, original_height


    or_w, or_h = resize_image(image_path)

    # CUDA check
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Scale details
    try:
        up_data = int(open(r"config/upscale.ini", "r").read())
        if up_data not in [2, 4]:
            up_data = 4
    except:
        open(r"config/upscale.ini", "w").write(str(4))
        up_data = 4
    
    model = RealESRGAN(device, scale=int(up_data))
    model.load_weights(fr"model/upscaler/RealESRGAN_x{up_data}.pth", download=False)

    # Path
    path_to_image = fr"cache/{os.path.split(image_path)[1]}"
    image = Image.open(path_to_image).convert("RGB")

    # Output
    sr_image = model.predict(image)
    sr_image = sr_image.resize((or_w*up_data, or_h*up_data))
    file_name, file_extension = os.path.splitext(os.path.split(image_path)[1])
    output_path = os.path.split(image_path)[0] + "/" + file_name + fr"_ProPixel_AI_UpScl_{up_data}x" + file_extension
    sr_image.save(output_path)

    # Remove cache folder
    try:
        shutil.rmtree("cache")
    except: pass

    return output_path

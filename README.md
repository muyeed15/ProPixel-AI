![ProPixel-AI_Git_2000](https://github.com/muyeed15/ProPixel-AI/assets/101888493/39a687d3-e601-441f-b99f-e74ea7bb58de)

# ProPixel AI

ProPixel AI is a Python-based image processing tool for Microsoft Windows that offers three powerful features: Background Removal, Image Colorization, and Image Upscaling. The tool leverages state-of-the-art deep learning models for each functionality.

## Download executable file
[![Download Brightness Control](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/propixel-ai/files/latest/download)

## Features

### 1. Remove Background
ProPixel AI uses the Dichotomous Image Segmentation (DIS) model by xuebinqin to accurately remove backgrounds from images.

![Old_Man_RemBG_SL](https://github.com/muyeed15/ProPixel-AI/assets/101888493/b4fb5f16-b72e-4d6f-814b-4ddf1840f772)
![Bird_RemBG_SL](https://github.com/muyeed15/ProPixel-AI/assets/101888493/008789dc-6d25-4cdf-9fca-6175e58de1b0)

### 2. Colorize Image
ProPixel AI utilizes the Colorful Image Colorization Model by richzhang to add vibrant colors to black and white images.

![Boy_Colorize_SL](https://github.com/muyeed15/ProPixel-AI/assets/101888493/ae4aebb6-a732-48d4-9c79-f87ee9d54140)
![Boat_Colorize_SL](https://github.com/muyeed15/ProPixel-AI/assets/101888493/a15e8060-2468-48bf-bc16-80c4a74db51b)

### 3. Upscale Image
The tool employs the Real-ESRGAN model by Xintao to upscale low-resolution images while preserving details.

![Girl_Upscl_SL](https://github.com/muyeed15/ProPixel-AI/assets/101888493/a81e1a57-3459-4f8c-821d-2f56296973fc)
![Structure_Upscl_SL](https://github.com/muyeed15/ProPixel-AI/assets/101888493/1d435d6e-95b6-4c17-8e74-f4339397c35e)


## Getting Started

### System Requirements
- Microsoft Windows
- Python 3.11

### Installation
```bash
pip install tk, customtkinter, pillow, requests, hdpitkinter, numpy, opencv-python, onnxruntime, torch
```

```bash
pip install git+https://github.com/sberbank-ai/Real-ESRGAN.git
```

### Download Models
You must download the models from the provided links, and you'll find these links in the respective directories within the model folders. Place the downloaded files in their corresponding directories.

### Usage
```bash
python main.py
```

## Acknowledgments
- [xuebinqin](https://github.com/xuebinqin/DIS)
- [richzhang](https://github.com/richzhang/colorization/tree/caffe)
- [Xintao](https://github.com/xinntao/Real-ESRGAN)
- [ai-forever](https://github.com/ai-forever/Real-ESRGAN)
- [TomSchimansky](https://github.com/TomSchimansky/CustomTkinter)

## License
This project is licensed under the "Creative Commons Zero v1.0 Universal" - see the [LICENSE.md](https://github.com/muyeed15/ProPixel-AI/blob/main/LICENSE) file for details.

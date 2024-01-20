![ProPixel-AI_Git_2000](https://github.com/muyeed15/ProPixel-AI/assets/101888493/39a687d3-e601-441f-b99f-e74ea7bb58de)

# ProPixel AI

ProPixel AI is a Python-based image processing tool for Windows OS that offers three powerful features: Background Removal, Image Colorization, and Image Upscaling. The tool leverages state-of-the-art deep learning models for each functionality.

## Features

### 1. Remove Background
ProPixel AI uses the Dichotomous Image Segmentation (DIS) model by xuebinqin to accurately remove backgrounds from images.

![Old Man - Before and After](https://github.com/muyeed15/ProPixel-AI/assets/101888493/92a1e5e7-7bb6-4f01-bc4a-7b7b09f03cef)
![Bird - Before and After](https://github.com/muyeed15/ProPixel-AI/assets/101888493/a6118cd9-944b-40b6-aa70-649ff9b073cb)

### 2. Colorize Image
ProPixel AI utilizes the Colorful Image Colorization Model by richzhang to add vibrant colors to black and white images.

![Boy - Colorized](https://github.com/muyeed15/ProPixel-AI/assets/101888493/a4483771-8889-48e4-a7e3-e80686603dfa)
![Boat - Colorized](https://github.com/muyeed15/ProPixel-AI/assets/101888493/f03bd848-2206-48e9-9fb6-a1424176c534)

### 3. Upscale Image
The tool employs the Real-ESRGAN model by Xintao to upscale low-resolution images while preserving details.

![Girl - Upscaled](https://github.com/muyeed15/ProPixel-AI/assets/101888493/be36bcf2-4969-4fc2-b25a-678fafedaad1)
![Structure - Upscaled](https://github.com/muyeed15/ProPixel-AI/assets/101888493/d9537e3e-895b-40f2-add1-926af3736741)

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

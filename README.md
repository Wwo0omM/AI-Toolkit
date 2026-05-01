[English](README.md) | [Русский](README.ru.md)
# AI Toolkit (Blender Add-on)

AI Toolkit is a Blender add-on that allows you to generate 3D models and images using AI via Hugging Face Spaces.

## Features

- Generate 3D models from an image (Hunyuan3D)
  - Automatic import into the Blender viewport
  - Saves the model to the desktop
- Generate images from a text prompt (FLUX)
  - Adjustable image resolution
- Partial support for multiple APIs / models
- Built-in access to a manual

## How It Works

The add-on connects to Hugging Face Spaces via API:

- **Hunyuan3D** generates a 3D model from an input image  
- **FLUX** generates an image from a text prompt  

Image generation requires a Hugging Face API token.

## Installation

1. Download the add-on (.zip)
2. Open Blender
3. Go to: `Edit → Preferences → Add-ons → Install`
4. Select the `.zip` file
5. Enable the add-on

## Requirements

- Blender 4.0+
- Internet connection
- Hugging Face API token (for image generation)

## Usage

### 3D Model Generation

1. Add an input image
2. Select a model (if available)
3. Click `Generate`
4. Wait for the result (about 3–10 minutes)

Result:
- The model is automatically imported into Blender
- The model is also saved to the desktop

### Image Generation

1. Enter a text prompt
2. Set the resolution
3. Enter your Hugging Face API token
4. Click `Generate Image`

Result:
- The image is saved to the desktop

Generation time: about 1–2 minutes

## Limitations

- Generation may take time
- Some features are still in development
- Image-to-image generation (FLUX) is not working
- Depends on the availability of Hugging Face Spaces

## Possible Future Features

- Texture generation based on UV maps
- Improved material workflow
- Expanded model support

## Manual

The add-on includes an `Open Manual` button  
(online documentation, domain not set yet)

## License

MIT License

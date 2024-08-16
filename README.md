# Houne Tools Blender Addon

Houne Tools is a Blender addon that allows users to generate and execute Python scripts directly from the 3D Viewport based on text prompts.

## Features

- Generate Python scripts for Blender using natural language prompts.
- Execute scripts directly within Blender's 3D Viewport.
- Simple and intuitive UI.

## Ollama API Integration

This addon uses the [Ollama](https://ollama.com) API to generate Python scripts. We use the `llama3.1` model by default, which is designed for general-purpose language tasks, including generating code.

### Improving Results

While the `llama3.1` model provides good results, you may see better script generation and more accurate responses by using a more advanced model from Ollama. If you have access to a larger model, such as `llama4.0` or any other more advanced version, we recommend switching to it in the `generate_blender_script` function for improved results.

## Installation

1. Download the repository as a ZIP file.
2. Open Blender, go to `Edit > Preferences > Add-ons`.
3. Click `Install` and select the downloaded ZIP file.
4. Activate the addon by checking the box next to "Houne Tools".

## Usage

1. Open the 3D Viewport in Blender.
2. Press `N` to open the sidebar.
3. Navigate to the "HouneTools" tab.
4. Enter your prompt in the text box and click "Generate".
5. The generated script will be executed automatically.


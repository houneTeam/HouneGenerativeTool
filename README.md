# Houne Generative Tool

Houne Generative Tool — это аддон для Blender, который позволяет пользователям генерировать и выполнять Python-скрипты прямо из 3D Viewport на основе текстовых подсказок.

![Houne Tools](https://github.com/houneTeam/HouneGenerativeTool/blob/main/image.png)

## Особенности

- Генерация Python-скриптов для Blender с использованием естественных языковых подсказок.
- Выполнение скриптов непосредственно в 3D Viewport Blender.
- Простой и интуитивно понятный интерфейс.

## Интеграция Ollama API

Этот аддон использует [Ollama](https://ollama.com) API для генерации Python-скриптов. Мы используем модель `llama3.1` по умолчанию, которая разработана для общих языковых задач, включая генерацию кода.

### Улучшение Результатов

Хотя модель `llama3.1` обеспечивает хорошие результаты, вы можете получить более точные ответы и улучшить генерацию скриптов, используя более продвинутую модель от Ollama. Если у вас есть доступ к более продвинутой модели, такой как `llama4.0` или любой другой версии, мы рекомендуем переключиться на неё в функции `generate_blender_script` для улучшения результатов.

## Установка

1. Скачайте и установите Ollama с официального сайта: [Ollama Download](https://ollama.com/download).
2. После установки загрузите необходимую модель, выполнив команду: `ollama run llama3.1` в терминале.
3. Найдите исполняемый файл Python, используемый Blender, обычно он находится по пути `\3.6\python\bin\python.exe`.
4. Используйте этот исполняемый файл Python для установки всех необходимых библиотек. Откройте командную строку или терминал, перейдите в каталог Python для Blender и выполните следующую команду:
'python.exe -m pip install ollama'
5. Скачайте этот репозиторий как ZIP-файл.
6. Откройте Blender, перейдите в `Edit > Preferences > Add-ons`.
7. Нажмите `Install` и выберите загруженный ZIP-файл.
8. Активируйте аддон, отметив галочкой "Houne Tools".

## Использование

1. Откройте 3D Viewport в Blender.
2. Нажмите `N`, чтобы открыть боковую панель.
3. Перейдите на вкладку "HouneTools".
4. Введите ваш запрос в текстовое поле и нажмите "Generate".
5. Сгенерированный скрипт будет выполнен автоматически.


========================================

# Houne Generative Tool

Houne Generative Tool is a Blender addon that allows users to generate and execute Python scripts directly from the 3D Viewport based on text prompts.

![Houne Tools](https://github.com/houneTeam/HouneGenerativeTool/blob/main/image.png)

## Features

- Generate Python scripts for Blender using natural language prompts.
- Execute scripts directly within Blender's 3D Viewport.
- Simple and intuitive UI.

## Ollama API Integration

This addon uses the [Ollama](https://ollama.com) API to generate Python scripts. We use the `llama3.1` model by default, which is designed for general-purpose language tasks, including generating code.

### Improving Results

While the `llama3.1` model provides good results, you may see better script generation and more accurate responses by using a more advanced model from Ollama. If you have access to a larger model, such as `llama4.0` or any other more advanced version, we recommend switching to it in the `generate_blender_script` function for improved results.

## Installation

1. Download and install Ollama from the official website: [Ollama Download](https://ollama.com/download).
2. After installation, download the required model by running the command: `ollama run llama3.1` in the terminal.
3. Locate the Python executable used by Blender, typically found at `\3.6\python\bin\python.exe`.
4. Use this Python executable to install all the necessary libraries. Open a command prompt or terminal and navigate to the Blender Python 
'python.exe -m pip install ollama'
5. Download this repository as a ZIP file.
6. Open Blender, go to `Edit > Preferences > Add-ons`.
7. Click `Install` and select the downloaded ZIP file.
8. Activate the addon by checking the box next to "Houne Tools".

## Usage

1. Open the 3D Viewport in Blender.
2. Press `N` to open the sidebar.
3. Navigate to the "HouneTools" tab.
4. Enter your prompt in the text box and click "Generate".
5. The generated script will be executed automatically.


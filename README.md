# python-text-2-voice

A simple Python script that converts text to speech using the Siri voices available on macOS. This tool is designed to easily generate spoken messages for use in the Home Assistant app on your phone.

## Table of Contents
1. [Overview](#overview)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Pixi](#pixi)
6. [Author](#author)
7. [License](#license)

## Overview

This script allows you to convert any text to speech using macOS’s built-in Siri voices. You can save the spoken message as a WAV file, which can then be used in applications like Home Assistant for notifications or alerts.

The script works in two modes:
1. **Voice Selection Mode**: Allows you to choose a voice from the available Siri voices, and save that choice into a configuration file for future use.
2. **Text to Speech Mode**: Reads the voice from the config file and converts any entered text into speech. If no voice is selected, it will ask you to select one first.

### Features
- Uses macOS's `say` command for generating speech
- Converts AIFF files to WAV for cross-compatibility
- Automatically creates the output folder if it doesn't exist
- Plays the resulting audio file for quick feedback

## Requirements

- macOS (this script utilizes the `say` command, available on macOS)
- Python 3.x
- [Pixi](https://docs.pixi.sh/) for environment management

## Installation

To run this script, you need to have `pixi` set up. Follow these steps:

1. Install `pixi` by following their [installation guide](https://docs.pixi.sh/installation).

2. Once `pixi` is installed, navigate to the project folder and initialize the environment:

   ```bash
   pixi run speak
   ```

3. `pixi` will automatically install the necessary dependencies, like `pydub`, using the provided `pixi.toml` file.

## Usage

1. **Choosing a Voice**
   First, you need to choose a Siri voice that the script will use. To do this, run the script and select from the available voices:

   ```bash
   pixi run speak
   ```

   The script will display a list of available voices on your system. Choose one, and it will be saved for future use in a configuration file.

2. **Converting Text to Speech**
   Once you have a voice configured, you can enter the text you want spoken. The script will use the preselected voice and create a WAV file of the spoken message. This file will be saved in the `audio-files` folder.

   If the folder does not exist, it will be created automatically.

3. **Playing the Audio**
   After generating the WAV file, the script will automatically play the audio so you can verify that everything works as expected.

## Pixi

Pixi is a minimal environment manager, similar to Conda, that ensures your project dependencies and environment are consistent across platforms.

In this project, the `pixi.toml` file is used to define the project setup, including:

- The project name, version, and description.
- Dependencies (e.g., `pydub`) that the script requires.
- Task definitions, such as `speak`, which is the command that runs the Python script.

To get started with `pixi`, make sure you have it installed. Then, simply use the `pixi run` command to execute tasks:

```bash
pixi run speak
```

This command will install dependencies if necessary and run the `speak.py` script.

## Author

**Theo van der Sluijs**
Email: theo@vandersluijs.nl
Resume: [theovandersluijs.nl](https://theovandersluijs.nl)
Website: [itheo.tech](https://itheo.tech)
Hire me for your next gig!

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

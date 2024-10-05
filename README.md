# Voice Assistant 

## Overview
This project implements a voice-activated assistant called "Jarvis" that can answer questions, manage a to-do list, play YouTube videos, and open files using voice commands. It leverages various libraries to handle audio input, web scraping, text-to-speech, and speech recognition, providing a comprehensive interface for user interaction.

## Features
- **Voice Commands**: Responds to voice commands for various tasks, including web searches and file management.
- **To-Do List Management**: Allows users to add, remove, and view tasks in a to-do list.
- **YouTube Integration**: Plays videos directly on YouTube based on user requests.
- **Text-to-Speech**: Converts text responses into speech using Google's Text-to-Speech API.
- **Speech Recognition**: Recognizes spoken commands using the SpeechRecognition library.
- **Audio Recording**: Records audio input for processing commands.

## Requirements
- Python 3.x
- Required libraries:
  - `requests`
  - `beautifulsoup4`
  - `pywhatkit`
  - `pygame`
  - `gtts`
  - `sounddevice`
  - `wavio`
  - `numpy`
  - `SpeechRecognition`

Install the required libraries using pip:

```bash
pip install requests beautifulsoup4 pywhatkit pygame gtts sounddevice wavio numpy SpeechRecognition
```

## How It Works
1. **Wake Word Detection**: The assistant listens for the wake word "Jarvis" to activate.
2. **Command Processing**: Once activated, it listens for voice commands that can include:
   - Playing a song or video on YouTube.
   - Managing a to-do list (add/remove tasks).
   - Opening files.
   - Fetching information from the web.
3. **Text-to-Speech Response**: After processing a command, it provides auditory feedback using text-to-speech.
4. **To-Do List Management**: Users can interact with their to-do list via voice commands.

## Recording and Recognizing Speech
- The program records audio for a specified duration and saves it as a WAV file.
- It then recognizes the speech from the recorded file and extracts the command.

## Main Function
To start the assistant, run the script. The program will prompt you to input the device ID of your microphone.

```bash
python voice_assistant.py
```

### Microphone Selection
When you run this code, it will display all available microphones. Choose your microphone and enter its number (e.g., `0`, `1`, etc.) to ensure the assistant uses the correct input device.

## Extracting Zipped Files
The project has been compressed using **7-Zip** into parts, each of 10 MB size, as shown in the image (e.g., `ai.zip.001`, `ai.zip.002`, etc.). To extract the files from these multiple parts after downloading them from GitHub, follow these steps:

1. **Download all parts**: Ensure you have downloaded all parts (e.g., `ai.zip.001`, `ai.zip.002`, and so on) from the GitHub repository.

2. **Install 7-Zip**: If you don't already have it, download and install 7-Zip from [here](https://www.7-zip.org/).

3. **Extract the files**:
   - Right-click on the first part (`ai.zip.001`).
   - Select **7-Zip > Extract Here** or **Extract to "ai.zip/"** (if you want to extract the contents into a separate folder).
   - 7-Zip will automatically combine all parts and extract the files.

4. **Move the Extracted Files**: After extracting the files:
   - **Cut and paste** the extracted `ai` folder into the **Virtual Keyboard** project folder, the one that contains the `.main` file. This ensures that the virtual keyboard can correctly access the extracted files and run smoothly.

## Note
Make sure your microphone is properly configured and the device ID is correctly set when starting the program to ensure optimal performance.

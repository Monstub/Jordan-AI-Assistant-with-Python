# Jordan-AI-Assistant-with-Python

## Introduction

Jordan is an AI Assistant built using Python, which can perform various tasks such as playing YouTube videos, opening applications, telling the time, providing Wikipedia summaries, telling jokes, and performing Google searches. The assistant uses speech recognition to take voice commands and responds accordingly.

## Features

- **Play YouTube Videos**: Command Jordan to play a song or video on YouTube.
- **Open Applications**: Open applications like Notepad or Chrome.
- **Tell Time**: Get the current time.
- **Wikipedia Summaries**: Get a brief summary of a topic from Wikipedia.
- **Tell Jokes**: Listen to a random joke.
- **Google Search**: Perform a Google search with a given query.

## How It Works

1. **Speech Recognition**: Listens for voice commands using the microphone.
2. **Voice Processing**: Uses Google's speech recognition to process commands.
3. **Command Execution**: Executes the command based on the recognized speech.
4. **Text-to-Speech**: Responds using a text-to-speech engine to talk back.

## Prerequisites

- Python 3.x
- Libraries: `speech_recognition`, `pyttsx3`, `pywhatkit`, `datetime`, `wikipedia`, `pyjokes`

## Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/Monstub/Jordan-AI-Assistant-with-Python.git
   ```
2. **Navigate to the Project Directory**:
   ```sh
   cd Jordan-AI-Assistant-with-Python
   ```
3. **Install the Required Libraries**:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Assistant

1. **Run the Python Script**:
   ```sh
   python main.py
   ```
2. **Start Giving Commands**: Use the keyword "Jordan" in your commands to trigger the assistant. For example:
   - "Jordan play Despacito on YouTube"
   - "Jordan open the application Notepad"
   - "Jordan tell me the time"
   - "Jordan tell me about Python"
   - "Jordan tell me a joke"
   - "Jordan search for AI assistants on Google"

## Example Commands

- **Play a Song on YouTube**:
  ```
  Jordan play Shape of You on YouTube
  ```
- **Open Notepad**:
  ```
  Jordan open the application Notepad
  ```
- **Get Current Time**:
  ```
  Jordan what is the time
  ```
- **Get Wikipedia Summary**:
  ```
  Jordan tell me about Albert Einstein
  ```
- **Tell a Joke**:
  ```
  Jordan tell me a joke
  ```
- **Perform a Google Search**:
  ```
  Jordan search for Python tutorials on Google
  ```

## Tips for Using the Assistant

- Ensure your microphone is working properly.
- Speak clearly and at a moderate pace for better recognition.
- Make sure you have an active internet connection for speech recognition and Wikipedia summaries.
- Adjust the `voice` property in the `pyttsx3` engine setup if you want a different voice.

## Feedback

I appreciate your feedback! If you encounter any issues or have suggestions for improvements, please create an issue in the project repository. Your input helps me to make Jordan better for everyone.

# voyc

### Voyc Chatbot

#### Description

The Voyc Chatbot is an advanced voice-controlled chatbot that leverages real-time speech recognition and OpenAI's GPT-3.5 to deliver interactive conversational experiences. It utilizes a WebSocket connection to stream audio data for transcription, generates responses with GPT-3.5, and converts these responses to speech. This project is ideal for applications requiring hands-free interaction and natural language processing capabilities.

#### Key Features

- **Real-time Speech Recognition**: Utilizes AssemblyAI's WebSocket API for real-time speech-to-text conversion.
- **AI-Driven Responses**: Integrates with OpenAI's GPT-3.5 for generating contextual and coherent responses based on user input.
- **Text-to-Speech Conversion**: Converts the chatbot's responses back to speech using the ElevenLabs API.
- **Interactive Audio Feedback**: Plays the generated speech audio to the user and waits for further input.
- **Thread Management**: Uses multi-threading to handle real-time data streaming and processing.

#### Dependencies

The project requires the following dependencies:
- `pyaudio`
- `numpy`
- `websocket-client`
- `requests`
- `pygame`
- `sounddevice`
- `openai`
- `assemblyai`

#### Configuration

Set your API keys and other configurations in the `CONFIG` dictionary within the script:
```python
CONFIG = {
    "ASSEMBLY_API_KEY": "your_assembly_api_key",
    "OPENAI_KEY": "your_openai_key",
    "ELEVENLABS_API_KEY": "your_elevenlabs_api_key",
    "FRAMES_PER_BUFFER": 3200,
    "DTYPE": np.int16,
    "CHANNELS": 1,
    "SAMPLE_RATE": 16000,
    "OUTPUT_RATE": 44100
}
```

#### How It Works

1. **Configuration**: API keys and other settings are configured in the `CONFIG` dictionary.
2. **WebSocket Connection**: Establishes a WebSocket connection with AssemblyAI's real-time transcription service.
3. **Audio Streaming**: Captures audio using PyAudio and streams it to the WebSocket server.
4. **Message Handling**: Processes incoming messages from the WebSocket, extracting transcribed text and generating responses using GPT-3.5.
5. **Response Playback**: Converts the GPT-3.5 response to audio and plays it back to the user.
6. **Graceful Shutdown**: Handles SIGINT for a clean shutdown of the WebSocket connection and stops all threads.

#### Example Usage

To start the chatbot, simply run the following command:
```sh
python voyc_chatbot.py
```
This will initiate the chatbot, which will listen for audio input, transcribe it, generate a response, and play the response back to you.

#### Detailed Script Explanation

1. **Imports and Configurations**: The script begins by importing necessary libraries and setting up configuration parameters, including API keys and audio settings.
2. **Audio Stream Setup**: Initializes PyAudio for capturing audio input.
3. **WebSocket Handlers**: Defines functions for handling WebSocket messages (`on_message`), sending audio data (`send_data`), and managing the WebSocket connection (`on_open`).
4. **GPT-3.5 Response Generation**: Implements the function `get_chatgpt_response` to communicate with the OpenAI API and generate responses based on transcribed text.
5. **Text-to-Speech Conversion**: Uses the `text_to_speech` function to convert text responses to audio and plays the audio using `pygame`.
6. **Root Mean Square (RMS) Calculation**: Calculates RMS to measure audio volume.
7. **Main Execution**: Sets up the WebSocket connection, starts the audio stream, and handles graceful shutdown on interrupt signals.

#### Future Enhancements

- Support for additional languages and dialects.
- Improved error handling and reconnection logic for WebSocket communication.
- Customizable voice options for text-to-speech conversion.

This project demonstrates the integration of several powerful APIs to create an interactive voice-controlled chatbot, leveraging real-time audio streaming and advanced natural language processing to provide an engaging user experience.

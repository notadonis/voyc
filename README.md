# Real-Time Voice Assistant with ChatGPT, AssemblyAI, and ElevenLabs

This project is a real-time voice assistant that transcribes your speech, processes it using OpenAI's ChatGPT, and responds back using ElevenLabs' text-to-speech service. It leverages AssemblyAI for real-time speech recognition and provides an interactive conversational experience.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **Real-Time Speech Recognition**: Uses AssemblyAI's WebSocket API to transcribe speech in real-time.
- **Conversational AI**: Integrates with OpenAI's GPT-3.5 Turbo model for generating responses.
- **Text-to-Speech**: Converts the AI's text responses into speech using ElevenLabs' API.
- **Audio Playback**: Plays the generated audio responses directly through your speakers.

## Prerequisites

- **Python 3.7 or higher**
- **Microphone**: For capturing real-time audio input.
- **Speakers**: For audio output.
- **API Keys**: You'll need API keys for the following services:
  - [AssemblyAI API Key](https://www.assemblyai.com/)
  - [OpenAI API Key](https://platform.openai.com/)
  - [ElevenLabs API Key](https://elevenlabs.io/)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your_username/your_repository.git
   cd your_repository
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**

   Install the dependencies listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

   **Note**: If you don't have a `requirements.txt`, you can install the packages individually:

   ```bash
   pip install json websocket-client pyaudio numpy openai requests pygame sounddevice
   ```

   **Additional Dependencies for Windows Users**:

   - **PyAudio**: You may need to install PyAudio using a precompiled binary. Download the appropriate `.whl` file from [PyAudio Downloads](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it using:

     ```bash
     pip install PyAudio‑<version>‑cp37‑cp37m‑win_amd64.whl
     ```

## Configuration

1. **Set Your API Keys**

   Open the script file and locate the `CONFIG` dictionary. Replace the empty strings with your API keys:

   ```python
   CONFIG = {
       "ASSEMBLY_API_KEY": "your_assemblyai_api_key",
       "OPENAI_KEY": "your_openai_api_key",
       "ELEVENLABS_API_KEY": "your_elevenlabs_api_key",
       "FRAMES_PER_BUFFER": 3200,
       "DTYPE": np.int16,
       "CHANNELS": 1,
       "SAMPLE_RATE": 16000,
       "OUTPUT_RATE": 44100
   }
   ```

2. **Set Voice ID for ElevenLabs**

   Replace the `VOICE_ID` in the `text_to_speech` function with the voice ID you wish to use from ElevenLabs:

   ```python
   VOICE_ID = 'your_elevenlabs_voice_id'
   ```

   You can find available voice IDs in your ElevenLabs account dashboard.

## Usage

1. **Run the Script**

   ```bash
   python your_script_name.py
   ```

2. **Interact with the Assistant**

   - The assistant will start listening automatically.
   - Speak into your microphone; your speech will be transcribed and sent to ChatGPT.
   - The AI's response will be converted to speech and played back to you.
   - The assistant waits for 5 seconds before listening again.

3. **Terminate the Program**

   - Press `Ctrl + C` to safely terminate the program.

## Limitations

- **API Rate Limits**: Be mindful of the rate limits imposed by AssemblyAI, OpenAI, and ElevenLabs.
- **Audio Latency**: There might be slight delays in processing due to network latency.
- **Error Handling**: The script includes basic error handling but may need enhancements for production use.
- **Platform Compatibility**: Tested primarily on Unix-based systems. Windows users may need additional configuration.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature/YourFeature
   ```

3. Commit your changes:

   ```bash
   git commit -m "Add your message"
   ```

4. Push to the branch:

   ```bash
   git push origin feature/YourFeature
   ```

5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **[AssemblyAI](https://www.assemblyai.com/)** for real-time speech recognition.
- **[OpenAI](https://www.openai.com/)** for the GPT-3.5 Turbo model.
- **[ElevenLabs](https://elevenlabs.io/)** for text-to-speech synthesis.
- **Python Libraries**:
  - `pyaudio` and `sounddevice` for audio input/output.
  - `pygame` for audio playback.
  - `websocket-client` for WebSocket communication.

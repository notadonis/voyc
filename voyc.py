import json
from websocket import WebSocketApp
import pyaudio
import numpy as np
import base64
from threading import Thread
import openai
import requests
import os
import struct
import math
import time
import signal
import sys
import sounddevice as sd

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

# API Keys and Configurations
CONFIG = {
    "ASSEMBLY_API_KEY": "",
    "OPENAI_KEY": "",
    "ELEVENLABS_API_KEY": "",
    "FRAMES_PER_BUFFER": 3200,
    "DTYPE": np.int16,
    "CHANNELS": 1,
    "SAMPLE_RATE": 16000,
    "OUTPUT_RATE": 44100
}

file_counter = 0
p = pyaudio.PyAudio()
stream = p.open(
   format=pyaudio.paInt16,
   channels=CONFIG['CHANNELS'],
   rate=CONFIG['SAMPLE_RATE'],
   input=True,
   frames_per_buffer=CONFIG['FRAMES_PER_BUFFER']
)
  # To increment filenames

def on_message(ws, message):
    global current_text
    transcript = json.loads(message)
    if transcript.get('message_type') == 'SessionBegins':
        return
    if 'text' in transcript:
        if transcript["message_type"] == "FinalTranscript":
            print(f"You: {transcript['text']}")
            current_text = transcript['text']
            response = get_chatgpt_response(current_text)
            print(f"GPT-3: {response}")
            audio = text_to_speech(response)
            time.sleep(5)  # Wait for 5 seconds before listening again
            print("Listening...")  # Prompt the user that it's time for their next input

def get_chatgpt_response(prompt):
    openai.api_key = CONFIG['OPENAI_KEY']
    chat_payload = [{"role": "user", "content": prompt}]
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_payload,
            max_tokens=4000
        )
        
        chat_response = response.choices[0].message['content'] if response.choices else ""
        print(f"GPT-3 Response: {chat_response}")
        return chat_response
    except Exception as e:
        print(f"Error occurred: {e}")
        return ""

import pygame

def text_to_speech(text):
    global file_counter
    VOICE_ID = 'yquIuEryzO11cSxHoOyy'
    headers = {
        "accept": "audio/mpeg",
        "xi-api-key": CONFIG['ELEVENLABS_API_KEY'],
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.5}
    }
    response = requests.post(f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}", headers=headers, json=data)
    
    # Save the audio data to a file with an incremented filename
    audio_filename = f"audio_output_{file_counter}.mp3"
    with open(audio_filename, 'wb') as audio_file:
        audio_file.write(response.content)
    
    # Play the saved audio using pygame
    pygame.mixer.init()
    pygame.mixer.music.load(audio_filename)
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    print("Audio saved to:", audio_filename)
    file_counter += 1  # Increment the file counter
    
def calculate_rms(data):
    '''Calculate Root Mean Square (RMS) which is a measure of volume.'''
    count = len(data)/2
    format = "%dh"%(count)
    shorts = struct.unpack(format, data)
    sum_squares = 0.0
    for sample in shorts:
        n = sample * (1.0/32768)
        sum_squares += n*n
    return math.sqrt(sum_squares / count)

global response_received
response_received = False

def send_data():
    global file_counter, response_received
    while not ws.sock or not ws.sock.connected:
        time.sleep(1)
    print("Listening...")
    while ws.sock.connected:
        data = stream.read(CONFIG['FRAMES_PER_BUFFER'])
        sd.wait()
        data = base64.b64encode(data).decode("utf-8")
        json_data = json.dumps({"audio_data": str(data)})

        if not ws.sock or not ws.sock.connected:
            print("WebSocket connection is closed.")
            return

        ws.send(json_data)

        # Introduce a delay only after a response has been received
        if response_received:
            time.sleep(3)
            response_received = False
    print("\nConnection closed.")

def on_open(ws):
    Thread(target=send_data).start()

# Set up the WebSocket connection
auth_header = {"Authorization": CONFIG['ASSEMBLY_API_KEY']}
ws = WebSocketApp(
    f"wss://api.assemblyai.com/v2/realtime/ws?sample_rate={CONFIG['SAMPLE_RATE']}",
    header=auth_header,
    on_message=on_message,
    on_open=on_open
)

# Graceful shutdown
def signal_handler(signum, frame):
    print("Closing WebSocket and stopping threads...")
    ws.close()  # Close the WebSocket connection
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

ws.run_forever()

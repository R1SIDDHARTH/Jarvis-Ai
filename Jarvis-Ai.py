import requests
from bs4 import BeautifulSoup
import pywhatkit
import webbrowser
import os
import tempfile
from gtts import gTTS
import pygame
import sounddevice as sd
import wavio
import numpy as np
import speech_recognition as sr

# Initialize pygame mixer
pygame.mixer.init()

# To-Do List
to_do_list = []

# Fetch Web Answer
def fetch_web_answer(query):
    search_url = f"https://www.google.com/search?q={query}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        answer = soup.find('div', {'class': 'BNeawe'}).text
    except AttributeError:
        answer = "Sorry, I couldn't find an answer to that question."
    return answer

# Play YouTube Video
def play_youtube_video(query):
    speak_text(f"Playing {query} on YouTube.")
    pywhatkit.playonyt(query)

# Open YouTube Home
def open_youtube_home():
    speak_text("Opening YouTube home page.")
    webbrowser.open("https://www.youtube.com")

# Open File
def open_file(file_path):
    try:
        os.startfile(file_path)
        speak_text(f"Opening file: {file_path}")
    except FileNotFoundError:
        speak_text(f"File not found: {file_path}")
    except Exception as e:
        speak_text(f"Error opening file: {str(e)}")

# Text-to-Speech
def speak_text(text):
    tts = gTTS(text=text, lang='en')
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
        temp_filename = fp.name
        tts.save(temp_filename)
    pygame.mixer.music.load(temp_filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.music.unload()
    os.remove(temp_filename)

# To-Do List Management
def add_to_do(task):
    to_do_list.append(task)
    speak_text(f"Added to your to-do list: {task}")

def remove_to_do(task):
    global to_do_list
    to_do_list = [item for item in to_do_list if item.lower() != task.lower()]
    speak_text(f"Removed from your to-do list: {task}")

def show_to_do_list():
    if not to_do_list:
        speak_text("Your to-do list is empty.")
    else:
        tasks = "\n".join([f"{i+1}. {task}" for i, task in enumerate(to_do_list)])
        speak_text("Your to-do list:")
        print(tasks)
        speak_text(tasks)

# Chatbot Response
def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    if 'play' in user_input and ('song' in user_input or 'video' in user_input):
        query = user_input.replace('play', '').replace('song', '').replace('video', '').strip()
        play_youtube_video(query)
    elif 'open my to do list' in user_input:
        speak_text("You can add or remove tasks now. Say 'add to do' or 'remove to do'.")
        while True:
            command = listen_for_command().strip().lower()
            if 'add' in command:
                task = command.replace('add', '').strip()
                add_to_do(task)
            elif 'remove' in command:
                task = command.replace('remove', '').strip()
                remove_to_do(task)
            elif 'done' in command or 'exit' in command:
                speak_text("Finished managing your to-do list.")
                break
    elif 'what is my to do list' in user_input:
        show_to_do_list()
    elif 'open youtube home' in user_input:
        open_youtube_home()
    elif 'open' in user_input and 'file' in user_input:
        file_path = user_input.replace('open', '').replace('file', '').strip()
        open_file(file_path)
    else:
        answer = fetch_web_answer(user_input)
        speak_text(answer)
        print(answer)

# Audio Recording and Speech Recognition
def record_audio(duration=5, fs=44100, device=None):
    print("Recording audio...")

    # Explicitly specify device, use default if None
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype=np.int16, device=device)
    sd.wait()  # Wait until recording is finished
    return audio

def save_audio(audio, filename, fs=44100):
    wavio.write(filename, audio, fs, sampwidth=2)

def recognize_speech_from_file(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        return command
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

def listen_for_command(duration=5, device=None):
    audio = record_audio(duration, device=device)
    temp_filename = "temp.wav"
    save_audio(audio, temp_filename)
    command = recognize_speech_from_file(temp_filename)
    os.remove(temp_filename)
    return command

# Wake Word Detection and Main Loop
def listen_for_wake_word(device=None):
    print("Say 'Jarvis' to wake up.")
    while True:
        command = listen_for_command(device=device)
        if "jarvis" in command:
            print("Wake word detected!")
            speak_text("How can I assist you?")
            listen_for_commands(device=device)

def listen_for_commands(device=None):
    while True:
        command = listen_for_command(device=device)
        if command:
            if "jarvis" in command:
                command = command.replace("jarvis", "").strip()  # Ensure command is without wake word
                if command in ['exit', 'quit', 'bye', "that's all"]:
                    speak_text("Goodbye!")
                    break
                chatbot_response(command)
                speak_text("Say 'Jarvis' to wake up.")

# Main Function
def main():
    # Query available audio devices
    print(sd.query_devices())

    # Set device ID if needed (use index of your input device)
    device_id = int(input("Please enter the device ID for the microphone: "))

    listen_for_wake_word(device=device_id)

if __name__ == "__main__":
    main()

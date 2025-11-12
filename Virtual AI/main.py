import datetime
import time
import pyttsx3
import speech_recognition as sr
import webbrowser
import pyautogui
import os
import sys
import json
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import random
import numpy as np
import psutil

def initialize_engine():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume+0.25)
    return engine

def speak(text):
    engine = initialize_engine()
    engine.say(text)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening..." ,end="" ,flush=True)
        r.pause_threshold = 1.0
        r.phrase_threshold = 0.3
        r.sample_rate = 48000
        r.dynamic_energy_threshold = True
        r.operation_timeout = 5
        r.non_speaking_duration = 0.5
        r.dynamic_energy_adjustment = 2
        r.energy_threshold = 4000
        r.phrase_time_limit = 10
        #print(sr.Microphone.list_microphone_names())
        audio = r.listen(source)
    try:
        print("\r", end="", flush=True)
        print("Recognizing...\n", end="", flush=True)
        query = r.recognize_google(audio, language='en-in')
        print(f"{query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def cal_day():
    day = datetime.datetime.today().weekday() + 1
    day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    return day_dict.get(day, '')

def wishme():
    hour = int(datetime.datetime.now().hour)
    t = time.strftime("%I:%M %p")
    day = cal_day()

    if hour < 12:
        greet = "Good Morning"
    elif hour < 18:
        greet = "Good Afternoon"
    else:
        greet = "Good Evening"

    speak(f"{greet} Sir! Today is {day} and the time is {t}")

def social_media(command):
    if 'open facebook' in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com/")
    elif 'open instagram' in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com/")
    elif 'open discord' in command:
        speak("Opening Discord")
        webbrowser.open("https://discord.com/")
    elif 'open gmail' in command:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com/")
    elif 'open linkedin' in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com/")
    elif 'open chatgpt' in command:
        speak("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com/")
    else:
        speak("Social media platform not recognized.")

def openApp(command):
        if "calculator" in command:
            speak("Opening Calculator")
            os.startfile('C:\\Windows\\System32\\calc.exe')
        elif "notepad" in command:
            speak("Opening Notepad")
            os.startfile('C:\\Windows\\System32\\notepad.exe')
        elif "whatsapp" in command:
            speak("Opening WhatsApp")
            os.startfile('C:\\Users\\piyus\\AppData\\Local\\WhatsApp\\WhatsApp.exe')
        elif "chrome" in command:
            speak("Opening Google Chrome")
            os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
        elif "microsoft store" in command:
            speak("Opening Microsoft Store")
            os.startfile('C:\\Program Files\\WindowsApps\\Microsoft.WindowsStore_22110.1401.4.0_x64__8wekyb3d8bbwe\\WinStore.App.exe')
        else :
            speak("Application not recognized.")

def condition():
    usage =str(psutil.cpu_percent())
    speak(f"CPU is at {usage} percentage.")
    battery = psutil.sensors_battery()
    percentage = battery.percent
    speak(f"Sir, Battery is at {percentage} percentage.")

    if percentage >=75:
        speak("We have enough battery to continue our work.")
    elif percentage >=40 and percentage <75:
        speak("We should consider charging the system soon.")
    elif percentage >=15 and percentage <40:
        speak("We need to charge the system now.")
    elif percentage <7:
        speak("Sir, I should take sleep now.Will Meet in a while after charging.")

def closeApp(command):
    if "calculator" in command:
        speak("Closing Calculator")
        os.system("taskkill /f /im calc.exe")
    elif "notepad" in command:
        speak("Closing Notepad")
        os.system("taskkill /f /im notepad.exe")
    elif "whatsapp" in command:
        speak("Closing WhatsApp")
        os.system("taskkill /f /im WhatsApp.exe")
    elif "chrome" in command:
        speak("Closing Google Chrome")
        os.system("taskkill /f /im chrome.exe")
    elif "microsoft store" in command:
        speak("Closing Microsoft Store")
        os.system("taskkill /f /im WinStore.App.exe")

def browsing(query):
    if "open google" in query:
        speak("What should I search on Google?")
        s = command().lower()
        speak(f"Searching {s} on Google")
        webbrowser.open(f"https://www.google.com/search?q={s}")
    elif "open youtube" in query:
        speak("What should I play on Youtube?")
        s = command().lower()
        speak(f"Playing {s} on Youtube")
        webbrowser.open(f"https://www.youtube.com/results?search_query={s}")

def schedule():
    day = cal_day().lower()
    speak(f"Fetching schedule for {day}")
    week = {
        "monday": "9 AM to 10 AM: Mathematics, 10 AM to 11 AM: Physics, 11 AM to 12 PM: Chemistry",
        "tuesday": "9 AM to 10 AM: English, 10 AM to 11 AM: Computer Science, 11 AM to 12 PM: Physical Education",
        "wednesday": "9 AM to 10 AM: Biology, 10 AM to 11 AM: History, 11 AM to 12 PM: Geography",
        "thursday": "9 AM to 10 AM: Economics, 10 AM to 11 AM: Political Science, 11 AM to 12 PM: Sociology",
        "friday": "9 AM to 10 AM: Art, 10 AM to 11 AM: Music, 11 AM to 12 PM: Drama",
        "saturday": "No classes scheduled. Enjoy your weekend!",
        }
    if day in week.keys():
        speak(week[day])

if __name__ == "__main__":
    wishme()

    while True:
        query = command().lower()
        #query = input("Enter your command: ")
        if ( 'open facebook' in query) or ( 'open instagram' in query) or ( 'open discord' in query) or ( 'open gmail' in query) or ( 'open linkedin' in query) or ('open chatgpt' in query) or ('open whatsapp' in query):
            social_media(query)
        elif ("University Time Table" in query) or ("schedule" in query):
            schedule()
        elif ("volume up" in query) or ("increase volume" in query):
            pyautogui.press("volumeup")
            speak("Volume Increased")
        elif ("volume down" in query) or ("decrease volume" in query):
            pyautogui.press("volumedown")
            speak("Volume Decreased")
        elif ("mute" in query) or ("volume mute" in query):
            pyautogui.press("volumemute")
            speak("Volume Muted")
        elif ("open notepad" in query) or ("open calculator" in query) or ("open whatsapp" in query) or ("open chrome" in query) or ("open microsoft store" in query):
            openApp(query)
        elif ("close notepad" in query) or ("close calculator" in query) or ("close whatsapp" in query) or ("close chrome" in query) or ("close microsoft store" in query):
            closeApp(query)
        elif("what" in query) or ("who" in query) or ("how" in query) or ("hi" in query) or ("thanks" in query) or ("hello" in query) or ("Is anyone there" in query) or ("hey" in query) or ("good day" in query) or ("namaste" in query):
            # Load intents data from JSON file
            with open("intents.json", "r") as file:
                data = json.load(file)
            # Load the trained model
            model = load_model('chat_model.h5')
            # load tokenizer object
            with open('tokenizer.pkl', 'rb') as f:
                tokenizer = pickle.load(f)
            padded_sequences = pad_sequences(tokenizer.texts_to_sequences([query]), maxlen=20, truncating='post')
            result = model.predict(padded_sequences)
            # load label encoder object
            with open('label_encoder.pkl', 'rb') as encoder_file:
                label_encoder = pickle.load(encoder_file)
            tag = label_encoder.inverse_transform([np.argmax(result)])

            for i in data['intents']:
                if i['tag'] == tag:
                    speak(np.random.choice(i['responses']))
        elif ("open google" in query) or ("youtube" in query):
            browsing(query)
        elif ("system condition" in query) or ("condition of system" in query):
            speak("Checking the system condition")
            condition()
        elif 'exit' in query or 'quit' in query or 'stop' in query:
            speak("Taking a leave. Have a nice day sir!")
            sys.exit()
import speech_recognition as sr
import pyttsx3
import pyautogui
import threading
import state

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def process_command(cmd):
    cmd = cmd.lower()

    if "jarvis" in cmd:
        state.assistant_active = True
        speak("Hello boss")

    elif "stop" in cmd:
        state.assistant_active = False
        speak("Stopped")

    elif "click" in cmd:
        pyautogui.click()

    elif "right click" in cmd:
        pyautogui.rightClick()

    elif "double click" in cmd:
        pyautogui.doubleClick()

    elif "scroll up" in cmd:
        pyautogui.scroll(100)

    elif "scroll down" in cmd:
        pyautogui.scroll(-100)

    elif "open" in cmd:
        app = cmd.replace("open", "").strip()
        speak(f"Opening {app}")
        pyautogui.press("win")
        pyautogui.write(app)
        pyautogui.press("enter")

def voice_loop():
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)

            while True:
                audio = recognizer.listen(source)
                cmd = recognizer.recognize_google(audio)
                print("Voice:", cmd)
                process_command(cmd)

    except:
        print("⚠️ Mic not working → switching to TEXT mode")
        while True:
            cmd = input("Type command: ")
            process_command(cmd)

def start_voice():
    threading.Thread(target=voice_loop, daemon=True).start()
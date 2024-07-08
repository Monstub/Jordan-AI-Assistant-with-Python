import speech_recognition as sr
import os
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jordan' in command:
                command = command.replace('jordan', '')
                print(command)
    except:
        pass
    return command
def run_jordan():
    command = take_command()
    print(command)

    if "on youtube" in command:
        song = command.replace("on youtube", "")
        talk('playing ' + song + 'on youtube')
        pywhatkit.playonyt(song)

    elif "open the application" in command:
        app_name = command.replace("open the application", "").strip()
        if app_name == "notepad":
            os.startfile("notepad.exe")
        elif app_name == "chrome":
            os.startfile("chrome.exe")

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('sorry, I have a headache')


    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif "on google" in command:
        query = command.replace("on google", "")
        pywhatkit.search(query)

    else:
        talk('Please say the command again.')

while True:
    run_jordan()
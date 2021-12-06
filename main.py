import datetime
import time
import webbrowser
from random import random

import requests
import speech_recognition as sr
import pyttsx3
from secondfile import *
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play

r = sr.Recognizer()
name = ''


def say(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


rooms = ['admin room', 'hall', 'bedroom']


def takeVoiceInputFromUser():
    try:
        with sr.Microphone() as source2:
            print('Listening')
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print("Did you say " + MyText)
            # say(MyText)
            return MyText
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")


def wishme():
    timeHour = datetime.datetime.now().hour
    if 0 <= timeHour < 12:
        say(' good morning')
    if 12 <= timeHour < 4:
        say('good afternoon')
    if 4 <= timeHour <= 23:
        say('good evening')


def checkRoom(command):
    for a in rooms:

        if a in command:
            print(a)
            print('returning true by check room')
            return True
    print('returning FaLSE by check room')
    return False


while True:
    json = requests.get('http://mac.j/s/1/').json()
    command = json['command']
    command = str(command).lower()
    is_executed = json['is_executed']

    if command != '' and is_executed == False:
        print('i am inside the command ')
        data = {
    "command": " a",
    "is_executed": True
}
        print(requests.put('http://mac.j/s/1/', data=data))
        if command == 'good morning' or command == 'good afternoon' or command == 'good evening':
            wishme()

        elif command == 'good night':
            say('good night, i will turn off all lights')
            turnOffAdminRoomLights()

        elif 'light on' in command or 'lights on' in command:
            turnOnAdminRoomLights()

        elif 'light off' in command or 'lights off' in command and checkRoom(command):
            if 'hall' in command:
                print(' hall lights off')
            if 'admin room' in command:
                print('admin room lights off')
            if 'bedroom' in command:
                print('bedroom lights off')
        # else:
        #     print('i am inside lights off else condition')
        #     ASkWhichRoomlightoff()  # which light should bee off?

        elif 'open youtube' in command:
            print("opening youtube")
            webbrowser.open_new_tab("https://www.youtube.com")
            say("youtube is open now")
            time.sleep(5)
        elif 'open google' in command:
            webbrowser.open_new_tab("https://www.google.com")
            say("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in command:
            webbrowser.open_new_tab("gmail.com")
            say("Google Mail open now")
            time.sleep(5)
        elif 'time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"the time is {strTime}")

        elif 'news' in command:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            say('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)
        elif 'search' in command:
            command = command.replace("search", "")
            webbrowser.open_new_tab(command)
            time.sleep(5)
        elif 'date' in command:
            say(datetime.date.today())
        elif 'love' in command:
            a = ["lorry nikaathhuuu", "dai , una pathi therium daa ", "serrraa dai "]
            print(len(a))

            b = (random.randint(0, len(a) - 1))
            print(b)
            result = a[b]
            print(result)
            say(result)



        else:
            say('sorry i cant understad'+command)
            print(command)

    # break

# No, in Ask all lights should be offed function

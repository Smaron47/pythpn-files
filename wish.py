import pyttsx3
import datetime 
from os import system as c



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[10].id)
k=engine.getProperty('rate')
volume = engine.getProperty('volume')
engine.setProperty('rate',170)
engine.setProperty('volume',3.5)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    date= datetime.datetime.today().strftime("%A")
    time= datetime.datetime.now().hour
    time2=datetime.datetime.now().minute

    if hour>=0 and hour<12:
        speak(f"Good Morning Sir. Sir today is {date}. Now it\'s {time} o\'clock {time2}")

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon Sir. Sir today is {date}. Now it\'s {time} o\'clock {time2}")
    elif hour>=18 and hour < 22:
        speak(f"Good Evening Sir. today is {date}. It\'s {time} o\'clock {time2}")
    else:
        speak(f"Good Night Sir. Sir today is {date}. It\'s {time} o\'clock {time2}")
'''
def tc():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listing....')
        r.pause_threshold = 1
        audio = r.listen(source)
        q=r.recognize_google(audio, language='en-in')

        print(f' you said {q}')

'''
speak("WELCOME")
wishMe()
c('google-chrome')

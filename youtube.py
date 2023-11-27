import requests
import webbrowser
import speech_recognition as sr  
import pyautogui as pg
import pyttsx3
import datetime 
import os

date= datetime.datetime.today().strftime("%A")


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 110)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 494
        r.adjust_for_ambient_noise(source, duration=1.5)
        audio = r.listen(source)

    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language='en-bd')
        print(f'User said: {query}\n')

    except Exception as e:
        print(e)

        print('Say that again please...')
        return 'None'
    return query



    
while True:
    s=takeCommand().lower()
    print(s)
    if 'hi friday' in s:
        speak('hello sir. how are u today?')
    if 'open fcebook' in s:
        webbrowser.open('https://www.facebook.com')



    elif (('friday play song') or ('friday play something') or ('friday play a song')) in s:
         speak("which song do you want to play")
         s=takeCommand().lower()
         s.replace('play','')
         s.replace(' ','+')
         r=requests.get(f"https://www.youtube.com/results?search_query={s}").text
         k=r.find('watch?v=')
         l=requests.get(f'https://www.youtube.com/{r[k:k+19]}').text
         webbrowser.open(f'https://www.youtube.com/{r[k:k+19]}')
    elif 'break' in s:
        break
    elif 'next song' in s:
        os.system("taskkill /im MicrosoftEdgeCP.exe /f")
        k=l.find('watch?v=')
        webbrowser.open(f'https://www.youtube.com/{l[k:k+19]}')
    elif 'volume up' in s:
        
        pg.hotkey('fn','f8')
    elif 'stop song' in s:
        pg.hotkey('fn','f9')
    elif 'shutdown' in s:
        os.system('shutdown -p')
    elif 'type for me' in s:
        speak('sir what should i type??')
        while True:
            j=takeCommand().lower()
            print(j)
            pg.typewrite(j)
            if 'break' in j:
                break
    elif (('friday whats the time') or ('what time is it') or ('what is the time') or ('tell me the time')) in s:
        
        speak(f"sir it's {datetime.datetime.now().hour} o'clock {datetime.datetime.now().minute}")
    elif (('friday what is the day') or ('tell me the day name') or ('what is the day')) in s:
        print(date)
        speak(date)

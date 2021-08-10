import pyttsx3
import datetime
import os
import speech_recognition as sr
import sys
import shutil
import cv2
import numpy as np
import random
from requests import  get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib


# initialisation

# testing
# engine.say("welcome to sonu AI PLATEFORM")
# engine.say("Thank you , FOR  VIGITING")
# engine.runAndWait()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)




#convert  text into voices
def speak(audio):
    engine.say(audio)
    # print(audio)
    engine.runAndWait()

#wish
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")
        print("Good Morning Sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")
        print("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")
        print("Good Evening Sir !")

    speak("I am your Assistant")
    speak("What should i call you sir")
    uname = takeCommand()
    speak(f"Welcome Mister {uname}")
    # speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you Sir")

    print("I am your assistant. please tell me  how can i help you")


#convert voice into text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=4,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        print("Unable to Recognize your voice.")
        speak("Say that again please....")
        return "None"

    return query
def sandEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('7781988982sonu@gmail.com','passawad')
    server.sendmail('1900950100079@coet.in',to,content)
    server.close()




if __name__== '__main__':
    # wishMe()
    while True:
        query = takeCommand().lower()
        #logic bullding for  tasks
        if "open notepad" in query:
            npath ="C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
        elif "open camera" in query:
            # Capturing video
            cap = cv2.VideoCapture(0)

            while True:

                ret, img = cap.read()  # Ret returns whether it's true or false
                cv2.imshow('webcam', img)

                if (cv2.waitKey(1) & 0xff) == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
        elif "play music" in query:
            music_dir ="F:\\videos\\TubeMateVidmate\\music"
            songs = os.listdir(music_dir)#if you want to play music random than install random module
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))#songs[1]

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")
        elif "wikipedia" in query:
            speak("searching wikipedia......")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)
        elif "open youtub" in query:
            webbrowser.open("www.youtube.com")
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
        elif "open chrome" in query:
            webbrowser.open("www.chrome.com")
        elif "open linkedln" in query:
            webbrowser.open("www.linkedln.com")
        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
        elif "send message" in query:
            kit.sendwhatmsg("+919651724313","hello",17,42)
        # elif "play song on YouTube" in query:
        #     kit.playonyt("hindi song")
        elif "email to sonu" in query:
            try:
                speak("what should i say ?")
                content = takeCommand().lower()
                to = "1900950100079@coet.in"
                sandEmail(to,content)
                speak("Email has been sent to sonu")

            except Exception as e:
                print(e)
        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()

        speak("sir,do you have any other work")







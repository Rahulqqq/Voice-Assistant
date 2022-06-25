import pyttsx3 
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import pywhatkit     # to playing something like music,video
import wolframalpha  #to calculate strings into formula
import requests
import re            # for open websites

#from gtts import gTTS     # google text to speech 

import os        # to save/open files 
from selenium import webdriver       #to control browser operations





# chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'

# webbrowser.open('https://www.google.co.in/')


engine = pyttsx3.init('sapi5') 

'''get voices'''

voices = engine.getProperty('voices') 

engine.setProperty('voice', voices[0].id)


# audio argument 

def speak(audio):
    engine.say(audio)

    engine.runAndWait() 

    '''runAndwait is a function'''


def wishme():

    hour = int(datetime.datetime.now().hour)
    

    if hour >=0 and hour<12:

        speak("Good Morning")
    

    elif hour>=12 and hour<=18:

        speak("Good Afternoon")


    else:

        speak("Good Evening")


    speak(" I am william how can i help you ")


#it takes microphone input from the user return string output

def takecommand():

    #it takes microphone input from the user return string output


    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        r.pause_threshold = 1

        audio = r.listen(source)

    try:

       print("Recognizing...")

       query = r.recognize_google(audio, language="en-US")

       print(f"user said: {query}\n")


    except Exception as e:

        #print(e) # forprint Error

        print("say that again please... sir")      #its optional if you want to comment out 

        speak("say that again please... sir")

        return "None"

    return query





if __name__ =="__main__":
    wishme()

    while(1):            #if you want continue n time write: while True
        

        query=takecommand().lower()
        

        if query==0:
            continue
            

        if "close" in query:

            speak("Ok bye and take care")

            break


        # logic for executiing based on query

        if 'wikipedia' in query:

            speak('searching wikipedia...')

            query = query.replace("wikipedia", "")

            results = wikipedia.summary(query, sentences=2)

            speak("According to wikipedia")

            #print(results)

            speak(results)  



         # just say search and william search everything for you
        elif 'search'  in query:

            query = query.replace("search", "")

            webbrowser.open_new_tab (query)
        
        

        elif 'open youtube' in query:

            webbrowser.open("https://www.youtube.com/")



        elif 'opengoogle' in query:

            webbrowser.open("https://www.google.com/")





        elif  'time' in query:

            strTime = datetime.datetime.now().strftime("%H:%M:%S")

            speak(f"sir, the time is{strTime}")


            
        elif 'who are you' in query:

            speak("I am william,sir")


    
        elif 'thank you'in query:

            speak("welcome sir, any work for me sir"  )


        elif 'what are you doing ' in query:

            speak('i am updating ')


        
        elif 'play' in query:

            song = query.replace('play', '')

            speak('playing' + song)

            pywhatkit.playonyt(song)


        # elif "calculate"   in query: 

        #     question=takecommand()

        #     app_id="8RP37W-HAW4LWJE74"
          


        #     client = wolframalpha.Client(app_id)

        #     res = client.query(takecommand)

        #     answer = next(res.results).query 
        #     speak("The answer is " + answer)



        # for open websites 
        # elif 'open' in query:
        #     reg=re.search('open (.+)', query)
        #     if reg:
        #         domain = reg.group(1)
        #         print(domain)
        #         url = 'https://www.' + domain 
        #         webbrowser.open(url)
        #         speak('The website you have requested has been opened for you Sir.')
        #     else:
        #         pass
                
            
    
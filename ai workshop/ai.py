import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wiki
import pyautogui
import json
import requests
import openai
import pywhatkit as kit
import smtplib
import sample
import os


headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiY2U2YzAxNjktNTY3ZS00NzFjLTg1ZjctMzBjZjE2NzY3MDZiIiwidHlwZSI6ImFwaV90b2tlbiJ9.__qNaVZd1yMZQd904DEnf9_39nJ30nyHbeXc6vRAkRU"}

url = "https://api.edenai.run/v2/text/chat"
payload = {
    "providers": "openai",
    "text": "Tell me my name",
    "chatbot_global_action": "Act as an assistant",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "Anjali"
}
x=pyttsx3.init()
def youtube(elem):
    kit.playonyt(elem)
    
def chrome(elem1):
    kit.search(elem1)
    
def whatsapp(t,msg):
    kit.sendwhatmsg_instantly(t,msg)
    
def sendemail(to,msg):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('anjalikadali05@gmail.com','vzxe cmny nedf upsj')
    server.sendmail('anjalikadali05@gmail.com',to,msg)
    server.close()

def talktoai(query):
    payload["text"]=query
    #print(payload)
    response = requests.post(url, json=payload, headers=headers)
    #print(response.text)
    result=json.loads(response.text)
    speak(result['openai']['generated_text'])


def speak(audio):
    x.say(audio)
    x.runAndWait()
# speak("Hi I am Itachi AI How can i help you")
def time():
    t=datetime.datetime.now().strftime("%H:%M:%S")
    # print(t)
    speak(t)
# time()
def date():
    y=str(datetime.datetime.now().year)
    m=str(datetime.datetime.now().month)
    d=str(datetime.datetime.now().day)
    speak(d)
    speak(m)
    speak(y)
    # print(y)
# date()
def wish():
    h = datetime.datetime.now().hour
    if h<12:
        speak("Good Morning ")
    elif h>=12 and h<=18:
        speak("Good Afternoon ")
    elif h>18 and h<=21:
        speak("Good Evening")
    else:
        speak("Good Night ")
    speak("How can i help you today")
# str=input()
# wish()
def inp():
    x1 = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        x1.pause_threshold=1
        audio=x1.listen(source)
        try:
            print("Recognizing...")
            query = x1.recognize_google(audio,language='en-in')
            print(query)
        except Exception as e:
            print(e)
            speak("Can you repeat again")
            inp()
            return "None"
        return query
# inp()
def screenshot():
    im1=pyautogui.screenshot()
    im1.save("C:/Users/anjal/OneDrive/Desktop/ai workshop/img.png")
    
if __name__=="__main__":
    wish()
    while True:
        query=inp().lower()
        # query=input()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("iam ssummaarizing the wikipedia search")
            query=query.replace("wikipedia", "")
            result= wiki.summary(query,sentences=2)
            print(result)
            speak(result)
        elif "screenshot" in query:
            speak("iam taking screenshot of the screen")
            screenshot()
        elif "open YouTube" in query:
            speak("what you want to browse?")
            elem=inp()
            speak("opening Youtube")
            youtube(elem)
            #exit()
        elif "Chrome" in query:
            speak("what you want to search?")
            elem1=inp()
            speak("Browsing")
            chrome(elem1)
        elif "Whatsapp" in query:
            try:
                speak("input recepient as text")
                t=input()
                speak("say msg to send")
                msg=inp()
                whatsapp(t,msg)
            except Exception as e:
                print(e)
                speak("Failed to send")
            
        elif "remember"  in query:
            speak("What should i remember sir?")
            data=inp()
            speak("You said me that"+data)
            remember=open('data.txt','w')   
            remember.write(data)
            remember.close()  
        elif "play song" in query:
            song_path=input("enter song path:")
            sample.play_song(song_path)
        elif "pause the song" in query:
            sample.control("pause")
        elif "unpause" in query:
            sample.control("unpause")
        elif "play" in query:
            try:
                sample.play_song(song_path)
            except:
                print("please say play a song")
        elif "stop" in query:
            sample.control("stop")
        elif "any data" in query:
            remember=open('data.txt','r')
            speak("you said that"+remember.read())
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "send email" in query:
            try:
                speak("What msg u want to send?")
                msg=inp()
                speak("please enter sender email")
                to=input()
                sendemail(to,msg)
                speak("Successfully")
            except Exception as e:
                print(e)
                speak("Fail to send")
        elif "exit" in query:
            speak("Exiting")
            print("bye bye")
            exit()
        else:
            talktoai(query)
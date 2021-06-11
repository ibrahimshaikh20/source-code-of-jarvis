from platform import platform, python_revision
from urllib.request import URLopener
import pyttsx3
import pywhatkit
import instaloader
import speech_recognition as sr
import datetime
import ctypes
import os
import winshell
import json
from urllib.request import urlopen
from requests import get
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import webbrowser as web
import json
import sys
import wikipedia
import random
import wolframalpha
import webbrowser
import pyautogui
import keyboard
import pyjokes
import operator
import requests
from googletrans import Translator
from bs4 import BeautifulSoup
import requests
import time
import smtplib
import turtle
import AMP
from playsound import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[5].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! Sir")


    elif hour>=12 and hour<18:
        speak("Good Afternoon! Sir")

    else:
        speak("Good Evening Sir")



def takecommand():

     r = sr.Recognizer()
     with sr.Microphone() as source:
         print("Listening....")
         r.pause_threshold = 0.8
         audio = r.listen(source)

     try:
         print("Recognizing....")
         query = r.recognize_google(audio, language='en-in')
         print(f"user said: {query}\n")

     except Exception as e:
         print("say that again sir")
         return "None"
     return query


def TaskExecution():
    wishMe()

    def Music():

        speak("Tell me the name of the song sir")
        musicName = takecommand()
        
        if 'Dura' in musicName:
            os.startfile('C:\\music\\Dura.mp3')

        elif 'Faded' in musicName:
            os.statfile('C:\\music\\Faded.mp3') 

        else:
            pywhatkit.playonyt(musicName)

        speak("your song has been started, Enjoy sir")            

    def News():
        speak("Sir , please tell me the name of the Channel")
        channelName = takecommand()

        if 'Aaj Tak' in channelName:
            webbrowser.open("https://www.youtube.com//watch?v=UUxkVYP36gA")

        elif 'Republic bharat' in channelName:
            webbrowser.open("https://www.youtube.com//watch?v=614UTCYPlVg")

        else:

            pywhatkit.playonyt(channelName)

            speak("Here you go for your news")

    def PlayOnYouTube():

        speak("Sir, which video you would like to watch on YouTbe")

        VideoName = takecommand()

        if 'Gaming video' in VideoName:
            webbrowser.open("https://www.youtube.com//results?search_query=gaming")

        else:
            pywhatkit.playonyt(VideoName)

            speak("Sir, You'r Video is started,Enjoy Sir")

    def Whatsapp():
        speak("Tell me the name of the person sir")
        name = takecommand()

        if 'Mohit' in name:
            speak("What should i say to Mohit")
            msg = takecommand()
            speak("Tell me the time")
            speak("time in hours")
            hour = int(takecommand())
            speak("Time in minutes")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+91 8452907114", msg, hour, min, 20)
            speak("Sir,The message has been delivered succesfully to Mohit")


        elif 'Prem' in name:
            speak("What should i say to Prem")
            msg = takecommand()
            speak("Tell me the time")
            speak("time in hours")
            hour = int(takecommand())
            speak("Time in minutes")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+91 8928503290", msg, hour, min, 20)
            speak("The message has been deliver succesfully to Prem")

        elif 'head boy' in name:
            speak("What should I say to Head boy")
            msg = takecommand()
            speak("Tell me the time sir")
            speak("time in hours")
            hour = int(takecommand())
            speak("Time in minutes")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+91 8693870118", msg, hour, min, 20)
            speak("Sir,The message has been delivered sucessfully to Head boy")

        elif 'Shameem' in name:
            speak("What should i say to Shammem")
            msg = takecommand()
            speak("Tell me the time sir")
            speak("time in hours")
            hour = int(takecommand())
            speak("Time in minutes")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+91 9820133595", msg, hour, min, 20)
            speak("Sir,The message has been delivered sucessfully to Shameem")

        elif 'mit' in name:
            speak("What should i say to mit")
            msg = takecommand()
            speak("Tell me the time sir")
            speak("time in hours")
            hour = int(takecommand())
            speak("Time in minutes")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+91 7045225202", msg, hour, min, 20)
            speak("Sir,The message has been delivered sucessfully to MIT")

        elif 'MIT' in name:
            speak("What should i say to MIT")
            msg = takecommand()
            speak("Tell me the time sir")
            speak("time in hours")
            hour = int(takecommand())
            speak("Time in minutes")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+91 7045225202", msg, hour, min, 20)
            speak("Sir,The message has been delivered sucessfully to Mit")

        elif 'Harsh' in name:
            speak("TWhat should i say to Harsh")
            msg = takecommand()
            speak("Tell me the time sir")
            speak("time in hours")
            hour = int(takecommand())
            speak("Time in minutes")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+91 8097132196", msg, hour, min, 20)
            speak("Sir,The message has been delivered sucessfully to Harsh")

    def GoogleMaps(Place):

        Url_Place = "https://www.google.com/maps/place/" + str(Place)

        webbrowser.open(url=Url_Place)

        geolocator = Nominatim(user_agent="myGeocoder")

        location = geolocator.geocode(Place, addressdetails=True)

        target_latlon = location.latitude, location.longitude

        location = location.raw['address']

        target = {'city': location.get('city', ''),
                  'state': location.get('state', '')}

        current_loca = geocoder.ip('m')

        current_latlon = current_loca.latlng

        distance = str(great_circle(current_latlon, target_latlon))
        distance = str(distance.split(' ', 1)[0])
        distance = round(float(distance), 2)


        speak(target)
        speak(f"Sir, {Place} is {distance} Kilometer away from you'r Location")

    def Design():

        import turtle

        t = turtle.Turtle()
        move = 1

        for i in range(360):
            t.pendown()
            t.right(move)
            t.forward(100)
            t.right(30)
            t.forward(60)
            t.left(30)
            t.forward(30)
            t.penup()
            t.home()
            move = move + 1

    def Design2():

        import turtle

        t = turtle.Turtle()
        move = 1

        for i in range(360):
            t.pendown()
            t.right(move)
            t.forward(100)
            t.right(30)
            t.forward(60)
            t.left(30)
            t.forward(30)
            t.penup()
            t.home()
            move = move + 1

    def readmessage():

        if 'messages' in query:
            speak("Sir we have the message from your contacts, please check it our sir")

        else:
            a = ("Sir, we don't have any messages, Fell free sir", "Sir,I think so we are all cought up, we Don't have any WhatsAap messages")
            speak(random.choice(a))

    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com')
        server.ehlo()
        server.starttls()
        server.login('ibrahimsh1910@gmail.com', 'ibrahimshaikh2020')
        server.sendmail('ibrahimsh1910@gmail.com', to, content)
        server.close()


    while True:
        query = takecommand()

        if 'hello' in query or 'hii buddy' in query:
            a = ("Hello Sir", "Hii Sir")
            speak(random.choice(a))

        elif 'what tasks can you do' in query or 'what things can you do' in query:
            speak('''Sir i can do many Tasks like, I can Check Messages , I can Set Alarm, I can Find Any Wikipedia That you want
            , I can open Various websites That you Want, I can play Anything You Want On YouTube, I can Tell You News, I can Send Messages
            , I can AutoMate The System, And Many More Tasks Are There That I Can Do For You, Thank You''')

        elif 'welcome back' in query or 'welcome back Jarvis' in query or 'online' in query or 'online Jarvis' in query:
            playsound('jarvis welcome back sir ! jarvis voice.mp3')

        elif 'introduce yourself' in query:
            playsound("Jarvis (3).mp3")

        elif 'how are you' in query:
            a = ("fine sir what about you", "Everything Is Working Good Sir", "I am All Right")
            speak(random.choice(a))

        elif 'send email' in query:
            try:
                speak("What Should i say, Sir?")
                content = takecommand()
                speak("Whome would you like to send Email, Sir")
                to = input()
                sendEmail(to, content)
                speak("Email has been sent, Successfully")

            except Exception as e:
                print(e)
                speak("I have unable to send email Due to some Internet Problem You Should Try Again After Some Time")

        elif 'I am fine' in query:
            speak("wow, nice to hear that")

        elif 'music' in query:
            Music()  

        elif 'send message' in query:
            Whatsapp()

        elif 'check for messages' in query or 'look for my messages' in query:
            os.startfile("C:\\ProgramData\\91809\\WhatsApp\\WhatsApp.exe")
            readmessage()

        elif "what is today's date" in query or "tell me the date" in query:
            e = datetime.datetime.now()
            speak("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))

        elif "I will back soon" in query or "I need a break" in query:
            a = ("Sir, You can grab a cup of coffie, I will handle the system", "Ohh, yaa I can understand you sir,Take your time")
            speak(random.choice(a))

        elif 'thanks buddy' in query:
            speak("Enjoy sir")

        elif 'alarm' in query or 'Alarm' in query:
            speak("Enter the time to set the alarm, sir !")
            time = input(": Enter the Time to set the alarm :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    a = ("Your Alarm is Running sir", "Time to wake up,Sir")
                    speak(random.choice(a))
                    playsound('Reminder.mp3')
                    playsound('wake up.mp3.mp3')
                    speak("Alarm Closed")
                    wishMe()
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    speak("Current time is " + time)

                elif now>time:
                    break

        elif 'I want to check my WhatsAap' in query or 'check my WhatsApp' in query:
            speak("Opening whatsapp sir")
            os.startfile("C:\\ProgramData\\91809\\WhatsApp\\WhatsApp.exe")
            speak("Here, you go and check for messages on WhatsAap")

        elif 'open IP logger' in query:
            speak("Opening sir , wait a minute")
            webbrowser.open("https://www.opentracker.net//feature//ip-tracker/")

        elif 'news' in query:

            try:
                jsonObj = urlopen('''https://newsapi.org/v2/top-headlines?country=in&apiKey=a6f7ac1a1da5472bb0de06f688bdb330''')
                data = json.load(jsonObj)
                i = 1

                speak("Here are some top news from times of india")
                print('''================TIMES OF INDIA=============''')

                for item in data['articles']:

                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))

        elif 'go to sleep' in query:
            speak("ok sir, you can call me anytime you want, Just say wake up jarvis")
            break

        elif "who are you" in query:
            speak("i am jarvis sir,An AI coded by Ibrahim Shaikh, you can ask me anything you want")

        elif 'who created you' in query:
            speak("Sir, i was created by Ibrahim. First he trained me for some basiscs Tasks and then We go from basics to adavanced")    

        elif "help me Jarvis" in query:
            speak("sure sir , why not, tell me what should i do")

        elif 'wait a minute' in query:
            speak("take your time sir")

        elif 'play news' in query:
            News()

        elif 'Wikipedia' in query:
            speak("searching wikipedia sir...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif 'thank you' in query:
            speak("No problem sir")


        elif "good work Jarvis" in query:
            speak("Thank you sir")

        elif 'open screenshot folder' in query:
            speak("As your wish sir")
            os.startfile("C:\\jarvis.screenshot")

        elif 'open command prompt' in query:
            speak("opening command prompt sir")
            os.system("start cmd")

        elif 'activate system design' in query:
            speak("Activating sir")
            Design()

        elif 'activate Turtle' in query or 'open my design' in query:
            speak("As your wish sir")
            Design2()

        elif 'open Notepad' in query:
            speak("opening notepad sir")
            os.system("%windir%\\system32\\notepad.exe")

        elif 'close Notepad' in query:
            speak("ok sir, closing notepad")
            os.system("TASKILL /F /im  notepad.exe")

        elif 'open Opera browser' in query:
            speak("opening opera browser")
            os.system("www.Opera browser.com")

        elif 'are you there' in query:
            speak("Welcome Home,Sir")

        elif "open instagram profile" in query or "Instagram profile" in query:
            speak("Sir,Please enter The name of that insta user")
            name = input("Enter the user name")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Sir here is the profile of the user {name}")
            speak("Sir,Would YOu Like To Download This Profile of This account.")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("I am done Sir, profile picture is saved in our main folder")
            elif "no" in condition or "No" in condition:
                speak("Ok, Sir the download of this profile is Denied")
            else:
                pass

        elif 'open YouTube' in query:
            speak("as your wish")
            webbrowser.open("www.YouTube.com")

        elif 'can you hear me' in query:
            speak("yes Sir, tell me what to do")

        elif 'where is' in query:
            Place = query.replace("where is ","")
            Place = Place.replace("Jarvis","")
            GoogleMaps(Place)

        elif 'Jarvis copy my lines' in query:
            speak("speak sir")
            jj = takecommand()
            speak(f"you said : {jj}")

        elif 'remember that' in query:
            rememberMsg = query.replace("remember that","")
            rememberMsg = rememberMsg.replace("Jarvis","")
            speak("You Tell Me To Remember That :"+rememberMsg)
            remember = open('data.txt','w')
            remember.write(rememberMsg)
            remember.close()

        elif 'do you have anything' in query:
            remember = open('data.txt','r')
            speak("You Tell Me That" + remember.read())

        elif 'close command prompt' in query:
            speak("closing command prompt sir")
            os.system("TASKKILL /F /im cmd.exe")

        elif 'close YouTube' in query:
            speak("closing youtube sir")
            os.system("TASKKILL /F /im msedge.exe")

        elif 'open Gmail' in query:
            speak("opening Gmail Sir, Wait A second")
            webbrowser.open("https://mail.google.com//mail//u//0//#inbox")

        elif 'stop' in query:
            keyboard.press_and_release('space bar')

        elif 'pause' in query:
            keyboard.press_and_release('k')

        elif 'open setting' in query or 'open settings' in query:
            speak("Opening setting, Sir")
            keyboard.press_and_release('windows + i')

        elif 'initiate system' in query:
            speak("Initializing System")
            speak("Scanning for hardware changes")
            os.startfile("C:\\Program Files\\Rainmeter\\Rainmeter.exe")
            speak("Loading system Information")
            speak("Syatem Initilization Have been succesfully Launched")

        elif 'clean the desktop' in query:
            speak("All right Sir")
            os.system("TASKKILL /F /im Rainmeter.exe")

        elif 'minimize window' in query:
            speak("As your wish sir")
            keyboard.press_and_release('windows + m')

        elif 'switch window' in query:
            speak("Switching Windows")
            keyboard.press_and_release('Alt + Tab')

        elif 'open start' in query:
            keyboard.press_and_release('window')

        elif 'press enter' in query or 'enter' in query:
            keyboard.press_and_release('Enter')

        elif 'take a screenshot' in query or 'screenshot' in query:
            img = pyautogui.screenshot()
            img.save("C:\\jarvis.screenshot\\js.png")
            os.startfile("C:\\jarvis.screenshot")
            speak("done sir, i have taken and saved the screenshot on jarvis.py folder in c drive , you may check")

        elif "take a screenshot" in query:
            screenshot()

        elif 'play something on YouTube' in query or 'play video' in query:
            PlayOnYouTube()

        elif 'do something new Jarvis' in query:
            speak("sir, i can play music for you")

        elif 'open Google' in query:
            speak("what are you trying to do sir")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif 'good morning Jarvis' in query:
            speak("good morning boss")

        elif 'good afternoon Jarvis' in query:
            speak("good afternoon sir")

        elif 'good evening Jarvis' in query:
            speak("good evening boss")

        elif 'Jarvis tell me a joke' in query:
            speak(pyjokes.get_joke())

        elif 'write a note' in query:
            speak("What should i write sir")
            note = takecommand()
            speak("Done Sir, I have saved Your note in jarvis.txt file in python")
            file = open('jarvis.txt', 'w')
            snfm = takecommand()

            if 'yes' in snfm or 'sure' in snfm:
                strfTime = datetime.datetime.now().strftime("% H % M: %S")
                file.write(strfTime)
                file.write(" :- ")
                file.write(note)

            else:
                file.write(note)

        elif 'show note' in query:
            speak("Showing Notes")
            file = open("jarvis.txt", 'r')
            speak(file.read())
            speak(file.read())

        elif 'open WhatsApp' in query:
            speak("opening WhatsAap")
            os.system("C:\\ProgramData\\91809\\WhatsApp\\WhatsApp.exe")

        elif 'close WhatsApp' in query:
            speak("As your wish")
            os.system("TASKKILL /F /im WhatsApp.exe")

        elif "camera" in query or "take a photo" in query:
            from ecapture import ecapture as ec
            ec.capture(0, "Jarvis Camera", "img.jpg")

        elif 'check for messages' in query:
            speak("Scanning sir")
            os.system("C:\\ProgramData\\91809\\WhatsApp\\WhatsApp.exe")
            speak("here we go,check for messages")

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif 'Jarvis shut down my system' in query or "Jarvis shutdown" in query or "turn of" in query:
            speak("do you really want to shut down the system sir")
            reply = takecommand().lower()

            if 'yes' in reply:
                speak("as your wih sir, have a great day")
                os.system("shutdown /s /t 1")

            elif 'no' in query:
                speak("System Shutdown have been cancelled")

        elif 'Good night' in query:
            speak("good night sir, have a sweet dream")

        elif 'YouTube search' in query:
            speak("ok sir, this is what i found for your search")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("done sir")

        elif 'Jarvis volume up' in query or "turn up the volume"in query or "increase the volume" in query:
            pyautogui.press("volumeup")

        elif 'Jarvis volume down' in query  or "turn down the volume" in query or "decrease the volume" in query:
            pyautogui.press("volumedown")

        elif 'Jarvis mute' in query:
            pyautogui.press("volumemute")

        elif 'what can you do Jarvis' in query: 
             speak("Sir, i am here to assist you, i can play music for you , I can open your commands releated to herments base, i can tell you what ever you want to know , i can search news for you from goodle ,an i can do many more things sir")       

        elif 'website' in query:
            speak("ok sir, launching....")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            speak("launched!")

        elif 'Jarvis what to do now' in query:
            speak("ohh, yaa, Sir you have to give more code for me")    

        elif 'launch' in query:
            speak("tell me the name of the website sir")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            speak("Done sir")

        elif 'find my IP address' in query or 'what is my IP address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"Sir, your ip address is {ip}")

        elif 'open Youtube' in query:
            speak("opening youtube sir")
            webbrowser.open('www.youtube.com')

        elif 'open Chrome' in query:
            speak("opening chrome sir")
            webbrowser.open("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'close the window' in query:
            speak("wait a second sir")
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            speak("opening new windows sir")
            keyboard.press_and_release('ctrl + n')

        elif 'open history' in query:
            keyboard.press_and_release('ctrl + h')

        elif 'full screen mode' in query:
            keyboard.press_and_release('f')

        elif 'exit full screen mode' in query:
            keyboard.press_and_release('Esc')

        elif 'skip' in query:
            keyboard.press_and_release('L')

        elif 'back' in query:
            keyboard.press_and_release('J')

        elif 'pause' in query:
            keyboard.press_and_release('k')

        elif "unpause" in query or "un pause" in query:
            keyboard.press_and_release('space bar')

        elif "replay the video" in query or "play again" in query:
            keyboard.press_and_release(0)

        elif 'what are you doing Jarvis' in query:
            speak("Sir i am here to assist you, And nothing else")

        elif 'you need a rest' in query:
            speak("as your wish sir, have a great day")
            sys.exit()

        elif 'who is' in query:
            speak("Searching Your Command Sir")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,1)
            print(results)
            speak(results)

        elif "what is" in query:
            speak("Give Me A Second Sir, I Am Working On It")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,1)
            print(results)
            speak(results)

        elif 'I am not sir' in query:
            speak("But Mam, Ibrahim has coded me like a sir, I can't do anything sorry!")

        elif 'what should we do Jarvis' in query:
            speak('sir i think you should take a break')

        elif 'what is the time' in query or 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak("Current time is " + time)

        elif 'calculate' in query:
            speak("What should i Calculate, Sir")
            gh = takecommand().lower()
            res = app.query(gh)
            speak(next(res.results).text)

        elif 'temperature' in query or 'weather' in query:
            res = app.query(query)
            speak(next(res.results).text)


        elif 'search' in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            query = query.replace("google","")
            speak("Sir, I found this for you")
            pywhatkit.search(query)

            try:
                pywhatkit.search(query)
                result = googleScrap.summary(query,2)
                speak(result)
               
            except:
                speak("No speakable data available sir, sorry")

        elif 'how much power left Jarvis' in query or"how much power we have" in query or "battery" in query:
            import psutil
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery")
            if percentage>=75:
                speak("Sir we have enough power to continue or work")
            elif percentage>=40 and percentage<=75:
                speak("Sir if you understand me , then we should connect our system to a charging point")
            elif percentage<=15 and percentage<=30:
                speak("we don't have enough power to work,please connect the charger")
            elif percentage<=15:
                speak("we have a very low power sir, please connect to charger yhe system will shutdown very soon")


app = wolframalpha.Client("XVQY7E-TRHRT7V798")

if __name__ == "__main__":
    while True:
        permission = takecommand()

        if 'wake up' in permission or 'hey Jarvis' in permission or 'good morning Jarvis' in permission or 'good evening Jarvis' in permission or 'good afternoon Jarvis' in permission or "hi Jarvis" in permission or "hii Jarvis" in permission or  'back online' in permission or 'online' in permission:
            TaskExecution()


































import pyttsx3
import datetime
import pyaudio
import wikipedia
import os
import smtplib
import pyjokes
import pywhatkit as kit
import requests, json
# from bs4 import BeautifulSoup
from datetime import date
from gnewsclient import gnewsclient
import webbrowser #for us to move to any site
import speech_recognition as sr

engine= pyttsx3.init()
engine.setProperty('rate', 190)

client=gnewsclient.NewsClient(language='english', location='india', max_results=3)

chrome_path='C:\\Users\\Dell\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe'
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome')

mailbox={
    'friday':'fridayemail@gmail.com',
    'jarvis':'jarvisemail@gmail.com'}

    

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour= int(datetime.datetime.now().hour) #To take hour from current time
    speak("initializing System settings")
    speak("system online")
    print("WELCOME")
    if hour>=0 and hour<12:
        speak("good Morning!")
    elif hour>=12 and hour <18:
        speak('Good Afternoon')
    else:
        speak("good eavening")
    speak("hi, i am jarvis ! how may i help you?")


def takeCommand():
    #will take microphone input and will return string 

    r=sr.Recognizer()
    # r.recognize_google()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"user said {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(To,content):
    
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('myemail@gmail.com', 'pwd')
    server.sendmail('myemail@gmail.com', To, content)
    server.close()

def weather(location):
    search= f"Weather in {location}"
    url= f"https://www.google.com/search?q={search}"
    r= requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temperature= data.find("div", class_="BNeawe").text
    speak(f"Current temperature in {location} is {temperature}")

def shutdown():
    speak("Shure sir , shutting down!")
    exit()

if __name__ == "__main__":
    # speak(audio)

    wishme()
    while True:
        query= takeCommand().lower()
        # And here ill write the logic
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)

        # elif 'open youtube' in query:
        #     speak("opening youtube")pip install flask

        #     webbrowser.get('chrome').open('Youtube.com')
        elif 'why' in query:
            query=query.replace("jarvis","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'how' in query:
            query=query.replace("jarvis","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)


        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            webbrowser.get('chrome').open('web.whatsapp.com')

        elif 'open telegram' in query:
            speak("opening telegram")
            webbrowser.get('chrome').open('web.telegram.org')
           
        elif 'open google' in query:
            speak("opening google")
            webbrowser.get('chrome').open('google.com')
        
        elif 'open instagram' in query:
            speak("opening instagram")
            webbrowser.get('chrome').open('instagram.com')

        elif 'open facebook' in query:
            speak("opening facebook")
            webbrowser.get('chrome').open('facebook.com')

        elif 'open github' in query:
            speak("opening github")
            webbrowser.get('chrome').open('github.com')
            
        elif 'play music' in query:
            speak("Enjoy your music")
            webbrowser.get('chrome').open('https://gaana.com/song/venom-77')    

        # elif ' youtube'  in query:
        #     try:
        #         speak("what do you want me to play on youtube")
        #         pl = takeCommand()
        #         print(pl)
        #         kit.playonyt(f"{pl}")
        #     except Exception as e:
        #         print(e)
        #         webbrowser.get('chrome').open('youtube.com')
     


        elif 'open command' in query:
            speak("opening commands")
            os.system("start cmd")

        elif ' computer' in query:
            speak("opening this pc")
            os.system("start shell:mycomputerfolder")

        elif ' this pc' in query:
            speak("opening this pc")
            os.system("start shell:mycomputerfolder")

        elif 'Disk c' in query:
            speak("opening c drive")
            comp="C:"
            os.startfile(comp)
        elif 'Disk E ' in query:
            speak("opening E drive")
            e="E:"
            os.startfile(e)
        elif 'disk D' in query:
            speak("opening E drive")
            e="E:"
            os.startfile(e)



        elif 'send email' in query:
            
            try:
                speak("what should i say")
                content= takeCommand()
                To="nadeemsaifi98711@gmail.com"
                print(content)
                sendEmail(To,content)
                speak("Email has been send")
            except Exception as e:
                print(e)
                speak("sorry i cannot do that")


        elif "weather" in query:
            speak("sure")
            try:
                speak("can you specify the city")
                location = takeCommand()
                weather(location)
            except Exception as e:
                print(e)
                speak("i didnt find it sorry")

        elif 'need to eat'  in query:
            speak("Wanna have some biryani sir?")
            webbrowser.get('chrome').open('zomato.com/ncr/hammad-chicken-biryani-2-jasola-new-delhi')

        elif  'need food'  in query:
            speak("Wanna have some biryani sir?")
            webbrowser.get('chrome').open('zomato.com/ncr/hammad-chicken-biryani-2-jasola-new-delhi')

        elif 'hungry' in query:

            speak("Wanna have some biryani sir?")
            webbrowser.get('chrome').open('zomato.com/ncr/hammad-chicken-biryani-2-jasola-new-delhi')

        elif 'time' in query:    
            strTime= datetime.datetime.now().strftime("%I :%M , %p")
            speak(f"The Time is {strTime}")

        elif 'fool' in query:    
            speak("please dont speak mean words, i also have feelings!")   
        elif 'how are you' in query:    
            speak("I am fine sir, what about you?")   
        elif 'stupid' in query:    
            speak("please dont speak mean words, i also have feelings!")   
        elif 'date' in query:
            strD= date.today().strftime("%B %d, %Y")
            print(strD)
            speak(f"The Date is {strD}")



        elif 'joke' in query:
            speak(pyjokes.get_joke(language='en', category='all'))



        elif 'open excel' in query:
            speak("opening microsoft Exel")
            excel= "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(excel)
            
        elif 'open acrobat' in query:
            speak("opening adobe acrobat")
            acrobat= "C:\\Program Files (x86)\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe"
            os.startfile(acrobat)

        elif 'open illustrator' in query:
            speak("opening adobe Illustrator")
            Illustrator= "C:\\Program Files\\Adobe\\Adobe Illustrator 2020\\Support Files\\Contents\\Windows\\Illustrator.exe"
            os.startfile(Illustrator)

        elif 'open code' in query:
            speak("opening microsoft Visual studio code")
            code="C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code)

        elif 'open word' in query:
            speak("opening microsoft word")
            word="C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(word)

        elif 'auto cad' in query:
            speak("opening auto cad")
            cad= "C:\\Program Files\\Autodesk\\AutoCAD 2018\\acad.exe"
            os.startfile(cad)

        elif 'photoshop' in query:
            speak("opening adobe photoshop")
            photoshop= "C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe"
            os.startfile(photoshop)

        elif 'quit' in query:
            shutdown()
        elif 'shutdown' in query:
            shutdown()

        elif 'news'in query:    
            news_list=client.get_news()
            speak("Today news!")
            for item in news_list:
                print("Title:",item['title'])
                print(f"\nlink: {item['link']} \n")
                speak(item['title'])

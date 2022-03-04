import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pyjokes
import smtplib
import pywhatkit

emails = {'funny gamer': 'funnygamer1066','yash': 'aryayash1066','papa': 'vikram70072000', 'avik': 'akarya176','yatin':'yatinchhabra108'}
contacts = {'avik':'+917270072000','nitesh':'+919654707652','yatin':'+918950269437','papa':'+919558900044','sapna mam':'+919810340200','alka mam':'+919811945214'}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voice",voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme ():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternnoon!")
    else:
        speak("good evening!")
    speak("i am ginux. sir how can i help you")  

def takecommand():
    #it takes microphone input from the user and returns string output 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query 
    pass

def takecommand2():
    #it takes microphone input from the user and returns string output 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

    try:  
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e: 
        return "None"
    return query 
    pass


def sendemail(to,content):
    s=smtplib.SMTP("smtp.gmail.com",587)
    s.ehlo()
    s.starttls()
    s.login('sankiyash1714@gmail.com','S.Y.@yt1714')
    s.sendmail('sankiyash1714@gmail.com',to,content)
    s.close()

if __name__ == "__main__":
    while True:
        
        query1 = takecommand2().lower()
        #to start the assistant actiavtion
        if 'ok genix' in query1 :
        
            wishme()
            asname = "ginux"
            while True:

                query =takecommand().lower()

                #logic for executing tasks
                if 'wikipedia' in query:
                    speak("searching on wikipedia....")
                    query=query.replace("wikipedia","")
                    result=wikipedia.summary(query,sentences=2)
                    print(result)
                    speak(result)
                
                elif "what's your name" in query or "what is your name" in query:
                    speak(f"my  name is {asname}")
                
                elif "open youtube" in query:
                    webbrowser.open_new_tab("youtube.com")
                    speak('opening youtube')
                
                elif "open google" in query:
                    webbrowser.open_new_tab("google.com")
                    speak("opening google web page")

                elif "open stack overflow" in query:
                    webbrowser.open_new_tab("stackoverflow.com")
                    speak("opening stack pverflo web page")

                elif "open gmail" in query:
                    webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
                    speak("opening gmail")

                elif "toss a coin" in query:
                    x=random.choice([1,2])
                    if x==1:
                        speak("it's an head")
                    else :
                        speak("it's an tail") 
                
                elif "roll a dice" in query:
                    x=random.choice([1,2,3,4,5,6])
                    if x==1:
                        speak("you got a number one")
                    elif x==2:
                        speak("you got a number two")
                    elif x==3:
                        speak("you got a number three")
                    elif x==4:
                        speak("you got a number four")
                    elif x==5:
                        speak("you got a number five")
                    elif x==6:
                        speak("you got a number six")

                elif "play music" in query:
                    music_dir = 'C:\\Users\\dell\\Music'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                
                elif "open powerpoint" in query or "open ms powerpoint" in query:
                    address = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\PowerPoint 2013'
                    os.startfile(address)
                    speak("opening powerpoint")

                elif "open codeblocks" in query or "open code blocks" in query :
                    address = "C:\\Program Files\\CodeBlocks\\codeblocks.exe"
                    os.startfile(address)
                    speak("opening codeblocks")

                elif "open visual studio code" in query or "open vs code" in query:
                    address = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(address)
                    speak("opening vs code")


                elif "open calculator" in query:
                    address = 'C:\\Users\\Admin\\OneDrive\\Desktop\\Calculator'
                    os.startfile(address)
                    speak("opening calculator")

                elif "open whatsapp" in query or "open desktop whatsapp" in query:
                    address = 'C:\\Users\\Admin\\OneDrive\\Desktop\\WhatsApp Desktop'
                    os.startfile(address)
                    speak("opening whatsapp")

                elif "open alarm and clock" in query or "open alarm clock" in query :
                    address = 'C:\\Users\\Admin\\OneDrive\\Desktop\\Alarms & Clock'
                    os.startfile(address)
                    speak("opening alarm clock")

                elif "open calendar" in query:
                    address = 'C:\\Users\\Admin\\OneDrive\\Desktop\\Calendar'
                    os.startfile(address)
                    speak("opening calendar")

                elif "open adobe reader" in query:
                    address = "C:\\Program Files (x86)\\Adobe\\Reader 10.0\\Reader\\AcroRd32.exe"
                    os.startfile(address)
                    speak("opening adobe reader")

                elif "open control panel" in query:
                    address = 'C:\\Users\\Admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel'
                    os.startfile(address)
                    speak("opening control panel")

                # elif "send a message" in query:
                #     speak ('do want to use sms or whatsapp')
                #     a= takecommand().lower()
                #     if a=='sms' :
                #         resp = requests.post('https://textbelt.com/text', {'phone': '+917270072000', 'message': 'Hello world','key': 'textbelt'})
                #         print(resp.json())

                elif "send message on whatsapp" in query or "send a message on whatsapp" in query:
                    speak("who do you want to send message")
                    b = takecommand().lower()
                    if b in contacts:
                        to = contacts[b]
                        speak("got it, what's the message")
                        message = takecommand().lower()
                        if message!="nothing" and message!="cancel it" and message!="cancel the message":
                            a=int(datetime.datetime.now().strftime("%H"))
                            b=(1+int(datetime.datetime.now().strftime("%M")))
                            pywhatkit.sendwhatmsg(to,message,a,b)
                            speak("message sended successfully")
                    else:
                        speak("the name is not in your contact list")

                elif "open excel" in query or "open ms excel" in query:
                    address = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Excel 2013'
                    os.startfile(address)
                    speak("opening ms excel")

                elif "open ms word" in query or "open word" in query:
                    address = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Word 2013'
                    os.startfile(address)
                    speak("opening ms word")

                elif "open scilab" in query:
                    address = "C:\\Program Files\\scilab-6.0.2\\bin\\WScilex.exe"
                    os.startfile(address)
                    speak("opening scilab")

                elif "open notepad" in query:
                    address = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
                    os.startfile(address)
                    speak("opening notepad")

                elif "send email" in query or "send an email" in query or "send a email" in  query:
                    try:
                        speak ('who do you want to email?')
                        b = takecommand().lower()
                        if b in emails:
                            to = emails[b]+'@gmail.com'             
                            speak("what's the message")
                            content = takecommand()
                            if content!="nothing" and content!="cancel it" and content!="cancel the email":
                                sendemail(to,content)
                                speak("email has been sent!")
                            else:
                                speak("ok no problem i will cancel it")
                        else :
                            speak( 'their is no email in your list with this name') 
                    except Exception as e:
                        speak("sorry sending of email fails due to any error")
                
                elif 'shutdown the system' in query or "shutdown the pc" in query or "shutdown pc" in query or "shutdown system" in query: 
                    speak("are you sure to shutdown your pc")
                    a = takecommand().lower()
                    if 'yes' in a or "yup" in a or "yeah" in a:
                        speak("Hold On a Second ! Your system is on its way to shut down") 
                        os.system('shutdown /s')
                    else:
                        pass
                elif "restart system" in query: 
                    speak("are you sure to restart your pc")
                    a=takecommand().lower()
                    if 'yes' in a or "yup" in a or "yeah" in a:
                        os.system("shutdown /r")
                    else:
                        pass

                elif "hibernate system" in query or "sleep mode" in query or 'hibernate the pc' in query : 
                    speak("are you sure to hibernate your pc")
                    a=takecommand().lower()
                    if 'yes' in a or "yup" in a or "yeah" in a:
                        speak("Hibernating") 
                        os.system("shutdown /h")
                    else:
                        pass

                elif "joke" in query:
                    a=pyjokes.get_joke()
                    print(a)
                    speak(a)
                    
                elif "not so funny" in query or "too bad" in query: 
                    speak ("i will try my best next time to make you happy ")
                    
                elif "good job" in query or "nice work" in query or "impressive" in query or "excellent work" in query:
                    speak("thanks")
                
                elif "who are you" in query:
                    speak("i am your ginux assistant")

                elif "change background" in query:
                    pass

                elif 'news' in query: 
                    webbrowser.open("https://inshorts.com/en/read")

                elif "the time" in query:
                    time= datetime.datetime.now().strftime("%H:%M:%S")
                    print(time)
                    speak(f"its {time}")

                elif "search"  in query:
                    query=query.replace("search","")
                    webbrowser.open(f"{query}") 
                    
                elif "stop yourself" in query :
                    query1 = "stop yourself"
                    break

                elif query != 'none':
                    webbrowser.open(f"{query}")

        if "stop yourself" in query1:
            break
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

#Listening 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Wish
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if (hour>=0 and hour<12):
        speak("Good Morning")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am ALEX your Personal Assistant , Hello Abhinav sir,Please tell me how can i help you?")

#Take Command from user
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing..")
        query=r.recognize_google(audio, language="en-in")
        print(f"User Said {query}\n")
    except Exception as e:
        # print(e)

        speak("Sorry sir couldn't hear you,Please say that again")
        return "None"
    return query


if __name__=="__main__":
    wishMe()                                                            #Calling wish function
    while True:
        query = takeCommand().lower()                                   #query stores our speech in text format

        if 'wikipedia' in query:                                        #Search anything on wikipedia
            speak("Searching on Wikipedia..")
            query=query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:                                    #Opening YouTube
            webbrowser.open("youtube.com")
        
        elif 'play song' in query:                                       #Play any song stored in curretn directory
            music_dir='C:\\Users\\Abhinav\\Desktop\\new\\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'open code' in query:                                       #Opening VScode
            location="C:\\Users\\Abhinav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(location)
         
        elif 'open chrome' in query:                                     #Opening Chrome
            location1="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(location1)
        
        elif 'google' in query:                                          #Searching anythig on Google
            search="https://www.google.com/search?q="
            query=query.replace("google","")
            webbrowser.open(search+query)
        
        elif 'open chat gpt' in query:                                   #Opening chatgpt
            webbrowser.open("https://chat.openai.com")

        elif 'open a new word file and start typing' in query:           #Typing on speech
            speak("What should i write")
            query1=takeCommand()
            f1=open("output.docx","a")
            f1.write(query1)
            f1.write("\n")  
            f1.close()
            speak("ok sir done")

        elif 'stop' in query:                                            #Stop code
            speak("thank you sir for having me , just call me when ever you need me bbyyee")
            break

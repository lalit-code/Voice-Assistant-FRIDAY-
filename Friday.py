import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import os
import wikipedia
import random
import pyjokes
import webbrowser

# Function for taking voice input
def take_command():
    me = sr.Recognizer()
    with sr.Microphone() as micvar:
        print("Listning...")
        audio = me.listen(micvar)

    try:
        print("Wait..")
        text = me.recognize_google(audio)
        if text =="":
            return None
        else:
            if "friday" in text:
                text = text.replace('friday','')
            else:
                print("You said : ",text)
                return text

    except Exception as Error:
        print("Cant Recognize - Say that again !")

# Function for giving voice output
def say(text):   
    speaker = pyttsx3.init()
    speaker.setProperty('rate', 130 )
    speaker.say(text)
    speaker.runAndWait()

# Function that greets the user by the Assistent
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        say("Good morning sir")
    elif hour>=12 and hour<18:
        say("Good afternoon sir")
    else:
        say("Good evening sir") 

    print(" I am FRIDAY, How can i help you")
    say(" I am friday, how can i help you")
    print("______________________________________________________")
    print("You can use these following commands :-")
    print("______________________________________________________")
    print("- Open Code                   - (Query) on Wikipedia    ")
    print("- Open Notepad                - (Query) on Youtube      ")
    print("- Open Browser                - (Query) on Google       ")
    print("- Open Google                 - Tell me Time            ")
    print("- Open Youtube                - Ok Bye                  ")
    print("- Play Music                  - Tell me a Joke          ")
    print("-------------------------------------------------------")
    print("")

# MAIN LOGIC of the program :-
def Initialize():
        greet() 
        while 1:  
            query = take_command()
            if query == None:
                print("I cant Hear You")
            else:
                query = query.lower()    
                if "open code" in query:
                    vspath = "C:\\Users\\abc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(vspath)

                elif "open notepad" in query:
                    notepath = "C:\\Windows\\system32\\notepad.exe"
                    os.startfile(notepath)

                elif "open browser" in query:
                    chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                    os.startfile(chrome_path)

                elif "play music" in query:
                    songs_dr = "E:\\NEW SONG"
                    songs = os.listdir(songs_dr)
                    songs_lenght = songs.__len__()
                    song_no = random.randint(0,songs_lenght)
                    os.startfile(os.path.join(songs_dr, songs[song_no]))

                elif "wikipedia" in query:
                    say("Ok let me search")
                    query = query.replace('on wikipedia','')
                    result = wikipedia.summary(query, sentences=2)
                    say("Accouding to wikipedia:")
                    print(result)
                    say(result)

                elif "tell me time" in query:
                    present_time = datetime.datetime.now().strftime("%I:%M %p")
                    print("FRIDAY: ",present_time)
                    say("its"+ present_time)

                elif "joke" in query:
                    print("Ok let me think")
                    say("Ok let me think")
                    say(pyjokes.get_joke())

                elif "ok bye" in query:
                    print("FRIDAY: Ok bye sir, Have a good day")
                    say("Sure sir, Have a good day")
                    exit()

                elif "open youtube" in query:
                    webbrowser.open("https://www.youtube.com")

                elif "on youtube" in query:
                    query = query.replace('on youtube','')
                    webbrowser.open("https://www.youtube.com/results?search_query="+query)

                elif "open google" in query:
                    webbrowser.open("https://www.google.com")

                elif "on google" in query:
                    query = query.replace('on google','')
                    webbrowser.open("https://www.google.com/search?q="+query)

                else:
                    print("(*** I can't do that, what you are saying ***)")
                    say("I can't do that, what you are saying.")
                

# To Initialise the ASSISTANT 
if __name__ == "__main__":
    Initialize()



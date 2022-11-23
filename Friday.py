import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

friday = pyttsx3.init()
voice = friday.getProperty('voices')
friday.setProperty('voice', voice[1].id)


def speak(audio):
    print("Friday : " + audio)
    friday.say(audio)
    friday.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I: %M : %p")
    speak(Time)


def Welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak("Good moring sir")
    elif hour >= 12 and hour <= 18:
        speak("Good affternoon sir")
    elif hour >= 18 and hour <= 24:
        speak("Good evening sir")
    speak("How can I help you?")


def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 2
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language='en')
        print('Van Hai :' + query)
    except sr.UnknownValueError:
        print("Oops!  Repeat again sir.  Try again...")
        query = str(input("Your answer : "))
    return query


if __name__ == "__main__":
    Welcome()
    while True:
        query = command().lower()

        if "google" in query:
            speak("What should I can search boss !")
            search = command().lower()
            url = f"https://www.google.com/serch?query={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on Google')

        if "youtube" in query:
            speak("What should I can search boss !")
            search = command().lower()
            url = f"https://www.youtube.com/serch?query={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on Youtube')

        elif "open video" in query:
            meme = r"C:\Users\haiz2\Videos\superidol\superidol.mp4"
            os.startfile(meme)
        elif "time" in query:
            time()
        elif "who am i" in query:
            speak("You are a stupid dog !")
        elif "quit" in query:
            speak("Friday is quit! . Good bye sir")
            quit()

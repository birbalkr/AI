import pyttsx3
# import pyaudio
import speech_recognition as sr


def spack(text):
    engine = pyttsx3.init()
    id=r'Zara'
    engine.setProperty('voice',id)
    engine.say(text=text)
    engine.runAndWait()


def speechrecognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)
    try:
        print("Recogizing.....")
        query = r.recognize_google(audio,language="en")
        # spack(query.lower())
        return query.lower()
    except:
        return ""

def mainfunction(query):
    query=str(query).lower()

    if "hello" in query:
        spack("Hello sir, Welcome back! ")

    else:
        spack("Nice to meet you sir, have a nice day!")

while True:
    print("")
    query = speechrecognition()
    mainfunction(query)

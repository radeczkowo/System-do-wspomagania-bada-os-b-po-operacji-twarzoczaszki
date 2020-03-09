from constants import *
import speech_recognition as sr
from Functions import musicpath
import time
r = sr.Recognizer()

def recordaudio():
    with sr.Microphone() as source:
        print("Mow!")
        audio = r.listen(source, phrase_time_limit=3)
    return audio

def voicerec(word, e):
    recword = ""
    while recword != word and e.is_set():
        try:
            recword = r.recognize_google(recordaudio(), language='pl-PL')
            print("Rozpoznano: " + recword)
        except:
            if e.is_set():
                musicpath(os.path.join(SOUNDDIR, 'Ponow.wav')).play()
                time.sleep(2)
    e.clear()

def voicerecrating(q, e):
    global rating
    helpflag = False
    while (helpflag == False) and e.is_set():
        try:
            recword = r.recognize_google(recordaudio(), language='pl-PL')
            if recword == "1":
                q.put(1)
                helpflag = True
            if recword == "jeden":
                q.put(1)
                helpflag = True
            if recword == "dwa":
                q.put(2)
                helpflag = True
            if recword == "2":
                q.put(2)
                helpflag = True
            if recword == "3":
                q.put(3)
                helpflag = True
            if recword == "trzy":
                q.put(3)
                helpflag = True
            if recword == "4":
                q.put(4)
                helpflag = True
            if recword == "cztery":
                q.put(4)
                helpflag = True
            if recword == "5":
                q.put(5)
                helpflag = True
            print("Rozpoznano: " + recword)
        except:
            if e.is_set():
                musicpath(os.path.join(SOUNDDIR, 'Ponow.wav')).play()
                time.sleep(2)
    e.clear()

def voicerecdouble(word1,word2, e,q):
    while e.is_set():
        try:
            recword = r.recognize_google(recordaudio(), language='pl-PL')
            print("Rozpoznano: " + recword)
            if recword == word1:
                q.put(True)
                e.clear()
            elif recword == word2:
                q.put(False)
                e.clear()
        except:
            if e.is_set():
                musicpath(os.path.join(SOUNDDIR, 'Ponow.wav')).play()
                time.sleep(2)








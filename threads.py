from webcamemotions import *
import time
from pygaze import libtime
from constants import *


def flag(event):
    event.set()
    time.sleep(10.5)
    event.clear()

def emorec(event, q):
    event.wait()
    global emotion
    emotion = q.get()
    while event.is_set():
        emotion = videoemotionrec()

def dostuff(event,t0, q):
    event.wait()
    while event.is_set():
        if not q.empty():
            t1 = libtime.get_time()
            currenttime.append(round((t1 - t0), 2))
            trackerpos.append(q.get())
            emotionslist.append(emotion)










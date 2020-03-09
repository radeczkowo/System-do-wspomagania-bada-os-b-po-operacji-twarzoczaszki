from pygaze import eyetracker
from pygaze import liblog
from pygaze.libinput import Keyboard
from Functions import *
from heatmap import *
from threads import *
from voicerecognition import *
import threading
import queue
kb = Keyboard(keylist=['space', '1', '2', '3', '4', '5', 'escape'], timeout=1)
date = timeanddate()
musiccommands(music)
disp = libscreen.Display()
tracker = eyetracker.EyeTracker(disp)
importimages(imgs)
scrsttart = startscreen()
disp.fill(scrsttart)
disp.show()
musicpath(os.path.join(SOUNDDIR, 'Start.wav')).play()
time.sleep(2.8)
e = threading.Event()
e.set()
thread1 = threading.Thread(target=voicerec, args=("start", e))
thread1.start()
spacepass(kb, e)
thread1.join()
scrsttart.clear()
for images in range(len(imgs)):
    print "e"
    img = resizeimagefunction(imgs[images], calcresolution())
    a = imagescreen(img)
    disp.fill(a)
    disp.show()
    libtime.expstart()
    print "wwwwwww"
    for number in fastrange(music):
        music[number].play()
        soundfilename = writecommandname(soundfiles[number])
        directory = liblogpath(imgs[images], soundfilename, date)
        time.sleep(2.5)
        tracker.start_recording()
        q = queue.Queue()
        q2 = queue.Queue()
        emotion = videoemotionrec()
        q2.put(emotion)
        t0 = libtime.get_time()
        t1 = libtime.get_time()
        thread2 = threading.Thread(target=flag, args=(e,))
        thread3 = threading.Thread(target=emorec, args=(e, q2,))
        thread4 = threading.Thread(target=dostuff, args=(e, t0, q))
        thread2.start()
        thread3.start()
        thread4.start()
        trackersample(t0, q, 0, tracker, 2.5)
        tracker.stop_recording()
        thread2.join()
        thread3.join()
        thread4.join()
        createheatmap(trackerpos, imgs[images], heatmapsave(imgs[images], soundfilename, date))
        musicpath(os.path.join(SOUNDDIR, 'Ocena.wav')).play()
        time.sleep(11.5)
        e.set()
        thread5 = threading.Thread(target=voicerecrating, args=(q, e))
        thread5.start()
        numberinput(e, kb, q)
        thread5.join()
        rating = q.get()
        musicpath(os.path.join(SOUNDDIR, 'OcenaOtrzymana.wav')).play()
        time.sleep(2)
        writetofile(directory, 20, 80, currenttime, trackerpos, emotionslist, soundfilename, rating)
        del currenttime[:]
        del trackerpos[:]
        del emotionslist[:]
        if number < (len(music)-1):
            e.set()
            thread6 = threading.Thread(target=voicerec, args=("dalej", e))
            musicpath(os.path.join(SOUNDDIR, 'Dalej.wav')).play()
            time.sleep(3.8)
            thread6.start()
            spacepass(kb, e)
            thread6.join()
    if images < (len(imgs) - 1):
        e.set()
        thread7 = threading.Thread(target=voicerecdouble, args=("dalej", "koniec", e, q))
        musicpath(os.path.join(SOUNDDIR, 'Koniec.wav')).play()
        time.sleep(5.8)
        thread7.start()
        spacepassdouble(kb, e, q)
        thread7.join()
    if not q.get():
        a.clear()
        break
    a.clear()
tracker.close()
disp.fill(endscreen())
disp.show()
time.sleep(3)
disp.close()


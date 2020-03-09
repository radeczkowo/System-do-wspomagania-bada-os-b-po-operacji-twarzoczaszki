from pygaze import libscreen
from pygaze import libsound
from pygaze import libtime
from PIL import Image
import glob
from datetime import datetime
from webcamemotions import *

def startscreen():
    mainscreen = libscreen.Screen(bgc=(15, 129, 5, 0), fgc=(50, 90, 0, 55))
    image = "Backgrounds/backend.jpg"
    mainscreen.draw_image(image)
    w, h = calcresolution()
    mainscreen.draw_rect(colour=(255, 255, 255), x=w/2 - 0.5*w/2, y=h/2-0.4*h/2, w=0.5*w, h=0.4*h, pw=1, fill=True)
    mainscreen.draw_text(text='Badanie reakcji na widok\n twarzy po operacji', colour=(0, 0, 0), pos=None,
                         center=True, font='mono', fontsize=40, antialias=True)
    return mainscreen

def endscreen():
    mainscreen = libscreen.Screen(bgc=(15, 129, 5, 0), fgc=(50, 90, 0, 55))
    image = "Backgrounds/backend.jpg"
    mainscreen.draw_image(image)
    w, h = calcresolution()
    mainscreen.draw_rect(colour=(255, 255, 255), x=w / 2 - 0.5 * w / 2, y=h / 2 - 0.4 * h / 2, w=0.5 * w, h=0.4 * h,
                         pw=1, fill=True)
    mainscreen.draw_text(text='Badanie zakonczone', colour=(0, 0, 0), pos=None,
                         center=True, font='mono', fontsize=40, antialias=True)
    return mainscreen

def musiccommands(Scommands, comcounter = 0):
    while comcounter != len(soundfiles):
        Scommands.append(libsound.Sound(soundfile=soundfiles[comcounter]))
        comcounter = comcounter + 1

def imagescreen(image):
    scr = libscreen.Screen()
    scr.draw_image(image)
    return scr

def clause1(letter, breakpoint):
    if letter == breakpoint:
        return True
    else:
        return False

def writecommandname(name):
    word = ""
    letternr = name.find("Music")
    for number in fastrange(name):
        if name[number] == ".":
            break
        if number >= letternr+6:
            word = word + name[number]
    return word

def fastrange(list):
    return range(len(list))

def musicpath(path):
    return libsound.Sound(soundfile=path)

def resizeimagefunction(image, size):
    img = cv2.imread(image, cv2.IMREAD_COLOR)
    if (img.shape[1] == size[0]) and (img.shape[0] == size[1]):
        pass
    else:
        print size[0]
        wscale = float(size[0]) / float(img.shape[1])
        print wscale
        hscale = float(size[1]) / float(img.shape[0])
        print hscale
        if hscale <= wscale:
            img = cv2.resize(img, (0, 0), fx=hscale, fy=hscale)
        else:
            img = cv2.resize(img, (0, 0), fx=wscale, fy=wscale)
        cv2.imwrite(image, img)
        img = Image.open(image)
        imghelp = Image.new('RGB', size, (255, 255, 255))
        imghelp.paste(img, ((size[0] - img.size[0]) / 2,
                            (size[1] - img.size[1]) / 2))
        imghelp.save(image, "JPEG")
    imgimge = Image.open(image)
    return imgimge

def saveresizeimage(image, size,):
    img = resizeimagefunction(image, size)
    img.save(image, "JPEG")

def importimages(list):
    for file in glob.glob("./Sources/*.jpg"):
        list.append(file)


def writeimagename(name):
    word = ""
    letternr = name.find("Sources")
    for number in fastrange(name):
        if number >= letternr+8:
            word = word + name[number]
        if name[number+1] == ".":
            break
    return word

def heatmapsave(filename, soundname,date):
    imgname = writeimagename(filename)
    directory = 'Results/'+imgname+'/'+date+'/Heatmaps'
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory+"/"+soundname

def addelements(time, sample, emotion):
    currenttime.append(time)
    trackerpos.append(sample)
    emotionslist.append(emotion)

def timeanddate():
    return datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

def liblogpath(filename, soundname,date):
    imgname = writeimagename(filename)
    directory = 'Results/' + imgname + '/' + date + '/Data'
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory+'/'+soundname

def numberinput(e,kb,q):
    while e.is_set():
        t = kb.get_key()[0]
        if t == '1':
            q.put(1)
            e.clear()
        elif t == '2':
            q.put(2)
            e.clear()
        elif t == '3':
            q.put(3)
            e.clear()
        elif t == '4':
            q.put(4)
            e.clear()
        elif t == '5':
            q.put(5)
            e.clear()


def trackersample(t0, q, tstart=0, tracker=None, tsample=3):
    t1 = libtime.get_time()
    while t1 - t0 < 10000:
        t1 = libtime.get_time()
        if t1 - t0 > 0 + tstart:
            if tracker.sample()[0] >= 0:
                if tracker.sample()[1] >= 0:
                    q.put(tracker.sample())
                    tstart = tstart + tsample

def spacepass(kb, e):
    while (kb.get_key()[0] != 'space') and e.is_set():
        pass
    e.clear()

def writetofile(directory,a,b,list1,list2, list3,soundname,rating):
    directory = directory + ".txt"
    with open(directory, "w") as file:
        string = ""
        string += soundname
        string += "\n"
        file.write(string)
        for i in range(len(list1)):
            string = ""
            string += str(list1[i])
            if len(string) < a:
                string += (a - len(string)) * " "
            string += str(list2[i])
            if len(string) < b:
                string += (b - len(string)) * " "
            string += str(list3[i])
            string += "\n"
            file.write(string)
        string = ""
        string += str(rating)
        file.write(string)

def spacepassdouble(kb, e,q):
    while e.is_set():
        t = kb.get_key()[0]
        if t == 'space':
            q.put(True)
            e.clear()
        elif t == 'escape':
            q.put(False)
            e.clear()




import os.path
import cv2
import ctypes

def calcresolution():
    user32 = ctypes.windll.user32
    if SCREENNR == 0:
        screen_width, screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    elif SCREENNR == 1:
        screen_width, screen_height = user32.GetSystemMetrics(78) - user32.GetSystemMetrics(0)\
            , user32.GetSystemMetrics(79)
    return screen_width, screen_height

# MAIN
DUMMYMODE = False # False for gaze contingent display, True for dummy mode (using mouse or joystick)
LOGFILENAME = 'default' # logfilename, without path
LOGFILE = LOGFILENAME[:] # .txt; adding path before logfilename is optional; logs responses (NOT eye movements, these are stored in an EDF file!)


# DIRECTORY
DIR = os.path.split(os.path.abspath(__file__))[0]
DATADIR = os.path.join(DIR, 'trackerlogdata')
LOGFILE = os.path.join(DATADIR, LOGFILENAME) # .txt; adding path before logfilename is optional; logs responses (NOT eye movements, these are stored in an EDF file!)
RESDIR = os.path.join(DIR, 'Sources')
BACKDIR = os.path.join(DIR, 'Backgrounds')
SOUNDDIR = os.path.join(DIR, 'Music')
STARTFOTO = [os.path.join(RESDIR, 'backstart.jpg')]



# DISPLAY
# used in libscreen, for the *_display functions. The values may be adjusted,
# but not the constant's names
SCREENNR = 0  # number of the screen used for displaying experiment
DISPTYPE = 'psychopy'  # either 'psychopy' or 'pygame'
DISPSIZE = calcresolution()  # canvas size
SCREENSIZE = (34.5, 19.7)  # physical display size in cm
MOUSEVISIBLE = True  # mouse visibility
# BGC = (125, 125, 125, 255)  # backgroundcolour
# FGC = (0, 0, 0, 255)  # foregroundcolour

# SOUND
# defaults used in libsound. The values may be adjusted, but not the constants'
# names
soundfiles = [os.path.join(SOUNDDIR, 'LeweUcho.wav'),
              os.path.join(SOUNDDIR, 'PraweUcho.wav'),
              os.path.join(SOUNDDIR, 'Nos.wav'),
              os.path.join(SOUNDDIR, 'Usta.wav')]





# EYETRACKER
# general
TRACKERTYPE = 'opengaze' # either 'smi', 'eyelink' or 'dummy' (NB: if DUMMYMODE is True, trackertype will be set to dummy automatically)
SACCVELTHRESH = 35 # degrees per second, saccade velocity threshold
SACCACCTHRESH = 9500 # degrees per second, saccade acceleration threshold


# LISTS
music = []
currenttime = []
trackerpos = []
imgs = []
emotionslist = []
threads = []
Emotions = ["anger", "disgust", "fear",  "happy", "sadness", "surprise", "neutral"]
# Variables
tsample = 0
emotionsample = 0
rating = 0
IMG_SIZE = 48
emotion = ""
blank = ""
heatmap = 0


# CNN
faceclassifier1 = cv2.CascadeClassifier("CNN/Haarcascades/haarcascade_frontalface_default.xml")
faceclassifier2 = cv2.CascadeClassifier("CNN/Haarcascades/haarcascade_frontalface_alt2.xml")
faceclassifier3 = cv2.CascadeClassifier("CNN/Haarcascades/haarcascade_frontalface_alt_tree.xml")
faceclassifier4 = cv2.CascadeClassifier("CNN/Haarcascades/haarcascade_frontalface_alt.xml")


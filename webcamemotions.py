from facedetection import *
from constants import *
from keras import models


def loadmodel(pathandname):
    model = models.load_model(pathandname)
    return model

model = loadmodel('CNN/Models/model2704')
def videoemotionrec():
    video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    _, frame = video.read()
    video.release()
    try:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame, flag = findaface(frame, IMG_SIZE, IMG_SIZE)
        frame = frame.reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    except:
        flag = False
        pass
    if flag == True:
        prediction = model.predict([frame])
        print prediction
        label = Emotions[prediction.argmax()]
        print label
        return label
    else:
        print "None"
        return "None"

"""
while True:
    videoemotionrec()

"""


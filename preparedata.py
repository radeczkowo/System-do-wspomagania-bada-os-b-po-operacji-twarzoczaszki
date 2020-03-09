import numpy as np
import pandas as pd
import pickle
from facedetection import *
import matplotlib.pyplot as plt
import random

def importcsvdata(data, sizex, sizey):
    tdata = []
    xx = -1
    yy = 0
    data = pd.read_csv(data)
    for number in range(len(data)):
        img_array = np.zeros((sizex, sizey), dtype=np.uint8)
        img = data["pixels"][number]
        val = img.split()
        x_pixels = np.array(val, 'float32')
        emotion = int(data["emotion"][number])
        for number1 in range(len(x_pixels)):
            if number1 % sizey == 0:
                xx += 1
                yy = 0
            img_array[xx][yy] = x_pixels[number1]
            yy += 1
        img_array, bhelp = findaface(img_array, sizex, sizey)
        #plt.imshow(img_array, cmap="gray")
        #plt.show()
        if bhelp == True:
            tdata.append([img_array, emotion])
        xx = -1
        yy = 0
    return tdata

def importdataromdirectories(datapath,sizex,sizey, tdata):
    for emo in Emotions:
        path = os.path.join(datapath, emo)
        emotion = Emotions.index(emo)
        for img in os.listdir(path):
                img = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                img_array, bhelp = findaface(img, sizex, sizey)
                #plt.imshow(img_array, cmap="gray")
                #plt.show()
                if bhelp == True:
                    tdata.append([img_array, emotion])
    random.shuffle(tdata)
    return tdata



def editdata(tdata):
    x = []
    y = []
    for features, label in tdata:
        x.append(features)
        y.append(label)
    X = np.array(x).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    X = np.array(X, dtype="float32")
    y = np.array(y, dtype="float32")
    return X, y

def savedata(pathname, data):
    pickdata = open(pathname, "wb")
    pickle.dump(data, pickdata)
    pickdata.close()



tdata = importcsvdata("CNN/Datasets/csv/fer2013.csv", IMG_SIZE, IMG_SIZE)
print len(tdata)
tdata = importdataromdirectories("CNN/Datasets/cohn-kanade", IMG_SIZE, IMG_SIZE, tdata)
print len(tdata)
X, y = editdata(tdata)
savedata("CNN/Trainingdata/XX", X)
savedata("CNN/Trainingdata/yy", y)

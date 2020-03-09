from constants import *

def findaface(array,sizex, sizey):
    bhelp = False
    result1 = faceclassifier1.detectMultiScale(array, minSize=(5, 5), scaleFactor=1.2)
    result2 = faceclassifier2.detectMultiScale(array, minSize=(5, 5), scaleFactor=1.2)
    result3 = faceclassifier3.detectMultiScale(array, minSize=(5, 5), scaleFactor=1.2)
    result4 = faceclassifier4.detectMultiScale(array, minSize=(5, 5), scaleFactor=1.2)
    if len(result1) == 1:
        faceout = result1
    elif len(result2) == 1:
        faceout = result2
    elif len(result3) == 1:
        faceout = result3
    elif len(result4) == 1:
        faceout = result4
    else:
        faceout = ""
    for (x, y, w, h) in faceout:
        array = array[y:y + h, x:x + w]
        try:
            array = cv2.resize(array, (sizex, sizey))
            bhelp = True
        except:
            bhelp = False
            pass
    return array, bhelp



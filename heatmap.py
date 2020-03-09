import numpy as np
import threading
from constants import *


def gauss(w, h, sigma=4, center=(0, 0), a=1, r=45):
    global heatmap
    x0 = int(center[0])
    y0 = int(center[1])
    if ((x0 - r) >= 0) and ((x0 + r) <= w):
        x = np.arange((x0 - r), (x0 + r), 1, float)
    if ((x0 - r) >= 0) and ((x0 + r) > w):
        x = np.arange(x0 - r, w, 1, float)
    if ((x0 - r) < 0) and ((x0 + r) <= w):
        x = np.arange(0, x0 + r, 1, float)
    if ((x0 - r) < 0) and ((x0 + r) > w):
        x = np.arange(0, w, 1, float)
    if ((y0 - r) >= 0) and ((y0 + r) <= h):
        y = np.arange(y0 - r, y0 + r, 1, float)
    if ((y0 - r) >= 0) and ((y0 + r) > h):
        y = np.arange(y0 - r, h, 1, float)
    if ((y0 - r) < 0) and ((y0 + r) <= h):
        y = np.arange(0, y0 + r, 1, float)
    if ((y0 - r) < 0) and ((y0 + r) > h):
        y = np.arange(0, h, 1, float)

    x, y = np.meshgrid(x, y)
    xstart = int(x[0][0])
    xend = x.shape[1] + xstart
    ystart = int(y[0][0])
    yend = len(y) + ystart

    heatmap[ystart:yend, xstart:xend] += a*np.exp(-((x-x0)**2+(y-y0)**2)/(2*(sigma**2)))


def calculateheatmap(pointsarray, w, h, image, threshold=5, alfa = 0.5, beta=0.8):
    global heatmap
    heatmap = np.zeros((h, w))
    for point in range(pointsarray.shape[0]):
        t = threading.Thread(target=gauss, args=(w, h, 8, (pointsarray[point, 0], pointsarray[point, 1])),
                             name="thread{}".format(point+1))
        threads.append(t)
        t.start()
    for tnr in threads:
        tnr.join()
    heatmap = ((heatmap - np.amin(heatmap))/(np.amax(heatmap)-np.amin(heatmap)))*255
    heatmap = heatmap.astype("uint8")
    heatmapcolor = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    mask = np.where(heatmap <= threshold, 1, 0)
    mask = np.reshape(mask, (h, w, 1))
    finalimg =image*mask+heatmapcolor*(1-mask)
    finalimg = finalimg.astype("uint8")
    finalimg = cv2.addWeighted(image, alfa, finalimg, beta, 0)
    return finalimg


def createheatmap(points, image, path):
    global heatmap
    img = cv2.imread(image)
    pointsarray = np.asarray(points)
    H = img.shape[0]
    W = img.shape[1]
    heatmap = calculateheatmap(pointsarray, W, H, img, 5, 0.3, 0.7)
    path = path+".jpg"
    cv2.imwrite(path, heatmap)
    heatmap = 0

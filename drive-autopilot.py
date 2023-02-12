import sys
from lib.camera.camera import makePhoto
from lib.drive.motor import forward, left, right, stop
import numpy as np
from picamera import PiCamera
from keras.models import load_model
import os, cv2
from lib.camera.preprocess import img_preprocess, imread

camera = PiCamera()

drivePath = "./drive/"

if(os.path.exists(drivePath) == False):
  os.mkdir(drivePath)

currentDriveSeqPath = drivePath + "drive_" + str(len(next(os.walk(drivePath))[1])+1) + "/"
os.mkdir(currentDriveSeqPath)

model = load_model('../model/lane_navigation_check.h5')

def predict(image)->int:
    Y_pred = model.predict([image])
    for y in Y_pred:
        print(y)
        if (y < 3.1):
            return 1
        elif (y >= 3.1 and y < 3.2):
            return 2
        elif (y >= 3.2110):
            return 3
        else:
            return int(y)

def mapActionToCommand(cmd: int):
    direction = {
        1: "forward",
        2: "left",
        3: "right"
    }
    return direction[cmd]

while 1:
    path = makePhoto(currentDriveSeqPath, camera)
    photo = img_preprocess(imread(path))
    cmd = predict(np.array([photo]))

    debugPath = 'debug'
    if (os.path.exists(debugPath) == False):
        os.mkdir(debugPath)

    index = len(next(os.walk(debugPath))[2])
    debugPath = debugPath + "/" + str(index + 1)  + "_" + mapActionToCommand(cmd) + "_" + str(cmd) + ".jpg"
    camera.capture(debugPath)

    print('command: {0} = {1}'.format(cmd, mapActionToCommand(cmd)))
    if(cmd == 1):
        forward(0.5)
        stop()
    if(cmd == 2):
        left(0.5)
        stop()
    if(cmd == 3):
        right(0.5)
        stop()

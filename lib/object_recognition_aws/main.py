from picamera import PiCamera
from time import sleep
import os
from rekognition import recognize_img
from lib.camera.camera import makePhoto
from lib.text_to_speech.text_to_speech import readText

lastPhotos = []

photosPath = "./photos/"

camera = PiCamera()

if(os.path.exists(photosPath) == False):
  os.mkdir(photosPath)
    
while( True ):
    if(len(lastPhotos) >=10):
        os.remove(photosPath + lastPhotos[0])
        lastPhotos.pop(0)
    
    lastPhotos.append(makePhoto(photosPath, camera))
    
    result = recognize_img(lastPhotos[-1])
    print(result)
    for res in result:
        readText(res)

    sleep(5)

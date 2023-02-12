import datetime

photosPath = "../../sample/cameraBuffer/"

def makePhoto(path, camera):
    fileName = path + str(datetime.datetime.now()) + ".jpg"
    camera.capture(fileName)
    return fileName
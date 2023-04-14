from picamera import PiCamera
from lib.drive.motor import forward, backward, left, right, stop
from lib.camera.camera import makePhoto
import json
import os

camera = PiCamera()

seqJson = {"sequence": []}

sequencesPath = "./sequences/"

if(os.path.exists(sequencesPath) == False):
  os.mkdir(sequencesPath)

currentSeqPath = sequencesPath + "sequence_" + str(len(next(os.walk(sequencesPath))[1])+1) + "/"
os.mkdir(currentSeqPath)

while 1:
    cmd = input()
    print(cmd)
    print(seqJson["sequence"])
    currentIteration = {}
    currentIteration["photo"] = makePhoto(currentSeqPath, camera)
    if(cmd == 'w'):
        currentIteration["action"] = 'forward'
        forward(1)
        stop()
    if(cmd == 's'):
        currentIteration["action"] = 'backward'
        backward(0.5)
        stop()
    if(cmd == 'a'):
        currentIteration["action"] = 'left'
        left(0.5)
        stop()
    if(cmd == 'd'):
        currentIteration["action"] = 'right'
        right(0.5)
        stop()
    if(cmd == 'x'):
        stop()
    if(cmd == 'z'):
        with open(currentSeqPath + "sequence.json", "w") as outfile:
          outfile.write(json.dumps(seqJson, indent=4))
        break
    seqJson["sequence"].append(currentIteration)
    
from lib.drive.motor import forward, backward, left, right, stop

while 1:
    cmd = input()
    print(cmd)

    if(cmd == 'w'):
        forward()
    if(cmd == 's'):
        backward()
    if(cmd == 'a'):
        left()
    if(cmd == 'd'):
        right()
    if(cmd == 'x'):
        stop()
    if (cmd == 'z'):
        stop()
        break

stop()
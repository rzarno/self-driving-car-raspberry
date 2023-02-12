from threading import Thread
from time import sleep

def listen_command(command):
    while command[0] != 'x':
#         put here contant of drive loop
        sleep(.5)

command = ['o']
t = Thread(target=modify_variable, args=(var, ))
t.start()

# listen for break command in main thread
while command[0] != 'x':
    print(command[0])
    command[0] = input()
    sleep(.5)
    
t.join()

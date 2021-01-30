import os

F = 0
inp = ''

while F == 0:
    inp = input('> ')
    #Set cpu frequency to slow
    if inp == 'slow':
        #Min frequency
        os.system("sudo cpupower frequency-set -d 800MHz")
        #Max frequency
        os.system("sudo cpupower frequency-set -u 800MHz")
    #Set cpu frequency to fast
    elif inp == 'fast':
        #Min frequency
        os.system("sudo cpupower frequency-set -d 1.5GHz")
        #Max frequency
        os.system("sudo cpupower frequency-set -u 3GHz")
    #Check the cpu frequency
    elif inp == 'check':
        os.system("cat /proc/cpuinfo | grep MHz")
    #Start the server
    elif inp == 'start':
        os.system("./run.sh")
    #Close the program
    elif inp == 'q':
        exit()

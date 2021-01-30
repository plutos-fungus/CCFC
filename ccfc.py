import os

F = 0
inp = ''

#Just a loop
while F == 0:
    inp = input('> ')
    #Set CPU frequency to slow
    if inp == 'slow':
        #Min frequency
        os.system("sudo cpupower frequency-set -d 800MHz")
        #Max frequency
        os.system("sudo cpupower frequency-set -u 800MHz")
    #Set CPU frequency to fast
    elif inp == 'fast':
        #Min frequency
        os.system("sudo cpupower frequency-set -d 1.5GHz")
        #Max frequency
        os.system("sudo cpupower frequency-set -u 3GHz")
    #Dissable 4 CPU cores
    #Needs sudo su for some reason :(
    elif inp == 'dis':
        os.system("echo 0 > /sys/devices/system/cpu/cpu1/online")
        os.system("echo 0 > /sys/devices/system/cpu/cpu2/online")
        os.system("echo 0 > /sys/devices/system/cpu/cpu3/online")
        os.system("echo 0 > /sys/devices/system/cpu/cpu4/online")
    #Enables 4 CPU cores
    #Also needs sudo su for some reason :(
    elif inp == 'ena':
        os.system("echo 1 > /sys/devices/system/cpu/cpu1/online")
        os.system("echo 1 > /sys/devices/system/cpu/cpu2/online")
        os.system("echo 1 > /sys/devices/system/cpu/cpu3/online")
        os.system("echo 1 > /sys/devices/system/cpu/cpu4/online")
    #Check the CPU frequency
    elif inp == 'check':
        os.system("cat /proc/cpuinfo | grep MHz")
    #Start the server
    #The java file has to be in the same folder as this script
    elif inp == 'start':
        os.system("./run.sh")
    #Close the program
    elif inp == 'q':
        exit()

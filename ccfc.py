import os
import subprocess

F = 0
inp = ''

print("Commands:")
print("slow  >   Makes the CPU to utilize a slower frequency")
print("fast  >   Makes the CPU to utilize a faster frequency")
print("dis   >   Dissables 4 CPU cores")
print("ena   >   Enables the 4 dissabled cores")
print("check >   Checks the CPU frequency for every CPU thread")
print("start >   Starts the Java Paper Spigot Minecraft server")
print("q     >   Quits the Python script")
print("h     >   Help")

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
    #Doesn't work right now
    elif inp == 'dis':
        subprocess.call(['sh', './dissable.sh'])
        #os.system("./dissable.sh")

    #Enables 4 CPU cores
    #Also needs sudo su for some reason :(
    #Doesn't work right now
    elif inp == 'ena':
        subprocess.call(['sh', './enable.sh'])
        #os.system("./enable.sh")

    #Check the CPU frequency
    elif inp == 'check':
        #Frequency pr. CPU thread
        print("Frequency pr. CPU thread")
        os.system("cat /proc/cpuinfo | grep MHz")
        #Amount of CPU threads online
        print("Amount of CPU threads online")
        os.system("grep 'processor' /proc/cpuinfo")

    #Start the server
    #The java file has to be in the same folder as this script
    elif inp == 'start':
        subprocess.call(['sh', './run.sh'])
        #os.system("./run.sh")

    #Close the script
    elif inp == 'q':
        exit()

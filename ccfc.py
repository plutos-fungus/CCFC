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
    if inp == "slow" or inp == "s":
        #Min frequency
        os.system("sudo cpupower frequency-set -d 800MHz")
        #Max frequency
        os.system("sudo cpupower frequency-set -u 800MHz")

    #Set CPU frequency to fast
    elif inp == "fast" or inp == "f":
        #Min frequency
        os.system("sudo cpupower frequency-set -d 2GHz")
        #Max frequency
        os.system("sudo cpupower frequency-set -u 3.8GHz")

    #Dissable 4 CPU cores
    elif inp == "dis" or inp == "d":
        subprocess.call(['sh', './dissable.sh'])
        #os.system("./dissable.sh")

    #Enables 4 CPU cores
    elif inp == "ena" or inp == "e":
        subprocess.call(['sh', './enable.sh'])
        #os.system("./enable.sh")

    #Check the CPU frequency
    elif inp == "check" or inp == "c":
        #Frequency pr. CPU thread
        print("Frequency pr. CPU thread")
        os.system("cat /proc/cpuinfo | grep MHz")
        #Amount of CPU threads online
        print("Amount of CPU threads online")
        os.system("grep 'processor' /proc/cpuinfo")

    #Start the server
    #The java file has to be in the same folder as this script
    elif inp == "start" or inp == "ss":
        subprocess.call(['sh', './run.sh'])
        #os.system("./run.sh")

    elif inp == "help" or inp == "h":
        print("Commands:")
        print("s or slow  >   Makes the CPU to utilize a slower frequency")
        print("f or fast  >   Makes the CPU to utilize a faster frequency")
        print("d or dis   >   Dissables 4 CPU cores")
        print("e or ena   >   Enables the 4 dissabled cores")
        print("c or check >   Checks the CPU frequency for every CPU thread")
        print("S or start >   Starts the Java Paper Spigot Minecraft server")
        print("q     >   Quits the Python script")
        print("h     >   Help")

    #Close the script
    elif inp == "q":
        exit()

import os

F = 0
inp = ''

#Just a loop
while F == 0:
    inp = input('> ')
    print("Commands:")
    print("slow  >   Makes the CPU to utilize a slower frequency")
    print("fast  >   Makes the CPU to utilize a faster frequency")
    print("dis   >   Dissables 4 CPU cores")
    print("ena   >   Enables the 4 dissabled cores")
    print("check >   Checks the CPU frequency for every CPU thread")
    print("start >   Starts the Java Paper Spigot Minecraft server")
    print("q     >   Quits the Python script")

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
        os.system("./dissable.sh")
    #Enables 4 CPU cores
    #Also needs sudo su for some reason :(
    #Doesn't work right now
    elif inp == 'ena':
        os.system("./enable.sh")
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

#Import needed libs
import winsound
import time

#Function to get and play th windows sound
def windowsSound():
    winsound.PlaySound("Sound2.wav", winsound.SND_ASYNC)

#Function to play the windows sound every half a second on a loop
def Repeatstuff():
    while True:
        time.sleep(0.5)
        windowsSound()


#Prints directions to quit
print("Press ctrl + C to close program. Thank you.")

#calls function
Repeatstuff()


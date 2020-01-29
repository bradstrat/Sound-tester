import winsound
import time

def yumsoundyeet():
    winsound.PlaySound("Sound2.wav", winsound.SND_ASYNC)


def beautifulHell():
    while True:
        time.sleep(0.5)
        yumsoundyeet()



print("Press ctrl + C to close program. Thank you.")
beautifulHell()


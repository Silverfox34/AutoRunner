#from pynput.keyboard import Key, Controller
import time
import pydirectinput


def main():
    mainLogic()
    
        
def mainLogic():

    while True:
        

        pydirectinput.keyDown('w')
        time.sleep(3600)
        pydirectinput.keyUp('w')


if __name__ == "__main__":
    main()
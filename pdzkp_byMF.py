from pynput.keyboard import Key, Controller
import time
import pydirectinput


def main():
    mainLogic()
    
        
def mainLogic():
    
    keyboard = Controller()

    
    
    while True:
        

        pydirectinput.keyDown('w')
        time.sleep(1)
        pydirectinput.keyUp('w')


if __name__ == "__main__":
    main()
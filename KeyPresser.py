from pynput.keyboard import Key, Controller
import time
from pynput import keyboard as kb
import os

import pydirectinput






def main():
    print('Main process started')
    keyboard = Controller()

    
    
    while True:
        

        pydirectinput.keyDown('w')
        time.sleep(1)
        pydirectinput.keyUp('w')
        




def mainLogic():
    pass
    


def listeningThread():
    myListener = kb.Listener(on_press = customListenerOnPress, on_release=customListenerOnRelease)
    myListener.start()
    myListener.join()


def customListenerOnRelease(key : Key):
        if("pressed-{0}".format(key) == 'pressed-\'s\'' or key == Key.shift):
            os._exit(1)

def customListenerOnPress(key : Key):
    print("pressed-{0}".format(key))
        


        
    
    
    
                        
#hm = pyWinhook.HookManager()
#hm.KeyDown = OnKeyboardEvent
#hm.HookKeyboard()




if __name__ == "__main__":
    main()
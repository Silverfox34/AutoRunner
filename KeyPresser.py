from pynput.keyboard import Key, Controller
import time
from pynput import keyboard as kb
import os
#import pyWinhook as pyWinhook






def main():
    print('Main process started')
    keyboard = Controller()
    
    #KeyPresser soll KeypresserStarter mit conda python starten und auf die Inputs hören
    
    

    while(True):
        with keyboard.pressed('w'):
            #
            time.sleep(0.05)
            keyboard.release('w')




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
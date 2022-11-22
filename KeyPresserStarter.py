import pythoncom as pc
import subprocess
import os
from pyWinhook import HookManager
import pydirectinput
import signal





myProcess = None

def main():
    pc.PumpMessages()



def OnKeyboardEvent(event):
    global myProcess
   
    print(event.Key)

    if(event.Key == 'Escape'):
        if(myProcess != None):
            os.kill(myProcess.pid, signal.SIGINT) 
            myProcess.terminate()
            myProcess.kill()
            myProcess = None

        os._exit(1)

    
    
    if(event.Key == 'Oem_Plus'):  
        if(myProcess == None):    
            myProcess = subprocess.Popen("python KeyPresser.py")

    if((event.Key == 'S' or event.Key == 'Lshift') and myProcess != None):
        print('process stopped')
        myProcess.kill()
        myProcess = None
        pydirectinput.keyUp('w')
        

    return True


hm = HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()



if __name__ == "__main__":
    
    pc.PumpMessages()
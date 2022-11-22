import pythoncom as pc
import subprocess
import os
from pyWinhook import HookManager


#

myProcess = None

def main():
    pc.PumpMessages()



#

def OnKeyboardEvent(event):
    global myProcess

    if(event.Key == 'Escape'):
        if(myProcess != None):
            myProcess.kill()
            myProcess = None

        os._exit(1)

    print(event.Key)
    
    if(event.Key == 'Oem_Plus'):
       
        if(myProcess == None):    
            myProcess = subprocess.Popen("python KeyPresser.py")

    if((event.Key == 'S' or event.Key == 'Lshift') and myProcess != None):
        myProcess.kill()
        myProcess = None
        
    #+wwwwwws

    return True


hm = HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()

                        






if __name__ == "__main__":
    
    pc.PumpMessages()
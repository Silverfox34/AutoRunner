import pythoncom as pc
import subprocess
import os
from pyWinhook import HookManager
import pydirectinput
import signal


#Automatic Key Presser
#Made by Moritz Fesseler on 22.11.2022
#Moritz.Fesseler@gmx.de



myProcess = None

def main():
    pc.PumpMessages()



def OnKeyboardEvent(event):
    global myProcess
   
    print(event.Key)

    if(event.Key == 'Escape'):
        if(myProcess != None):
            os.system("taskkill /F /im pdzkp_byMF.exe")
            myProcess = None

        
        os._exit(1)

    
    
    if(event.Key == 'Oem_Plus'):
        print("main process started with pressing oem_plus" ) 
        if(myProcess == None):    
            myProcess = subprocess.Popen("pdzkp_byMF.exe")

    if((event.Key == 'S' or event.Key == 'Lshift') and myProcess != None):
        print('process stopped')

        os.system("taskkill /F /im pdzkp_byMF.exe")
        pydirectinput.keyUp('w')
        myProcess = None
        

    
    return True


    


hm = HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()



if __name__ == "__main__":
    
    pc.PumpMessages()
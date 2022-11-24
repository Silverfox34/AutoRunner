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


def OnKeyboardEvent(event):
    global myProcess
   
    print(event.Key)

    if(event.Key == 'Escape'):
        if(myProcess != None):
            os.system("taskkill /F /im pdzkp_byMF.exe")
            myProcess = None

        
        os._exit(1)

    
    
    if(event.Key == 'Oem_Plus'):
        print("Main process started with pressing plus" ) 
        if(myProcess == None):    
            myProcess = subprocess.Popen("pdzkp_byMF.exe")

    if((event.Key == 'S' or event.Key == 'Lshift' or event.Key == 'Tab') and myProcess != None):
        

        os.system("taskkill /F /im pdzkp_byMF.exe")
        pydirectinput.keyUp('w')
        myProcess = None
        print('The program stopped. To end it, press ESC.\nTo continue the program, press plus again.')

    
    return True


    


hm = HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()



if __name__ == "__main__":
    print('Welcome to the Autorunner-Tool\nThis program will automatically press and hold the \'w\'-button in-game for you!\n\nOperation manual:\n - Start: press plus (+)\n - Stop: press shift OR s OR Tab\n - End: press ESC\n----------\n')
    pc.PumpMessages()

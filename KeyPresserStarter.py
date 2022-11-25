import pythoncom as pc
import subprocess
import os
from pyWinhook import HookManager
import pydirectinput
import time
import mouse


#Automatic Key Presser
#Made by Moritz Fesseler on 22.11.2022
#Moritz.Fesseler@gmx.de



myProcess_walking = None
myProcess_clicking_flag = False


def OnKeyboardEvent(event):
    global myProcess_walking
    global myProcess_clicking_flag
   
    print(event.Key)

    if(event.Key == 'End'):
        if(myProcess_walking != None and myProcess_clicking_flag == False):
            os.system("taskkill /F /im pdzkp_byMF.exe")
            myProcess_walking = None
            print("Program has been terminated successfully while walking.")
            

        if(myProcess_walking == None and myProcess_clicking_flag != False):
            os.system("taskkill /F /im pdzkp_byMF_roast.exe")
            myProcess_clicking_flag = False
            print("Program has been terminated successfully while clicking.")
               

        
        print("Bye bye !")
        time.sleep(2) 
        os._exit(1)


    if((event.Key == 'S' or event.Key == 'Lshift' or event.Key == 'Tab') and myProcess_walking != None and myProcess_clicking_flag == False): 
        os.system("taskkill /F /im pdzkp_byMF.exe")     
        pydirectinput.keyUp('w')
        myProcess_walking = None
        print('The walking process stopped. To end the program, press End.\nTo continue the program, press \'Insert\' or \'Delete\' again.')



    if((event.Key == 'Lshift' or event.Key == 'S' or event.Key == 'W' or event.Key == 'D' or event.Key == 'A' or event.Key == 'Tab') and myProcess_walking == None and myProcess_clicking_flag != False): 
        #os.system("taskkill /F /im pdzkp_byMF_roast.exe")     
        mouse.release(button='left')
        myProcess_clicking_flag = False
        print('The clicking process stopped. To end the program, press End.\nTo continue the program, press \'Insert\' or \'Delete\' again.')



    if(event.Key == 'Insert' and myProcess_walking == None and myProcess_clicking_flag == False):
        print("Walking process started with pressing \'Insert\'" )    
        myProcess_walking = subprocess.Popen("pdzkp_byMF.exe")



    if(event.Key == 'Delete' and myProcess_walking == None and myProcess_clicking_flag == False):
        print("Clicking process started with pressing \'Delete\'" )    
        mouse.press(button='left')
        myProcess_clicking_flag = True

    
    if(myProcess_clicking_flag != False and myProcess_walking != None):
        print('FATAL ERROR OCCURED !\nThe program is ending now')
        time.sleep(2)
        os._exit(1)



    
    return True
    


hm = HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()




if __name__ == "__main__":
    print('Welcome to the Autorunner-Tool\nThis program will automatically press and hold the \'w\'-button or left mouse button in-game for you!\n\nOperation manual:\n - Start walking: press \'Insert\'\n - Start holding left mouse: press\'Delete\'\n - Stop program: press shift OR s OR Tab\n - End program: press End\n----------\n')
    pc.PumpMessages()

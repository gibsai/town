import numpy as np
import cv2
import time
import pyautogui
import os
from found_click import Search

#from upgrade import open_terminal
startTime = time.time()


#Create list of methods to use
methods = [cv2.TM_CCOEFF_NORMED,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF_NORMED]

method = cv2.TM_CCOEFF_NORMED 

#path='/home/user01/Documents/Town/resources/Arena/'
#name='skip_battle.png'
def check_open(path,name):
    template = cv2.imread('{}{}'.format(path,name),0)
    isvisible = False #start with a open variable as False

    pyautogui.screenshot("/home/user01/Pictures/screen.png")    #Take screenshot
    img = cv2.imread('/home/user01/Pictures/screen.png',0)      #Read screenshot and convert to black and white with 0 option
    img2 = img.copy()                                           #Copy to another variable so can edit
    os.system ("rm /home/user01/Pictures/screen*.png")          #Delete screenshot

    #Check to if menu icon is visible
    #Get result of matchtemplate method which tries to match to the open terminal photo 
    result = cv2.matchTemplate(img2, template, method)             
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)  #Put values into variables

    #Check to see if there is a match from the matchTemplate method
    #Any max value is over 90% is considered a match. We are matching
    #first against the open menu template
    if max_val >= 0.9:  #If max value is over 90%
        isvisible=True       #then true
    else:               #If max value is under 90%
        isvisible=False      #then false

    return(isvisible)

#The purpose of this function is to wait until the menu can be seen on the screen
#When the full script is running the menu icon should always be visible unless loading
def waitforopen(path,name):
    runs = 0
    wU=True             #Create a variable wU representing "Wait Until"
    isvisible = False   #Create open_menu variable which will hold True False value if the menu is open or not
    while wU==True:     #wU remains true until the condition happens, then it will change to False
        #Check to see if the menu is open by running check_menu function and
        #Returning value to open_menu variable
        print("searching for {}".format(name))
        isvisible=check_open(path,name)                                  
        if isvisible == True: #If the menu is open
            wU = False #Turn the wU variable to false so doesn't run again
            print("Found {}".format(name))
        else:
            time.sleep(2) #wait two seconds to check again


def check_home():
    path = '/home/user01/Documents/Town/resources/'
    name = 'homepage.png'
    template = cv2.imread('{}{}'.format(path,name),0)
    method = cv2.TM_CCOEFF_NORMED
    note1 = "{} found".format(name)
    note2 = "{} not found".format(name)
    print("\nSearching for {}".format(name))
    click = Search(template,method,note1,note2)
    return(click)

#check_home()

#waitforopen(file,name)
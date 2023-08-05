import numpy as np
import cv2
import time
import pyautogui as pg
import os

pg.sleep(3)
startTime = time.time()

#The purpose of this method is to have a template to click
#if a template is found. Different methods can be create with this
#and provide their own template and method (need to flesh out adding list of methods)
def Search(template,method,note1,note2):
    #print("searching for red X")
        
    pg.screenshot("/home/user01/Pictures/screen.png")
    img = cv2.imread('/home/user01/Pictures/screen.png',0)
    img2 = img.copy()
    h, w = template.shape
    
    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    location = max_loc
    
    if max_val >= 0.9: #Click if 90% accurate
    	#print(location[0],location[1])
        time.sleep(1)
        #pg.click(location[0],location[1],3)
        found = True
    else:
        print(note2)
        found = False

    bottom_right = (location[0] + w, location[1] + h)    

    os.system ("rm /home/user01/Pictures/screen*")
    time.sleep(2)
    return(found,location)

#The purpuse of this method is to click on the red X
#when it appears as an add.
def Found_X():
    template = cv2.imread('/home/user01/Documents/Town/resources/X.png',0)
    method = cv2.TM_CCOEFF_NORMED
    note1 = "X found"
    note2 = "No X found"
    print("Searching for X")
    click = Search(template,method,note1,note2)
    if click[0] == True:
        pg.click(click[1])

# Found_X()

def Found_redback():
    path = '/home/user01/Documents/Town/resources/'
    name = 'red_back.png'
    template = cv2.imread('{}{}'.format(path,name),0)
    method = cv2.TM_CCOEFF_NORMED
    note1 = "{} found".format(name)
    note2 = "{} not found".format(name)
    print("\nSearching for {}".format(name))
    click = Search(template,method,note1,note2)
    if click[0] == True:
        pg.click(click[1])

def Found_yellowback():
    path = '/home/user01/Documents/Town/resources/'
    name = 'yellow_back.png'
    template = cv2.imread('{}{}'.format(path,name),0)
    method = cv2.TM_CCOEFF_NORMED
    note1 = "{} found".format(name)
    note2 = "{} not found".format(name)
    print("\nSearching for {}".format(name))
    click = Search(template,method,note1,note2)
    if click[0] == True:
        pg.click(click[1])

def found_popup():
    Found_X()
    pg.sleep(3)
    Found_redback()
    pg.sleep(3)
    Found_yellowback()
    pg.sleep(3)



#found_popup()
import numpy as np
import cv2
import time
import pyautogui as pg
import os
from found_click import Search
from match import waitforopen , check_open

pg.sleep(3)

path = '/home/user01/Documents/Town/resources/'

method = cv2.TM_CCOEFF_NORMED 

def check_popup():
    print("checking for Pop ups")
    #Set template and create list
    temp01 = cv2.imread(path+'yellow_back.png',0)
    temp02 = cv2.imread(path+'red_back.png',0)
    temp03 = cv2.imread(path+'X.png',0)
   

    templates = [temp01,temp02,temp03]

    for template in templates:
        pg.screenshot("/home/user01/Pictures/screen.png")
        img = cv2.imread('/home/user01/Pictures/screen.png',0)
        img2 = img.copy()
        os.system ("rm /home/user01/Pictures/screen.png")
        
        #cv2.imshow('Template',template) #Show Image
        #cv2.waitKey(0) #Wait until any key is pressed
        #cv2.destroyAllWindows() #Destroy all windows
        
        result = cv2.matchTemplate(img2, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]: #These are inverted so need to use minimum location
            location = min_loc
            #print(min_val)
        else:
            location = max_loc
            #print(min_val)
        
        if max_val >= 0.9: #Click if 90% accurated
        	#print(location[0],location[1])
        	pg.click(location[0],location[1],5)
        else:
        	break

            #bottom_right = (location[0] + w, location[1] + h)    
            #cv2.rectangle(img2, location, bottom_right, 255, 5)
            #cv2.rectangle(img2, location, bottom_right, 0,0,255)
            #cv2.imshow('Match', img2)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()

        
        
        
    #print(time.time() - startTime)

#check_popup()

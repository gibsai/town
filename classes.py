import numpy as np
import cv2
import time
import pyautogui
import os

method = cv2.TM_CCOEFF_NORMED

class Match:

	#method = cv2.TM_CCOEFF_NORMED
	
	def __init__(self, path, name, method):
		self.path = path
		self.name = name
		self.method = method
		#self.template = path+name
		
	def check_open(self):
		template = cv2.imread('{}{}'.format(self.path,self.name),0)
		isvisible = False #start with a open variable as False
		pyautogui.screenshot("/home/user01/Pictures/screen.png")    #Take screenshot
		img = cv2.imread('/home/user01/Pictures/screen.png',0)      
		img2 = img.copy()                             #Copy to another variable so can edit
		os.system ("rm /home/user01/Pictures/screen*.png")          
		result = cv2.matchTemplate(img2, template, self.method)             
		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)  #Put values into variables
		print("\nSearching for {}".format(self.name))
		#Check to see if there is a match from the matchTemplate method
		#Any max value is over 90% is considered a match. We are matching
		#first against the open menu template
		if max_val >= 0.9:  #If max value is over 90%
			isvisible=True       #then true
		else:               #If max value is under 90%
        		isvisible=False      #then false

		return(isvisible)

path_arena = '/home/user01/Documents/Town/resources/Arena/'

OpenArena = Match(path_arena,'arena1.png', cv2.TM_CCOEFF_NORMED)

SkipBattle = Match(path_arena,'skip_battle.png', cv2.TM_CCOEFF_NORMED)

#print(type(SkipBattle.template))
SkipBattle.method

print(OpenArena.check_open())

def arena_open():
    name = 'arena1.png'
    template = cv2.imread('{}{}'.format(path,name),0)
    method = cv2.TM_CCOEFF_NORMED
    note1 = "{} found".format(name)
    note2 = "{} not found".format(name)
    print("\nSearching for {}".format(name))
    Found_Click(template,method,note1,note2)


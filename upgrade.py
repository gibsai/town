#!/usr/bin/env python3

import numpy as np
import cv2
import time
import os
import pyautogui, sys
import pandas as pd
from datetime import datetime
import time
import random
from match import openBrave, find_brave, waitforbrave, open_terminal, click_guac, waitformenu

#time.sleep(5)
###########
#Variables#
###########
browser_coord = 30,130

#Read IP list to pandas then convert to list of tupes
IPs = pd.read_csv("~/Documents/brave-swarm/IPs.csv", index_col=False)
#Set the IP column to be the index
IPs.set_index('IP',inplace=True)
#Convert pandas dataframe to list of tuples
IPs = IPs.to_records()
IPs = list(IPs)

#Creat template to find to see if terminal is open
Oterminal = cv2.imread('/home/user01/Pictures/terminal.png',0)
Bterminal = cv2.imread('/home/user01/Pictures/terminal2.png',0)
Omenu = cv2.imread('/home/user01/Pictures/menu.png',0)


#Create list of methods to use
method = cv2.TM_CCOEFF_NORMED            

#Create empty lists to put in date and True/False. They will determine if 
#updates (UpToday) and upgrades (UgToday) have taken place today.
#Starts as today's date and False
today = datetime.today().strftime('%Y-%m-%d')
UpToday = [today,False]
UgToday = [today,False]

###########
#FUNCITONS#
###########
#The purpose of this function is to check to see if the menu icon is visible
def check_menu():
	menu = False #start with a menu variable as False

	pyautogui.screenshot("/home/user01/Pictures/screen.png")	#Take screenshot
	img = cv2.imread('/home/user01/Pictures/screen.png',0) 		#Read screenshot and convert to black and white with 0 option
	img2 = img.copy() 											#Copy to another variable so can edit
	os.system ("rm /home/user01/Pictures/screen*.png")			#Delete screenshot

	#Check to if menu icon is visible
	#Get result of matchtemplate method which tries to match to the open terminal photo 
	result = cv2.matchTemplate(img2, Omenu, method)				
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)	#Put values into variables

	#Check to see if there is a match from the matchTemplate method
	#Any max value is over 90% is considered a match. We are matching
	#first against the open menu template
	if max_val >= 0.9:	#If max value is over 90%
		menu=True		#then true
	else:				#If max value is under 90%
		menu=False		#then false

	return(menu)

#The purpose of this function is to wait until the menu can be seen on the screen
#When the full script is running the menu icon should always be visible unless loading
def waitformenu():
	runs = 0
	wU=True				#Create a variable wU representing "Wait Until"
	open_menu = False	#Create open_menu variable which will hold True False value if the menu is open or not
	while wU==True:		#wU remains true until the condition happens, then it will change to False
		#Check to see if the menu is open by running check_menu function and
		#Returning value to open_menu variable
		open_menu=check_menu()									
		if open_menu == True: #If the menu is open
			wU = False #Turn the wU variable to false so doesn't run again
			print("Found menu")
		else:
			runs =runs+1    #add 1 to runs
			if runs == 15:  #if brave has not been found for 30 runs
				openBrave()
				pyautogui.sleep(5)
				pyautogui.click(155,75) #hit refresh
				runs = 0 #reset runs to 0
			print("Waiting for client menu. Run #: {}".format(runs))
			time.sleep(2) #wait two seconds to check again
			
#Purpose of this function is to check to see if there is already
#a terminal open. Returns #1. True/False #2. Location
def check_terminal():
	waitformenu()
	pyautogui.screenshot("/home/user01/Pictures/screen.png")	#Take screenshot
	img = cv2.imread('/home/user01/Pictures/screen.png',0) 		#Read screenshot and convert to black and white with 0 option
	img2 = img.copy() 											#Copy to another variable so can edit
	os.system ("rm /home/user01/Pictures/screen*.png")			#Delete screenshot


	#Check to if terminal is open on top
	result = cv2.matchTemplate(img2, Oterminal, method) 		#Get result of matchtemplate method which tries to match to the open terminal photo 
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)	#Put values into variables

	#Check to see if there is a match from the matchTemplate method
	#Any max value is over 90% is considered a match. We are matching
	#first against the open terminal template
	if max_val >= 0.9: 				#If max value is over 90%
		terminal=True 				#If a 90% match terminal equals true
		location = max_loc 			#If a 90% match location equals max location
		return(terminal,location)	#If a match return the value of terminal and the location

	#If not 90% accurate then there isn't a terminal window open in the foreground
	#so will check to see if there is one open in background
	elif max_val <= 0.9:
		#First must run the matchtemplate method which tries to match to the CLOSED terminal photo
		Nresult = cv2.matchTemplate(img2, Bterminal, method) #The result will be held in Nresult variable
		Nmin_val, Nmax_val, Nmin_loc, Nmax_loc = cv2.minMaxLoc(Nresult) #Put values of Nresult into seperate variables

		if Nmax_val >= 0.9: 			#Checks to see there is 90% match of CLOSED terminal template
			terminal=True 				#If a 90% match terminal equals true
			Nlocation = Nmax_loc			#If a 90% match location equals max location
			return(terminal,Nlocation)	#If a match return the value of terminal and the location
		
		#If neither the open or closed terminal template have found a match then
		#a terminal windows is not open so will close the statement
		else:
			terminal=False				#Since no match has been found terminal equals False
			return(terminal,"none")		#Since no match has been found only False needs to be returned
										#But need to pass something as the run_update function expections
										#more then one object being returned

#The purpose of this function is to open the terminal
# def open_terminal():
# 	#menu
# 	pyautogui.moveTo(90,110,3)
# 	pyautogui.sleep(1)
# 	pyautogui.click()
# 	pyautogui.write("Mate terminal")
# 	pyautogui.press("enter")

#The purpose of this function is to run updates
#Resources are the check_terminal & open terminal functions
def run_update():
	#Run the check terminal function which returns a list of True or False into a variable
	term=check_terminal()
	open_term = term[0] 	#Creates True or False variable if open or not
	location=term[1]		#Give location

	#Mate terminal
	#If the terminal is open click on the location
	if open_term == True:
		pyautogui.click(location[0],location[1],5)
	#If the terminal is not open open the terminal
	else:
		open_terminal()

	pyautogui.sleep(2)
	pyautogui.write("sudo apt-get update")
	pyautogui.press("enter")
	pyautogui.sleep(5)

	return(True)

#The purpose of this function is to run updates
#Its assumed that update has just taken place so terminal is in foreground
def run_upgrade():

	#Run the check_terminal function which checks to see if there is already
	#a terminal open. Return #1. True/False #2. Location of terminal 
	term=check_terminal()	#Runs the function
	open_term = term[0]		#Creates True or False variable if open or not
	location=term[1]		#Give location of terminal
	
	#If the terminal is open click on it (will be on screen or on menu bar)
	if open_term == True:
		pyautogui.click(location[0],location[1],5)
	else:
		open_terminal() #If a terminal window isnt open it will open one with the open_terminal function

	pyautogui.sleep(2)
	pyautogui.write("sudo apt upgrade -y")
	pyautogui.press("enter")
	pyautogui.sleep(1)

def close_brave():
    #Wait for client brave to open
    waitformenu()
    #if find_brave()[0] == True:
    waitforbrave()
    #Click on close
    pyautogui.click(1005, 140,1)
    pyautogui.sleep(2)
    #Click on "Close all"
    pyautogui.click(645,395,3)


#############
#Run Program#
#############

def up_and_grade():

	#Script will be running all the time. Will update the day every time it loops
	#to see if it has updated tooday
	date = datetime.today().strftime('%Y-%m-%d')	#Create variable of today's date
	UpToday[0] = date								#The first item of the list create previously is the date	
	
	#Will check the UpToday list to see if first entry is today's date and if second entry is true or false
	#If UpToday list first item is today's date and the second is fals itterate through containers
	if UpToday[0] == date and UpToday[1] == False:	
		for ports in IPs:									#IPs - list of tuples holding IP:Port
			cur_con = str(ports[0]) + ":" + str(ports[1])	#Create cur_con (current container) variable
			#Move to then click on host browser
			pyautogui.moveTo(browser_coord)
			pyautogui.click()

			#Move and click on search bar
			pyautogui.moveTo(745,75,3)
			pyautogui.click()
				      
			#Write in IP
			pyautogui.write(cur_con)
			pyautogui.press("enter")
			pyautogui.sleep(5)

			click_guac() #In case add has been click on open the guacomole client tab

			close_brave() #Close brave so upgrade can begin

			#Run update returns True when run
			update = run_update()
		
		UpToday[0] = date
		UpToday[1] = True

	#Check list to see if updates & upgrades have been completed today
	#First item of UpToday /UgToday list is date, second item is True or False
			
	if UpToday[0] == date and UpToday[1] == True\
	and UgToday[0] == date and UgToday[1] == False:
		for ports in IPs:
			cur_con = str(ports[0]) + ":" + str(ports[1])
			#Move to then click on browser
			pyautogui.moveTo(browser_coord)
			pyautogui.click()

			#Move and click on search bar
			pyautogui.moveTo(745,75,3)
			pyautogui.click()
				      
			#Write in IP
			pyautogui.write(cur_con)
			pyautogui.press("enter")
			pyautogui.sleep(5)

			run_upgrade()


		UgToday[0] = date
		UgToday[1] = True

#up_and_grade()

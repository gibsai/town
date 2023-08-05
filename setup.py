import pyautogui, sys
import pandas as pd
from datetime import datetime
import time
import os
import random

print('Press Ctrl-C to quit.')

#Variables
browser_coord = 30,130
search_coord =  "510,75,5"
home_coord = 190,200
settings_coord = 1000,200
history_coord = 755,275
menu_coord = 115,110
rsettings_coord = 840,200
internet_coord = 145,325
internetb_coord = 300,325
brave_coord = 300,175

#screen = 75,125 to 1020,735
xrand = 75,1020
yrand = 225,735

IPs = pd.read_csv("~/Desktop/IPs.csv", index_col=False)
n=-1
IPlist = IPs["IP"].tolist()

for i in IPlist:
	n=n+1
	#Move to then click on browser
	pyautogui.moveTo(browser_coord)
	pyautogui.click()
	
	#Move and click on search bar
	pyautogui.moveTo(510,75,3)
	pyautogui.click()
		      
	#Write in IP
	pyautogui.write(str(IPs.at[n,"IP"]) + ":" + str(IPs.at[n,"Port"]))
	pyautogui.press("enter")
	pyautogui.sleep(2)
	
	#Move to middle and click
	for i in range(3):
		pyautogui.moveTo(random.randrange(75,1020),random.randrange(125,735),3)
		pyautogui.click(clicks=1)
		pyautogui.sleep(3)

	#RUN SCRIPT TO OPEN BRAVE ON BOOT	
	#search
	#menu
	pyautogui.moveTo(115,110,1)
	pyautogui.sleep(1)
	pyautogui.click()
	pyautogui.moveTo(135,140,1)
	pyautogui.sleep(1)
	pyautogui.click()
	pyautogui.write("Mate terminal")
	pyautogui.moveTo(275,180,1)
	pyautogui.click()
	
	pyautogui.sleep(2)
	pyautogui.write("bash ~/resources/first.sh")
	pyautogui.press("enter")
	
	#Remove screen saver
	#menu
	pyautogui.moveTo(115,110,1)
	pyautogui.sleep(1)
	pyautogui.click()
	#search
	pyautogui.moveTo(135,140,1)
	pyautogui.sleep(1)
	pyautogui.click()
	pyautogui.write("screensaver")
	pyautogui.moveTo(275,180,1)
	pyautogui.click()
	#unclick option
	pyautogui.moveTo(267,635,1)
	pyautogui.click()
	pyautogui.moveTo(267,666,1)
	pyautogui.click()
	
	#CONFIGURE BRAVE BROWSER
	#menu
	pyautogui.moveTo(115,110,1)
	pyautogui.sleep(1)
	pyautogui.click()
	pyautogui.moveTo(135,140,1)
	pyautogui.sleep(1)
	pyautogui.click()
	pyautogui.write("brave")
	pyautogui.moveTo(275,180,1)
	pyautogui.click()

	#Default browser
	pyautogui.moveTo(750,530,1)
	pyautogui.click()
	pyautogui.sleep(2)

	#Ad settings
	pyautogui.moveTo(425,210,1)
	pyautogui.click()
	pyautogui.write("brave://rewards/")
	pyautogui.press("enter")
	#pyautogui.sleep(2)
	
	#Start using rewards
	pyautogui.moveTo(400,685,3)
	pyautogui.sleep(2)
	pyautogui.click()
	
	#Skip tut
	pyautogui.moveTo(865,280,1)
	pyautogui.click()

	#Move to scroll
	pyautogui.moveTo(1005,290,2)
	#Drag to
	pyautogui.dragTo(1005,345,3,button='left')

	#Turn on ads
	#pyautogui.moveTo(645,275,1)
	#pyautogui.click()
	#Ad settings
	pyautogui.moveTo(575,275,1)
	pyautogui.sleep(1)
	pyautogui.click()

	#Choose ads an hour
	pyautogui.moveTo(575,345,1)
	pyautogui.click()
	#Click on ten
	pyautogui.moveTo(575,615,1)
	pyautogui.click()
	#turn of auto contribute
	pyautogui.moveTo(645,485,1)
	pyautogui.click()	

	#Change new tab when open
	pyautogui.moveTo(425,210,1)
	pyautogui.click()
	pyautogui.write("brave://settings/")
	pyautogui.press("enter")
	pyautogui.moveTo(258,560,1)
	pyautogui.click()

	#Search bar
	pyautogui.moveTo(425,210,1)
	pyautogui.click()
	pyautogui.write("brave://settings/?search=home")
	pyautogui.press("enter")
	
	#Set home
	pyautogui.moveTo(850,485,1)
	pyautogui.click()
	pyautogui.moveTo(500,580,1)
	pyautogui.click()
	pyautogui.write("brave://rewards/")
	pyautogui.press("tab")
	
	#Close brave
	pyautogui.moveTo(1005,45,2)
	pyautogui.click()
	
	time.sleep(5)


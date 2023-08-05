import numpy as np
import cv2
import time
import pyautogui as pg
import os
from match import check_open, waitforopen
from found_click import Search

pg.sleep(3)

path = '/home/user01/Documents/Town/resources/Prize/'
#All the functions to click when found
def click_prize():
	print("Searching for daily prizes")
	name = "prize1.png"
	template = cv2.imread('/home/user01/Documents/Town/resources/Prize/{}'.format(name),0)
	method = cv2.TM_CCOEFF_NORMED
	note1 = "{} found".format(name)
	note2 = "{} not found".format(name)
	print("\nSearching for {}".format(name))
	click = Search(template,method,note1,note2)
	if click[0] == True:
		pg.click(click[1])

def click_reward():
	#path = '/home/user01/Documents/Town/resources/Prize/'
    name = "get_reward.png"
    template = cv2.imread('{}{}'.format(path,name),0)
    method = cv2.TM_CCOEFF_NORMED
    note1 = "{} found".format(name)
    note2 = "{} not found".format(name)
    print("\nSearching for {}".format(name))
    click = Search(template,method,note1,note2)
    if click[0] == True:
        pg.click(click[1])

def click_prizeContinue():
	#path = '/home/user01/Documents/Town/resources/Prize/'
    name="prize_continue.png"
    template = cv2.imread('{}{}'.format(path,name),0)
    method = cv2.TM_CCOEFF_NORMED
    note1 = "{} found".format(name)
    note2 = "{} not found".format(name)
    print("\nSearching for {}".format(name))
    click = Search(template,method,note1,note2)
    if click[0] == True:
        pg.click(click[1])

#All the functions to wait until including the click
def waitfor_reward():
	name = "get_reward.png"
	waitforopen(path,name)
	click_reward()

def waitfor_continue():
	name="prize_continue.png"
	waitforopen(path,name)
	click_prizeContinue()

#The purpose of this function is to put all the methods
#together to check for prizes
def prizes():
	click_prize()
	waitfor_reward()
	waitfor_continue()


prizes()
#The purpose of this is to check for free prizes
# def Found_Prize():
#     #print("Searching for daily prizes")

# 	path = '/home/user01/Documents/Town/resources/Prize/'
#     name = "prize1.png"
#     template = cv2.imread('{}{}'.format(path,name),0)
#     method = cv2.TM_CCOEFF_NORMED
#     note1 = "{} found".format(name)
#     note2 = "{} not found".format(name)
#     print("\nSearching for {}".format(name))
#     click = Search(template,method,note1,note2)
#     if click[0] == True:
#         pg.click(click[1])

#     path = '/home/user01/Documents/Town/resources/Prize/'
#     name = "get_reward.png"
#     template = cv2.imread('{}{}'.format(path,name),0)
#     method = cv2.TM_CCOEFF_NORMED
#     note1 = "{} found".format(name)
#     note2 = "{} not found".format(name)
#     print("\nSearching for {}".format(name))
#     click = Search(template,method,note1,note2)
#     if click[0] == True:
#         pg.click(click[1])

#     path = '/home/user01/Documents/Town/resources/Prize/'
#     name="prize_continue.png"
#     template = cv2.imread('{}{}'.format(path,name),0)
#     method = cv2.TM_CCOEFF_NORMED
#     note1 = "{} found".format(name)
#     note2 = "{} not found".format(name)
#     print("\nSearching for {}".format(name))
#     click = Search(template,method,note1,note2)
#     if click[0] == True:
#         pg.click(click[1])

#     #Close the prize window
#     pg.sleep()
#     Found_X()
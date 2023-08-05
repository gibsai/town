import numpy as np
import cv2
import time
import pyautogui as pg
import os
from found_click import Found_Click
from match import waitforopen , check_open

pg.sleep(3)
startTime = time.time()

path = '/home/user01/Documents/Town/resources/Arena/'

#The purpose of this function is to enter the arena from the main page
def arena_open():
    name = 'arena1.png'
    template = cv2.imread('{}{}'.format(path,name),0)
    method = cv2.TM_CCOEFF_NORMED
    note1 = "{} found".format(name)
    note2 = "{} not found".format(name)
    print("\nSearching for {}".format(name))
    Found_Click(template,method,note1,note2)

#The purpose of this function is to open any chests
def open_chest():
    name = 'arena1.png'
    template = cv2.imread('{}{}'.format(path,name),0)
    method = cv2.TM_CCOEFF_NORMED
    note1 = "{} found".format(name)
    note2 = "{} not found".format(name)
    print("\nSearching for {}".format(name))
    Found_Click(template,method,note1,note2)

#arena_open(path)


def skip_battle():
    print("Beginning Battle")

    name = 'skip_battle.png'
    template = cv2.imread('{}{}'.format(path,name),0)
    method = cv2.TM_CCOEFF_NORMED
    note1 = "{} found".format(name)
    note2 = "{} not found".format(name)
    print("\nSearching for {}".format(name))

    waitforopen(path,name)
    print("clicking on 'skip battle'")
    Found_Click(template,method,note1,note2)

    #The purpose of this is to begin a battle

# skip_battle()

def start_battle():
    print("Beginning Battle")

    name = 'arena_battle.png'
    template = cv2.imread('{}{}'.format(path,name),0)
    method = cv2.TM_CCOEFF_NORMED
    note1 = "{} found".format(name)
    note2 = "{} not found".format(name)
    print("\nSearching for {}".format(name))
    Found_Click(template,method,note1,note2)

    pg.sleep(5)
    #skip_battle(path)

#start_battle(path)

def continue_battle():
    print("Beginning Battle")

    name = 'continue.png'
    template = cv2.imread('{}{}'.format(path,name),0)
    method = cv2.TM_CCOEFF_NORMED
    note1 = "{} found".format(name)
    note2 = "{} not found".format(name)
    print("\nSearching for {}".format(name))

    waitforopen(path,name)
    print("clicking on 'continue'")
    Found_Click(template,method,note1,note2)

# continue_battle()
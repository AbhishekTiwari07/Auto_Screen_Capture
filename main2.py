import numpy as np
import cv2 
import pyautogui 
import time

TAB = 2
KEY = 2
RESET = 30 #(>TAB+KEY*10)

def screenshot(i):
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), 
                        cv2.COLOR_RGB2BGR)
    cv2.imwrite("Scoreboard "+str(i)+".png", image)

def pressKey(i):
    time.sleep(TAB)
    pyautogui.keyDown("tab")
    screenshot(i)
    pyautogui.keyUp("tab")

def char_screenshot(i,j):
    time.sleep(KEY)
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),
                        cv2.COLOR_RGB2BGR)
    cv2.imwrite("P"+str(j)+"-"+str(i)+".png", image)

def char_pressKey(i,j): 
    j = str(j)
    pyautogui.keyDown(j)
    char_screenshot(i,j)
    pyautogui.keyUp(j)

def start():
    i=0
    j=0
    while True:
        for j in range(10):
            char_pressKey(i,j)
        pressKey(i)
        i=(i+1)%10
        time.sleep(RESET)

start()
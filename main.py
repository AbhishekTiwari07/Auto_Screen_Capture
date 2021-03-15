import numpy as np 
import cv2 
import pyautogui 
import time

def screenshot(i):
    image = pyautogui.screenshot() 
    image = cv2.cvtColor(np.array(image), 
                        cv2.COLOR_RGB2BGR) 
    cv2.imwrite("image"+str(i)+".png", image)

def pressKey(i):
    pyautogui.keyDown("tab")
    screenshot(i)
    pyautogui.keyUp("tab")   

def start():
    i=0
    while i<10:
        pressKey(i)
        i=i+1
        time.sleep(5)

start()
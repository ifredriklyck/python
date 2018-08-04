from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():
    replayBtn = (376,386)
    dinosaur = (143,391)
    #box = (158, 382, 238, 446)
    #boxUpperLeftX = (158)
    #boxUpperLeftY = (382)
    #boxLowerRight = (238,446)
    # 212 = x-cordinate to check for tree
    # y-cordinate 410

def restartGame():
    pyautogui.click(Cordinates.replayBtn)
    pyautogui.click(Cordinates.replayBtn)

def pressSpace():
        pyautogui.keyDown('space')
        #time.sleep(0.05)
        print("Jump")
        pyautogui.keyUp('space')

def imageGrab():

    #box = (Cordinates.boxUpperLeft[0],Cordinates.boxUpperLeft[1],Cordinates.boxLowerRight[1],Cordinates.boxLowerRight[0])
    #box = (Cordinates.dinosaur[0]+240,Cordinates.dinosaur[1],Cordinates.dinosaur[1],Cordinates.dinosaur[0])
    #box = ImageGrab.grab(())
    #image = ImageGrab.grab(box)
    #box = (158, 382, 238, 446)
    box = (258, 382, 338, 421)
    image = ImageGrab.grab(bbox=(box))
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return a.sum()

def main():
    restartGame()
    while True:
        if (imageGrab() > 3370):
            #(imageGrab()!=5450):
            pressSpace()
            #time.sleep(0.1)
main()

#pressSpace()

while True:
    imageGrab()
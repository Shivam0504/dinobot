from numpy import *
from PIL import ImageGrab,ImageOps
import  pyautogui as py

def pressSpace():
    py.keyDown('space')
    py.keyUp('space')

def IMG():
    Box=(170,468,280,490);
    image=ImageGrab.grab(Box);
    image=ImageOps.grayscale(image)
    arr=array(image.getcolors())
    return (arr.sum())

def main():
    x=0
    while(1):
        if(IMG()!=2667):
            pressSpace()
            x=x+1;
            print("Jumping" + str(x))

main()
#IMG()
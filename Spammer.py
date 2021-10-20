import pyautogui as pya;
import time

time.sleep(5)

p = open("para.txt", "r")
for word in p:
    pya.typewrite(word)
    pya.press("enter")
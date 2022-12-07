"""Remove friends from discord"""
import pyautogui
import time

three_dots = {
    "x": 913,
    "y": 225
}

remove_button = {
    "x": 969,
    "y": 313
}

# We dont want to run a loop forever, so we will use this amount to loop for a specified time
friends = 475
time.sleep(5)   

for _ in range(0, friends):
    pyautogui.click(three_dots["x"], three_dots["y"])
    time.sleep(0.3)
    pyautogui.click(remove_button["x"], remove_button["y"])
    time.sleep(0.3)
    pyautogui.press('Enter')
    time.sleep(2)
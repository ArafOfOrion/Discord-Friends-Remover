"""Remove all the pending friend requests"""
import pyautogui
import time

# We dont want to run a loop forever, so we will use this amount to loop for a specified times
pending_requests = 203  
time.sleep(5)   

# Keep your mouse cursor on the reject button after running the script
reject_button_position = pyautogui.position()

for _ in range(0, pending_requests):
    pyautogui.click(reject_button_position.x, reject_button_position.y)
   
    # Sleeping 2 seconds because it takes discord some times to reject a request
    time.sleep(2)
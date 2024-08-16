import pyautogui as p
import time
limit = input("Enter the limit: ")

i = 0
message = input("Enter your message: ")
time.sleep(5)
while i<int(limit):
    p.typewrite(message)
    p.press("Enter")
    i+=1
    time.sleep(0.5)
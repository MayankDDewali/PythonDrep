import pywhatkit as kit
import time
import pyautogui

# Phone number
number = "+918534002139"

# Wait for 5 seconds
time.sleep(5)

# Send the message
kit.sendwhatmsg(number, 'Happy Birthday!', 17, 44)

# Wait for a short delay to ensure WhatsApp Web is fully loaded
time.sleep(5)

# Simulate pressing the Enter key to send the message
pyautogui.press('enter')

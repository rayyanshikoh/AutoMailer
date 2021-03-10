import pyautogui
import time
import os
from email_msg import message
from email_msg import subject

file = open('list.txt')
browser_location = '/System/Applications/Mail.app'
os.system(f"open {browser_location}")
email_list = []

for x in file:
    y = x[0:-1]
    email_list.append(y)
print('Emailing: ')
time.sleep(10)
for email in email_list:
    print(email)
    pyautogui.hotkey('command', 'n')
    pyautogui.write(email)
    pyautogui.press('tab', presses=2)
    pyautogui.write(subject)
    pyautogui.press('tab')
    pyautogui.write(message)
    pyautogui.hotkey('shift', 'command', 'd')
    time.sleep(1)
time.sleep(30)
pyautogui.hotkey('command', 'q')
print('Done!')
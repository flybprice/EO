from selenium import webdriver
import pyautogui
from datetime import datetime as dt
import time


'''
340,431
529,432
721,436
912,436
1107,435
1293,436
1484,434
'''
coords = [(440, 431), (657, 432), (825, 436), (1025, 436), (1225, 435), (1425, 436), (1625, 434)]
prog_time_start = dt.now().strftime("%H:%M:%S")
login_time = '08:59:30'
click_time = '08:59:55'
end_break = '09:00:03'
dow = dt.today().weekday()
today = coords[dow]

pyautogui.click(721, 432)
print(today)
time.sleep(1)
pyautogui.click(1395, 408)  # EO LIST
time.sleep(1)
pyautogui.click(1001, 507)  # EO LIST SUBMIT
time.sleep(1)
pyautogui.click(1026, 500)  # EO LIST SUBMIT
time.sleep(1)
pyautogui.click(1127, 507)  # close
time.sleep(1)
pyautogui.click(1390, 531)  # close
pyautogui.click(1384, 572)  # close
print(today)
t = dt.now().strftime("%H:%M:%S")
x = 0
while x <= 30:

    if t >= end_break:
        pyautogui.click(1387, 571)  # close after on EO

        break
    else:
        pyautogui.click(today)
        pyautogui.click(1323, 408)  # EO LIST
        pyautogui.click(1026, 500)  # EO LIST SUBMIT
        pyautogui.click(1026, 500)  # EO LIST SUBMIT
        pyautogui.click(1127, 507)  # close
        pyautogui.click(1390, 531)  # close

    x += 1
    t = dt.now().strftime("%H:%M:%S")
print(f'Time is {dt.now().strftime("%H:%M:%S")}')
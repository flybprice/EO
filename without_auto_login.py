import pyautogui

# x = 0
# while x <= 100:
#
#     pyautogui.click(1606, 436)  # EO LIST
#     pyautogui.click(1460, 428)  # EO LIST
#     pyautogui.click(1141, 500)  # EO LIST SUBMIT
#     pyautogui.click(1070, 500)  # EO LIST SUBMIT
#     pyautogui.click(1251, 507)  # close
#     pyautogui.click(1514, 542)  # close
#
# x += 1
# 3 2 1
# Point(x=994, y=346)
# 3 2 1
# Point(x=937, y=306)
# 3 2 1
# Point(x=951, y=316)
# 3 2 1
# Point(x=920, y=170)
# 3 2 1
# Point(x=1172, y=373)
# 3 2 1
# Point(x=860, y=1321)

# This is for the phone in USB Debug mode using scrcpy
x = 0
pyautogui.screenshot('Sunday.png')
while x <= 20:
    pyautogui.moveTo(x=994, y=346)  # DAY (Sunday-1 down..Saturday on top)
    pyautogui.click()
    pyautogui.moveTo(x=937, y=306)  # EO List
    pyautogui.click()
    pyautogui.moveTo(x=951, y=316)  # Submit
    pyautogui.click()
    pyautogui.moveTo(x=915, y=177)  # back
    pyautogui.click()

    x += 1

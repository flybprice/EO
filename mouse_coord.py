import pyautogui, sys
#
x=0
while x < 10:
    pyautogui.countdown(3)

    print(pyautogui.position())
    x+=1


# im1 = pyautogui.screenshot('calander.png')
# pyautogui.countdown(3)
# im2= pyautogui.screenshot('EOLIST.png')
# pyautogui.countdown(3)
# im3= pyautogui.screenshot('SubmitorClose.png')
# pyautogui.countdown(3)
# im4 = pyautogui.screenshot('close.png')
# pyautogui.countdown(3)
# im5 = pyautogui.screenshot('close.png')
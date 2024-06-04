import pyautogui
from time import sleep

pyautogui.hotkey('win', 'r')
sleep(2)
pyautogui.write('notepad')
pyautogui.press('enter')
sleep(1)
pyautogui.write('abriu com robô')
sleep(2)
close_window = pyautogui.getActiveWindow()
close_window.close()
pyautogui.press('tab')
sleep(1)
pyautogui.press('enter')
# pyautogui.hotkey('alt', 'F4')
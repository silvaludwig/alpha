import pyautogui
from time import sleep


pyautogui.press('WIN')
sleep(1)
pyautogui.write('Google Chrome')
pyautogui.press('enter')
sleep(2)
pyautogui.keyDown('CTRL')
pyautogui.press('t')
pyautogui.keyUp('CTRL')
sleep(1)
pyautogui.write('dolar hoje')
pyautogui.press('enter')


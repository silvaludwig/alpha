import pyautogui
from time import sleep


escolha = pyautogui.confirm('escolha uma opção:', buttons = ['notepad', 'calculadora'])

if escolha == 'notepad':
    pyautogui.hotkey('win', 'r')
    sleep(1)
    pyautogui.write('notepad')
    pyautogui.press('enter')
    sleep(2)
    pyautogui.write('escolhi abrir o notepad')
    sleep(3)
    close_window = pyautogui.getActiveWindow()
    close_window.close()
    pyautogui.press('tab')
    pyautogui.press('enter')

else:
    pyautogui.hotkey('win', 'r')
    sleep(1)
    pyautogui.write('calc')
    pyautogui.press('enter')

    sleep(2)
    pyautogui.write('500')
    sleep(1)
    pyautogui.press('-')
    sleep(1)
    pyautogui.write('450')
    pyautogui.press('enter')
    sleep(3)
    close_window = pyautogui.getActiveWindow()
    close_window.close()



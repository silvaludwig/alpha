from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyautogui
from time import sleep

escolha = pyautogui.confirm('escolha uma opção:', buttons = ['dolar', 'euro'])

if escolha == 'dolar':
    navegador = webdriver.Chrome()
    sleep(2)
    navegador.get('https://www.google.com')
    navegador.find_element('xpath', '//*[@id="APjFqb"]').send_keys('dolar hoje')
    navegador.find_element('xpath', '//*[@id="APjFqb"]').send_keys(Keys.RETURN)
    # pyautogui.press('enter')
    dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
    print(f'hj o dolar custa o equivalente a R${dolar}')
    close_window = pyautogui.getActiveWindow()
    close_window.close()

else:
    navegador = webdriver.Chrome()
    sleep(2)
    navegador.get('https://www.google.com')
    navegador.find_element('xpath', '//*[@id="APjFqb"]').send_keys('euro hoje')
    navegador.find_element('xpath', '//*[@id="APjFqb"]').send_keys(Keys.RETURN)
    # pyautogui.press('enter')
    euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
    print(f'hj o euro custa o equivalente a R${euro}')
    close_window = pyautogui.getActiveWindow()
    close_window.close()
        
while not close_window: pass

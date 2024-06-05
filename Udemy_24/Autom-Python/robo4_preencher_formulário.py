import pyautogui
from time import sleep
from selenium import webdriver
from openpyxl import load_workbook
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

caminho_arquivo = 'C:\\Users\\Ludwig\\Desktop\\git-repo\\alpha\\Udemy_24\\Autom-Python\\preencherformulario.xlsx'
planilha = load_workbook(caminho_arquivo)
pagina_login = planilha['dados_login']

print(pagina_login['A2'].value)
print(pagina_login['B2'].value)

# abrir o site, fazer login
navegador.get('https://institutoalexa.paineldoaluno.com.br/professor_login')
sleep(2)
navegador.find_element('xpath', '//*[@id="usuario"]').send_keys(pagina_login['A2'].value)
navegador.find_element('xpath', '//*[@id="senha"]').send_keys(pagina_login['B2'].value)
sleep(1)
navegador.find_element('xpath', '//*[@id="Meio"]/td[2]/form/fieldset/input').click()






# fecha a janela e encerra o processo
sleep(5)
close_window = pyautogui.getActiveWindow()
close_window.close()

# while True: pass
while not close_window: pass

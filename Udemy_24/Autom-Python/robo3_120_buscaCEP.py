from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
from time import sleep
import pyautogui
import os

navegador = webdriver.Chrome()
navegador.get('https://www2.correios.com.br/sistemas/buscacep/buscaCepEndereco.cfm')
sleep(2)
navegador.find_element(By.XPATH, '//*[@id="Geral"]/div/div/span[2]/label/input').send_keys('38400220')
navegador.find_element(By.XPATH, '//*[@id="Geral"]/div/div/div[6]/input').click()
sleep(2)


rua = navegador.find_elements(By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[1]' )[0].text
bairro = navegador.find_elements(By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[2]' )[0].text
cidade = navegador.find_elements(By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[3]' )[0].text
cep = navegador.find_elements(By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[4]' )[0].text

print(rua, bairro, cidade, cep)

arquivo = 'C:\\Users\\Ludwig\\Desktop\\git-repo\\alpha\\Udemy_24\\Autom-Python\\buscacep.xlsx'
planilha = load_workbook(arquivo)
sheet_dados_coletados = planilha['dados_coletados']

linha = len(sheet_dados_coletados['A']) + 1
coluna_rua = 'A' + str(linha)
coluna_bairro = 'B' + str(linha)
coluna_cidade = 'C' + str(linha)
coluna_cep = 'D' + str(linha)

sheet_dados_coletados[coluna_rua] = rua
sheet_dados_coletados[coluna_bairro] = bairro
sheet_dados_coletados[coluna_cidade] = cidade
sheet_dados_coletados[coluna_cep] = cep

planilha.save(filename=arquivo)

os.startfile(arquivo)




sleep(5)
close_window = pyautogui.getActiveWindow()
close_window.close()
        
while not close_window: pass

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
from time import sleep
import pyautogui
import os

# abrindo navegador e pesquisando o CEP
navegador = webdriver.Chrome()
navegador.get('https://www2.correios.com.br/sistemas/buscacep/buscaCepEndereco.cfm')
sleep(2)

# abrindo o arquivo .xlsx / colando os dados coletados do site de CEP
caminho_arquivo = 'C:\\Users\\Ludwig\\Desktop\\git-repo\\alpha\\Udemy_24\\Autom-Python\\buscacep.xlsx'
planilha = load_workbook(caminho_arquivo)
pagina_cep_a_consultar = planilha['cep_a_consultar']

linha_pagina_cep_a_consultar = len(pagina_cep_a_consultar['A']) + 1


# inserindo dados de cep e buscando
navegador.find_element(By.XPATH, '//*[@id="Geral"]/div/div/span[2]/label/input').send_keys('38400222')
navegador.find_element(By.XPATH, '//*[@id="Geral"]/div/div/div[6]/input').click()


for linha_cep in range(2, len(pagina_cep_a_consultar['A']) + 1 ):

    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[6]/a').click()
    
    sleep(2)
    cep_a_pesquisar = pagina_cep_a_consultar['A%s' % linha_cep].value

    # inserindo dados de cep e buscando
    navegador.find_element(By.XPATH, '//*[@id="Geral"]/div/div/span[2]/label/input').send_keys(cep_a_pesquisar)
    navegador.find_element(By.XPATH, '//*[@id="Geral"]/div/div/div[6]/input').click()

    # extraindo dados 
    rua = navegador.find_elements(By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[1]' )[0].text
    bairro = navegador.find_elements(By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[2]' )[0].text
    cidade = navegador.find_elements(By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[3]' )[0].text
    cep = navegador.find_elements(By.XPATH,'/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[4]' )[0].text

    # imprimindo dados no termial
    print(rua, bairro, cidade, cep)

    pagina_dados_coletados = planilha['dados_coletados']
    linha_pagina_dados_coletados = len(pagina_dados_coletados['A']) + 1

    # linha = len(pagina_dados_coletados['A'])
    coluna_rua = 'A' + str(linha_pagina_dados_coletados)
    coluna_bairro = 'B' + str(linha_pagina_dados_coletados)
    coluna_cidade = 'C' + str(linha_pagina_dados_coletados)
    coluna_cep = 'D' + str(linha_pagina_dados_coletados)

    pagina_dados_coletados[coluna_rua] = rua
    pagina_dados_coletados[coluna_bairro] = bairro
    pagina_dados_coletados[coluna_cidade] = cidade
    pagina_dados_coletados[coluna_cep] = cep

    planilha.save(filename=caminho_arquivo)


sleep(2)
close_window = pyautogui.getActiveWindow()
close_window.close()
        
while not close_window: pass

os.startfile(caminho_arquivo)
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
pagina_formulario_amarela = planilha['formulario_amarela']
pagina_formulario_verde = planilha['formulario_verde']
pagina_formulario_azul = planilha['formulario_azul']
pagina_formulario_repertorio = planilha['formulario_repertorio']

linha_pagina_amarela = len(pagina_formulario_amarela['B']) + 1
print(pagina_login['A2'].value)
print(pagina_login['B2'].value)

navegador.get('https://institutoalexa.paineldoaluno.com.br/professor_login') # abrir o site
sleep(2)
navegador.find_element('xpath', '//*[@id="usuario"]').send_keys(pagina_login['A2'].value) # fazendo login pegando dados na planilha
navegador.find_element('xpath', '//*[@id="senha"]').send_keys(pagina_login['B2'].value) # fazendo login pegando dados na planilha
sleep(1)
navegador.find_element('xpath', '//*[@id="Meio"]/td[2]/form/fieldset/input').click() # clicando em "ok"
sleep(1)
navegador.find_element(By.XPATH, '//*[@id="esquerdo"]/ul/li[4]/a').click() # clicando em "aulas"
sleep(5)

# quarta feira
for linha in range(2, len(pagina_formulario_amarela['B']) + 1): # passando por cada linha da coluna B e inserindo os dados nos campos correspondentes do formulario
    navegador.find_element(By.XPATH, '//*[@id="dias_horarios_aulas"]/li/div/div[1]').click() # aula do topo, esquerda
    sleep(2)
    dados_a_preencher = pagina_formulario_amarela['B%s' % linha].value
    navegador.find_element(By.XPATH, '//*[@id="conteudoMinistrado"]').send_keys(dados_a_preencher) # preenchendo conteudo ministrado
    sleep(1) 
    navegador.find_element(By.XPATH, '//*[@id="objetivo_aprendizagem"]').send_keys(dados_a_preencher) # preenchendo objetivos de aprendizagem
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="licao_de_casa"]').send_keys(dados_a_preencher) # preenchendo licao de casa
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="metodologia"]').send_keys(dados_a_preencher) # preenchendo metodologia
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="interacao"]').send_keys(dados_a_preencher) # preenchendo interação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="participacao_estudantes"]').send_keys(dados_a_preencher) # preenchendo formas de registro
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="avaliacao_nao_presencial"]').send_keys(dados_a_preencher) # formas de avaliação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="btnSalvar"]').click() # clicando em salvar
    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[8]/div[3]/button').click() # confirmando salvar
    break

sleep(5)

for linha_verde in range(2, len(pagina_formulario_verde['B']) + 1): 
    navegador.find_element(By.XPATH, '//*[@id="dias_horarios_aulas"]/li/div/div[2]').click() # aula do topo, direita
    sleep(2)
    dados_turma_verde = pagina_formulario_verde['B%s' % linha_verde].value
    navegador.find_element(By.XPATH, '//*[@id="conteudoMinistrado"]').send_keys(dados_turma_verde) # preenchendo conteudo ministrado
    sleep(1) 
    navegador.find_element(By.XPATH, '//*[@id="objetivo_aprendizagem"]').send_keys(dados_turma_verde) # preenchendo objetivos de aprendizagem
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="licao_de_casa"]').send_keys(dados_turma_verde) # preenchendo licao de casa
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="metodologia"]').send_keys(dados_turma_verde) # preenchendo metodologia
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="interacao"]').send_keys(dados_turma_verde) # preenchendo interação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="participacao_estudantes"]').send_keys(dados_turma_verde) # preenchendo formas de registro
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="avaliacao_nao_presencial"]').send_keys(dados_turma_verde) # formas de avaliação
    break


# navegador.find_element(By.XPATH, '//*[@id="dias_horarios_aulas"]/li/div/div[3]').click() # baixo, esquerda
# navegador.find_element(By.XPATH, '//*[@id="dias_horarios_aulas"]/li/div/div[4]').click() # baixo, direita



# fecha a janela e encerra o processo
sleep(5)
close_window = pyautogui.getActiveWindow()
close_window.close()

# while True: pass
while not close_window: pass

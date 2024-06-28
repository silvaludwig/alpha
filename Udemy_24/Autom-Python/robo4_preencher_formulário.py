from time import sleep
import pyautogui
from selenium import webdriver
from openpyxl import load_workbook
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

os.environ['DISPLAY'] = ':0'


servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

caminho_arquivo = '/home/ludwig/Desktop/alpha/Udemy_24/Autom-Python/preencherformulario.xlsx'
planilha = load_workbook(caminho_arquivo)
pagina_login = planilha['dados_login']
pagina_formulario_amarela = planilha['formulario_amarela']
pagina_formulario_verde = planilha['formulario_verde']
pagina_formulario_azul = planilha['formulario_azul']
pagina_formulario_repertorio = planilha['formulario_repertorio']

linha_pagina_amarela = len(pagina_formulario_amarela['B']) + 1
print(pagina_login['A2'].value)
print(pagina_login['B2'].value)


navegador.get('https://institutoalexa.paineldoaluno.com.br/professor_login') # abrir o sitep
sleep(2)
navegador.find_element('xpath', '//*[@id="usuario"]').send_keys(pagina_login['A2'].value) # fazendo login pegando dados na planilha
navegador.find_element('xpath', '//*[@id="senha"]').send_keys(pagina_login['B2'].value) # fazendo login pegando dados na planilha
sleep(1)
navegador.find_element('xpath', '//*[@id="Meio"]/td[2]/form/fieldset/input').click() # clicando em "ok"
sleep(1)
navegador.find_element(By.XPATH, '//*[@id="esquerdo"]/ul/li[4]/a').click() # clicando em "aulas"
sleep(5)


def quarta_feira():    
    navegador.find_element(By.XPATH, '//*[@id="dias_horarios_aulas"]/li/div/div[1]').click() # quarta feira, turma amarela manhã
    sleep(5)
    navegador.find_element(By.XPATH, '//*[@id="conteudoMinistrado"]').send_keys(pagina_formulario_amarela['B1'].value) # preenchendo conteudo ministrado
    sleep(1) 
    navegador.find_element(By.XPATH, '//*[@id="objetivo_aprendizagem"]').send_keys(pagina_formulario_amarela['B2'].value) # preenchendo objetivos de aprendizagem
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="licao_de_casa"]').send_keys(pagina_formulario_amarela['B3'].value) # preenchendo licao de casa
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="metodologia"]').send_keys(pagina_formulario_amarela['B4'].value) # preenchendo metodologia
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="interacao"]').send_keys(pagina_formulario_amarela['B5'].value) # preenchendo interação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="participacao_estudantes"]').send_keys(pagina_formulario_amarela['B6'].value) # preenchendo formas de registro
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="avaliacao_nao_presencial"]').send_keys(pagina_formulario_amarela['B7'].value) # formas de avaliação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="btnSalvar"]').click() # clicando em salvar
    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[8]/div[3]/button').click() # confirmando salvar
    sleep(2)

    navegador.find_element(By.XPATH, '//*[@id="dias_horarios_aulas"]/li/div/div[2]').click() # quarta feira, turma verde manhã
    sleep(5)
    navegador.find_element(By.XPATH, '//*[@id="conteudoMinistrado"]').send_keys(pagina_formulario_verde['B1'].value) # preenchendo conteudo ministrado
    sleep(1) 
    navegador.find_element(By.XPATH, '//*[@id="objetivo_aprendizagem"]').send_keys(pagina_formulario_verde['B2'].value) # preenchendo objetivos de aprendizagem
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="licao_de_casa"]').send_keys(pagina_formulario_verde['B3'].value) # preenchendo licao de casa
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="metodologia"]').send_keys(pagina_formulario_verde['B4'].value) # preenchendo metodologia
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="interacao"]').send_keys(pagina_formulario_verde['B5'].value) # preenchendo interação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="participacao_estudantes"]').send_keys(pagina_formulario_verde['B6'].value) # preenchendo formas de registro
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="avaliacao_nao_presencial"]').send_keys(pagina_formulario_verde['B7'].value) # formas de avaliação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="btnSalvar"]').click() # clicando em salvar
    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[8]/div[3]/button').click() # confirmando salvar
    sleep(2)
    
    navegador.find_element(By.XPATH, '//*[@id="dias_horarios_aulas"]/li/div/div[3]').click() # quarta feira, turma amarela tarde
    sleep(5)
    navegador.find_element(By.XPATH, '//*[@id="conteudoMinistrado"]').send_keys(pagina_formulario_amarela['B1'].value) # preenchendo conteudo ministrado
    sleep(1) 
    navegador.find_element(By.XPATH, '//*[@id="objetivo_aprendizagem"]').send_keys(pagina_formulario_amarela['B2'].value) # preenchendo objetivos de aprendizagem
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="licao_de_casa"]').send_keys(pagina_formulario_amarela['B3'].value) # preenchendo licao de casa
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="metodologia"]').send_keys(pagina_formulario_amarela['B4'].value) # preenchendo metodologia
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="interacao"]').send_keys(pagina_formulario_amarela['B5'].value) # preenchendo interação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="participacao_estudantes"]').send_keys(pagina_formulario_amarela['B6'].value) # preenchendo formas de registro
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="avaliacao_nao_presencial"]').send_keys(pagina_formulario_amarela['B7'].value) # formas de avaliação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="btnSalvar"]').click() # clicando em salvar
    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[8]/div[3]/button').click() # confirmando salvar
    sleep(2)
    
    navegador.find_element(By.XPATH, '//*[@id="dias_horarios_aulas"]/li/div/div[4]').click() # quarta feira, turma verde tarde
    sleep(5)
    navegador.find_element(By.XPATH, '//*[@id="conteudoMinistrado"]').send_keys(pagina_formulario_verde['B1'].value) # preenchendo conteudo ministrado
    sleep(1) 
    navegador.find_element(By.XPATH, '//*[@id="objetivo_aprendizagem"]').send_keys(pagina_formulario_verde['B2'].value) # preenchendo objetivos de aprendizagem
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="licao_de_casa"]').send_keys(pagina_formulario_verde['B3'].value) # preenchendo licao de casa
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="metodologia"]').send_keys(pagina_formulario_verde['B4'].value) # preenchendo metodologia
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="interacao"]').send_keys(pagina_formulario_verde['B5'].value) # preenchendo interação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="participacao_estudantes"]').send_keys(pagina_formulario_verde['B6'].value) # preenchendo formas de registro
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="avaliacao_nao_presencial"]').send_keys(pagina_formulario_verde['B7'].value) # formas de avaliação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="btnSalvar"]').click() # clicando em salvar
    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[8]/div[3]/button').click() # confirmando salvar
    sleep(5)
    

def terca_feira():    
    navegador.find_element(By.XPATH, '//*[@id="dias_horarios_aulas"]/li/div/div[1]').click() # terça feira, turma verde manhã
    sleep(5)
    navegador.find_element(By.XPATH, '//*[@id="conteudoMinistrado"]').send_keys(pagina_formulario_verde['B1'].value) # preenchendo conteudo ministrado
    sleep(1) 
    navegador.find_element(By.XPATH, '//*[@id="objetivo_aprendizagem"]').send_keys(pagina_formulario_verde['B2'].value) # preenchendo objetivos de aprendizagem
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="licao_de_casa"]').send_keys(pagina_formulario_verde['B3'].value) # preenchendo licao de casa
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="metodologia"]').send_keys(pagina_formulario_verde['B4'].value) # preenchendo metodologia
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="interacao"]').send_keys(pagina_formulario_verde['B5'].value) # preenchendo interação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="participacao_estudantes"]').send_keys(pagina_formulario_verde['B6'].value) # preenchendo formas de registro
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="avaliacao_nao_presencial"]').send_keys(pagina_formulario_verde['B7'].value) # formas de avaliação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="btnSalvar"]').click() # clicando em salvar
    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[8]/div[3]/button').click() # confirmando salvar
    sleep(2)
    
    navegador.find_element(By.XPATH, '//*[@id="dias_horarios_aulas"]/li/div/div[2]').click() # terça feira, turma amarela manhã
    sleep(5)
    navegador.find_element(By.XPATH, '//*[@id="conteudoMinistrado"]').send_keys(pagina_formulario_amarela['B1'].value) # preenchendo conteudo ministrado
    sleep(1) 
    navegador.find_element(By.XPATH, '//*[@id="objetivo_aprendizagem"]').send_keys(pagina_formulario_amarela['B2'].value) # preenchendo objetivos de aprendizagem
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="licao_de_casa"]').send_keys(pagina_formulario_amarela['B3'].value) # preenchendo licao de casa
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="metodologia"]').send_keys(pagina_formulario_amarela['B4'].value) # preenchendo metodologia
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="interacao"]').send_keys(pagina_formulario_amarela['B5'].value) # preenchendo interação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="participacao_estudantes"]').send_keys(pagina_formulario_amarela['B6'].value) # preenchendo formas de registro
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="avaliacao_nao_presencial"]').send_keys(pagina_formulario_amarela['B7'].value) # formas de avaliação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="btnSalvar"]').click() # clicando em salvar
    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[8]/div[3]/button').click() # confirmando salvar
    sleep(2)

    navegador.find_element(By.XPATH, '//*[@id="dias_horarios_aulas"]/li/div/div[3]').click() # quarta feira, turma amarela tarde
    sleep(5)
    navegador.find_element(By.XPATH, '//*[@id="conteudoMinistrado"]').send_keys(pagina_formulario_amarela['B1'].value) # preenchendo conteudo ministrado
    sleep(1) 
    navegador.find_element(By.XPATH, '//*[@id="objetivo_aprendizagem"]').send_keys(pagina_formulario_amarela['B2'].value) # preenchendo objetivos de aprendizagem
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="licao_de_casa"]').send_keys(pagina_formulario_amarela['B3'].value) # preenchendo licao de casa
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="metodologia"]').send_keys(pagina_formulario_amarela['B4'].value) # preenchendo metodologia
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="interacao"]').send_keys(pagina_formulario_amarela['B5'].value) # preenchendo interação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="participacao_estudantes"]').send_keys(pagina_formulario_amarela['B6'].value) # preenchendo formas de registro
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="avaliacao_nao_presencial"]').send_keys(pagina_formulario_amarela['B7'].value) # formas de avaliação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="btnSalvar"]').click() # clicando em salvar
    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[8]/div[3]/button').click() # confirmando salvar
    sleep(2)
    
    navegador.find_element(By.XPATH, '//*[@id="dias_horarios_aulas"]/li/div/div[4]').click() # terça feira, turma verde tarde
    sleep(5)
    navegador.find_element(By.XPATH, '//*[@id="conteudoMinistrado"]').send_keys(pagina_formulario_verde['B1'].value) # preenchendo conteudo ministrado
    sleep(1) 
    navegador.find_element(By.XPATH, '//*[@id="objetivo_aprendizagem"]').send_keys(pagina_formulario_verde['B2'].value) # preenchendo objetivos de aprendizagem
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="licao_de_casa"]').send_keys(pagina_formulario_verde['B3'].value) # preenchendo licao de casa
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="metodologia"]').send_keys(pagina_formulario_verde['B4'].value) # preenchendo metodologia
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="interacao"]').send_keys(pagina_formulario_verde['B5'].value) # preenchendo interação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="participacao_estudantes"]').send_keys(pagina_formulario_verde['B6'].value) # preenchendo formas de registro
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="avaliacao_nao_presencial"]').send_keys(pagina_formulario_verde['B7'].value) # formas de avaliação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="btnSalvar"]').click() # clicando em salvar
    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[8]/div[3]/button').click() # confirmando salvar
    sleep(5)


def segunda_feira():
    navegador.find_element(By.XPATH, '//*[@id="dias_horarios_aulas"]/li/div/div[1]').click() # segunda feira, repertório
    sleep(5)
    navegador.find_element(By.XPATH, '//*[@id="conteudoMinistrado"]').send_keys(pagina_formulario_repertorio['B1'].value) # preenchendo conteudo ministrado
    sleep(1) 
    navegador.find_element(By.XPATH, '//*[@id="objetivo_aprendizagem"]').send_keys(pagina_formulario_repertorio['B2'].value) # preenchendo objetivos de aprendizagem
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="licao_de_casa"]').send_keys(pagina_formulario_repertorio['B3'].value) # preenchendo licao de casa
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="metodologia"]').send_keys(pagina_formulario_repertorio['B4'].value) # preenchendo metodologia
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="interacao"]').send_keys(pagina_formulario_repertorio['B5'].value) # preenchendo interação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="participacao_estudantes"]').send_keys(pagina_formulario_repertorio['B6'].value) # preenchendo formas de registro
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="avaliacao_nao_presencial"]').send_keys(pagina_formulario_repertorio['B7'].value) # formas de avaliação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="btnSalvar"]').click() # clicando em salvar
    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[8]/div[3]/button').click() # confirmando salvar
    sleep(2)    

    navegador.find_element(By.XPATH, '//*[@id="dias_horarios_aulas"]/li/div/div[2]').click() # segunda feira, turma azul noite
    sleep(5)
    navegador.find_element(By.XPATH, '//*[@id="conteudoMinistrado"]').send_keys(pagina_formulario_azul['B1'].value) # preenchendo conteudo ministrado
    sleep(1) 
    navegador.find_element(By.XPATH, '//*[@id="objetivo_aprendizagem"]').send_keys(pagina_formulario_azul['B2'].value) # preenchendo objetivos de aprendizagem
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="licao_de_casa"]').send_keys(pagina_formulario_azul['B3'].value) # preenchendo licao de casa
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="metodologia"]').send_keys(pagina_formulario_azul['B4'].value) # preenchendo metodologia
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="interacao"]').send_keys(pagina_formulario_azul['B5'].value) # preenchendo interação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="participacao_estudantes"]').send_keys(pagina_formulario_azul['B6'].value) # preenchendo formas de registro
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="avaliacao_nao_presencial"]').send_keys(pagina_formulario_azul['B7'].value) # formas de avaliação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="btnSalvar"]').click() # clicando em salvar
    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[8]/div[3]/button').click() # confirmando salvar
    sleep(5)

def semana_completa():
    quarta_feira() # chama a função e preenche os formulários de quarta feira
    navegador.find_element(By.XPATH, '//*[@id="Capa_1"]').click() # clica em voltar pro dia de aula anterior, que no caso vai levar pra terça feira
    sleep(5)
    terca_feira() # chama a fução e preenche os formulários de terça feira
    navegador.find_element(By.XPATH, '//*[@id="Capa_1"]').click() # clica em voltar pro dia de aula anterior, que no caso vai levar pra segunda feira
    sleep(5)
    segunda_feira() # a mesma coisa só que pra segunda 
    navegador.find_element(By.XPATH, '//*[@id="Capa_1"]').click() # clica em voltar pro dia de aula anterior, que no caso vai levar pra quarta feira de novo
    sleep(3)

semana_completa()
semana_completa()
semana_completa()
semana_completa()
semana_completa()
semana_completa()
semana_completa()
semana_completa()
semana_completa()
semana_completa()
semana_completa()
semana_completa()
semana_completa()
semana_completa()
semana_completa()
semana_completa()
semana_completa()
semana_completa()
semana_completa()

# fecha a janela e encerra o processo
sleep(5)
close_window = pyautogui.getActiveWindow()
close_window.close()

# while True: pass
while not close_window: pass
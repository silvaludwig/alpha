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

login_usuario = "11309681627"
login_senha = 80444

# variáveis turma amarela
conteudo_ministrado_amarela = "Revisão do conteúdo visto anteriormente, escalas e exercícios preparatórios e técnicos, repertório de apresentação."
objetivos_amarela = "Desenvolver habilidades de nível iniciante, básico, tais como postura com o instrumento sentado, em pé, em posição de tocar e descanso. Bem como trabalhar a consciência corporal e auditiva. Conhecimento básico sobre os termos e práticas musicais. Noções básicas de dedilhado e escalas maiores e repertório de apresentações com foco no acompanhamento."
licao_amarela = "Como nem todos os alunos possuem instrumento para praticar em casa, não foi passada nenhuma lição prática para casa."
metodologia_amarela = "Aula expositiva dialogada com foco no aprendizado por imitação e desenvolvimento em grupo, tendo como base a metodologia sociointerativista."
interacao_amarela = "Aula coletiva com troca de saberes entre os participantes."
registro_amarela = "Lista de chamada e registros fotográficos"
avaliacao_amarela = "Presença, consistência, evolução técnica, conhecimentos teóricos, conhecimento do repertório, postura, comportamento em sala."

# variáveis turma verde
conteudo_ministrado_verde = "Revisão do conteúdo visto anteriormente, escalas e exercícios preparatórios e técnicos, repertório de apresentação."
objetivos_verde = "Desenvolver habilidades de nível iniciante, intermediário, tais como postura com o instrumento sentado, em pé, em posição de tocar e descanso. Bem como trabalhar a consciência corporal e auditiva. Conhecimento intermediário sobre os termos e práticas musicais. Escalas maiores, menores e repertório de apresentações com foco no solo e melodias principais."
licao_verde = "Como nem todos os alunos possuem instrumento para praticar em casa, não foi passada nenhuma lição prática para casa."
metodologia_verde = "Aula expositiva dialogada com foco no aprendizado por imitação e desenvolvimento em grupo, tendo como base a metodologia sociointerativista."
interacao_verde = "Aula coletiva com troca de saberes entre os participantes."
registro_verde = "Lista de chamada e registros fotográficos"
avaliacao_verde = "Presença, consistência, evolução técnica, conhecimentos teóricos, conhecimento do repertório, postura, comportamento em sala."



navegador.get('https://institutoalexa.paineldoaluno.com.br/professor_login') # abrir o sitep
sleep(2)
navegador.find_element('xpath', '//*[@id="usuario"]').send_keys(login_usuario) # fazendo login com usuário
navegador.find_element('xpath', '//*[@id="senha"]').send_keys(login_senha) # fazendo login com senha
sleep(5)
navegador.find_element('xpath', '//*[@id="Meio"]/td[2]/form/fieldset/input').click() # clicando em "ok"
sleep(1)
navegador.find_element(By.XPATH, '//*[@id="esquerdo"]/ul/li[4]/a').click() # clicando em "aulas"
sleep(5)


def quarta_feira():    
    navegador.find_element(By.XPATH, '//*[@id="dias_horarios_aulas"]/li/div/div[1]').click() # quarta feira, turma amarela manhã
    sleep(5)
    navegador.find_element(By.XPATH, '//*[@id="conteudoMinistrado"]').send_keys(conteudo_ministrado_amarela) # preenchendo conteudo ministrado
    sleep(1) 
    navegador.find_element(By.XPATH, '//*[@id="objetivo_aprendizagem"]').send_keys(objetivos_amarela) # preenchendo objetivos de aprendizagem
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="licao_de_casa"]').send_keys(licao_amarela) # preenchendo licao de casa
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="metodologia"]').send_keys(metodologia_amarela) # preenchendo metodologia
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="interacao"]').send_keys(interacao_amarela) # preenchendo interação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="participacao_estudantes"]').send_keys(registro_amarela) # preenchendo formas de registro
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="avaliacao_nao_presencial"]').send_keys(avaliacao_amarela) # formas de avaliação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="btnSalvar"]').click() # clicando em salvar
    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[8]/div[3]/button').click() # confirmando salvar
    sleep(2)

    navegador.find_element(By.XPATH, '//*[@id="dias_horarios_aulas"]/li/div/div[2]').click() # quarta feira, turma verde manhã
    sleep(5)
    navegador.find_element(By.XPATH, '//*[@id="conteudoMinistrado"]').send_keys(conteudo_ministrado_verde) # preenchendo conteudo ministrado
    sleep(1) 
    navegador.find_element(By.XPATH, '//*[@id="objetivo_aprendizagem"]').send_keys(objetivos_verde) # preenchendo objetivos de aprendizagem
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="licao_de_casa"]').send_keys(licao_verde) # preenchendo licao de casa
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="metodologia"]').send_keys(metodologia_verde) # preenchendo metodologia
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="interacao"]').send_keys(interacao_verde) # preenchendo interação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="participacao_estudantes"]').send_keys(registro_verde) # preenchendo formas de registro
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="avaliacao_nao_presencial"]').send_keys(avaliacao_verde) # formas de avaliação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="btnSalvar"]').click() # clicando em salvar
    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[8]/div[3]/button').click() # confirmando salvar
    sleep(2)
    
    navegador.find_element(By.XPATH, '//*[@id="dias_horarios_aulas"]/li/div/div[3]').click() # quarta feira, turma amarela tarde
    sleep(5)
    navegador.find_element(By.XPATH, '//*[@id="conteudoMinistrado"]').send_keys(conteudo_ministrado_amarela) # preenchendo conteudo ministrado
    sleep(1) 
    navegador.find_element(By.XPATH, '//*[@id="objetivo_aprendizagem"]').send_keys(objetivos_amarela) # preenchendo objetivos de aprendizagem
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="licao_de_casa"]').send_keys(licao_amarela) # preenchendo licao de casa
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="metodologia"]').send_keys(metodologia_amarela) # preenchendo metodologia
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="interacao"]').send_keys(interacao_amarela) # preenchendo interação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="participacao_estudantes"]').send_keys(registro_amarela) # preenchendo formas de registro
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="avaliacao_nao_presencial"]').send_keys(avaliacao_amarela) # formas de avaliação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="btnSalvar"]').click() # clicando em salvar
    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[8]/div[3]/button').click() # confirmando salvar
    sleep(2)
    
    navegador.find_element(By.XPATH, '//*[@id="dias_horarios_aulas"]/li/div/div[4]').click() # quarta feira, turma verde tarde
    sleep(5)
    navegador.find_element(By.XPATH, '//*[@id="conteudoMinistrado"]').send_keys(conteudo_ministrado_verde) # preenchendo conteudo ministrado
    sleep(1) 
    navegador.find_element(By.XPATH, '//*[@id="objetivo_aprendizagem"]').send_keys(objetivos_verde) # preenchendo objetivos de aprendizagem
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="licao_de_casa"]').send_keys(licao_verde) # preenchendo licao de casa
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="metodologia"]').send_keys(metodologia_verde) # preenchendo metodologia
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="interacao"]').send_keys(interacao_verde) # preenchendo interação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="participacao_estudantes"]').send_keys(registro_verde) # preenchendo formas de registro
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="avaliacao_nao_presencial"]').send_keys(avaliacao_verde) # formas de avaliação
    sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="btnSalvar"]').click() # clicando em salvar
    sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[8]/div[3]/button').click() # confirmando salvar
    sleep(5)
    


def rotina_mensal():
    navegador.find_element(By.XPATH, '//*[@id="Capa_1"]').click() # clica em voltar pro dia de aula anterior, que no caso vai levar pra terça feira
    sleep(5)
    quarta_feira() # chama a função e preenche os formulários de quarta feira
    sleep(2)
    navegador.find_element(By.XPATH, '//*[@id="Capa_1"]').click() # clica em voltar pro dia de aula anterior, que no caso vai levar pra segunda feira
    sleep(5)

rotina_mensal()
rotina_mensal()
rotina_mensal()
rotina_mensal()
rotina_mensal()
rotina_mensal()
rotina_mensal()
rotina_mensal()
rotina_mensal()
rotina_mensal()
rotina_mensal()
rotina_mensal()
rotina_mensal()
rotina_mensal()
rotina_mensal()
rotina_mensal()
rotina_mensal()
rotina_mensal()
rotina_mensal()
rotina_mensal()

# fecha a janela e encerra o processo
sleep(5)
close_window = pyautogui.getActiveWindow()
close_window.close()

# while True: pass
while not close_window: pass
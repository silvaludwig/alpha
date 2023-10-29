from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep


servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)


# abrir o site, fazer login
def login():
    navegador.get('https://institutoalexa.paineldoaluno.com.br/professor_login')
    navegador.find_element('xpath', '//*[@id="usuario"]').send_keys('11309681627')
    navegador.find_element('xpath', '//*[@id="senha"]').send_keys('80444')
    navegador.find_element('xpath', '//*[@id="Meio"]/td[2]/form/fieldset/input').click()

# acessar o painel de aulas
def aulas():
    navegador.find_element('xpath', '//*[@id="esquerdo"]/ul/li[4]/a').click()

# quinta feira repertório
def quinta_repert():
    navegador.find_element('xpath', '//*[@id="dias_horarios_aulas"]/li/div/div[1]').click()

# quinta feira azul
def quinta_azul():
    navegador.find_element('xpath', '//*[@id="dias_horarios_aulas"]/li/div/div[2]').click()

# quarta feira manha
def quarta_manha():
    navegador.find_element('xpath', '//*[@id="dias_horarios_aulas"]/li/div/div[1]').click()

# quarta feira tarde
def quarta_tarde():
    navegador.find_element('xpath', '//*[@id="dias_horarios_aulas"]/li/div/div[2]').click()

# terca verde manha
def terca_verde_manha():
    navegador.find_element('xpath', '//*[@id="dias_horarios_aulas"]/li/div/div[1]').click()

# terca amarela manha
def terca_amarela_manha():
    navegador.find_element('xpath', '//*[@id="dias_horarios_aulas"]/li/div/div[2]').click()

# terca verde tarde
def terca_verde_tarde():
    navegador.find_element('xpath', '//*[@id="dias_horarios_aulas"]/li/div/div[4]').click()

# terca amarela tarde
def terca_amarela_tarde():
    navegador.find_element('xpath', '//*[@id="dias_horarios_aulas"]/li/div/div[3]').click()

def preenchimento_dados():
    navegador.find_element('xpath', '/html/body/div[1]/div[2]/div/div[1]/div[5]/div[1]/div/textarea[4]').send_keys('Aula expositiva dialogada com foco no aprendizado por imitação e desenvolvimento em grupo, tendo como base a metodologia sociointerativista.')
    sleep(2)
    navegador.find_element('xpath', '//*[@id="interacao"]').send_keys('Aula coletiva com troca de saberes entre os participantes.')
    sleep(2)
    navegador.find_element('xpath', '//*[@id="participacao_estudantes"]').send_keys('Lista de chamada e registros fotográficos')
    sleep(2)
    navegador.find_element('xpath', '//*[@id="avaliacao_nao_presencial"]').send_keys('Os alunos foram avaliados individualmente de acordo com a capacidade de execução do repertório e exercícios propostos.')
    sleep(2)
    navegador.find_element('xpath', '//*[@id="btnSalvar"]').click()
    sleep(2)
    navegador.find_element('xpath', '/html/body/div[8]/div[3]/button').click()

def pagina_anterior():
    navegador.find_element('xpath', '//*[@id="Prev"]').click()

def rotina_semanal():
    quinta_repert()
    sleep(2)
    preenchimento_dados()
    sleep(2)
    quinta_azul()
    sleep(2)
    preenchimento_dados()
    sleep(2)
    pagina_anterior()
    sleep(2)
    quarta_manha()
    sleep(2)
    preenchimento_dados()
    sleep(2)
    quarta_tarde()
    sleep(2)
    preenchimento_dados()
    sleep(2)
    pagina_anterior()
    sleep(2)
    terca_amarela_manha()
    sleep(2)
    preenchimento_dados()
    sleep(2)
    terca_amarela_tarde()
    sleep(2)
    preenchimento_dados()
    sleep(2)
    terca_verde_manha()
    sleep(2)
    preenchimento_dados()
    sleep(2)
    terca_verde_tarde()
    sleep(2)
    preenchimento_dados()
    sleep(2)
    pagina_anterior()
    sleep(2)

# ultima quinta feira outubro
def outubro():
    navegador.find_element('xpath', '//*[@id="show-datepicker"]').click()
    navegador.find_element('xpath', '//*[@id="select-delivery-date-input"]/div/table/tbody/tr[4]/td[5]/a').click()

# ultima quinta feira setembro
def setembro():
    navegador.find_element('xpath', '//*[@id="show-datepicker"]').click()
    navegador.find_element('xpath', '//*[@id="select-delivery-date-input"]/div/div/a[1]').click()
    navegador.find_element('xpath', '//*[@id="select-delivery-date-input"]/div/table/tbody/tr[5]/td[5]/a').click()

# ultima quinta feira agosto
def agosto():
    navegador.find_element('xpath', '//*[@id="show-datepicker"]').click()
    navegador.find_element('xpath', '//*[@id="select-delivery-date-input"]/div/div/a[1]').click()
    navegador.find_element('xpath', '//*[@id="select-delivery-date-input"]/div/table/tbody/tr[5]/td[5]/a').click()

login()
sleep(2)
aulas()
sleep(2)
outubro()
sleep(2)
rotina_semanal()
rotina_semanal()
rotina_semanal()
rotina_semanal()
sleep(2)
setembro()
sleep(2)
rotina_semanal()
rotina_semanal()
rotina_semanal()
rotina_semanal()
sleep(2)
agosto()
sleep(2)
rotina_semanal()
rotina_semanal()
rotina_semanal()
rotina_semanal()
rotina_semanal()

while True: pass
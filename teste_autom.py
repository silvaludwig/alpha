import pyautogui as pg
from time import sleep
import subprocess

# AUTOMACAO WHATSAPP WEB NO SAFARI
# o programa abre o Safari, clica na conversa,
# que nesse caso é comigo mesmo, digita e envia
# as coordenadas são para o meu computador, com
# a janela aberta ocupando metade da tela
# deve-se alterar de acordo com as coordenadas
# levando em considaração onde o programa será
# executado.

app_name = 'Safari'

# abrir safari
subprocess.Popen(['open', '-a', app_name])

# clicar na conversa (cmg mesmo)
pg.click(91,200,duration=2)

# clicar e escrever a mensagem
pg.click(411,669,duration=1)
pg.write('automacao baby!')

# clicar em enviar a mensagem
pg.click(582,669,duration=1)

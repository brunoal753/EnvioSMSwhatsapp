########### --> SMS AUTOMÁTICO NO WHATSAPP <-- ###########

## STEP BY STEP

# 1 - TER UMA LISTA DE CONTATOS WHATSAPP
# 2 - ENVIAR INDIVIDUALMENTE UMA MENSAGEM PRA CADA CONTATO
# 3 - PAUSAR ENTRE CADA AÇÃO PARA NÃO TOMAR BLOCK



# ESCOLHER CONTATO
# ENVIAR MENSAGEM PARA CONTATO
# REPETIR ISSO PARA TODOS OS CONTATOS

import webbrowser
import pyautogui
from time import sleep
import pyperclip

telefones = [553198706734,5531999000000,5531999999999]

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(3)
    tecla_iniciar = pyautogui.locateCenterOnScreen('iniciarConv.png')
    pyautogui.click(tecla_iniciar[0],tecla_iniciar[1],duration=1.5)
    sleep(3)
    tecla_wtsWeb = pyautogui.locateCenterOnScreen('whatsWeb.png')
    pyautogui.click(tecla_wtsWeb[0],tecla_wtsWeb[1],duration=1.5)
    sleep(10)
    pyautogui.typewrite('Esta mensagem é de um projeto criado com Python. Desconsidere.')
    sleep(4)
    pyautogui.press('enter')
    sleep(5)
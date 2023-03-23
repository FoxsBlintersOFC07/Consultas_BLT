# Importações...
import requests
import platform
import os
import sys
import json
import time
import base64
import re
from colorama import Fore
from requests.api import request
import threading

def limpar(): #CRIA A FUNÇÃO PRA LIMPAR A TELA
   if platform.system() == "Windows":
      os.system("cls")
   elif platform.system() == "Linux":
      os.system("clear")
   else:
       os.system("clear")

# Banner's...
BannerMenu = (f'''
    {Fore.MAGENTA}    
░█████╗░░█████╗░███╗░░██╗░██████╗██╗░░░██╗██╗░░░░░████████╗░█████╗░░██████╗░░░░░░
██╔══██╗██╔══██╗████╗░██║██╔════╝██║░░░██║██║░░░░░╚══██╔══╝██╔══██╗██╔════╝░░░░░░
██║░░╚═╝██║░░██║██╔██╗██║╚█████╗░██║░░░██║██║░░░░░░░░██║░░░███████║╚█████╗░█████╗
██║░░██╗██║░░██║██║╚████║░╚═══██╗██║░░░██║██║░░░░░░░░██║░░░██╔══██║░╚═══██╗╚════╝
╚█████╔╝╚█████╔╝██║░╚███║██████╔╝╚██████╔╝███████╗░░░██║░░░██║░░██║██████╔╝░░░░░░
░╚════╝░░╚════╝░╚═╝░░╚══╝╚═════╝░░╚═════╝░╚══════╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░░░░░░
                        ██████╗░██╗░░░░░████████╗
                        ██╔══██╗██║░░░░░╚══██╔══╝
                        ██████╦╝██║░░░░░░░░██║░░░
                        ██╔══██╗██║░░░░░░░░██║░░░
                        ██████╦╝███████╗░░░██║░░░
                        ╚═════╝░╚══════╝░░░╚═╝░░░ 
                               1.0 (BETA)
                       \033[1;91m<═══\033[1;41m\033[1;97m by FOXS BLINTERS \033[;0m\033[1;91m═══>\033[1;92m
    ''')

bannerip= (f'''
           _____                   ____         _    
         / ___/__  ___  ___ __ __/ / /____ _   (_)__ 
        / /__/ _ \/ _ \(_-</ // / / __/ _ `/  / / _ \
        \___/\___/_//_/___/\_,_/_/\__/\_,_/  /_/ .__/
                                            /_/       
                
                \033[1;91m<═══\033[1;41m\033[1;97m by FOXS BLINTERS \033[;0m\033[1;91m═══>\033[1;92m                                                                 
''')
bannercpf= (f'''
            _________  _  ________  ____ _________     ________  ____
           / ___/ __ \/ |/ / __/ / / / //_  __/ _ |   / ___/ _ \/ __/
          / /__/ /_/ /    /\ \/ /_/ / /__/ / / __ |  / /__/ ___/ _/  
          \___/\____/_/|_/___/\____/____/_/ /_/ |_|  \___/_/  /_/    
                                                                 
                             \033[1;91m<═══\033[1;41m\033[1;97m by FOXS BLINTERS \033[;0m\033[1;91m═══>\033[1;92m                                             
    ''')
bannerbin= (''' 
       _________  _  ________  ____ _________     ____________ 
      / ___/ __ \/ |/ / __/ / / / //_  __/ _ |   / ___/ __/ _ \
     / /__/ /_/ /    /\ \/ /_/ / /__/ / / __ |  / /__/ _// ___/
     \___/\____/_/|_/___/\____/____/_/ /_/ |_|  \___/___/_/    
                          \033[1;91m<═══\033[1;41m\033[1;97m by FOXS BLINTERS \033[;0m\033[1;91m═══>\033[1;92m                                 
    ''')
bannercnpj= (f'''
          _________  _  ________  ____ _________     ______  _____     __
         / ___/ __ \/ |/ / __/ / / / //_  __/ _ |   / ___/ |/ / _ \__ / /
        / /__/ /_/ /    /\ \/ /_/ / /__/ / / __ |  / /__/    / ___/ // / 
        \___/\____/_/|_/___/\____/____/_/ /_/ |_|  \___/_/|_/_/   \___/  
                            \033[1;91m<═══\033[1;41m\033[1;97m by FOXS BLINTERS \033[;0m\033[1;91m═══>\033[1;92m                           
    ''')
bannercep= ('''
       _________  _  ________  ____ _________     ____________ 
      / ___/ __ \/ |/ / __/ / / / //_  __/ _ |   / ___/ __/ _ \
     / /__/ /_/ /    /\ \/ /_/ / /__/ / / __ |  / /__/ _// ___/
     \___/\____/_/|_/___/\____/____/_/ /_/ |_|  \___/___/_/                                            
                            \033[1;91m<═══\033[1;41m\033[1;97m by FOXS BLINTERS \033[;0m\033[1;91m═══>\033[1;92m  ''')
# Menu inicial...

#CARREGAMENTO INICIAL: 
def startscreen():
    limpar()
    print(f"{Fore.GREEN}Carregando.")
    print(''' █▒▒▒▒▒▒▒▒▒ 10%''');time.sleep(1.0)
    limpar()
    print("Carregando..")
    print('''███▒▒▒▒▒▒▒ 30%''');time.sleep(.30)
    limpar()
    print("Carregando...")
    print('''█████▒▒▒▒▒ 50%''');time.sleep(0.30)
    limpar()
    print("Carregando.")
    print('''███████▒▒▒ 70%''');time.sleep(0.46)
    limpar()
    print("Carregando..")
    print('''█████████▒ 90%''');time.sleep(1.0)
    limpar()
    print("Carregando...")
    print(f'''██████████ 100%{Fore.LIGHTWHITE_EX}''');time.sleep(1.2)
def menu():
    print(BannerMenu)
    print(f'''
    
    ''')
    print(f''' 
    {Fore.LIGHTYELLOW_EX}[01]{Fore.LIGHTWHITE_EX} ➥ Consulta CEP
    {Fore.LIGHTYELLOW_EX}[02]{Fore.LIGHTWHITE_EX} ➥ Consulta CPF {Fore.LIGHTRED_EX}[TEMP. OFF]{Fore.LIGHTWHITE_EX}
    {Fore.LIGHTYELLOW_EX}[03]{Fore.LIGHTWHITE_EX} ➥ Consulta CNPJ
    {Fore.LIGHTYELLOW_EX}[04]{Fore.LIGHTWHITE_EX} ➥ Consulta Bin
    {Fore.LIGHTYELLOW_EX}[05]{Fore.LIGHTWHITE_EX} ➥ Consulta Numero {Fore.LIGHTRED_EX}[TEMP. OFF]{Fore.LIGHTWHITE_EX}
    {Fore.LIGHTYELLOW_EX}[06]{Fore.LIGHTWHITE_EX} ➥ Checker CC 
    {Fore.LIGHTYELLOW_EX}[07]{Fore.LIGHTWHITE_EX} ➥ Consulta IP
    {Fore.LIGHTRED_EX}[00] ➥ Fechar{Fore.LIGHTWHITE_EX}
    ''')
    inputt = input('➤ : ')
    if inputt == '0' or inputt == '00':
        print('')
        os.system('cls')
        exit()
    if inputt == '1' or inputt == '01':
        print('')
        consultacep()
    if inputt == '2' or inputt == '02':
        print('')
        consultacpf()
    if inputt == '3' or inputt == '03':
        print('')
        consultacnpj()
    if inputt == '4' or inputt == '04':
        print('')
        consultabin()
    if inputt == '5' or inputt == '05':
        print('')
        consultanum()
    if inputt == '6' or inputt == '06':
        print('')
        checkercc()        
    if inputt == '7' or inputt == '07':
        print('')
        consultaip()
    if inputt == '0' or inputt == '00':
        os.system('cls')
        exit()
    else:
        print('')
        error404()
# Comandos...
def consultacep():
    os.system('cls')
    print(bannercep)
    cep = input('Digite o CEP:\n')
    url = f"https://ws.apicep.com/cep/{cep}.json"
    json: object = requests.get(url).json()
    cep = json["code"]
    bairro = json["district"]
    estado = json["state"]
    cidade = json["city"]
    rua = json["address"]
    Spinner()
    print('')
    print('Busca Completa')
    print('Dados coletados...')
    print('-============///////=============-')
    print('CEP :', json["code"])
    print('Bairro :', json["district"])
    print('Endereco :', json["address"] )
    print('Cidade :', json["city"])
    print('Estado :', json["state"])
    print('-============///////=============-')
    print('')
    print(f'{Fore.MAGENTA}[RETOMANDO VOCÊ PARA O MENU EM 5 SEGUNDOS...]')
    print('''█▒▒▒▒▒▒▒▒▒ 10%''');time.sleep(1.0)
    print('''███▒▒▒▒▒▒▒ 30%''');time.sleep(1.0)
    print('''████▒▒▒▒▒▒ 30%''');time.sleep(1.0)
    print('''█████▒▒▒▒▒ 50%''');time.sleep(0.30)
    print('''███████▒▒▒ 70%''');time.sleep(0.30)
    print('''█████████▒ 90%''');time.sleep(0.30)
    print('''██████████ 100%''');time.sleep(0.30)
    time.sleep(5.0)
    os.system('cls')
    menu()
def consultacpf():
    os.system('cls')
    print(f'''
    {Fore.LIGHTRED_EX}SINTO MUITO, ISSO ESTÁ INDISPONÍVEL POR ENQUANTO...{Fore.LIGHTWHITE_EX}
    ''')
    print('')
    print(f'{Fore.MAGENTA}[RETOMANDO VOCÊ PARA O MENU EM 5 SEGUNDOS...]')
    print('''█▒▒▒▒▒▒▒▒▒ 10%''');time.sleep(1.0)
    print('''███▒▒▒▒▒▒▒ 30%''');time.sleep(1.0)
    print('''████▒▒▒▒▒▒ 30%''');time.sleep(1.0)
    print('''█████▒▒▒▒▒ 50%''');time.sleep(0.30)
    print('''███████▒▒▒ 70%''');time.sleep(0.30)
    print('''█████████▒ 90%''');time.sleep(0.30)
    print('''██████████ 100%''');time.sleep(0.30)
    os.system('cls')
    menu()
def consultacnpj():
    os.system('cls')
    print(bannercnpj)
    cnpj = input('Digite o CNPJ :\n')
    print('CONSULTANDO, AGUARDE')
    url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'
    cpj = requests.get(url).json()
    Spinner()
    print('Encontrado!')
    print('')
    print('Dados coletados...')
    print('')
    print('-============///////=============-')
    print('Nome:', cpj["nome"])
    print('Nome Fantasia:', cpj["fantasia"])
    print('Estado:', cpj["uf"])
    print('Telefone:', cpj["telefone"])
    print('Email:', cpj["email"])
    print('Data de abertura:', cpj["abertura"])
    print('Capital:', cpj["capital_social"])
    print('Situacao:', cpj["situacao"])
    print('Municipio:', cpj["municipio"])
    print('CEP:', cpj["cep"])
    print('Bairro:', cpj["bairro"])
    print('Porte:', cpj["porte"])
    print('-============///////=============-')
    print('')
    print(f'{Fore.MAGENTA}[RETOMANDO VOCÊ PARA O MENU EM 5 SEGUNDOS...]')
    print('''█▒▒▒▒▒▒▒▒▒ 10%''');time.sleep(1.0)
    print('''███▒▒▒▒▒▒▒ 30%''');time.sleep(1.0)
    print('''████▒▒▒▒▒▒ 30%''');time.sleep(1.0)
    print('''█████▒▒▒▒▒ 50%''');time.sleep(0.30)
    print('''███████▒▒▒ 70%''');time.sleep(0.30)
    print('''█████████▒ 90%''');time.sleep(0.30)
    print('''██████████ 100%''');time.sleep(0.30)
    os.system('cls')
    menu()
def consultabin():
    print(bannerbin)
    BIin = input('Insira a Bin:')
    req = requests.get(f'https://bin-checker.net/api/{BIin}')
    BIN = json.loads(req.text)
    Spinner()
    print('Bin:', BIin)
    print('Bandeira:', BIN["scheme"])
    print('Nivel:', BIN["level"])
    print('')
    print(f'{Fore.MAGENTA}[RETOMANDO VOCÊ PARA O MENU EM 5 SEGUNDOS...]')
    print('''█▒▒▒▒▒▒▒▒▒ 10%''');time.sleep(1.0)
    print('''███▒▒▒▒▒▒▒ 30%''');time.sleep(1.0)
    print('''████▒▒▒▒▒▒ 30%''');time.sleep(1.0)
    print('''█████▒▒▒▒▒ 50%''');time.sleep(0.30)
    print('''███████▒▒▒ 70%''');time.sleep(0.30)
    print('''█████████▒ 90%''');time.sleep(0.30)
    print('''██████████ 100%''');time.sleep(0.30)
    os.system('cls')
    menu()
def consultanum():
    os.system('cls')
    print(f'''{Fore.RED}(SERVIÇO INDISPONÍVEL NO MOMENTO){Fore.LIGHTWHITE_EX}''')
    print(f'{Fore.MAGENTA}[RETOMANDO VOCÊ PARA O MENU EM 5 SEGUNDOS...]')
    print('''█▒▒▒▒▒▒▒▒▒ 10%''');time.sleep(1.0)
    print('''███▒▒▒▒▒▒▒ 30%''');time.sleep(1.0)
    print('''████▒▒▒▒▒▒ 30%''');time.sleep(1.0)
    print('''█████▒▒▒▒▒ 50%''');time.sleep(0.30)
    print('''███████▒▒▒ 70%''');time.sleep(0.30)
    print('''█████████▒ 90%''');time.sleep(0.30)
    print('''██████████ 100%''');time.sleep(0.30)
    os.system('cls')
    menu()
def checkercc():
    os.system('cls')
    print()
    print('Formato checker ( NumeroCC|Mes|Ano|CCV )')
    cc = input('Digite sua CC: ')
    url = requests.get(f'https://laganty.ml/.rest/chknet.php?cc={cc}')
    json.loads(url).json()
    Spinnercc()
    print(f''' 
    
    
    ''')
    time.sleep(5.0)
    os.system('cls')
    menu()

def consultaip():
    bannerip
    os.system("python ip.py")

def error404():
    os.system('cls')
    print('ERROR 404')
    print('')
    print('Em 1 Segundo voce voltara ao menu!')
    time.sleep(1.0)
    os.system('cls')
    menu()
#Só pra separar msm kkkkj#
def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write('\r''〘 F 〙 Consultando..'+i)
		sys.stdout.flush()
		time.sleep(0.3)
def Spinnercc():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write('\r''〘 F 〙 Analizando...'+i)
		sys.stdout.flush()
		time.sleep(0.3)

# Iniciar menu...
limpar()
startscreen()
limpar()
menu()

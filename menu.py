import subprocess
import time
import os
import platform

libs = ['requests', 'pydub', 'platform', 'os', 'sys', 'random', 'json', 'time', 'base64', 're', 'colorama', 'threading'] # lista de bibliotecas a serem verificadas

def Instalação(): #CRIA A FUNÇÃO PRA LIMPAR A TELA
   if platform.system() == "Windows":
      instalaçãowin()
   elif platform.system() == "Linux":
      instalaçãoter()
   else:
       instalaçãoter()

def instalaçãowin():
    for lib in libs: 
     try:
        __import__(lib)
        print(f"{lib} já está instalada.")
     except ImportError:
        print(f"{lib} não está instalada. Tentando instalar...")
        subprocess.check_call(["python", "-m", "pip", "install", lib]) # verifica se cada biblioteca está instalada e, se não estiver, tenta instalar usando o pip
    os.system ('pip install requests colorama')
    menu()

def instalaçãoter():
    for lib in libs: 
     try:
        __import__(lib)
        print(f"{lib} já está instalada.")
     except ImportError:
        print(f"{lib} não está instalada. Tentando instalar...")
        subprocess.check_call(["python", "-m", "pip", "install", lib]) # verifica se cada biblioteca está instalada e, se não estiver, tenta instalar usando o pip
    os.system('pkg install termux-api')
    menu()

def menu():
    if platform.system() == "Windows":
      os.system("python index_win.py")
    elif platform.system() == "Linux":
      os.system("python index_ter.py")
    else:
     os.system("python index_ter.py")

resposta = input("\033[1;31m É sua primeira vez no menu? (S/N)?\033[0;0m ")

if resposta.upper() == "S":
    Instalação()
elif resposta.upper() == "N":
    menu()
else:
    print("\033[1;31m Resposta inválida. Por favor, responda S ou N. \033[0;0m")

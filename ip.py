import requests, os, time
import os
import platform

def nv_consulta():
   print('\n\033[34;01m Deseja Realizar uma nova consulta ip?\n1. sim\n2. sair\n\033[0;0m\n')
   df=input('➥ ')
   if df == '1':
    ipss()
   elif df == '2':
    print('\n\033[32;1m Obrigado por usar nossas ferramentas :)\033[0;0m\n')
    voltar_ao_menu()
   elif df != 1 and 2:
    print('\n\033[33;1mCOMANDO INVÁLIDO, DIGITE "1" OU "2"\n')
    nv_consulta()       

def limpar(): #CRIA A FUNÇÃO PRA LIMPAR A TELA
   if platform.system() == "Windows":
      os.system("cls")
   elif platform.system() == "Linux":
      os.system("clear")
   else:
       os.system("clear")

def abrir_no_google_maps():
   import webbrowser
   latitude = input("\033[31m Cole a Latitude: \033[0;0m")
   longitude = input("\033[31m Cole a Longitude: \033[0;0m: ")
   url = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"
   webbrowser.open_new_tab(url)
   nv_consulta()

def voltar_ao_menu():
  limpar()
  os.system("python menu.py")

def ipss():
 limpar()
 print('\033[32;1m')
 print('\033[32;1m        _______    _____  __________ ')
 time.sleep(0.1)      
 print('\033[32;1m       /  _/ _ \  /  _/ |/ / __/ __ \'')
 time.sleep(0.1)      
 print('\033[32;1m      _/ // ___/ _/ //    / _// /_/ /')
 time.sleep(0.1)      
 print('\033[32;1m     /___/_/    /___/_/|_/_/  \____/')
 time.sleep(0.1)      
 print('''
 
      \033[1;91m<═══\033[1;41m\033[1;97m by FOXS BLINTERS \033[;0m\033[1;91m═══>\033[1;92m''')
 print('')
 print('''\033[34;1m

 
╔═━──────━▒۞▒━────━═╗
╟ [1]➢ DADOS DO IP ║
╟ [2]➢ AJUDA       ║
╟ [3]➢ SAIR        ║
╚═━──────━▒۞▒━────━═╝

 ''')
 s=input('\nDigite a opção que deseja\n          ➥ ')
 if s == '1':
  print('\n\033[34;1mDigite o endereço ip, exemplo: "164.163.178.24" , se caso o campo da digitação estiver sem nada, você receberá informações sobre seu próprio ip: \033[0;0m\n')
  ipg=input('➥ ')
  api = requests.get("https://ipapi.co/{}/json".format(ipg))
  resultado = api.json()
  zs=requests.get('http://ip-api.com/json/{}'.format(ipg))
  k=zs.json()
  lks=k['query']
  if 'message' not in k:
   print('\n\033[32;1m ⟾IP ENCONTRADO⟽\033[0;0m')
   print('\n\033[34;1m◆-▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱-◆\n◆-')
   print('\033[34;1m➢-Ip: \033[0;0m\033[37;1m{}'.format(lks))
   print('\033[34;1m➢-Pais: \033[0;0m\033[37;1m{}'.format(k['country']))
   print('\033[34;1m➢-Codigo do pais: \033[37;1m{}'.format(k['countryCode']))
   print('\033[34;1m➢-Regiao: \033[37;1m{}'.format(k['region']))
   print('\033[34;1m➢-Estado: \033[37;1m{}'.format(k['regionName']))
   print('\033[34;1m➢-Cidade: \033[37;1m{}'.format(k['city']))
   print('\033[34;1m➢-Cep: \033[37;1m{}'.format(k['zip']))
   print('\033[34;1m➢-Latitude: \033[37;1m{}'.format(k['lat']))
   print('\033[34;1m➢-Longitude: \033[37;1m{}'.format(k['lon']))
   print('\033[34;1m➢-Fuso horario: \033[37;1m{}'.format(k['timezone']))
   print('\033[34;1m➢-Isp: \033[37;1m{}'.format(k['isp']))
   print('\033[34;1m➢-Servidora: \033[37;1m{}'.format(k['org']))
   print('\033[34;1m➢-As: \033[37;1m{}'.format(k['as']))
   print('\033[34;1m➢-Abreviação do país: \033[37;1m{}'.format(resultado['country_code']))
   print('\033[34;1m➢-Capital do país: \033[37;1m{}'.format(resultado['country_capital']))
   print('\033[34;1m➢-População do país: \033[37;1m{}'.format(resultado['country_population']))
   print('\033[34;1m➢-Moeda: \033[37;1m{}'.format(resultado['currency']))
   print('\033[34;1m➢-Nome da moeda: \033[37;1m{}'.format(resultado['currency_name']))
   print('\033[34;1m➢-Código da região: \033[37;1m{}'.format(resultado['region_code']))
   print('\033[34;1m➢-Código do país: \033[37;1m{}'.format(resultado['country_code']))
   print('\033[34;1m➢-Código do país ISO3: \033[37;1m{}'.format(resultado['country_code_iso3']))
   print('\033[34;1m➢-Área do país: \033[37;1m{}'.format(resultado['country_area']))
   print('\033[34;1m➢-País TLD: \033[37;1m{}'.format(resultado['country_tld']))
   print('\033[34;1m➢-Código área: \033[37;1m{}'.format(resultado['country_area']))
   print('\033[34;1m➢-Código do continente: \033[37;1m{}'.format(resultado['continent_code']))
   print('\033[34;1m➢-União Européia: \033[37;1m{}'.format(resultado['in_eu']))
   print('\033[34;1m➢-Código de Chamada: \033[37;1m{}'.format(resultado['country_calling_code']))
   print('\033[34;1m➢-línguas: \033[37;1m{}'.format(resultado['languages']))
   print('\033[34;1m➢-ASN: \033[37;1m{}'.format(resultado['asn']))
   print('\033[34;1m➢-Deslocamento UTF: \033[37;1m{}'.format(resultado['utc_offset']))
   print('\033[34;1m➢-Versão: \033[37;1m{}'.format(resultado['version']))
   print('\033[34;1m◆-\n◆-▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱-◆')
   gmaps = input('Deseja abrir as coordenadas do IP no google maps?')
   if gmaps == "Sim" or 'sim' or 'yes' or 'Yes' or 'S' or 's' or 'y' or 'Y':
      print('\033[34;1m➢-Copie a Latitude: \033[37;1m{}'.format(k['lat']))
      print('\033[34;1m➢-Copie a Longitude: \033[37;1m{}'.format(k['lon']))
      abrir_no_google_maps()
   elif gmaps == 'Não' or 'N' or 'nao' or 'n' or 'NAO' or 'nAo' or 'NAo':
     nv_consulta()
   else:
      nv_consulta()
 if s =='2':
  print('\n\033[32;1mPara obter informações sobre seu ip-alvo, digite o endereço ip, exemplo: "164.163.178.24" , se caso o campo da digitação estiver sem nada, você receberá informações sobre seu próprio ip\n')
  nv_consulta()
 if s =='3':
  print('\n\033[32;1mObrigado por ultilizar nossas ferramentas :)\n')
  voltar_ao_menu()
 if s != 1 and 2 and 3 and '':
  print('\033[33;1mSeleção invalida\033[0;0m')
  time.sleep(3)
  ipss()
limpar()

ipss()
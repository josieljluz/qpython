# 𝓑𝔂 ✩𝙅𝙤𝙨𝙞𝙚𝙡 𝙅𝙚𝙛𝙛𝙚𝙧𝙨𝙤𝙣✩✔
# ╔═══════════════════════════════════════╗
# ║           PyEncrypt (LZMA + Base64) - (Fernet)
# ║  Autor        : Josiel Jefferson
# ║  Github       : https://github.com/josielljefferson
# ║  Tempo       : domingo, 2 de fevereiro de 2025, 12:47:40
# ╚═══════════════════════════════════════╝
import os
import base64
import lzma
import time
import unicodedata
import arrow
import pyfiglet
from cryptography.fernet import Fernet

# Exibe ASCII art
ascii_art = pyfiglet.figlet_format("PyEncrypt\nLZMA + Base64\nFernet", font="slant")

# Obtém data e hora atuais
now = arrow.now("America/Sao_Paulo")
data_extenso = now.format("dddd, D [de] MMMM [de] YYYY, HH:mm:ss", locale="pt_BR").lower()

# Função para normalizar caracteres
def normalizar_codigo(codigo):
    return unicodedata.normalize('NFKC', codigo)

# Função para gerar ou carregar chave Fernet
def gerar_chave():
    if not os.path.exists("key.key"):
        chave = Fernet.generate_key()
        with open("key.key", "wb") as chave_arquivo:
            chave_arquivo.write(chave)
    else:
        with open("key.key", "rb") as chave_arquivo:
            chave = chave_arquivo.read()
    return chave

# Métodos de criptografia e descriptografia
def criptografar_lzma_base64(codigo):
    codigo = normalizar_codigo(codigo)
    compactado = lzma.compress(codigo.encode('utf-8'))
    return base64.urlsafe_b64encode(compactado).decode('utf-8')

def descriptografar_lzma_base64(criptografado):
    try:
        decoded_code = base64.urlsafe_b64decode(criptografado)
        return lzma.decompress(decoded_code).decode('utf-8')
    except Exception as e:
        return f"Erro ao descriptografar: {e}"

def criptografar_fernet(codigo, chave):
    cipher = Fernet(chave)
    return cipher.encrypt(normalizar_codigo(codigo).encode()).decode('utf-8')

def descriptografar_fernet(criptografado, chave):
    try:
        cipher = Fernet(chave)
        return cipher.decrypt(criptografado.encode()).decode()
    except Exception as e:
        return f"Erro ao descriptografar: {e}"

# Função para salvar código criptografado
def salvar_codigo(caminho_arquivo, conteudo):
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        f.write(conteudo)

# Função principal com menu
def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\033[1;92m{ascii_art}\n\033[1;93m")
    print("1 - Criptografar código (LZMA + Base64)")
    print("2 - Criptografar código (Fernet)")
    print("3 - Descriptografar código")
    print("4 - Sair")

    opcao = input("\nEscolha uma opção:\033[1;92m ").strip()

    if opcao == "1" or opcao == "2":
        caminho_arquivo = input("\nDigite o caminho do arquivo .py:\033[1;38;5;229m ").strip()
        if not os.path.isfile(caminho_arquivo):
            print("\nErro: Arquivo não encontrado!")
            return
        
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            codigo = f.read()

        diretorio, nome_arquivo = os.path.split(caminho_arquivo)
        tipo = "lzma" if opcao == "1" else "fernet"
        nome_criptografado = nome_arquivo.replace(".py", f"_[{tipo}]_encrypted.py")
        caminho_criptografado = os.path.join(diretorio, nome_criptografado)

        if opcao == "1":
            criptografado = criptografar_lzma_base64(codigo)
            conteudo_criptografado = f"""# 𝓑𝔂 ✩𝙅𝙤𝙨𝙞𝙚𝙡 𝙅𝙚𝙛𝙛𝙚𝙧𝙨𝙤𝙣✩✔
# ╔═══════════════════════════════════════╗
# ║           PyEncrypt (LZMA + Base64)
# ║  Autor        : Josiel Jefferson
# ║  Github       : https://github.com/josielljefferson
# ║  Tempo       : {data_extenso}
# ╚═══════════════════════════════════════╝

import base64
import lzma

encoded_code = '''{criptografado}'''\n
decoded_code = base64.urlsafe_b64decode(encoded_code)\n
decompressed_code = lzma.decompress(decoded_code)\n
exec(decompressed_code.decode('utf-8'))\n
"""
        else:
            chave = gerar_chave()
            criptografado = criptografar_fernet(codigo, chave)
            conteudo_criptografado = f"""# 𝓑𝔂 ✩𝙅𝙤𝙨𝙞𝙚𝙡 𝙅𝙚𝙛𝙛𝙚𝙧𝙨𝙤𝙣✩✔
# ╔═══════════════════════════════════════╗
# ║           PyEncrypt (Fernet)
# ║  Autor        : Josiel Jefferson
# ║  Github       : https://github.com/josielljefferson
# ║  Tempo       : {data_extenso}
# ╚═══════════════════════════════════════╝

from cryptography.fernet import Fernet

with open("key.key", "rb") as chave_arquivo:
    chave = chave_arquivo.read()

cipher = Fernet(chave)\n
encoded_code = '''{criptografado}'''\n
decoded_code = cipher.decrypt(encoded_code.encode()).decode()\n
exec(decoded_code)\n
"""

        salvar_codigo(caminho_criptografado, conteudo_criptografado)
        print(f"\nCódigo criptografado salvo em: {caminho_criptografado}")

    elif opcao == "3":
        caminho_arquivo = input("\nDigite o caminho do arquivo criptografado: ").strip()
        if not os.path.isfile(caminho_arquivo):
            print("\nErro: Arquivo não encontrado!")
            return
        
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        if "lzma" in conteudo and "base64" in conteudo:
            criptografado = conteudo.split("encoded_code = '''")[1].split("'''")[0]
            descriptografado = descriptografar_lzma_base64(criptografado)
        elif "Fernet" in conteudo:
            chave = gerar_chave()
            criptografado = conteudo.split("encoded_code = '''")[1].split("'''")[0]
            descriptografado = descriptografar_fernet(criptografado, chave)
        else:
            print("\nErro: Tipo de criptografia não reconhecido!")
            return

        print("\nCódigo descriptografado:\n\n", descriptografado)

        if "Erro ao descriptografar" not in descriptografado:
            exec(descriptografado)
        else:
            print("\nErro ao executar o código.")

    elif opcao == "4":
        print("\nSaindo...\n")
        exit()
    else:
        print("\nOpção inválida!")

# Loop do menu
while True:
    menu()
    conti = input(f"\n   \033[1;38;5;215m𝐀𝐏𝐄𝐑𝐓𝐄 𝐄𝐍𝐓𝐄𝐑 𝐏𝐀𝐑𝐀 𝐑𝐄𝐈𝐍𝐈𝐂𝐈𝐀𝐑 𝐏𝐀𝐑𝐀 𝐌𝐄𝐍𝐔      \033[0;1m\n")
    os.system('cls' if os.name == 'nt' else 'clear')


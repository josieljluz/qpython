
import os
import base64
import lzma
import unicodedata
import arrow
import pyfiglet
from cryptography.fernet import Fernet

# Exibe a arte ASCII
def exibir_arte_ascii():
    ascii_art = pyfiglet.figlet_format("PyEncrypt\nLZMA + Base64\nFernet", font="slant")
    print(f"\033[1;92m{ascii_art}\n\033[1;93m")

# Obtém a data e hora atuais
def obter_data_hora():
    now = arrow.now("America/Fortaleza")
    return now.format("dddd, D [de] MMMM [de] YYYY, HH:mm:ss", locale="pt_BR").lower()

# Função para normalizar os caracteres
def normalizar_codigo(codigo):
    return unicodedata.normalize('NFKC', codigo)

# Função para gerar ou carregar uma chave Fernet
def gerar_chave(nome_arquivo_chave="chave.key"):
    """
    Gera ou carrega uma chave Fernet.
    Se o arquivo de chave não existir, ele é criado com uma nova chave.
    Caso contrário, a chave existente é carregada.

    :param nome_arquivo_chave: Nome do arquivo onde a chave será armazenada ou carregada.
    :return: A chave Fernet.
    """
    if not os.path.exists(nome_arquivo_chave):
        chave = Fernet.generate_key()
        with open(nome_arquivo_chave, "wb") as arquivo_chave:
            arquivo_chave.write(chave)
        print(f"Chave gerada e salva em: {nome_arquivo_chave}")
    else:
        with open(nome_arquivo_chave, "rb") as arquivo_chave:
            chave = arquivo_chave.read()
        print(f"Chave carregada de: {nome_arquivo_chave}")
    return chave

# Métodos de criptografia e descriptografia
def criptografar_lzma_base64(codigo):
    codigo = normalizar_codigo(codigo)
    comprimido = lzma.compress(codigo.encode('utf-8'))
    return base64.urlsafe_b64encode(comprimido).decode('utf-8')

def descriptografar_lzma_base64(criptografado):
    try:
        codigo_decodificado = base64.urlsafe_b64decode(criptografado)
        return lzma.decompress(codigo_decodificado).decode('utf-8')
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

# Função para salvar o código criptografado
def salvar_codigo(caminho_arquivo, conteudo):
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        f.write(conteudo)

# Função para carregar o código de um arquivo
def carregar_codigo(caminho_arquivo):
    if not os.path.isfile(caminho_arquivo):
        print("\nErro: Arquivo não encontrado!")
        return None
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        return f.read()

# Função para criptografar o código
def criptografar_codigo(opcao, caminho_arquivo, nome_arquivo_chave="chave.key"):
    codigo = carregar_codigo(caminho_arquivo)
    if codigo is None:
        return

    diretorio, nome_arquivo = os.path.split(caminho_arquivo)
    tipo_criptografia = "lzma" if opcao == "1" else "fernet"
    nome_criptografado = nome_arquivo.replace(".py", f"_[{tipo_criptografia}]_criptografado.py")
    caminho_criptografado = os.path.join(diretorio, nome_criptografado)

    if opcao == "1":
        criptografado = criptografar_lzma_base64(codigo)
        conteudo_criptografado = f"""# 𝓑𝔂 ✩𝙅𝙤𝙨𝙞𝙚𝙡 𝙅𝙚𝙛𝙛𝙚𝙧𝙨𝙤𝙣✩✔
# ╔═══════════════════════════════════════╗
# ║           PyEncrypt (LZMA + Base64)
# ║  Autor        : Josiel Jefferson
# ║  Github       : https://github.com/josielljefferson
# ║  Tempo        : {obter_data_hora()}
# ╚═══════════════════════════════════════╝

import base64
import lzma

codigo_codificado = '''{criptografado}'''\n
codigo_decodificado = base64.urlsafe_b64decode(codigo_codificado)\n
codigo_descomprimido = lzma.decompress(codigo_decodificado)\n
exec(codigo_descomprimido.decode('utf-8'))\n
"""
    else:
        chave = gerar_chave(nome_arquivo_chave)
        criptografado = criptografar_fernet(codigo, chave)
        conteudo_criptografado = f"""# 𝓑𝔂 ✩𝙅𝙤𝙨𝙞𝙚𝙡 𝙅𝙚𝙛𝙛𝙚𝙧𝙨𝙤𝙣✩✔
# ╔═══════════════════════════════════════╗
# ║           PyEncrypt (Fernet)
# ║  Autor        : Josiel Jefferson
# ║  Github       : https://github.com/josielljefferson
# ║  Tempo        : {obter_data_hora()}
# ╚═══════════════════════════════════════╝

from cryptography.fernet import Fernet

with open("{nome_arquivo_chave}", "rb") as arquivo_chave:
    chave = arquivo_chave.read()

cipher = Fernet(chave)\n
codigo_codificado = '''{criptografado}'''\n
codigo_decodificado = cipher.decrypt(codigo_codificado.encode()).decode()\n
exec(codigo_decodificado)\n
"""

    salvar_codigo(caminho_criptografado, conteudo_criptografado)
    print(f"\nCódigo criptografado salvo em: {caminho_criptografado}")

# Função para descriptografar o código
def descriptografar_codigo(caminho_arquivo, nome_arquivo_chave="chave.key"):
    conteudo = carregar_codigo(caminho_arquivo)
    if conteudo is None:
        return

    if "lzma" in conteudo and "base64" in conteudo:
        criptografado = conteudo.split("codigo_codificado = '''")[1].split("'''")[0]
        descriptografado = descriptografar_lzma_base64(criptografado)
    elif "Fernet" in conteudo:
        chave = gerar_chave(nome_arquivo_chave)
        criptografado = conteudo.split("codigo_codificado = '''")[1].split("'''")[0]
        descriptografado = descriptografar_fernet(criptografado, chave)
    else:
        print("\nErro: Tipo de criptografia não reconhecido!")
        return

    print("\nCódigo descriptografado:\n\n", descriptografado)

    if "Erro ao descriptografar" not in descriptografado:
        exec(descriptografado)
    else:
        print("\nErro ao executar o código.")

# Função principal com menu
def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_arte_ascii()
    print("1 - Criptografar o código (LZMA + Base64)")
    print("2 - Criptografar o código (Fernet)")
    print("3 - Descriptografar o código")
    print("4 - Sair")

    opcao = input("\nEscolha uma opção:\033[1;92m ").strip()

    if opcao == "1" or opcao == "2":
        caminho_arquivo = input("\nDigite o caminho do arquivo .py:\033[1;38;5;229m ").strip()
        if opcao == "2":
            nome_arquivo_chave = input("\nDigite o nome do arquivo de chave (padrão: chave.key): ").strip() or "chave.key"
            criptografar_codigo(opcao, caminho_arquivo, nome_arquivo_chave)
        else:
            criptografar_codigo(opcao, caminho_arquivo)
    elif opcao == "3":
        caminho_arquivo = input("\nDigite o caminho do arquivo criptografado: ").strip()
        nome_arquivo_chave = input("\nDigite o nome do arquivo de chave (padrão: chave.key): ").strip() or "chave.key"
        descriptografar_codigo(caminho_arquivo, nome_arquivo_chave)
    elif opcao == "4":
        print("\nSaindo...\n")
        exit()
    else:
        print("\nOpção inválida!")

# Loop do menu
while True:
    menu()
    continuar = input(f"\n   \033[1;38;5;215m𝐀𝐏𝐄𝐑𝐓𝐄 𝐄𝐍𝐓𝐄𝐑 𝐏𝐀𝐑𝐀 𝐑𝐄𝐂𝐎𝐌𝐄𝐂𝐀𝐑 𝐎 𝐌𝐄𝐍𝐔      \033[0;1m\n")
    os.system('cls' if os.name == 'nt' else 'clear')

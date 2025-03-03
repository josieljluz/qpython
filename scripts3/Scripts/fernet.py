# -*- coding: utf-8 -*-
from cryptography.fernet import Fernet

def gerar_chave():
    """Gera uma chave de criptografia."""
    return Fernet.generate_key()

def salvar_chave(chave, nome_arquivo='chave.key'):
    """Salva a chave em um arquivo."""
    with open(nome_arquivo, 'wb') as arquivo_chave:
        arquivo_chave.write(chave)

def carregar_chave(nome_arquivo='chave.key'):
    """Carrega a chave de um arquivo."""
    return open(nome_arquivo, 'rb').read()

def criptografar_arquivo(chave, nome_arquivo, nome_arquivo_saida):
    """Criptografa um arquivo Python."""
    fernet = Fernet(chave)
    with open(nome_arquivo, 'rb') as arquivo:
        dados = arquivo.read()
    dados_criptografados = fernet.encrypt(dados)
    with open(nome_arquivo_saida, 'wb') as arquivo_saida:
        arquivo_saida.write(dados_criptografados)
    print(f"Arquivo '{nome_arquivo}' foi criptografado e salvo como '{nome_arquivo_saida}'.")

def descriptografar_arquivo(chave, nome_arquivo, nome_arquivo_saida):
    """Descriptografa um arquivo Python."""
    fernet = Fernet(chave)
    with open(nome_arquivo, 'rb') as arquivo:
        dados_criptografados = arquivo.read()
    dados_descriptografados = fernet.decrypt(dados_criptografados)
    with open(nome_arquivo_saida, 'wb') as arquivo_saida:
        arquivo_saida.write(dados_descriptografados)
    print(f"Arquivo '{nome_arquivo}' foi descriptografado e salvo como '{nome_arquivo_saida}'.")

def menu():
    print("╔════════════════════════════════════════════╗")
    print("║          Criptografia de Arquivos          ║")
    print("║            Feito em Python                 ║")
    print("║  Escolha uma opção:                        ║")
    print("║  [1] Gerar chave                           ║")
    print("║  [2] Criptografar arquivo                  ║")
    print("║  [3] Descriptografar arquivo               ║")
    print("║  [4] Sair                                  ║")
    print("╚════════════════════════════════════════════╝")

    opcao = input(" [-] Opção : ")

    if opcao == '1':
        chave = gerar_chave()
        salvar_chave(chave)
        print("Chave gerada e salva como 'chave.key'.")
    elif opcao == '2':
        nome_arquivo = input(" [-] Nome do arquivo para criptografar : ")
        nome_arquivo_saida = input(" [-] Nome do arquivo criptografado (saída) : ")
        chave = carregar_chave()
        criptografar_arquivo(chave, nome_arquivo, nome_arquivo_saida)
    elif opcao == '3':
        nome_arquivo = input(" [-] Nome do arquivo para descriptografar : ")
        nome_arquivo_saida = input(" [-] Nome do arquivo descriptografado (saída) : ")
        chave = carregar_chave()
        descriptografar_arquivo(chave, nome_arquivo, nome_arquivo_saida)
    elif opcao == '4':
        print("Saindo...")
        exit()
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    while True:
        menu()
import base64
import os

def criptografar_texto(texto):
    return base64.b64encode(texto.encode()).decode()

def descriptografar_texto(texto_cripto):
    try:
        return base64.b64decode(texto_cripto).decode()
    except Exception as e:
        return f"Erro ao descriptografar: {e}"

def criptografar_arquivo(arquivo_origem, arquivo_destino):
    with open(arquivo_origem, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    conteudo_b64 = criptografar_texto(conteudo)
    script_cripto = f"""import base64\nexec(base64.b64decode('{conteudo_b64}'))"""
    with open(arquivo_destino, 'w', encoding='utf-8') as f:
        f.write(script_cripto)
    print(f"Arquivo criptografado salvo como: {arquivo_destino}")

def descriptografar_arquivo(arquivo_origem, arquivo_destino):
    with open(arquivo_origem, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    try:
        conteudo_b64 = conteudo.split("b64decode('")[1].split("'))")[0]
        conteudo_original = descriptografar_texto(conteudo_b64)
        with open(arquivo_destino, 'w', encoding='utf-8') as f:
            f.write(conteudo_original)
        print(f"Arquivo descriptografado salvo como: {arquivo_destino}")
    except Exception as e:
        print(f"Erro ao descriptografar: {e}")

def menu():
    while True:
        print("\n1. Criptografar texto")
        print("2. Descriptografar texto")
        print("3. Criptografar arquivo")
        print("4. Descriptografar arquivo")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            texto = input("Digite o texto a ser criptografado: ")
            print("Texto criptografado:")
            print(criptografar_texto(texto))
        elif opcao == '2':
            texto_cripto = input("Digite o texto criptografado: ")
            print("Texto descriptografado:")
            print(descriptografar_texto(texto_cripto))
        elif opcao == '3':
            origem = input("Digite o caminho do arquivo a ser criptografado: ")
            destino = input("Digite o nome do arquivo de saída: ")
            criptografar_arquivo(origem, destino)
        elif opcao == '4':
            origem = input("Digite o caminho do arquivo a ser descriptografado: ")
            destino = input("Digite o nome do arquivo de saída: ")
            descriptografar_arquivo(origem, destino)
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

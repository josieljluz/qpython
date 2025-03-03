import ast
import os
import subprocess
import logging
from pathlib import Path

# Configuração de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Função para encontrar as importações usadas no código
def encontrar_importacoes_usadas(codigo):
    try:
        tree = ast.parse(codigo)
        usadas = {alias.name for node in ast.walk(tree) for alias in getattr(node, 'names', [])}
        return usadas
    except Exception as e:
        logging.error(f"Erro ao analisar o código: {e}")
        return set()

# Função para remover os comentários do código
def remover_comentarios(codigo):
    try:
        linhas = codigo.split('\n')
        codigo_sem_comentarios = []
        for linha in linhas:
            sem_comentario = linha.split('#')[0].rstrip()
            if sem_comentario.strip():  # Ignorar linhas vazias
                codigo_sem_comentarios.append(sem_comentario)
        return '\n'.join(codigo_sem_comentarios)
    except Exception as e:
        logging.error(f"Erro ao remover comentários: {e}")
        return codigo

# Função para remover importações não utilizadas
def remover_importacoes_nao_usadas(codigo):
    try:
        importacoes_usadas = encontrar_importacoes_usadas(codigo)
        linhas = codigo.split('\n')
        codigo_sem_importacoes_nao_usadas = []
        for linha in linhas:
            if linha.startswith('import ') or linha.startswith('from '):
                if any(mod in linha for mod in importacoes_usadas):
                    codigo_sem_importacoes_nao_usadas.append(linha)
            else:
                codigo_sem_importacoes_nao_usadas.append(linha)
        return '\n'.join(codigo_sem_importacoes_nao_usadas)
    except Exception as e:
        logging.error(f"Erro ao remover importações não usadas: {e}")
        return codigo

# Função principal para verificar e limpar o código
def verificar_codigo(codigo):
    try:
        codigo_sem_comentarios = remover_comentarios(codigo)
        return remover_importacoes_nao_usadas(codigo_sem_comentarios)
    except Exception as e:
        logging.error(f"Erro ao verificar código: {e}")
        return codigo

# Função para limpar e salvar o script Python
def limpar_script(arquivo, nome_saida=None):
    try:
        with open(arquivo, 'r', encoding='utf-8') as file:
            codigo = file.read()
        codigo_limpo = verificar_codigo(codigo)
        nome_saida = nome_saida or f"limpo_{os.path.basename(arquivo)}"
        with open(nome_saida, 'w', encoding='utf-8') as file:
            file.write(codigo_limpo)
        logging.info(f"Arquivo limpo salvo como '{nome_saida}'.")
    except Exception as e:
        logging.error(f"Erro ao limpar o arquivo '{arquivo}': {e}")

# Função para remover importações não utilizadas com autoflake
def remover_importacoes_com_autoflake(file_path):
    try:
        subprocess.run(['autoflake', '--remove-all-unused-imports', '--in-place', file_path], check=True)
        logging.info(f"Importações não utilizadas removidas com sucesso no arquivo '{file_path}'.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro ao usar autoflake no arquivo '{file_path}': {e}")

# Função para encontrar código morto com vulture
def encontrar_codigo_morto(file_path):
    try:
        import vulture
        vult = vulture.Vulture()
        vult.scavenge([file_path])
        dead_code = vult.get_unused_code()
        if dead_code:
            logging.info("Código morto encontrado:")
            for item in dead_code:
                logging.info(f"Linha {item.lineno}: {item.source.strip()}")
        else:
            logging.info("Nenhum código morto encontrado.")
    except Exception as e:
        logging.error(f"Erro ao usar vulture no arquivo '{file_path}': {e}")

# Valida o caminho do arquivo
def validar_arquivo(caminho):
    return Path(caminho).exists() and Path(caminho).is_file()

# Menu interativo
def menu():
    while True:
        print("\nMenu de Opções:")
        print("1. Limpar script Python (remover comentários e importações não usadas)")
        print("2. Remover importações não utilizadas com autoflake")
        print("4. Encontrar código morto com vulture")
        print("3. Sair")
        opcao = input("Escolha uma opção (1-4): ")

        if opcao == '1':
            caminho = input("Digite o caminho do arquivo: ").strip()
            if validar_arquivo(caminho):
                nome_saida = input("Digite o nome do arquivo de saída (ou deixe em branco): ").strip() or None
                limpar_script(caminho, nome_saida)
            else:
                logging.warning("Arquivo inválido ou não encontrado.")
        elif opcao == '2':
            caminho = input("Digite o caminho do arquivo: ").strip()
            if validar_arquivo(caminho):
                remover_importacoes_com_autoflake(caminho)
            else:
                logging.warning("Arquivo inválido ou não encontrado.")
        elif opcao == '4':
            caminho = input("Digite o caminho do arquivo: ").strip()
            if validar_arquivo(caminho):
                encontrar_codigo_morto(caminho)
            else:
                logging.warning("Arquivo inválido ou não encontrado.")
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            logging.warning("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()

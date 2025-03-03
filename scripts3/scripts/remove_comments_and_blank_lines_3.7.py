import subprocess
import os

# Função para verificar e remover importações não utilizadas
def remove_unused_imports(file_path):
    try:
        # Verifica se o autoflake está instalado
        if subprocess.run(['which', 'autoflake'], capture_output=True).returncode != 0:
            print("Erro: 'autoflake' não está instalado. Instale com 'pip install autoflake'.")
            return
        
        # Remove importações não utilizadas
        subprocess.run(['autoflake', '--remove-all-unused-imports', '--in-place', file_path])
        print(f"Importações não utilizadas removidas de: {file_path}")
    
    except Exception as e:
        print(f"Erro ao remover importações não utilizadas: {e}")

# Função para remover comentários e linhas vazias
def remover_comentarios(arquivo_entrada, arquivo_saida):
    try:
        if not os.path.exists(arquivo_entrada):
            print(f"Erro: O arquivo {arquivo_entrada} não foi encontrado.")
            return
        
        with open(arquivo_entrada, 'r') as entrada:
            linhas = entrada.readlines()
        
        linhas_sem_comentarios = [
            linha.split('#')[0].rstrip() for linha in linhas if linha.split('#')[0].strip()
        ]
        
        with open(arquivo_saida, 'w') as saida:
            saida.write('\n'.join(linhas_sem_comentarios) + '\n')
        
        print(f"Arquivo sem comentários salvo como: {arquivo_saida}")
    
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Caminho do arquivo
arquivo_entrada = "/storage/emulated/0/qpython/scripts3/arquivo_morto.py"
arquivo_saida = "/storage/emulated/0/qpython/scripts3/arquivo.py"

# Executa as funções
remover_comentarios(arquivo_entrada, arquivo_saida)
remove_unused_imports(arquivo_saida)
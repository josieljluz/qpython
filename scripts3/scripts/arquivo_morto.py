import subprocess
import vulture

# Função para verificar e remover importações não utilizadas
def remove_unused_imports(file_path):
    # Usando autoflake para remover importações não utilizadas
    subprocess.run(['autoflake', '--remove-all-unused-imports', '--in-place', file_path])

# Função para verificar código morto com vulture
def find_dead_code(file_path):
    # Usando vulture para encontrar código morto
    vult = vulture.Vulture()
    vult.scan(file_path)

    dead_code = vult.get_unused_code()
    
    if dead_code:
        print("Código morto encontrado:")
        for line in dead_code:
            print(f"Linha {line.lineno}: {line.source.strip()}")
    else:
        print("Nenhum código morto encontrado.")

# Função principal
def clean_python_script(file_path):
    # Passo 1: Remover importações não utilizadas
    remove_unused_imports(file_path)
    
    # Passo 2: Encontrar e exibir código morto
    find_dead_code(file_path)

    print("\nScript limpo com sucesso!")

if __name__ == '__main__':
    # Usar input() para o caminho do arquivo Python
    script_path = input("Digite o caminho do script Python a ser limpo: ")
    
    # Verificar e limpar o script
    clean_python_script(script_path)
'''

import subprocess
import vulture
from shutil import copyfile

# Função para verificar e remover importações não utilizadas
def remove_unused_imports(file_path):
    # Usando autoflake para remover importações não utilizadas
    subprocess.run(['autoflake', '--remove-all-unused-imports', '--in-place', file_path])

# Função para verificar código morto com vulture
def find_dead_code(file_path):
    # Usando vulture para encontrar código morto
    vult = vulture.Vulture()
    vult.scan(file_path)

    dead_code = vult.get_unused_code()
    
    if dead_code:
        print("Código morto encontrado:")
        for line in dead_code:
            print(f"Linha {line.lineno}: {line.source.strip()}")
    else:
        print("Nenhum código morto encontrado.")

# Função principal
def clean_python_script(file_path, output_path=None):
    # Passo 1: Remover importações não utilizadas
    remove_unused_imports(file_path)
    
    # Passo 2: Encontrar e exibir código morto
    find_dead_code(file_path)
    
    # Passo 3: Copiar o arquivo limpo para o caminho de saída, se fornecido
    if output_path:
        copyfile(file_path, output_path)
        print(f"Script limpo salvo em: {output_path}")
    else:
        print("\nScript limpo no local original!")

if __name__ == '__main__':
    # Solicitar o caminho do script Python
    script_path = input("Digite o caminho do script Python a ser limpo: ")
    
    # Solicitar o caminho de saída (opcional)
    output_path = input("Digite o caminho de saída para o script limpo (pressione Enter para usar o caminho original): ").strip()
    if not output_path:
        output_path = None  # Usar o caminho original
    
    # Verificar e limpar o script
    clean_python_script(script_path, output_path)'''

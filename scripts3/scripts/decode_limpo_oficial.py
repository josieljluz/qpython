# -*- coding:utf8 -*-
import os
import sys
import zlib
import time
import base64
import marshal
import py_compile
dias_semana = {"Sunday": "domingo", "Monday": "segunda-feira", "Tuesday": "terça-feira", "Wednesday": "quarta-feira", "Thursday": "quinta-feira", "Friday": "sexta-feira", "Saturday": "sábado"}
meses = {"January": "janeiro", "February": "fevereiro", "March": "março", "April": "abril", "May": "maio", "June": "junho", "July": "julho", "August": "agosto", "September": "setembro", "October": "outubro", "November": "novembro", "December": "dezembro"}
data_ingles = time.strftime("%A, %d de %B de %Y, %H:%M:%S")
for eng, pt in dias_semana.items():
    data_ingles = data_ingles.replace(eng, pt)
for eng, pt in meses.items():
    data_ingles = data_ingles.replace(eng, pt)
time_extenso = "" + data_ingles
if sys.version_info[0] == 2:
    _input = "raw_input('%s')"
elif sys.version_info[0] == 3:
    _input = "input('%s')"
else:
    sys.exit("\n Sua versão do Python não é suportada!")
zlb = lambda in_: zlib.compress(in_)
b16 = lambda in_: base64.b16encode(in_)
b32 = lambda in_: base64.b32encode(in_)
b64 = lambda in_: base64.b64encode(in_)
mar = lambda in_: marshal.dumps(compile(in_, '<x>', 'exec'))
note = f"# 𝓑𝔂 ✩𝙅𝙤𝙨𝙞𝙚𝙡 𝙅𝙚𝙛𝙛𝙚𝙧𝙨𝙤𝙣✩✔\n# ╔═══════════════════════════════════════╗\n# ║           PyEncrypt (Ofuscado com PyObfuscate)\n# ║  Autor        : Josiel Jefferson\n# ║  Github       : https://github.com/josielljefferson\n# ║  Tempo       : {time_extenso}\n# ╚═══════════════════════════════════════╝\n\n"
note = f"""# 𝓑𝔂 ✩𝙅𝙤𝙨𝙞𝙚𝙡 𝙅𝙚𝙛𝙛𝙚𝙧𝙨𝙤𝙣✩✔\n# ╔═════════════════════════════════════════╗\n# ║          PyEncrypt (Ofuscado com PyObfuscate)\n# ║ Autor  : Josiel Jefferson\n# ║ Github : https://github.com/josielljefferson\n# ║ Tempo : {time_extenso}\n# ╚═════════════════════════════════════════╝\n"""
def banner():
    print(' ╔═════════════════════════════════╗\n ║          PyObfuscate            ║\n ║  Simple Python Code Obfuscator  ║\n ║  Author : Tahmid Rayat          ║\n ║  Github : Github.com/HTR-TECH   ║\n ╚═════════════════════════════════╝\n')
def menu():
    print("\n [01] Codificar com Marshal\n [02] Codificar com Zlib\n [03] Codificar com Base16\n [04] Codificar com Base32\n [05] Codificar com Base64\n [06] Codificar com Zlib, Base16\n [07] Codificar com Zlib, Base32\n [08] Codificar com Zlib, Base64\n [09] Codificar com Marshal, Zlib\n [10] Codificar com Marshal, Base16\n [11] Codificar com Marshal, Base32\n [12] Codificar com Marshal, Base64\n [13] Codificar com Marshal, Zlib, Base16\n [14] Codificar com Marshal, Zlib, Base32\n [15] Codificar com Marshal, Zlib, Base64\n [16] Codificação Simples\n [17] Decodificar Arquivo\n [18] Sair")
class FileSize:
    def datas(self, z):
        for x in ['Byte', 'KB', 'MB', 'GB']:
            if z < 1024.0:
                return "%3.1f %s" % (z, x)
            z /= 1024.0
    def __init__(self, path):
        if os.path.isfile(path):
            dts = os.stat(path).st_size
            print(" [-] Tamanho do Arquivo Codificado: %s\n" % self.datas(dts))
def Encode(option, data, output):
    loop = int(eval(_input % " [-] Quantidade de Codificações : "))
    if option == 1:
        xx = "mar(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__[::-1]);"
    elif option == 2:
        xx = "zlb(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__[::-1]);"
    elif option == 3:
        xx = "b16(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b16decode(__[::-1]);"
    elif option == 4:
        xx = "b32(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b32decode(__[::-1]);"
    elif option == 5:
        xx = "b64(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b64decode(__[::-1]);"
    elif option == 6:
        xx = "b16(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 7:
        xx = "b32(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));"
    elif option == 8:
        xx = "b64(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));"
    elif option == 9:
        xx = "zlb(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));"
    elif option == 10:
        xx = "b16(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b16decode(__[::-1]));"
    elif option == 11:
        xx = "b32(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b32decode(__[::-1]));"
    elif option == 12:
        xx = "b64(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b64decode(__[::-1]));"
    elif option == 13:
        xx = "b16(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1])));"
    elif option == 14:
        xx = "b32(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1])));"
    elif option == 15:
        xx = "b64(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"
    else:
        sys.exit("\n Opção inválida!")
    for x in range(loop):
        try:
            data = "exec((_)(%s))" % repr(eval(xx))
        except TypeError as s:
            sys.exit(" TypeError : " + str(s))
    with open(output, 'w') as f:
        f.write(note + heading + data)
        f.close()
def SEncode(data, output):
    for x in range(5):
        method = repr(b64(zlb(mar(data.encode('utf8'))))[::-1])
        data = "exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))" % method
    z = []
    for i in data:
        z.append(ord(i))
    sata = "_ = %s\nexec(''.join(chr(__) for __ in _))" % z
    with open(output, 'w') as f:
        f.write(note + "exec(str(chr(35)%s));" % '+chr(1)' * 10000)
        f.write(sata)
        f.close()
    py_compile.compile(output, output)
def Decode(file, output):
    """Descriptografa um arquivo Python ofuscado."""
    try:
        with open(file, 'r') as f:
            code = f.read()
        code = code.split("# -----------------------------")[1]
        exec(code, globals())
        decoded_code = eval("_")
        with open(output, 'w') as f:
            f.write(decoded_code.decode('utf8'))
        print(f"\n [-] Arquivo {file} descriptografado com sucesso!")
        print(f" [-] Salvo como {output}")
        FileSize(output)
    except Exception as e:
        sys.exit(f"\n Erro durante a descriptografia: {str(e)}")
def MainMenu():
    try:
        os.system('clear')
        banner()
        menu()
        try:
            option = int(eval(_input % " [-] Opção : "))
        except ValueError:
            sys.exit("\n Opção inválida!")
        if option > 0 and option <= 18:
            if option == 18:
                sys.exit("\n Obrigado por usar esta ferramenta")
            os.system('clear')
            banner()
        else:
            sys.exit('\n Opção inválida!')
        if option == 17:
            file = eval(_input % " [-] Nome do Arquivo Criptografado : ")
            output = file.lower().replace('_enc.py', '_dec.py')
            Decode(file, output)
            return
        try:
            file = eval(_input % " [-] Nome do Arquivo : ")
            data = open(file).read()
        except IOError:
            sys.exit("\n Arquivo Não Encontrado!")
        output = file.lower().replace('.py', '') + '_enc.py'
        if option == 16:
            SEncode(data, output)
        else:
            Encode(option, data, output)
        print("\n [-] Arquivo criptografado com sucesso: %s" % file)
        print(" [-] Salvo como %s" % output)
        FileSize(output)
    except KeyboardInterrupt:
        time.sleep(1)
        sys.exit()
if __name__ == "__main__":
    MainMenu()
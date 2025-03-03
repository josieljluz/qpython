import hashlib
from base64 import b64encode, b64decode
import binascii
import re
from time import sleep
import os
import platform
Limpar = "cls" if platform.system() == "Windows" else "clear"
os.system(Limpar)
def Apresentacao():
	os.system(Limpar)
	print("""\033[1;33m

                                          ....:..                               
                                     .^7JPPPPGPPP5YJ!:                          
                                   :?PGPBBB##&&&&&####BJ:                       
                                 .7PGBG#&&&&&&&&&&&&&&@@&5:                     
                                :YGGGB&&&&#GG#&&&&&&&&&&@@B!                    
                               .YPPG#&&&&&&&&&&&&&&&&&&&&&@&J                   
                              ..^^P@&&&&&&&&&&&&&&&&&&&&&&&@@J                  
                            .^^:::J@@&&&&&&&&&&&&&&&&&&&&&&&@#.                 
             :!7!: .^~^. .::^JJ^::^Y#&&&&&&&&&&&&&&&&&&&&&&&&&7                 
            ^#&&&#G#&&#G~:::::::^^~~!P@@@&&&&&&&&&&&&&&&&&&&&&~                 
            !PJB#GBPGB##!::^^^^~^^:^7J5GB&@&&&&&&&&&&&&&&&&&@&:                 
            .~ Y~:? ~~.                  ^B@&&&&&&&&&&&&&&&&@Y                  
             ^^5GPJJJJJ~                 :B@&&&&&&&&&&&&&&&&@G                   
            .Y##G! ?B&@?              :JG&@&&&&&&&&&&&&&&&&&@G~                   
           :7J!^    .~?Y7:         :?P#@@&&&&&&&&&&&&&&&&&&&&7                    
                                 :?B&&&&&&&&&&&&&&&&&&&&&@G.                    
                               ^YB#####&&&&&&&&&&&&&&&&&&&~                     
                             ^Y#&#######&&&&&&&&&&&&&&&&&&^                     
                           :Y###########&&&&&&&&&&&&&&&&&&7                     
                         .J#&###########&&@@@@@@@@@@@@@@@@@5:                   
                        .YGPPPPPPPPPPPPPPGGGGGGGGGGGGGGGGGGG5~                                                                                              
""")
def Again(frase, call):
	opcao1 = input(frase)
	if opcao1 == "s":
		call()
	elif opcao1 == "n":
		Escolha()
	else:
		Again(frase,call)
def Escolha():
	Apresentacao()
	print("""
	\033[1;33m[\033[1;33m*\033[1;33m]\033[0m \033[32mESCOLHA UMA DAS OPÇÕES ABAIXO PARA CONTINUAR:\033[0m
	\033[1;33mA\033[0m) \033[1;33mCODIFICAR\033[0m - \033[1;32mMD5\033[0m
	\033[1;33mB\033[0m) \033[1;33mCODIFICAR\033[0m - \033[1;32mSHA1\033[0m
	\033[1;33mC\033[0m) \033[1;33mCODIFICAR\033[0m - \033[1;32mSHA224\033[0m
	\033[1;33mD\033[0m) \033[1;33mCODIFICAR\033[0m - \033[1;32mSHA256\033[0m
	\033[1;33mE\033[0m) \033[1;33mCODIFICAR\033[0m - \033[1;32mSHA384\033[0m
	\033[1;33mF\033[0m) \033[1;33mCODIFICAR\033[0m - \033[1;32mSHA512\033[0m
	\033[1;33mG\033[0m) \033[1;33mCODIFICAR/DECODIFICAR\033[0m - \033[1;32mBASE64\033[0m
	\033[1;33mH\033[0m) \033[1;33mCODIFICAR/DECODIFICAR\033[0m - \033[1;32mBINÁRIO\033[0m
	\033[1;33mI\033[0m) \033[1;33mCODIFICAR/DECODIFICAR\033[0m - \033[1;32mHEXADECIMAL\033[0m
	\033[1;33mJ\033[0m) \033[1;33mCODIFICAR/DECODIFICAR\033[0m - \033[1;32mCIFRA DE CÉSAR\033[0m
	\033[1;33mK\033[0m) \033[1;33mINVERTER\033[0m - \033[1;32mTEXTO\033[0m
	\033[1;33mL\033[0m) \033[1;33mINVERTER\033[0m - \033[1;32mPALAVRAS\033[0m
	\033[1;33mS\033[0m) \033[1;32mSAIR\033[0m
""")
	opcao1 = input("\n\033[1;33mEscolha a opção senhor(a):\033[0m ")
	if opcao1 == "A" or opcao1 == "a":
		Md5()
	elif opcao1 == "B" or opcao1 == "b":
		Sha1()
	elif opcao1 == "C" or opcao1 == "c":
		Sha224()
	elif opcao1 == "D" or opcao1 == "d":
		Sha256()
	elif opcao1 == "E" or opcao1 == "e":
		Sha384()
	elif opcao1 == "F" or opcao1 == "f":
		Sha512()
	elif opcao1 == "G" or opcao1 == "g":
		Base64()
	elif opcao1 == "H" or opcao1 == "h":
		Binario()
	elif opcao1 == "I" or opcao1 == "i":
		Hexadecimal()
	elif opcao1 == "J" or opcao1 == "j":
		CifraDeCesar()
	elif opcao1 == "K" or opcao1 == "k":
		TextReverse()
	elif opcao1 == "L" or opcao1 == "l":
		WordsReverse()
	elif opcao1 == "S" or opcao1 == "s":
		exit(1)
	else:
		Escolha()
def Md5():
	Apresentacao()
	mystring = input("\033[32mINSIRA O TEXTO QUE DESEJA CRIPTOGRAFAR EM MD5:\033[0m ")
	hash_object = hashlib.md5(mystring.encode())
	print("")
	print(hash_object.hexdigest())
	print("")
	Again("\n\033[32mDESEJA FAZER OUTRA CRIPTOGRAFIA EM MD5 (s/n) ?:\033[1;m ", Md5)
def Sha1():
	Apresentacao()
	mystring = input("\033[32mINSIRA O TEXTO QUE DESEJA CRIPTOGRAFAR EM SHA1\033[0m: ")
	hash_object = hashlib.sha1(mystring.encode())
	print("")
	print(hash_object.hexdigest())
	print("")
	Again("\n\033[32mDESEJA FAZER OUTRA CRIPTOGRAFIA EM SHA1 (s/n) ?:\033[1;m ", Sha1)
def Sha224():
	Apresentacao()
	mystring = input("\033[32mINSIRA O TEXTO QUE DESEJA CRIPTOGRAFAR EM SHA224\033[0m: ")
	hash_object = hashlib.sha224(mystring.encode())
	print("")
	print(hash_object.hexdigest())
	print("")
	Again("\n\033[32mDESEJA FAZER OUTRA CRIPTOGRAFIA EM SHA224 (s/n) ?:\033[1;m ", Sha224)
def Sha256():
	Apresentacao()
	mystring = input("\033[32mINSIRA O TEXTO QUE DESEJA CRIPTOGRAFAR EM SHA256\033[0m: ")
	hash_object = hashlib.sha256(mystring.encode())
	print("")
	print(hash_object.hexdigest())
	print("")
	Again("\n\033[32mDESEJA FAZER OUTRA CRIPTOGRAFIA EM SHA256 (s/n) ?:\033[1;m ", Sha256)
def Sha384():
	Apresentacao()
	mystring = input("\033[32mINSIRA O TEXTO QUE DESEJA CRIPTOGRAFAR EM SHA384\033[0m: ")
	hash_object = hashlib.sha384(mystring.encode())
	print("")
	print(hash_object.hexdigest())
	print("")
	Again("\n\033[32mDESEJA FAZER OUTRA CRIPTOGRAFIA EM SHA384 (s/n) ?:\033[1;m ", Sha384)
def Sha512():
	Apresentacao()
	mystring = input("\033[32mINSIRA O TEXTO QUE DESEJA CRIPTOGRAFAR EM SHA512\033[0m: ")
	hash_object = hashlib.sha512(mystring.encode())
	print("")
	print(hash_object.hexdigest())
	print("")
	Again("\n\033[32mDESEJA FAZER OUTRA CRIPTOGRAFIA EM SHA512 (s/n) ?:\033[1;m ", Sha512)
def Base64Encode():
	Apresentacao()
	mystring = str(input("\033[32mINSIRA O TEXTO QUE DESEJA TRANSFORMAR EM BASE64\033[0m: "))
	print("")
	encode = b64encode(mystring.encode('utf-8'))
	decode = encode.decode('utf-8')
	print(decode)
	print("")
	Again("\n\033[32mDESEJA TRANSFORMAR OUTRO TEXTO EM BASE64 (s/n) ?:\033[1;m ", Base64Encode)
def Base64Decode():
	Apresentacao()
	mystring = str(input("\033[32mINSIRA O TEXTO QUE DESEJA DESCOBRIR EM BASE64\033[0m: "))
	print("")
	try:
		decode = b64decode(mystring).decode('utf-8')
		print(decode)
		print("")
	except:
		print("\n[\033[1;91m!\033[1;m] INCORRETO")
		sleep(3)
		Base64Decode()
	Again("\n\033[32mDESEJA DESCOBRIR OUTRO TEXTO EM BASE64 (s/n) ?:\033[1;m ", Base64Decode)
def Base64():
	Apresentacao()
	print("""
[\033[32m*\033[0m] \033[1;32mESCOLHA UMA DAS OPÇÕES ABAIXO PARA CONTINUAR:\033[0m
\033[1;33m1\033[0m) \033[1;33mCODIFICAR\033[0m - \033[1;32mBASE64\033[0m
\033[1;33m2\033[0m) \033[1;33mDECODIFICAR\033[0m - \033[1;32mBASE64\033[0m
""")
	opcao1 = input("\n\033[1;33m➤\033[0m ")
	if opcao1 == "1":
		Base64Encode()
	elif opcao1 == "2":
		Base64Decode()
	else:
		Base64()
def BinarioEncode(encoding='utf-8', errors='surrogatepass'):
	Apresentacao()
	try:
		mystring = input("\033[32mINSIRA O TEXTO QUE DESEJA TRANSFORMAR EM BINÁRIO\033[0m: ")
		print("")
		bits = bin(int(binascii.hexlify(mystring.encode(encoding, errors)), 16))[2:]
		print(bits.zfill(8 * ((len(bits) + 7) // 8)))
		print("")
	except:
		print("\n\n\033[32m[\033[0m\033[1;91m!\033[0m\033[32m] \033[1;91mERRO\033[0m")
		sleep(3)
		BinarioEncode()
	Again("\n\033[32mDESEJA TRANSFORMAR OUTRO TEXTO EM BINÁRIO (s/n) ?:\033[1;m ", BinarioEncode)
def BinarioDecode(encoding='utf-8', errors='surrogatepass'):
	Apresentacao()
	try:
		binario = input("\033[32mINSIRA A SEQUÊNCIA DE NÚMEROS QUE DESEJA DESCOBRIR EM BINÁRIO\033[0m: ")
		binario = binario.replace(" ", "")
		n = int(binario, 2)
		print("")
		print(int2bytes(n).decode(encoding, errors))
		print("")
	except:
		print("\n\n\033[32m[\033[0m\033[1;91m!\033[0m\033[32m] \033[1;91mERRO\033[0m")
		sleep(3)
		BinarioDecode()
	Again("\n\033[32mDESEJA DESCOBRIR OUTRA SEQUÊNCIA EM BINÁRIO (s/n) ?:\033[1;m ", BinarioDecode)
def int2bytes(i):
	hex_string = '%x' % i
	n = len(hex_string)
	return binascii.unhexlify(hex_string.zfill(n + (n & 1)))
def Binario():
	Apresentacao()
	print("""
[\033[1;32m*\033[1;m] \033[1;32mESCOLHA UMA DAS OPÇÕES ABAIXO PARA CONTINUAR:\033[0m
\033[1;33m1\033[0m) \033[1;33mCODIFICAR\033[0m - \033[1;32mBINÁRIO\033[0m
\033[1;33m2\033[0m) \033[1;33mDECODIFICAR\033[0m - \033[1;32mBINÁRIO\033[0m
""")
	opcao1 = input("\n\033[1;33m➤\033[0m ")
	if opcao1 == "1":
		BinarioEncode()
	elif opcao1 == "2":
		BinarioDecode()
	else:
		Binario()
def HexaEncode():
	Apresentacao()
	mystring = input("\033[32mINSIRA O TEXTO QUE DESEJA TRANSFORMAR EM HEXADECIMAL\033[0m: ")
	print("")
	encode = binascii.hexlify(bytes(mystring, "utf-8"))
	encode = str(encode).strip("b")
	encode = encode.strip("'")
	encode = re.sub(r'(..)', r'\1 ', encode).strip()
	print(encode)
	print("")
	Again("\n\033[32mDESEJA TRANSFORMAR OUTRO TEXTO EM HEXADECIMAL (s/n) ?:\033[1;m ", HexaEncode)
def HexaDecode():
	Apresentacao()
	try:
		mystring = input("\033[32mINSIRA A SEQUÊNCIA DE CARACTERES QUE DESEJA DESCOBRIR EM HEXADECIMAL\033[1;m: ")
		print("")
		decode = bytes.fromhex(mystring).decode('utf-8')
		print(decode)
		print("")
	except:
		print("\n\n\033[32m[\033[0m\033[1;91m!\033[0m\033[32m] \033[1;91mERRO\033[0m")
		sleep(3)
		HexaDecode()
	Again("\n\033[32mDESEJA DESCOBRIR OUTRA SEQUÊNCIA EM HEXADECIMAL (s/n) ?:\033[1;m ", HexaDecode)
def Hexadecimal():
	Apresentacao()
	print("""
[\033[1;32m*\033[1;m] \033[1;32mESCOLHA UMA DAS OPÇÕES ABAIXO PARA CONTINUAR:\033[0m
\033[1;33m1\033[0m) \033[1;33mCODIFICAR\033[0m - \033[1;32mHEXADECIMAL\033[0m
\033[1;33m2\033[0m) \033[1;33mDECODIFICAR\033[0m - \033[1;32mHEXADECIMAL\033[0m
""")
	opcao1 = input("\n\033[1;33m➤\033[0m ")
	if opcao1 == "1":
		HexaEncode()
	elif opcao1 == "2":
		HexaDecode()
	else:
		Hexadecimal()
def TextReverseEncode():
	Apresentacao()
	mystring = input("\033[32mINSIRA O TEXTO QUE DESEJA INVERTER\033[0m: ")
	print("")
	print(mystring[::-1])
	print("")
	Again("\n\033[32mDESEJA FAZER OUTRA INVERSÃO (s/n) ?:\033[1;m ", TextReverseEncode)
def TextReverseDecode():
	Apresentacao()
	mystring = input("\033[32mINSIRA O TEXTO QUE DESEJA DESCOBRIR A INVERSÃO\033[0m: ")
	print("")
	print(mystring[::-1])
	print("")
	Again("\n\033[32mDESEJA DESCOBRIR OUTRA INVERSÃO (s/n) ?:\033[1;m ", TextReverseDecode)
def TextReverse():
	Apresentacao()
	print("""
[\033[1;32m*\033[1;m] \033[1;32mESCOLHA UMA DAS OPÇÕES ABAIXO PARA CONTINUAR:\033[0m
\033[1;33m1\033[0m) \033[1;33mCODIFICAR\033[0m - \033[1;32mTEXTO-INVERTIDO\033[0m
\033[1;33m2\033[0m) \033[1;33mDECODIFICAR\033[0m - \033[1;32mTEXTO-INVERTIDO\033[0m
""")
	opcao1 = input("\n\033[1;33m➤\033[0m ")
	if opcao1 == "1":
		TextReverseEncode()
	elif opcao1 == "2":
		TextReverseDecode()
	else:
		TextReverse()
def WordsReverseEncode():
	Apresentacao()
	mystring = input("\033[32mINSIRA O TEXTO QUE DESEJA INVERTER AS PALAVRAS\033[0m: ")
	print("")
	print(' '.join(mystring.split()[::-1]))
	print("")
	Again("\n\033[32mDESEJA FAZER OUTRA INVERSÃO DE PALAVRAS (s/n) ?:\033[1;m ", WordsReverseEncode)
def WordsReverseDecode():
	Apresentacao()
	mystring = input("\033[32mINSIRA O TEXTO QUE DESEJA DESCOBRIR A INVERSÃO DAS PALAVRAS\033[0m: ")
	print("")
	print(' '.join(mystring.split()[::-1]))
	print("")
	Again("\n\033[32mDESEJA DESCOBRIR OUTRA INVERSÃO DE PALAVRAS (s/n) ?:\033[1;m ", WordsReverseDecode)
def WordsReverse():
	Apresentacao()
	print("""
[\033[1;32m*\033[1;m] \033[1;32mESCOLHA UMA DAS OPÇÕES ABAIXO PARA CONTINUAR:\033[0m
\033[1;33m1\033[0m) \033[1;33mCODIFICAR\033[0m - \033[1;32mINVERTER-PALAVRAS\033[0m
\033[1;33m2\033[0m) \033[1;33mDECODIFICAR\033[0m - \033[1;32mINVERTER-PALAVRAS\033[0m
""")
	opcao1 = input("\n\033[1;33m➤\033[0m ")
	if opcao1 == "1":
		WordsReverseEncode()
	elif opcao1 == "2":
		WordsReverseDecode()
	else:
		WordsReverse()
def CifraDeCesar():
	Apresentacao()
	print("""
[\033[1;32m*\033[1;m] \033[1;32mESCOLHA UMA DAS OPÇÕES ABAIXO PARA CONTINUAR:\033[0m
\033[1;33m1\033[0m) \033[1;33mCODIFICAR\033[0m - \033[1;32mCIFRA DE CÉSAR\033[0m
\033[1;33m2\033[0m) \033[1;33mDECODIFICAR\033[0m - \033[1;32mCIFRA DE CÉSAR\033[0m
""")
	opcao1 = input("\n\033[1;33m➤\033[0m ")
	if opcao1 == "1":
		ChamarBloco1()
	elif opcao1 == "2":
		ChamarBloco2()
	else:
		CifraDeCesar()
def cifrar(palavras, chave):
	abc = "abcdefghijklmnopqrstuvwxyz "
	text_cifrado = ''
	for letra in palavras:
		soma = abc.find(letra) + chave
		modulo = int(soma) % len(abc)
		text_cifrado = text_cifrado + str(abc[modulo])
	return text_cifrado
def decifrar(palavras, chave):
	abc = "abcdefghijklmnopqrstuvwxyz "
	text_cifrado = ''
	for letra in palavras:
		soma = abc.find(letra) - chave
		modulo = int(soma) % len(abc)
		text_cifrado = text_cifrado + str(abc[modulo])
	return text_cifrado
def ChamarBloco1():
	Apresentacao()
	try:
		c = str(input('\n\033[32mTEXTO PARA CIFRAR\033[0m: ')).lower()
		n = int(input('\033[32mCHAVE NUMÉRICA\033[0m: '))
		print("\033[32mRESULTADO\033[0m:", cifrar(c, n))
		print("")
	except:
		print("\n\n\033[32m[\033[0m\033[1;91m!\033[0m\033[32m] \033[1;91mERRO\033[0m")
		sleep(3)
		ChamarBloco1()
	Again("\n\033[32mDESEJA FAZER OUTRA CODIFICAÇÃO DA CIFRA DE CÉSAR (s/n) ?:\033[1;m ", ChamarBloco1)
def ChamarBloco2():
	Apresentacao()
	try:
		cc = str(input('\n\033[32mTEXTO PARA DECODIFICAR\033[0m: ')).lower()
		cn = int(input('\033[32mCHAVE NUMÉRICA\033[0m: '))
		print("\033[32mRESULTADO\033[0m:", decifrar(cc, cn))
		print("")
	except:
		print("\n\n\033[32m[\033[0m\033[1;91m!\033[0m\033[32m] \033[1;91mERRO\033[0m")
		sleep(3)
		ChamarBloco2()
	Again("\n\033[32mDESEJA FAZER OUTRA DECODIFICAÇÃO DA CIFRA DE CÉSAR (s/n) ?:\033[1;m ", ChamarBloco2)
Escolha()
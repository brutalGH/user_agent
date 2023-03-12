import os,sys,requests,rich,time,re,bs4,uuid,datetime,random
from concurrent.futures import ThreadPoolExecutor as thread
from bs4 import BeautifulSoup as soup
from rich.panel import Panel
from rich import print as jalan
ses = requests.Session()

# REUNIAN
vendor,pilih,uaget = [],[],[]

# WARNA
m = '\x1b[1;91m' 	# MERAH
x = '\33[m' 		# PUTIH
h = '\x1b[1;92m' 	# HIJAU +
hb = '\33[42m'		# HIJAU BOLD
mb = '\33[41m'		# MERAH BOLD

# MY USER-AGENT
awal = ses.get('https://my-user-agent.com/',headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}).text
wah = re.findall('span\>(.*?)\<\/div\>',awal)
open('.my_ua.txt','w').write(wah[0]);my_ua = open('.my_ua.txt','r').read()


# BANNER
def banner():
	os.system('clear')
	text = '[white]╔═╗╔╗╔╦╗╦   ╦╔╦╗\n╚═╗╠╩╗║ ║   ║ ║║\n╚═╝╚═╝╩ ╩═╝o╩═╩╝[white][green]\nCopyright 2023 By Brutal.ID[white]'
	ban = Panel(text,style="cyan")
	jalan(Panel(ban, title='v 0.1', style='white'))

# MENU
def menu():
	banner()
	print(f'╚ [{h} •{x} ] Menu Get User-Agent')
	print(f'    ╚ [{h} 1{x} ] Get User-Agent Random')
	print(f'    ╚ [{h} 2{x} ] Get User-Agent Manual')
	pilih = input(f'    ╚ [{h} •{x} ] Pilih : ')
	if '2' in pilih:
		vendors()
	else:
		random()

# VENDOR
def vendors():
	banner()
	try:
		os.system('rm -rf .vendor.txt')
	except:
		pass
	header = {'Accept':	'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language':	'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','Referer':	'https://user-agents.net/','sec-ch-ua':	'"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"','sec-ch-ua-platform':	'"Windows"','user-agents': my_ua}
	url = ses.get('https://user-agents.net/vendors',headers=header).text
	get = re.findall('<li\>\<a\ href\=\'(.*?)\'\>(.*?)\<\/a\>',url)
	for ap in get:
		ven = ap[1]
		vendor.append(ven)
		open('.vendor.txt','a').write(ap[0]+'\n')
	i = 0
	print(f'╚ [{h} •{x} ] Menu List Vendor')
	for dor in vendor:
		print(f'  [ {h}{i}{x} ] {dor}')
		i = i+1
	if 'smoot' in url:
		print(f' [{mb} ! {x}] Website Menghindari Spam, Mohon Tunggu 10 Detik')
	else:
		devices()

# DEVICES
def devices():
	no = int(input('	Pilih : '))
	banner()
	file = open('.vendor.txt','r').readlines()
	pil = file[no]
	ups = 'https://user-agents.net'+pil.replace('\n','')
	header = {'User-Agent':	my_ua}
	url = ses.get(ups,headers=header).text
	get = re.findall('h3\>(.*?)\<\/h3\>\<ul\ class\=(.*?)\</ul\>',url)
	try:
		os.system('rm -rf .devices.txt')
	except:
		pass
	i = 0
	print(f'╚ [ {h}•{x} ] Menu List Devices')
	for ok in get:
		print(f'\n  {h}• {x}'+ok[0])
		ambil = re.findall('<a\ href\=\'(.*?)\'\>(.*?)\<\/a\>',ok[1])
		for kumpul in ambil:
			open('.devices.txt','a').write(kumpul[0]+'\n')
			print(f'  {h}[ {i} ]{x} {kumpul[1]}')
			i = i+1
	ugentnya()

 # SCRAPT UGENT
def ugentnya():
	no = int(input('\n	Pilih : '))
	nama = input('	Input Nama File ( contoh.txt) : ')
	banner()
	file = open('.devices.txt','r').readlines()
	bahan = 'https://user-agents.net'+file[no].replace('\n','')
	header = {'User-Agent':	my_ua}
	url = ses.get(bahan,headers=header).text
	ua = re.findall('li\>\<a\ href\=\'(.*?)\'\>(.*?)\<\/a\>',url)
	for ok in ua:
		print(ok[1]);ugen = ok[1]+'\n';open('HASIL/'+nama,'a').write(ugen)
		uaget.append(ugen)
	print(f'\n [{hb} ! {x}] Succes Get {h}{len(uaget)}{x} User-Agent')
	print(f' [{hb} ! {x}] Result Di Simpan Ke [{h} HASIL/'+nama+f'{x} ]')

# RANDOM USER-AGENT
def random():
	banner()
	print(f'╚ [{mb} ! {x}] Input Max{m} 1000{x} User-Agent ')
	jumlah = input(f'╚ [{h} •{x} ] Input Jumlah User-Agent : ')
	nama = input(f'╚ [{h} •{x} ] Input Nama File ({h} contoh.txt{x}) : ')
	try:
		header = {
		'User-Agent':	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
		}
		data = {
		'action':	'generate',
		'limit':	jumlah
		}
		post = ses.post('https://user-agents.net/random',headers=header,data=data).text
		if 'smoot' in post:
			print(f' [{mb} ! {x}] Website Menghindari Spam, Mohon Tunggu 10 Detik')
		else:
			al = re.findall('li\>\<a\ href\=\"(.*?)\"\>(.*?)\<\/a\>\<\/li\>',post)
			for get in al:
				if 'Home' in get[1]:
					pass
				elif 'Download' in get[1]:
					pass
				elif 'Browsers' in get[1]:
					pass
				elif 'Bots' in get[1]:
					pass
				elif 'Devices' in get[1]:
					pass
				elif 'Lookup' in get[1]:
					pass
				elif 'Parser' in get[1]:
					pass
				elif 'My User Agent' in get[1]:
					pass
				elif 'Random' in get[1]:
					pass
				elif 'Contribute' in get[1]:
					pass
				elif 'Contacts' in get[1]:
					pass
				else:
					print(get[1])
					user = get[1]+'\n'
					open('HASIL/'+nama,'a').write(user)
					uaget.append(user)
			print(f'\n [{hb} ! {x}] Succes Get {h}{len(uaget)}{x} User-Agent')
			print(f' [{hb} ! {x}] Result Di Simpan Ke [{h} HASIL/'+nama+f'{x} ]')
	except Exception as e:
		print(e)

try:
	os.system('mkdir HASIL')
except:
	pass
menu()

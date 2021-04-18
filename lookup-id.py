#dont copy my code!!!
import re
from urllib.request import *
import sys
import os
from bs4 import *
import time
import socket
import random
import random
import requests
red = '\033[1;31m'
y= '\033[1;93m'
green = '\033[1;92m'
clear = '\033[1;0m'
bold = '\033[1;01m'
cyan = '\033[1;96m'
cy='\033[1;095m'
cya='\033[1;035m'
wh='\033[1;97m'
os.system("clear")
print(green)
os.system("figlet U-danbaiwa...")
print("\t\t\tAUTHOR: U-danbaiwa")
print(cyan+"  [×]"+red+" NOTE: E D U C A T I O N A l  P U R P O S E S  O N LY")
print(y+"""
██████████████████████████████
█▄─▄▄─█▄─▄─▀█▀▀▀▀▀██▄─▄█▄─▄▄▀█
██─▄████─▄─▀█████████─███─██─█
▀▄▄▄▀▀▀▄▄▄▄▀▀▀▀▀▀▀▀▀▄▄▄▀▄▄▄▄▀▀\n\t\tVersion: 2.0.1""")
print(cya+"~"*64)
print("\n")
#ur=a=requests.post("https://lookup-id.co/",data=b)
try:
	url=input(cyan+"[+] "+green+"Enter Facebook Link/Url: "+wh)
	print(cya+"\n")
	os.system("bash load.sh")
except Exception:
	print(green+"\n\t\tINVALID FACEBOOK URL")
	sys.exit()
try:
	data={'fburl': url, 'check': 'Lookup'}
	link=requests.post("https://lookup-id.com/",data=data)
	page=BeautifulSoup(link.content,"html.parser")
#hauka=page
#jekaja=huaka#wannan ne anin
#gumabeg=jekaja
#hsbsbsbs=gumabeg
	for i in page.find("p",{"id":"success"}).em:
	#hakane=i
		print("\n")
		time.sleep(3)
		print(y+"%"*55)
		print(wh)
		print(red+"\t(×)"+y+" VICTIM USERNAME: "+cyan+i)
		print("")
		print(y+"%"*55)
except Exception:
	print(cyan+"\n\t\tSOMETHING WRONG!!!")
	sys.exit()
try:
	for id in page.find("span",{"id":"code"}):
	#bsbshshsv=id
		print(cya)
		os.system("bash load2.sh")
		print("\n")
		time.sleep(3)
		print(y+"%"*55)
		print(wh)
		print(red+"\t(×) "+y+"FACEBOOK ID IS: "+cyan+id)
		print(wh)
		print(y+"%"*55)
except Exception:
	print(red+"\n\t\tSOMETHING WRONG!!!")
	sys.exit()
os.system("chmod +x lookup-id.py")
print("")


#ha=input("\tDID YOU WANT QUIT FROM THE TOOL?: ")
#if ha=="yes" or ha=="y" or ha=="YES":
#	sys.exit

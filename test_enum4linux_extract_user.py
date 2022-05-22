
import os
import subprocess
import sys
import re
import requests
from colorama import Fore, Back, Style
import fileinput
import requests
from urllib.request import urlopen
from urllib.error import *
import datetime
import schedule
import time


ipScan=input("insert ipscan: ")
repDir="prova"
cmd = subprocess.run(["mkdir",repDir])

s = open("Buffer" + repDir + "user_SMB.txt", "a")
cmd = subprocess.run(["./enum4linux/enum4linux.py","-U",ipScan],stdout=s)
s.close()

u= open("ListUser" + repDir + "user_SMB.txt", "a")
cmd = subprocess.run(["grep","username","Buffer" + repDir + "user_SMB.txt"],stdout=u)
u.close()

k= open("User" + repDir + "user_SMB.txt", "a")
cmd = subprocess.run(["awk","{print $2}","ListUser" + repDir + "user_SMB.txt"],stdout=k)
k.close()

with open("User" + repDir + "user_SMB.txt", "a") as f:
    f.write("guest\r\n")

#cmd = subprocess.run(["./enum4linux/enum4linux.py", "-U", ipScan, "|", "grep", "username", "|", "awk","'{print $2}'>" + repDir + "User_SMB_" + ipScan + ".txt"])


cmd = subprocess.run(['ncrack', "-vvv", ipScan, "-p", "smb", "-g", "to=30", "-f", "-U","User" + repDir + "user_SMB.txt", "-P","dictionary/pass_small.txt", "-oN", repDir + "/Ncrack_SMB_pass_discovered_" + ipScan + ".txt"])
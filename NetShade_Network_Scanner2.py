#!/bin/python3

# dependency check for the modules

try:
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
except ModuleNotFoundError:
    print('run the requirements.txt file to have all the requirements satisfied')


def menu():
    clear=subprocess.run("clear")
    print(Fore.LIGHTBLUE_EX + '''
 __   _ _______ _______ _______ _     _ _______ ______  _______
 | \  | |______    |    |______ |_____| |_____| |     \ |______
 |  \_| |______    |    ______| |     | |     | |_____/ |______

  /\     _|_  _  ._ _   _. _|_ o  _   (_   _  _. ._  ._   _  ._ 
 /--\ |_| |_ (_) | | | (_|  |_ | (_   __) (_ (_| | | | | (/_ |  
Autor: Fidemsrl.it	
    ''' + Style.RESET_ALL)

menu()

job=var_1=var_2=fast=deep=pn=bruteforce=evasion=Frag=Badsum=Datalength=Decoy=SourcePort=enum_mode=pn_enum=Nikto=Wapiti=arachni=Enum4linux=bruteforce_SMB=script_Nmap=Scheduling_enable=Day_of_week=Hour_of_day='n'
print(Fore.RED + "Setup job")

print(Fore.CYAN + "Enter name of job" + Style.RESET_ALL)
job = input()

menu()
print(Fore.RED + "Setup Target")

print(Fore.GREEN + "Enter the target of the net scan: (es.192.168.1.0)" + Style.RESET_ALL)
print(Fore.YELLOW + "NOTE:Alternatively, enter the single host to be analyzed (es.192.168.1.254)" + Style.RESET_ALL)
var_1 = input()

print(Fore.GREEN + "Enter the subnet of the net scan: (24)" + Style.RESET_ALL)
print(Fore.YELLOW + 'NOTE: Enter "32" for a single host' + Style.RESET_ALL)
var_2 = input()

menu()
print(Fore.RED + "Setup Type Scan")

print(Fore.GREEN + "Quick scan (not port scanner) (Y/N)" + Style.RESET_ALL)
fast="n"
fast = input()

print(Fore.GREEN + "Deep network scan and bruteforce common password on service discovered? (Y/N)" + Style.RESET_ALL)
deep="n"
deep = input()

if deep == 'Y':
    print(Fore.LIGHTGREEN_EX + ">> Deep Network Scan mode; Do you want use -Pn option ? (Y/N)" + Style.RESET_ALL)
    pn = input()

    print(Fore.LIGHTGREEN_EX + ">> Do you want to test common passwords on discovered services? (Y/N)" + Style.RESET_ALL)
    bruteforce = input()

print(Fore.BLUE + "IDS / FireWall evasion mode?(Y/N)" + Style.RESET_ALL)
evasion = input()

if evasion == 'Y':
    print(Fore.LIGHTBLUE_EX+ ">> Fragmentary packet mode:(Y/N)" + Style.RESET_ALL)
    Frag = input()
    print(Fore.LIGHTBLUE_EX + ">> Badsum check packet mode:(Y/N)" + Style.RESET_ALL)
    print(Fore.YELLOW + "NOTE:This scanning takes a long time")
    Badsum = input()
    print(Fore.LIGHTBLUE_EX + ">> Data random add packet mode:(Y/N)" + Style.RESET_ALL)
    Datalength = input()
    print(Fore.LIGHTBLUE_EX + ">> Decoy 5 random host mode:(Y/N)" + Style.RESET_ALL)
    Decoy = input()
    print(Fore.LIGHTBLUE_EX + ">> Source port DNS mode:(Y/N)" + Style.RESET_ALL)
    SourcePort = input()

menu()
print(Fore.RED + "Setup Enumeration Tool")

print(Fore.BLUE + "The next part of the tool will attempt to enumerate the services found in the NMAP scan." + Style.RESET_ALL)
print(Fore.LIGHTBLUE_EX + "Enumeration mode? (Y/N)" + Style.RESET_ALL)
enum_mode = input()
if enum_mode == 'Y':
    print(Fore.LIGHTBLUE_EX + ">> Do you want use -Pn option for port scanner? (Y/N)" + Style.RESET_ALL)
    pn_enum = input()
    print(Fore.LIGHTBLUE_EX + ">> Do you want use NIKTO? (Y/N)" + Style.RESET_ALL)
    Nikto = input()
    print(Fore.LIGHTBLUE_EX + ">> Do you want use WAPITI? (Y/N)" + Style.RESET_ALL)
    Wapiti = input()
    print(Fore.LIGHTBLUE_EX + ">> Do you want use ARACHNI? (Y/N)" + Style.RESET_ALL)
    arachni = input()
    print(Fore.LIGHTBLUE_EX + ">> Do you want use ENUM4LINUX? (Y/N)" + Style.RESET_ALL)
    Enum4linux = input()
    if Enum4linux == 'Y':
        print(Fore.LIGHTBLUE_EX + "-->> Do you want to test common passwords on discovered SAMBA services? (Y/N)" + Style.RESET_ALL)
        bruteforce_SMB = input()
    print(Fore.LIGHTBLUE_EX + ">> Do you want test the NMAP scripts? (Y/N)" + Style.RESET_ALL)
    script_Nmap = input()

menu()
print(Fore.RED + "Setup Scheduling Job")

print(Fore.MAGENTA + "The next part of the tool will attempt to scheduling the job" + Style.RESET_ALL)
print(Fore.MAGENTA + "Do you want to schedule the work? (Y/N)" + Style.RESET_ALL)
Scheduling_enable = input()

if Scheduling_enable == 'Y':
    print(Fore.LIGHTMAGENTA_EX + ">> Which day of the week?" + Style.RESET_ALL)
    print(
        Fore.YELLOW + "NOTE: WRITE 0 for Monday, 1 for Tuesday, 2 for Wednesday, 3 for Thursday, 4 for Friday, 5 for Saturday and 6 for Sunday ")
    Day_of_week = input()

    print(Fore.LIGHTMAGENTA_EX + ">> At that time?" + Style.RESET_ALL)
    print(Fore.YELLOW + "NOTE: WRITE es.  18:00 22:00 13:22 00:22 ")
    Hour_of_day = input()

########create variable and dir of report #########
var_nmap = var_1 + "/" + var_2
repDir = ''
z = ''


########create variable and dir of report #########
def setupVariableReportScan(a, b):
    Var_1 = a
    Var_2 = b
    time_string = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    RepDir = "Job_" + job + "_" + Var_1 + "_" + Var_2 + "_at_" + time_string
    cmd = subprocess.run(["mkdir", RepDir])
    return RepDir


###### weekday ####
def weekDay(a):
    if a == '0':
        outPut = "Monday"
        return outPut
    elif a == '1':
        outPut = "Tuesday"
        return outPut
    elif a == '2':
        outPut = "Wednesday"
        return outPut
    elif a == '3':
        outPut = "Thursday"
        return outPut
    elif a == '4':
        outPut = "Friday"
        return outPut
    elif a == '5':
        outPut = "Saturday"
        return outPut
    elif a == '6':
        outPut = "Sunday"
        return outPut


####### enter the Network-scanner ########


####### Fast Scan #######

def fastScan():
    if (fast == 'Y'):
        print(Fore.RED + '''
---Start Fast Scan Mode--- Scan started, please wait!
	''' + Style.RESET_ALL)
        try:
            # Fast Scan
            cmd = subprocess.run(["nmap", "-sn", var_nmap, "-oX", repDir + "/Fast_Scan_Nmap_" + var_1 + ".xml"],
                                 stdout=z)
            cmd = subprocess.run(["./nmap-converter.py", "-o", repDir + "/Fast_Scan_Nmap_XLS" + var_1 + ".xls",
                                  repDir + "/Fast_Scan_Nmap_" + var_1 + ".xml"])
        except KeyboardInterrupt:
            sys.exit()


####### Deep Scan #######

def deepScan():
    if (deep == 'Y'):
        print(Fore.RED + '''
---Start Deep Network Scan Mode---  Scan started, please wait!
	''' + Style.RESET_ALL)

        if pn == 'Y':
            try:
                # SCANNER NP mode NOT evasion mode
                cmd = subprocess.run(
                    ["nmap", "-Pn", "-p-", "-A", "-T4", var_nmap, "-oX", repDir + "/Deep_Scan_Nmap_" + var_1 + ".xml"],
                    stdout=z)
                cmd = subprocess.run(["./nmap-converter.py", "-o", repDir + "/Deep_Scan_Nmap_XLS" + var_1 + ".xls",
                                      repDir + "/Deep_Scan_Nmap_" + var_1 + ".xml"])

            except KeyboardInterrupt:
                sys.exit()

        # else of the scanner if
        elif pn != 'Y':
            try:
                # SCANNER NP mode NOT evasion mode
                cmd = subprocess.run(
                    ["nmap", "-p-", "-A", "-T4", var_nmap, "-oX", repDir + "/Deep_Scan_Nmap_" + var_1 + ".xml"],
                    stdout=z)
                cmd = subprocess.run(["./nmap-converter.py", "-o", repDir + "/Deep_Scan_Nmap_XLS" + var_1 + ".xls",
                                      repDir + "/Deep_Scan_Nmap_" + var_1 + ".xml"])

            except KeyboardInterrupt:
                sys.exit()

        if bruteforce == 'Y':
            try:
                print(Fore.RED + "Start Bruteforce Discovery Username and Password--- please wait!" + Style.RESET_ALL)
                cmd = subprocess.run(
                    ['ncrack', "-vvv", "-m", "telnet:to=10", "-m", "mysql:ssl=yes,to=20", "-iX",
                     repDir + "/Deep_Scan_Nmap_" + var_1 + ".xml", "-g", "to=60", "-f", "-U",
                     "dictionary/user_small.txt", "-P", "dictionary/pass_small.txt", "-oN",
                     repDir + "/Ncrack_password_discovered_" + var_1 + ".txt"])
            except KeyboardInterrupt:
                sys.exit()


def evasionScan():
    ####### enter the Network-scanner EVASION MODE ########

    if evasion == 'Y':
        print(Fore.BLUE + '''
---Start Evasion IDS/Firewall Scan Mode---
	''' + Style.RESET_ALL)
        try:
            # SCANNER evasion mode
            if Frag == 'Y':
                print(Fore.LIGHTBLUE_EX + '''
---Fragmentary mode--- Scan started, please wait!
			''' + Style.RESET_ALL)
                cmd = subprocess.run(
                    ["sudo", "nmap", "-f", var_nmap, "-oX", repDir + "/Nmap_evasion_mode_frag" + var_1 + ".xml"],
                    stdout=z)
                cmd = subprocess.run(
                    ["./nmap-converter.py", "-o", repDir + "/Nmap_evasion_mode_frag_XLS" + var_1 + ".xls",
                     repDir + "/Nmap_evasion_mode_frag" + var_1 + ".xml"])

            if Badsum == 'Y':
                print(Fore.LIGHTBLUE_EX + '''
---Badsum mode--- Scan started, please wait!
			''' + Style.RESET_ALL)
                cmd = subprocess.run(
                    ["sudo", "nmap", "--badsum", var_nmap, "-oX",
                     repDir + "/Nmap_evasion_mode_badsum" + var_1 + ".xml"], stdout=z)
                cmd = subprocess.run(
                    ["./nmap-converter.py", "-o", repDir + "/Nmap_evasion_mode_badsum_XLS" + var_1 + ".xls",
                     repDir + "/Nmap_evasion_mode_badsum" + var_1 + ".xml"])

            if Datalength == 'Y':
                print(Fore.LIGHTBLUE_EX + '''
---Data length mode--- Scan started, please wait!
			''' + Style.RESET_ALL)
                cmd = subprocess.run(["sudo", "nmap", "--data-length", "25", var_nmap, "-oX",
                                      repDir + "/Nmap_evasion_mode_data_length" + var_1 + ".xml"], stdout=z)
                cmd = subprocess.run(
                    ["./nmap-converter.py", "-o", repDir + "/Nmap_evasion_mode_data_length_XLS" + var_1 + ".xls",
                     repDir + "/Nmap_evasion_mode_data_length" + var_1 + ".xml"])

            if Decoy == 'Y':
                print(Fore.LIGHTBLUE_EX + '''
---Decoy mode--- Scan started, please wait!
			''' + Style.RESET_ALL)
                cmd = subprocess.run(
                    ["sudo", "nmap", "-D", "RND:5", var_nmap, "-oX",
                     repDir + "/Nmap_evasion_mode_decoy_random" + var_1 + ".xml"], stdout=z)
                cmd = subprocess.run(
                    ["./nmap-converter.py", "-o", repDir + "/Nmap_evasion_mode_decoy_random_XLS" + var_1 + ".xls",
                     repDir + "/Nmap_evasion_mode_decoy_random" + var_1 + ".xml"])

            if SourcePort == 'Y':
                print(Fore.LIGHTBLUE_EX + '''
---Source port DNS mode--- Scan started, please wait!
			''' + Style.RESET_ALL)
                cmd = subprocess.run(["sudo", "nmap", "--source-port", "53", var_nmap, "-oX",
                                      repDir + "/Nmap_evasion_mode_source_port_53" + var_1 + ".xml"], stdout=z)
                cmd = subprocess.run(
                    ["./nmap-converter.py", "-o", repDir + "/Nmap_evasion_mode_source_port_53_XLS" + var_1 + ".xls",
                     repDir + "/Nmap_evasion_mode_source_port_53" + var_1 + ".xml"])
        except KeyboardInterrupt:
            sys.exit()


def enumeration(a):

    ipScan = a

    print(Fore.RED + '''
---Start Enumeration Job--- 
        			''' + Style.RESET_ALL)

    if (enum_mode == 'Y'):

        print(Fore.LIGHTRED_EX + "Scanning host : " + ipScan + Style.RESET_ALL)

        f = open("Buffer_port_" + ipScan + "_" + repDir + ".txt", "a")

        print(Fore.CYAN + '''
---Port Scanner--- Scan started, please wait!
        			''' + Style.RESET_ALL)

        if (pn_enum == 'Y'):
            try:
                # SCANNER NP mode
                cmd = subprocess.run(["nmap", "-Pn", "-p-", "-T4", ipScan], stdout=f)
            except KeyboardInterrupt:
                sys.exit()
        # else of the scanner if
        elif (pn_enum != 'Y'):
            try:
                # SCANNER NP mode
                cmd = subprocess.run(["nmap", "-p-", "-T4", ipScan], stdout=f)
            except KeyboardInterrupt:
                sys.exit()

        f.close()
        x = open("Buffer_port_" + ipScan + "_" + repDir + ".txt")
        Parse = x.read()
        data = ''
        data = (re.findall(r'[0-9]+/', Parse))
        data = [x[:-1] for x in data]
        listToStr = ','.join([str(elem) for elem in data])

        print(Fore.YELLOW+"\n----------------Open Port on " + ipScan + "------------------\n"+Style.RESET_ALL)
        for x in data:
            print(Fore.LIGHTGREEN_EX+x+Style.RESET_ALL)
        print(Fore.YELLOW+"\n----------------------------------------------------------\n"+Style.RESET_ALL)

        try:
            cmd = subprocess.run(
                ["nmap", "-p", listToStr, "-A", "-T4", ipScan, "-oX", repDir + "/Nmap_portscanner_" + ipScan + ".xml"])
            cmd = subprocess.run(["./nmap-converter.py", "-o", repDir + "/Nmap_portscanner_" + ipScan + ".xls",
                                  repDir + "/Nmap_portscanner_" + ipScan + ".xml"])

        except KeyboardInterrupt:
            sys.exit()

        for port in data:

            print(Fore.YELLOW + '''
---HTTP/HTTPS Testing, please wait!
                    			''' + Style.RESET_ALL)
            ### test HTTP/HTTPS Service on port

            https_enable = ''
            http_enable = ''
            test_Url_https = "https://" + ipScan + ":" + port
            test_Url_http = "http://" + ipScan + ":" + port

            try:
                resp = requests.get(test_Url_https, timeout=10)
                print("Test connection HTTPS protocol host " + ipScan + ":" + port + " : " + str(resp))
                if str(resp) == '<Response [200]>':
                    https_enable = 'Y'
            except:
                print("Test connection HTTPS protocol host " + ipScan + ":" + port + " : ERROR")
                https_enable = 'N'

            try:
                resp1 = requests.get(test_Url_http, timeout=10)
                print("Test connection HTTP protocol host " + ipScan + ":" + port + " : " + str(resp1))
                if str(resp1) == '<Response [200]>':
                    http_enable = 'Y'
            except:
                print("Test connection HTTP protocol host " + ipScan + ":" + port + " : ERROR")
                https_enable = 'N'

            #### nikto ###
            if (Nikto == 'Y'):

                print(Fore.CYAN + '''
---"Start Nikto enumeration web service,  please wait!
                                ''' + Style.RESET_ALL)
                if https_enable == 'Y' or http_enable == 'Y':
                    print(Fore.YELLOW + "\n[*] execute Nikto on port " + port + " .\n" + Style.RESET_ALL)
                    try:
                        cmd = subprocess.run(["nikto", "-h", ipScan + ":" + port, "-Format", "txt", "-output",
                                              repDir + "/nikto_" + ipScan + ":" + port])

                    except KeyboardInterrupt:
                        sys.exit()

            #### Wapiti ###
            if (Wapiti == 'Y'):

                print(Fore.CYAN + '''
---"Start Wapiti enumeration web service,  please wait!
                                 ''' + Style.RESET_ALL)
                try:
                    if http_enable == 'Y':
                        print(
                            Fore.YELLOW + "\n[*] execute Wapiti (HTTP mode) on port " + port + " .\n" + Style.RESET_ALL)
                        cmd = subprocess.run(
                            ["wapiti", "--flush-session", "-u", "http://" + ipScan + ":" + port + "/", "-f", "txt",
                             "-o", repDir + "/wapiti_http_" + ipScan + ":" + port])
                    if https_enable == 'Y':
                        print(
                            Fore.YELLOW + "\n[*] execute Wapiti (HTTPS mode) on port " + port + " .\n" + Style.RESET_ALL)
                        cmd = subprocess.run(
                            ["wapiti", "--flush-session", "-u", "https://" + ipScan + ":" + port + "/", "-f", "txt",
                             "-o", repDir + "/wapiti_https_" + ipScan + ":" + port])
                except KeyboardInterrupt:
                    sys.exit()

            #### Arachni ###
            if (arachni == 'Y'):
                print(Fore.CYAN + '''
---"Start Arachni enumeration web service,  please wait!
                                                ''' + Style.RESET_ALL)
                try:  # arachni_reporter ../../example.com.afr --reporter=html:outfile=../../my_report.html.zip

                    if http_enable == 'Y':
                        print(
                            Fore.YELLOW + "\nExecute Arachni (HTTP mode) on port " + port + " .\n" + Style.RESET_ALL)
                        cmd = subprocess.run(["mkdir", repDir + "/Arachni_http_" + ipScan + "_" + port])
                        cmd = subprocess.run(["./arachni/bin/arachni", "--output-verbose", "--scope-include-subdomains",
                                              "http://" + ipScan + ":" + port,
                                              "--report-save-path=" + repDir + "/Arachni_http_" + ipScan + "_" + port + "/Arachni_http_" + ipScan + "_" + port + ".afr"])
                        cmd = subprocess.run(["./arachni/bin/arachni_reporter",
                                              repDir + "/Arachni_http_" + ipScan + "_" + port + "/Arachni_http_" + ipScan + "_" + port + ".afr",
                                              "--reporter=html:outfile=" + repDir + "/Arachni_http_" + ipScan + "_" + port + "/Arachni_http_" + ipScan + "_" + port + ".zip"])
                        cmd = subprocess.run(["unzip",
                                              repDir + "/Arachni_http_" + ipScan + "_" + port + "/Arachni_http_" + ipScan + "_" + port + ".zip",
                                              "-d", repDir + "/Arachni_http_" + ipScan + "_" + port])
                    if https_enable == 'Y':
                        print(
                            Fore.YELLOW + "\nExecute Arachni (HTTPS mode) on port " + port + " .\n" + Style.RESET_ALL)
                        cmd = subprocess.run(["mkdir", repDir + "/Arachni_https_" + ipScan + "_" + port])
                        cmd = subprocess.run(["./arachni/bin/arachni", "--output-verbose", "--scope-include-subdomains",
                                              "https://" + ipScan + ":" + port,
                                              "--report-save-path=" + repDir + "/Arachni_https_" + ipScan + "_" + port + "/Arachni_https_" + ipScan + "_" + port + ".afr"])
                        cmd = subprocess.run(["./arachni/bin/arachni_reporter",
                                              repDir + "/Arachni_https_" + ipScan + "_" + port + "/Arachni_https_" + ipScan + "_" + port + ".afr",
                                              "--reporter=html:outfile=" + repDir + "/Arachni_https_" + ipScan + "_" + port + "/Arachni_https_" + ipScan + "_" + port + ".zip"])
                        cmd = subprocess.run(["unzip",
                                              repDir + "/Arachni_https_" + ipScan + "_" + port + "/Arachni_https_" + ipScan + "_" + port + ".zip",
                                              "-d", repDir + "/Arachni_https_" + ipScan + "_" + port])
                except KeyboardInterrupt:
                    sys.exit()

            #### emun4linux ###
            if (Enum4linux == 'Y'):
                if (port == '139' or port == '445'):
                    try:
                        print(Fore.CYAN + '''
---"Start Emun4linux enumeration share service,  please wait!
                                         ''' + Style.RESET_ALL)
                        cmd = subprocess.run(
                            ["./enum4linux/enum4linux.py", "-A", ipScan, "-oA", repDir + "/enum4linux_" + ipScan])
                        print("\n Report enum4linux saved!")
                    except KeyboardInterrupt:
                        sys.exit()

                    if bruteforce_SMB == 'Y':

                        print(Fore.LIGHTCYAN_EX + '''
---"Start Bruteforce share service discovered,  please wait!
                                                        ''' + Style.RESET_ALL)
                        try:
                            s1 = open("Buffer" + repDir + "user_SMB.txt", "a")
                            cmd = subprocess.run(["./enum4linux/enum4linux.py", "-U", ipScan], stdout=s1)
                            s1.close()
                            try:
                                os.remove("Buffer" + repDir + "user_SMB.txt")
                            except:
                                print("not remove Buffer")

                            u = open("ListUser" + repDir + "user_SMB.txt", "a")
                            cmd = subprocess.run(["grep", "username", "Buffer" + repDir + "user_SMB.txt"], stdout=u)
                            u.close()
                            try:
                                os.remove("ListUser" + repDir + "user_SMB.txt")
                            except:
                                print("not remove Buffer")

                            k = open("User" + repDir + "user_SMB.txt", "a")
                            cmd = subprocess.run(["awk", "{print $2}", "ListUser" + repDir + "user_SMB.txt"], stdout=k)
                            k.close()

                            with open("User" + repDir + "user_SMB.txt", "a") as f:
                                f.write("guest\r\n")

                            # cmd = subprocess.run(["./enum4linux/enum4linux.py", "-U", ipScan, "|", "grep", "username", "|", "awk","'{print $2}'>" + repDir + "User_SMB_" + ipScan + ".txt"])

                            cmd = subprocess.run(['ncrack', "-vvv", ipScan, "-p", "smb", "-g", "to=30", "-f", "-U",
                                              "User" + repDir + "user_SMB.txt", "-P", "dictionary/pass_small.txt",
                                              "-oN", repDir + "/Ncrack_SMB_pass_discovered_" + ipScan + ".txt"])
                            try:
                                os.remove("User" + repDir + "user_SMB.txt")
                            except:
                                print("not remove Buffer")

                        except KeyboardInterrupt:
                            sys.exit()

        ### nmap script ###
        if (script_Nmap == 'Y'):

            print(Fore.CYAN + '''
---"Start NSE Nmap Script,  please wait!
                                            ''' + Style.RESET_ALL)
            try:
                print(Fore.YELLOW + "Start NMAP Script enumeration" + Style.RESET_ALL)
                print(Fore.BLUE + "Start Broadcast script" + Style.RESET_ALL)
                cmd = subprocess.run(["nmap", "--script", "broadcast", ipScan, "-oN",
                                      repDir + "/Nmap_script_broadcast_" + ipScan + ".txt"])

                print(Fore.BLUE + "Start Discovery script" + Style.RESET_ALL)
                cmd = subprocess.run(["nmap", "--script", "discovery", ipScan, "-oN",
                                      repDir + "/Nmap_script_discovery_" + ipScan + ".txt"])

                print(Fore.BLUE + "Start Malware script" + Style.RESET_ALL)
                cmd = subprocess.run(
                    ["nmap", "--script", "malware", ipScan, "-oN", repDir + "/Nmap_script_malware_" + ipScan + ".txt"])

                print(Fore.BLUE + "Start Exploit script" + Style.RESET_ALL)
                cmd = subprocess.run(
                    ["nmap", "--script", "exploit", ipScan, "-oN", repDir + "/Nmap_script_exploit_" + ipScan + ".txt"])

                print(Fore.BLUE + "Start Vuln script" + Style.RESET_ALL)
                cmd = subprocess.run(
                    ["nmap", "--script", "vuln", ipScan, "-oN", repDir + "/Nmap_script_vuln_" + ipScan + ".txt"])


            except KeyboardInterrupt:
                sys.exit()
        try:
            os.remove("Buffer_port_" + ipScan + "_" + repDir + ".txt")
        except:
            print("not remove Buffer")

def job_work(Job_ID,target,netmask,a,b,b1,b2,c,c1,c2,c3,c4,c5,d,d1,d2,d3,d4,d5,d51,d6,e,e1,e2):

    menu()
    print(Fore.RED+"---List process on Job: "+Fore.LIGHTBLUE_EX+Job_ID+Fore.RED+" ---"+Style.RESET_ALL)
    print(Fore.LIGHTRED_EX+"Target: "+Fore.LIGHTBLUE_EX+target+Fore.LIGHTRED_EX+" Netmask "+Fore.LIGHTBLUE_EX+netmask+Style.RESET_ALL)
    print(Fore.RED+"***********************************"+Style.RESET_ALL)
    if a=='Y':
        print(Fore.YELLOW+"[X] Fast Scan"+Style.RESET_ALL)
    else:
        print(Fore.YELLOW+"[ ] Fast Scan"+Style.RESET_ALL)
    if b=='Y':
        print(Fore.YELLOW+"[X] Deep Scan"+Style.RESET_ALL)
        if b1 == 'Y':
            print(Fore.LIGHTYELLOW_EX+"->[X] -PN option enable"+Style.RESET_ALL)
        else:
            print(Fore.LIGHTYELLOW_EX+"->[ ] -PN option enable"+Style.BRIGHT)
        if b2 == 'Y':
            print(Fore.LIGHTYELLOW_EX+"->[X] Bruteforce option enable"+Style.RESET_ALL)
        else:
            print(Fore.LIGHTYELLOW_EX+"->[ ] Bruteforce option enable"+Style.RESET_ALL)
    else:
        print(Fore.YELLOW+"[ ] Deep Scan"+Style.RESET_ALL)

    if c=='Y':
        print(Fore.YELLOW+"[X] Evasion IDS/Firewall Scan Mode"+Style.RESET_ALL)
        if c1 == 'Y':
            print(Fore.LIGHTYELLOW_EX+"->[X] Fragmentary mode"+Style.RESET_ALL)
        else:
            print(Fore.LIGHTYELLOW_EX+"->[ ] Fragmentary mode"+Style.BRIGHT)
        if c2 == 'Y':
            print(Fore.LIGHTYELLOW_EX+"->[X] Badsum mode"+Style.RESET_ALL)
        else:
            print(Fore.LIGHTYELLOW_EX+"->[ ] Badsum mode"+Style.RESET_ALL)
        if c3 == 'Y':
            print(Fore.LIGHTYELLOW_EX+"->[X] Data length mode"+Style.RESET_ALL)
        else:
            print(Fore.LIGHTYELLOW_EX+"->[ ] Data length mode"+Style.BRIGHT)
        if c4 == 'Y':
            print(Fore.LIGHTYELLOW_EX+"->[X] Decoy mode"+Style.RESET_ALL)
        else:
            print(Fore.LIGHTYELLOW_EX+"->[ ] Decoy mode"+Style.RESET_ALL)
        if c5 == 'Y':
            print(Fore.LIGHTYELLOW_EX+"->[X] Source port DNS mode"+Style.RESET_ALL)
        else:
            print(Fore.LIGHTYELLOW_EX+"->[ ] Source port DNS mode"+Style.RESET_ALL)
    else:
        print(Fore.YELLOW+"[ ] Evasion IDS/Firewall Scan Mode"+Style.RESET_ALL)
    if d=='Y':
        print(Fore.YELLOW+"[X] Enumeration mode"+Style.RESET_ALL)
        if d1 == 'Y':
            print(Fore.LIGHTYELLOW_EX+"->[X] -PN option enable"+Style.RESET_ALL)
        else:
            print(Fore.LIGHTYELLOW_EX+"->[ ] -PN option enable"+Style.BRIGHT)
        if d2 == 'Y':
            print(Fore.LIGHTYELLOW_EX+"->[X] MIKTO enable"+Style.RESET_ALL)
        else:
            print(Fore.LIGHTYELLOW_EX+"->[ ] NIKTO enable"+Style.RESET_ALL)
        if d3 == 'Y':
            print(Fore.LIGHTYELLOW_EX+"->[X] WAPITI enable"+Style.RESET_ALL)
        else:
            print(Fore.LIGHTYELLOW_EX+"->[ ] WAPITI enable"+Style.BRIGHT)
        if d4 == 'Y':
            print(Fore.LIGHTYELLOW_EX+"->[X] ARACHNI enable"+Style.RESET_ALL)
        else:
            print(Fore.LIGHTYELLOW_EX+"->[ ] ARACHNI enable"+Style.RESET_ALL)
        if d5 == 'Y':
            print(Fore.LIGHTYELLOW_EX+"->[X] ENUM4LINUX enable"+Style.RESET_ALL)
            if d51 == 'Y':
                print(Fore.LIGHTYELLOW_EX + "-->[X] Bruteforce SMB Service mode" + Style.RESET_ALL)
            else:
                print(Fore.LIGHTYELLOW_EX + "-->[ ] Bruteforce SMB Service mode" + Style.BRIGHT)
        else:
            print(Fore.LIGHTYELLOW_EX+"->[ ] ENUM4LINUX enable"+Style.BRIGHT)
        if d6 == 'Y':
            print(Fore.LIGHTYELLOW_EX+"->[X] NSE Nmap Script enable"+Style.RESET_ALL)
        else:
            print(Fore.LIGHTYELLOW_EX+"->[ ] NSE Nmap Script enable"+Style.RESET_ALL)
    else:
        print(Fore.YELLOW+"[ ] Enumeration mode"+Style.RESET_ALL)
    if e=='Y':
        print(Fore.YELLOW+"[X] Scheduling Job enable"+Style.RESET_ALL)
        print(Fore.LIGHTYELLOW_EX+"->Next job scheduled on "+str(weekDay(e1))+" at "+e2+Style.RESET_ALL)
    else:
        print(Fore.YELLOW+"[ ] Scheduling Job enable"+Style.RESET_ALL)


def finalOutMessage():
    print(Fore.LIGHTGREEN_EX+'''
The network scan is finished! 
The reports are in the folder named with the network address and the scan start date and time.
'''+Style.RESET_ALL)


def listOfIp():
    ####### list of IP up from all scan session ###########
    x = open("Buffer" + repDir + ".txt")
    Parse = x.read()
    data = re.findall(r"\b(?:[1-2]?[0-9]{1,2}\.){3}[1-2]?[0-9]{1,2}\b", Parse)
    data = list(filter(lambda x: all([int(y) <= 255 for y in x.split('.')]), data))

    #### remove duplicate   #####

    res = []
    for i in data:
        if i not in res:
            res.append(i)
    IPlist = '\n'.join([str(elem) for elem in res])

    ####print IP list #####
    print(Fore.MAGENTA+"\n----------- Host UP------------"+Style.RESET_ALL)
    print(Fore.LIGHTRED_EX+IPlist+Style.RESET_ALL)
    print(Fore.MAGENTA+"-------------------------------\n"+Style.RESET_ALL)
    return res


def cleanBuffer():
    ##### close buffer file #####
    z.close()
    try:
        os.remove("Buffer" + repDir + ".txt")
    except:
        print("not remove Buffer")


######## main function ########


if Scheduling_enable == 'Y':
    while 1:
        ora = datetime.datetime.now()
        if Day_of_week == str(ora.weekday()):
            if ora.strftime("%H:%M") == Hour_of_day:
                print(Fore.RED + "\nStart schedulated " + job + " Job\n" + Style.RESET_ALL)
                repDir = setupVariableReportScan(var_1, var_2)
                z = open("Buffer" + repDir + ".txt", "a")
                job_work(job, var_1, var_2, fast, deep, pn, bruteforce, evasion, Frag, Badsum, Datalength, Decoy,
                         SourcePort, enum_mode, pn_enum, Nikto, Wapiti, arachni, Enum4linux, bruteforce_SMB,
                         script_Nmap, Scheduling_enable, Day_of_week, Hour_of_day)
                time.sleep(30)
                menu()
                fastScan()
                menu()
                deepScan()
                menu()
                evasionScan()
                ip_list_up = listOfIp()
                for elem in ip_list_up:
                    menu()
                    enumeration(elem)
                menu()
                finalOutMessage()
                cleanBuffer()
                time.sleep(61)
        if ora.strftime("%S") == "00":
            menu()
            print(Fore.LIGHTMAGENTA_EX + "Scheduling active: Next scan " + weekDay(
                Day_of_week) + " at " + Hour_of_day + Style.RESET_ALL)
            time.sleep(10)
else:
    print(Fore.RED+"\nStart "+job+ " Job\n"+Style.RESET_ALL)
    repDir = setupVariableReportScan(var_1, var_2)
    z = open("Buffer" + repDir + ".txt", "a")
    job_work(job,var_1,var_2,fast,deep,pn,bruteforce,evasion,Frag,Badsum,Datalength,Decoy,SourcePort,enum_mode,pn_enum,Nikto,Wapiti,arachni,Enum4linux,bruteforce_SMB,script_Nmap,Scheduling_enable,Day_of_week,Hour_of_day)
    print(Fore.LIGHTBLUE_EX+"Execute the Job? (Y/N)")
    execute_job=input()
    if execute_job=='Y':
        menu()
        fastScan()
        menu()
        deepScan()
        menu()
        evasionScan()
        ip_list_up = listOfIp()
        for elem in ip_list_up:
            menu()
            enumeration(elem)
        menu()
        finalOutMessage()
        cleanBuffer()
    else:
        print("Thank you! Goodbye!")
        sys.exit()

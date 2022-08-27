#!/bin/python3

# dependency check for the modules

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
    import pdfkit
    import http.server
    import socketserver
    from json2html import *
    import json
    import array

except ModuleNotFoundError:
    print('run the requirements.txt file to have all the requirements satisfied')


def menu():
    cmd = subprocess.run("clear")
    print(Fore.LIGHTBLUE_EX + '''
 __   _ _______ _______ _______ _     _ _______ ______  _______
 | \  | |______    |    |______ |_____| |_____| |     \ |______
 |  \_| |______    |    ______| |     | |     | |_____/ |______

  /\     _|_  _  ._ _   _. _|_ o  _   (_   _  _. ._  ._   _  ._ 
 /--\ |_| |_ (_) | | | (_|  |_ | (_   __) (_ (_| | | | | (/_ |    ONLY ENUM4LINUX
Autor: Adriano Condrò
    ''' + Style.RESET_ALL)


menu()

job = var_1 = var_2 = arp_scan = fast = deep = pn = bruteforce = evasion = Frag = Badsum = Datalength = Decoy = SourcePort = enum_mode = pn_enum = Nikto = Wapiti = arachni = Enum4linux = bruteforce_SMB = script_Nmap = Scheduling_enable = Day_of_week = Hour_of_day = 'n'
print(Fore.RED + "Setup job")

print(Fore.CYAN + "Enter name of job" + Style.RESET_ALL)
job = input()

menu()
print(Fore.RED + "Setup Target")

#inizializza array target

job_array = []
job_nomedir = []

while(True):
    #crea target da verificare
    print(Fore.BLUE+"\nList of Network Target :")
    print("************** end list *****************")
    for target in job_array:
        print(Fore.LIGHTYELLOW_EX+target+Style.RESET_ALL)
    print(Fore.BLUE+"************** end list *****************\n")
    print(Fore.GREEN + "Enter the target of the net scan: (es.192.168.1.0)" + Style.RESET_ALL)
    print(Fore.YELLOW + "NOTE:Alternatively, enter the single host to be analyzed (es.192.168.1.254)" + Style.RESET_ALL)
    var_1 = input()

    print(Fore.GREEN + "Enter the subnet of the net scan: (24)" + Style.RESET_ALL)
    print(Fore.YELLOW + 'NOTE: Enter "32" for a single host' + Style.RESET_ALL)
    var_2 = input()

    #crea variabile target ip + netmask
    var_nmap = var_1 + "/" + var_2
    dir_net = var_1 + "_" + var_2

    job_array.append(var_nmap)
    job_nomedir.append(dir_net)
    print(Fore.LIGHTRED_EX+"Do you want insert addictional net scan?(Y/N)"+Style.RESET_ALL)
    other_net=input()
    if other_net != 'Y':
        print(Fore.LIGHTGREEN_EX + "\nList of Network Target Active:")
        print("************** end list *****************")
        for target in job_array:
            print(Fore.LIGHTYELLOW_EX + target + Style.RESET_ALL)
        print(Fore.LIGHTGREEN_EX + "************** end list *****************\n")
        break



print(Fore.LIGHTBLUE_EX + ">> Do you want use -Pn option for port scanner? (Y/N)" + Style.RESET_ALL)
pn = input()

print(Fore.LIGHTBLUE_EX + "-->> Do you want to test common passwords on discovered SAMBA services? (Y/N)" + Style.RESET_ALL)
bruteforce_SMB = input()
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

repDir = ''
z = ''
arph = ''


########create variable and dir of report #########
def setupVariableReportScan(a):
    dir_n = a
    time_string = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    RepDir = "Job_" + job + "_" + dir_n + "_at_" + time_string
    cmd = subprocess.run(["mkdir", RepDir])
    return RepDir

def html2pdf_fctn(a,b):

    input = a
    output = b
    options = {
        'page-size': 'A4',
        'margin-top': '0.50in',
        'margin-right': '0.50in',
        'margin-bottom': '0.50in',
        'margin-left': '0.50in',
        'encoding': "UTF-8",
        'no-outline': None
    }

    pdfkit.from_file(input, output, options=options)


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



def deepScan(x,y):
    var_nmap = x
    dir_net = y
    if (True):
        print(Fore.RED + '''
---Start Deep Network Scan Mode---  Scan started, please wait!
	''' + Style.RESET_ALL)

        if pn == 'Y':
            try:
                # SCANNER NP mode NOT evasion mode
                cmd = subprocess.run(
                    ["nmap", "-Pn", "-p 139,445","--open", "-A", var_nmap, "-oA", repDir + "/Deep_Scan_Nmap_Pn_" + dir_net,
                     "--stylesheet", "nmap-bootstrap.xsl"], stdout=z)
                cmd = subprocess.run(["./nmap-converter.py", "-o", repDir + "/Deep_Scan_Nmap_Pn_XLS" + dir_net + ".xls",
                                      repDir + "/Deep_Scan_Nmap_Pn_" + dir_net + ".xml"])
                cmd = subprocess.run(
                    ["xsltproc", "-o", repDir + "/Deep_Scan_Nmap_Pn_" + dir_net + ".html", "nmap-bootstrap.xsl",
                     repDir + "/Deep_Scan_Nmap_Pn_" + dir_net + ".xml"])

                pdfkit.from_file(repDir + "/Deep_Scan_Nmap_Pn_" + dir_net + ".html",
                                 repDir + "/Deep_Scan_Nmap_Pn_" + dir_net + ".pdf")

            except KeyboardInterrupt:
                sys.exit()

        # else of the scanner if
        elif pn != 'Y':
            try:
                # SCANNER NP mode NOT evasion mode
                cmd = subprocess.run(
                    ["nmap", "-p 139,445","--open", "-A", var_nmap, "-oA", repDir + "/Deep_Scan_Nmap_" + dir_net,
                     "--stylesheet", "nmap-bootstrap.xsl"], stdout=z)
                cmd = subprocess.run(["./nmap-converter.py", "-o", repDir + "/Deep_Scan_Nmap_XLS" + dir_net + ".xls",
                                      repDir + "/Deep_Scan_Nmap_" + dir_net + ".xml"])
                cmd = subprocess.run(
                    ["xsltproc", "-o", repDir + "/Deep_Scan_Nmap_" + dir_net + ".html", "nmap-bootstrap.xsl",
                     repDir + "/Deep_Scan_Nmap_" + dir_net + ".xml"])

                pdfkit.from_file(repDir + "/Deep_Scan_Nmap_" + dir_net + ".html",
                                 repDir + "/Deep_Scan_Nmap_" + dir_net + ".pdf")




            except KeyboardInterrupt:
                sys.exit()



def enumeration(a):
    ipScan = a

    print(Fore.RED + '''
---Start Enumeration Job--- 
                ''' + Style.RESET_ALL)

    if (True):

        print(Fore.LIGHTRED_EX + "Scanning host : " + ipScan + Style.RESET_ALL)

        f = open("Buffer_port_" + ipScan + "_" + repDir + ".txt", "a")

        print(Fore.CYAN + '''
---Port Scanner--- Scan started, please wait!
                ''' + Style.RESET_ALL)

        if (pn == 'Y'):
            try:
                # SCANNER NP mode
                cmd = subprocess.run(["nmap", "-Pn", "-p 139,445","--open", ipScan], stdout=f)
            except KeyboardInterrupt:
                sys.exit()
        # else of the scanner if
        elif (pn != 'Y'):
            try:
                # SCANNER NP mode
                cmd = subprocess.run(["nmap", "-p 139,445","--open", ipScan], stdout=f)
            except KeyboardInterrupt:
                sys.exit()

        f.close()
        x = open("Buffer_port_" + ipScan + "_" + repDir + ".txt")
        Parse = x.read()
        data = ''
        data = (re.findall(r'[0-9]+/', Parse))
        data = [x[:-1] for x in data]
        listToStr = ','.join([str(elem) for elem in data])

        print(Fore.YELLOW + "\n----------------Open Port on " + ipScan + "------------------\n" + Style.RESET_ALL)
        for x in data:
            print(Fore.LIGHTGREEN_EX + x + Style.RESET_ALL)
        print(Fore.YELLOW + "\n----------------------------------------------------------\n" + Style.RESET_ALL)

        try:
            cmd = subprocess.run(
                ["nmap", "-p", listToStr, "-A", ipScan, "-oX",
                 repDir + "/Nmap_portscanner_" + ipScan + ".xml"])
            cmd = subprocess.run(["./nmap-converter.py", "-o", repDir + "/Nmap_portscanner_" + ipScan + ".xls",
                                  repDir + "/Nmap_portscanner_" + ipScan + ".xml"])
            cmd = subprocess.run(
                ["xsltproc", "-o", repDir + "/Nmap_portscanner_" + ipScan + ".html", "nmap-bootstrap.xsl",
                 repDir + "/Nmap_portscanner_" + ipScan + ".xml"])


        except KeyboardInterrupt:
            sys.exit()

        for port in data:

            #### emun4linux ###
            if (True) and (port == '139' or port == '445'):
                if (port == '139' or port == '445'):
                    try:
                        print(Fore.CYAN + '''
---"Start Emun4linux enumeration share service,  please wait!
                                         ''' + Style.RESET_ALL)

                        result_enum =open(repDir+"/enum4linux_"+ipScan+".txt", "a")
                        cmd = subprocess.run(
                            ["./enum4linux/enum4linux.py", "-A", ipScan, "-oA", repDir + "/enum4linux_" + ipScan],stdout=result_enum)
                        print("\n Report enum4linux saved!")
                        result_enum.close()
                    except KeyboardInterrupt:
                        sys.exit()
                    with open(repDir + "/enum4linux_" + ipScan+".json", "r") as f:
                        json_object = json.loads(f.read())

                    print(json_object)
                    # conversione JSON to HTML
                    html = json2html.convert(json=json_object)
                    fenum = open(repDir + "/enum4linux_" + ipScan + ".html", "w")
                    fenum.write(html)
                    fenum.close

                    #conversione HTML to PDF
                    #pdfkit.from_file(repDir + "/enum4linux_" + ipScan + ".html", repDir + "/enum4linux_" + ipScan + ".pdf")
                    html2pdf_fctn(repDir + "/enum4linux_" + ipScan + ".html", repDir + "/enum4linux_" + ipScan + ".pdf")

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
                                                  "-oA", repDir + "/Ncrack_SMB_pass_discovered_" + ipScan])

                            try:
                                os.remove("User" + repDir + "user_SMB.txt")
                            except:
                                print("not remove Buffer")

                        except KeyboardInterrupt:
                            sys.exit()
        try:
            os.remove("Buffer_port_" + ipScan + "_" + repDir + ".txt")
        except:
            print("not remove Buffer")




def finalOutMessage():
    print(Fore.LIGHTGREEN_EX + '''
The network scan is finished! 
The reports are in the folder named with the network address and the scan start date and time.
''' + Style.RESET_ALL)


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
    print(Fore.MAGENTA + "\n----------- Host UP------------" + Style.RESET_ALL)
    print(Fore.LIGHTRED_EX + IPlist + Style.RESET_ALL)
    print(Fore.MAGENTA + "-------------------------------\n" + Style.RESET_ALL)
    time.sleep(20)
    return res


def create_index_html():
    # write-html.py

    filehtml = []
    filepdf = []
    filexls = []

    for x in os.listdir(repDir):
        if x.endswith(".html"):
            filehtml.append(x)

    link_page = ''
    for y in filehtml:
        link_page += "<p><a href=" + y + ">" + y + "</a></p>"

    for x in os.listdir(repDir):
        if x.endswith(".pdf"):
            filepdf.append(x)

    link_pdf_page = ''
    for y in filepdf:
        link_pdf_page += "<p><a href=" + y + ">" + y + "</a></p>"

    for x in os.listdir(repDir):
        if x.endswith(".xls"):
            filexls.append(x)

    link_xls_page = ''
    for y in filexls:
        link_xls_page += "<p><a href=" + y + ">" + y + "</a></p>"

    f = open('./' + repDir + '/index.html', 'w')
    if var_2 == '32':
        title = "<h2>Single Host Scan</h2>"
    else:
        title = "<h2>Net Scan</h2>"

    message = "<html><head></head><body><h1>List Scan</h1>" + title + link_page + "<h2>Download PDF</h2>" + link_pdf_page + "<h2>Download Excel file</h2>" + link_xls_page + "</body></html>"

    f.write(message)
    f.close()


def cleanBuffer():
    ##### close buffer file #####
    z.close()
    try:
        os.remove("Buffer" + repDir + ".txt")

    except:
        print("not remove Buffer")



######## main function ########


if Scheduling_enable == 'Y':
    menu()
    print(Fore.MAGENTA + " Job schedulated, please wait..." + Style.RESET_ALL)
    while 1:
        try:
            ora = datetime.datetime.now()
            if Day_of_week == str(ora.weekday()):
                if ora.strftime("%H:%M") == Hour_of_day:
                    i = 0;
                    print(Fore.RED + "\nStart schedulated " + job + " Job\n" + Style.RESET_ALL)
                    for a in range(len(job_nomedir)):
                        repDir = setupVariableReportScan(job_nomedir[a])
                        z = open("Buffer" + repDir + ".txt", "a")
                        deepScan(job_array[i], job_nomedir[a])
                        ip_list_up = listOfIp()
                        for elem in ip_list_up:
                             enumeration(elem)
                        finalOutMessage()
                        cleanBuffer()
                    time.sleep(61)
            if ora.strftime("%S") == "00":
                menu()
                print(Fore.LIGHTMAGENTA_EX + "Scheduling active: Next scan " + weekDay(
                    Day_of_week) + " at " + Hour_of_day + Style.RESET_ALL)
                time.sleep(10)
        except KeyboardInterrupt:
            sys.exit()
else:
    print(Fore.RED + "\nStart " + job + " Job\n" + Style.RESET_ALL)
    i = 0;
    print(Fore.LIGHTBLUE_EX + "Execute the Job? (Y/N)")
    execute_job = input()
    for a in range(len(job_nomedir)):
        repDir = setupVariableReportScan(job_nomedir[a])
        z = open("Buffer" + repDir + ".txt", "a")
        if execute_job == 'Y':
            deepScan(job_array[i],job_nomedir[a])
            ip_list_up = listOfIp()
            for elem in ip_list_up:
                enumeration(elem)
            finalOutMessage()
            cleanBuffer()
            create_index_html()
        else:
            print("Thank you! Goodbye!")
            sys.exit()
        i+=1
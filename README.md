# Scanner

This is simple network scanner.

for setup execute FIRST:

```
sudo chmod 777 Root_Requirement.sh" and "sudo ./Root_Requirement.sh"
```
SECOND:

```
sudo chmod 777 Requirement.sh" and "sudo ./Requirement.sh"
```

for use the script:

```
chmod 777 NetS*
```
and 

```
./NetShade_Network_Scanner
```

USE ROOT (SUDO) ONLY TEST EVASION MODE 

e.g.    sudo ./NetShade_Network_Scanner  (NOT USE FOR NOT EVASION OPERATION) 

NOTE:USING ROOT CAUSES ARACHNI NOT WORKING!!!

IMPORTANT! for scheduling firewall / IDS evasion operations it is necessary to enable the user to be root without having to enter the administrator password.

Add you user in the "visudo" file linux of S.O. 

```
myuser@host: sudo visudo
```
add follow string

```
myuser ALL=(ALL) NOPASSWD: ALL

```


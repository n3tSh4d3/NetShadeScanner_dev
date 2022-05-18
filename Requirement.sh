#!/bin/sh

echo "Install Nmap, Nikto and SmbMap\n";
apt install -y pip git nmap nikto smbmap wapiti ldap-utils polenum smbclient wget ;
sudo pip install python-libnmap XlsxWriter impacket ldap3 PyYAML>=5.1;
sudo pip3 install schedule

#download arachni
echo "\nDownload Arachni \n";
wget https://github.com/Arachni/arachni/releases/download/v1.6.1.1/arachni-1.6.1.1-0.6.1.1-linux-x86_64.tar.gz;
gzip -d arachni-1.6.1.1-0.6.1.1-linux-x86_64.tar.gz;
tar -xf arachni-1.6.1.1-0.6.1.1-linux-x86_64.tar;
mv arachni-1.6.1.1-0.6.1.1 arachni;
rm arachni-1.6.1.1-0.6.1.1-linux-x86_64.tar;
#download script collection NSE Nmap
echo "\nDownload Script collelction for Nmap \n";
git clone https://github.com/n3tSh4d3/Nmap_Script_Collection.git;
echo "\n Remove old script on /usr/share/nmap/scripts\n";
rm -R /usr/share/nmap/scripts/*;
echo "\nCopy Script collection on /usr/share/nmap/script\n";
cd Nmap_Script_Collection;
cp -R * /usr/share/nmap/scripts/;
cd ..; rm -R Nmap_Script_Collection;
echo "\nUpdate nmap db (--updatedb)\n";
nmap --script-updatedb;
echo "\nUpdate vulnscan script";
cd /usr/share/nmap/scripts/vulscan/;
echo "\nRemove old csv list exploit for vulscan script\n";
rm *.csv*;
chmod +x update.sh;
echo "\nUpdate csv list for vulscan script\n";
./update.sh;
cd ;

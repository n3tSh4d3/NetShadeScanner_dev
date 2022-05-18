#!/bin/sh

#download arachni
echo "\nDownload Arachni \n";
wget https://github.com/Arachni/arachni/releases/download/v1.6.1.1/arachni-1.6.1.1-0.6.1.1-linux-x86_64.tar.gz;
gzip -d arachni-1.6.1.1-0.6.1.1-linux-x86_64.tar.gz;
tar -xf arachni-1.6.1.1-0.6.1.1-linux-x86_64.tar;
mv arachni-1.6.1.1-0.6.1.1 arachni;
rm arachni-1.6.1.1-0.6.1.1-linux-x86_64.tar;

cd ;

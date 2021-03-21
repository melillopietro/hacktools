#!/bin/bash

#Trova i MAC address e relativi IP nella tabella arp del router

clear
echo '+--------------------------------------------+'
echo '|                                            |'
echo '|                    ARP                     |'
echo '|                                            |'
echo '+--------------------------------------------+'

x=$(arp -a)
elementi=$(echo $x | wc -w)
elementi=$(($elementi/7))
echo
ciclo=0
date=`date +%Y%m%d-%H%M%S`
for ((i = 1 ; i <= $elementi ; i++)); do
	name=$(echo $x | awk -v var=$(($i + $ciclo)) '{print $var}')
	ip=$(echo $x | awk -v var=$(($i + 1 + $ciclo)) '{print $var}')
	ip=${ip#"("}
	ip=${ip%")"}
	mac=$(echo $x | awk -v var=$(($i + 3 +$ciclo)) '{print $var}')
	connType=$(echo $x | awk -v var=$(($i + 4 + $ciclo)) '{print $var}')
	ciclo=$(($ciclo+6))
	echo -e "Name: "$name"\nip: "$ip"\nMAC: "$mac"\nConnType: "$connType"\n"
	echo -e "Name: "$name"\nip: "$ip"\nMAC: "$mac"\nConnType: "$connType"\n" >> Scan/$date.txt
	echo 
done

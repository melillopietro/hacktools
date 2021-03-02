#!/bin/bash
echo -e "Menu:\n1) Search CVE\n2) Search\n3) Update\n"
read -p "Option number: " scelta
case $scelta in
	1)
		read -p "CVE code: " selezionato
		x=$(grep "Name: CVE-$selezionato" ./Cve/Cve.txt)
		if [ "$x" = "" ]; then
			echo -e "\n\nNo result for [$selezionato]\n"
			exit
		fi	
		echo -e "\n\n+-------------------------------------------------------------------------------------------+\n\n"
		sed -n -e '/Name: CVE-'$selezionato'/,/======================================================/ p' ./Cve/Cve.txt | sed -e '$d'
		echo -e "+-------------------------------------------------------------------------------------------+"
	;;
	
	2)
		read -p "Keyword: " selezionato
		echo -e "\n"
		x=$(grep "$selezionato" ./Cve/Cve.txt)
		if [ "$x" = "" ]; then
			echo -e "\n\nNo result for ["$selezionato"]\n"
			exit
		fi
		pezzo=""
		flag=0
		while read line; do
			if [ "$line" != "======================================================" ]; then
				pezzo+="$line"
				pezzo+="\n"
			else
				if [[ "$pezzo" == *"$selezionato"* ]]; then
					echo -e "+-------------------------------------------------------------------------------------------+\n\n"
					echo -e $pezzo
				fi	
				pezzo=""
			fi
		done < ./Cve/Cve.txt
		echo -e "\n\n+-------------------------------------------------------------------------------------------+\n\n"
	;;
	
	3)
		echo -e "\nUpdating..."
		rm -f ./Cve/Cve.txt
		rm -f ./Cve/tmp.txt
		wget -nc -O ./Cve/tmp.txt https://cve.mitre.org/data/downloads/allitems.txt -q --show-progress
		sed -e '1,11d' ./Cve/tmp.txt > ./Cve/Cve.txt
		rm -f ./Cve/tmp.txt
		echo
	;;
esac



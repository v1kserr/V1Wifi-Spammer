# можно изменить 

1. bssid
2. essid
3. CH
4. ENC

***

sudo iw dev wlan1 interface add mon1 type monitor
sudo iw dev wlan1 interface add mon2 type monitor
sudo iw dev wlan1 interface add mon3 type monitor
sudo ip link set mon1 up
sudo ip link set mon2 up
sudo ip link set mon3 up


sudo airbase-ng -e "FreeWiFi_1" -c 1 -a 00:11:22:33:44:01 mon1

sudo airbase-ng -e "FreeWiFi_2" -c 6 -a 00:11:22:33:44:02 mon2

sudo airbase-ng -e "FreeWiFi_3" -c 11 -a 00:11:22:33:44:03 mon3


# Что обозначаеть каждый флаг

1. -e "name" - essid;

2. -c <> - CH;

3. -a <> - bssid;

4. -Z 4 - WPA2 | z 2 - WPA | -w <> - WEP | Без флага - открытая сеть;

***
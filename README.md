# Auto_Tor_IP_changer V 2.1.1
change your Ip Address automatically This tool based on tor project

how to install this tools :

requirements:

* sudo apt-get install tor
* sudo pip3 install requests
* sudo pip3 install stem

1: git clone https://github.com/jamalbalya/TOR_Auto_Changer_IP.git

2 : cd Auto_Tor_IP_changer

3 : chmod +x install.py

3 : python3 install.py

4 : sudo nano /etc/tor/torrc
    * unremark for: ControlPort and CookieAuthentication
    * and then save after doing unremark

4 : interminal type ( aut ) any where you want
  
5 : type time (on second) to change IP

6 : type how many time to change your ip 

    *[0 to infinte IP change]

6 : go to your browser / pc (sample: firefox) go to settings and scroll down you will see network setting and click settings  

7 : change configuration proxy into manual. on SOCKS Host write 127.0.0.1 for port 9050

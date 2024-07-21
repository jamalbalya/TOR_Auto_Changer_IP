import time
import os
import requests
import subprocess
from stem import Signal
from stem.control import Controller

# Check and install dependencies
try:
    subprocess.check_output('dpkg -s python3-pip', shell=True)
except subprocess.CalledProcessError:
    print('[+] pip3 not installed')
    subprocess.check_output('sudo apt update', shell=True)
    subprocess.check_output('sudo apt install python3-pip -y', shell=True)
    print('[!] pip3 installed successfully')

try:
    import requests
except ImportError:
    print('[+] python3 requests is not installed')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('[!] python3 requests is installed')

# Check for Tor installation
try:
    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:
    print('[+] tor is not installed !')
    subprocess.check_output('sudo apt update', shell=True)
    subprocess.check_output('sudo apt install tor -y', shell=True)
    print('[!] tor is installed successfully')


# Function to change Tor IP
def change_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)


# Function to fetch external IP
def get_external_ip():
    url = 'https://api.ipify.org/?format=text'
    try:
        response = requests.get(url, proxies={'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'})
        if response.status_code == 200:
            return response.text.strip()
        else:
            print(f"Error fetching IP: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error fetching IP: {e}")
        return None


# Main execution
if __name__ == "__main__":
    os.system("clear")
    print('''\033[1;32;40m \n
                    _          _______
         /\        | |        |__   __|
        /  \  _   _| |_ ___      | | ___  _ __
       / /\ \| | | | __/ _ \     | |/ _ \| '__|
      / ____ \ |_| | || (_) |    | | (_) | |
     /_/    \_\__,_|\__\___/     |_|\___/|_|
                    V 2.1.1
    from mrFD modify by nobody
    ''')
    print("\033[1;40;31m HACK THE WORLD\n")

    os.system("service tor start")
    time.sleep(3)
    print("\033[1;32;40m change your SOCKS to 127.0.0.1:9050 \n")

    os.system("service tor start")

    x = input("[+] time to change IP in seconds [type=60] >> ")
    lin = input("[+] how many times do you want to change your IP [type=1000]. For infinite IP change type [0] >> ")

    try:
        if int(lin) == 0:
            while True:
                try:
                    time.sleep(int(x))
                    change_ip()
                    print(f'[+] Your IP has been Changed to : {get_external_ip()}')
                except KeyboardInterrupt:
                    print('\nauto tor is closed ')
                    quit()
        else:
            for i in range(int(lin)):
                time.sleep(int(x))
                change_ip()
                print(f'[+] Your IP has been Changed to : {get_external_ip()}')
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

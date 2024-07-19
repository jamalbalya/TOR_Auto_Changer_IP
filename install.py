import os
import subprocess

def install_package(package_name):
    try:
        subprocess.check_output(f'dpkg -s {package_name}', shell=True)
    except subprocess.CalledProcessError:
        print(f'[+] {package_name} not installed')
        subprocess.check_output('sudo apt-get update', shell=True)
        subprocess.check_output(f'sudo apt-get install {package_name} -y', shell=True)
        print(f'[!] {package_name} installed successfully')

def install_pip_package(package_name):
    try:
        __import__(package_name)
    except ImportError:
        print(f'[+] python3 {package_name} is not installed')
        os.system(f'pip3 install {package_name}')
        os.system(f'pip3 install {package_name}[socks]')
        print(f'[!] python3 {package_name} is installed')

choice = input('[+] To install, press (Y); to uninstall, press (N) >> ').strip().lower()
run = os.system

if choice == 'y':
    # Installation process
    run('chmod 777 autoTOR.py')
    if not os.path.exists('/usr/share/aut'):
        run('mkdir /usr/share/aut')
    run('cp autoTOR.py /usr/share/aut/autoTOR.py')

    cmnd = '#! /bin/sh \n exec python3 /usr/share/aut/autoTOR.py "$@"'
    with open('/usr/bin/aut', 'w') as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/aut')
    run('chmod +x /usr/share/aut/autoTOR.py')

    # Install necessary packages
    install_package('python3-pip')
    install_pip_package('requests')
    install_pip_package('stem')
    install_package('tor')

    print('\n\nCongratulations! Auto Tor IP Changer is installed successfully.')
    print('From now on, just type \x1b[6;30;42maut\x1b[0m in the terminal.')

elif choice == 'n':
    # Uninstallation process
    run('rm -r /usr/share/aut ')
    run('rm /usr/bin/aut ')
    print('[!] Auto Tor IP Changer has been removed successfully.')

else:
    print('Invalid choice. Please enter Y or N.')

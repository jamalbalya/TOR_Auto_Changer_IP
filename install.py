import os

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
    print('\n\nCongratulations! Auto Tor IP Changer is installed successfully.')
    print('From now on, just type \x1b[6;30;42maut\x1b[0m in the terminal.')

elif choice == 'n':
    # Uninstallation process
    run('rm -r /usr/share/aut ')
    run('rm /usr/bin/aut ')
    print('[!] Auto Tor IP Changer has been removed successfully.')

else:
    print('Invalid choice. Please enter Y or N.')
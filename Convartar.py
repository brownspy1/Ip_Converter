import socket
import pyfiglet

def main():
    while True:
        banar = pyfiglet.figlet_format("\tIp Convart")
        print(banar)
        number = int(input('1.Domain to Ip\n'
                           '2.Ip to Domain\n'
                           '3.exit\n'
                           'Input A number in reng(1-3):'))
        if number == 1:
            domain = input('Enter Domain name: ')
            ip = socket.gethostbyname(domain)
            print('Ip For {} : {}'.format(domain,ip))
        elif number == 2:
            try:
                ip = input('Enter Ip Addres: ')
                domain = socket.gethostbyaddr(ip)
                print('Domain For {} : {}'.format(ip, domain))
            except:
                print(f'Wrong ip {ip} or this ip are not online!')
                return main()
        elif number == 3:
            ask = input('Do you want to really exit from this program Y/N')
            if ask == 'Y' or ask == 'y':
                break
            else:
                main()
        else:
            print('Wrong input!')



if __name__ == '__main__':
    main()
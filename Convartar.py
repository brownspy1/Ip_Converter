import socket
import pyfiglet


def main():
    while True:
        banner = pyfiglet.figlet_format("\tIP Converter")
        print(banner)

        print('1. Domain to IP')
        print('2. IP to Domain')
        print('3. Exit')

        choice = input('Enter a number (1-3): ')

        if choice == '1':
            domain_to_ip()
        elif choice == '2':
            ip_to_domain()
        elif choice == '3':
            ask_exit = input('Do you really want to exit the program? (Y/N): ')
            if ask_exit.lower() == 'y':
                break
        else:
            print('Invalid input! Please choose a valid option.')


def domain_to_ip():
    domain = input('Enter Domain name: ')
    try:
        ip = socket.gethostbyname(domain)
        print('IP Address for {}: {}'.format(domain, ip))
    except socket.gaierror:
        print('Unable to resolve domain:', domain)


def ip_to_domain():
    ip = input('Enter IP Address: ')
    try:
        domain = socket.gethostbyaddr(ip)
        print('Domain for {}: {}'.format(ip, domain[0]))
    except socket.herror:
        print('Unable to resolve IP:', ip)


if __name__ == '__main__':
    main()
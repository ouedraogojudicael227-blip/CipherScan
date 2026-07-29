import socket


def get_host():
    while True:

        host = input("Enter the host (IP address or domain name): ").strip()

        try:
            ip = socket.gethostbyname(host)

            print(f"IP found : {ip}")

            return ip

        except socket.gaierror:
            print("Invalid host. Please enter a valid IP address or domain name.")
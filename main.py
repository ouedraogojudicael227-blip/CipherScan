import argparse
import socket

from config import APP_NAME, VERSION
from network import get_host
from ports import get_port_range
from scanner import scan_ports


def get_arguments():

    parser = argparse.ArgumentParser(
        description="CipherScan - TCP Port Scanner"
    )

    parser.add_argument(
        "-t",
        "--target",
        help="Target IP or hostname"
    )

    parser.add_argument(
        "-p",
        "--ports",
        help="Port range (example: 1-1000)"
    )

    return parser.parse_args()



def main():

    print("=" * 40)
    print(f"{APP_NAME} - Version {VERSION}")
    print("=" * 40)


    args = get_arguments()


    # Gestion de la cible

    if args.target:

        try:
            ip = socket.gethostbyname(args.target)

            print(f"IP found : {ip}")

        except socket.gaierror:

            print("Invalid target.")
            return

    else:

        ip = get_host()



    # Gestion des ports

    if args.ports:

        try:

            start_port, end_port = map(
                int,
                args.ports.split("-")
            )

        except ValueError:

            print("Invalid port range format.")
            return

    else:

        start_port, end_port = get_port_range()



    print("\nSummary")

    print(f"Target host : {ip}")
    print(f"Ports       : {start_port} - {end_port}")


    scan_ports(
        ip,
        start_port,
        end_port
    )



if __name__ == "__main__":
    main()
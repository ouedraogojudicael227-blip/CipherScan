import socket


def get_banner(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            s.settimeout(2)

            s.connect((ip, port))

            banner = s.recv(1024).decode(
                "utf-8",
                errors="ignore"
            ).strip()

            return banner if banner else None

    except (socket.timeout, ConnectionRefusedError, OSError):
        return None
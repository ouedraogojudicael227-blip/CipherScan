import socket
import concurrent.futures
import time

from tqdm import tqdm
from colorama import Fore, Style, init

from config import TIMEOUT, MAX_WORKERS
from services import get_service
from report import save_report, save_report_json
from banner import get_banner


init(autoreset=True)


def scan_port(ip, port):

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(TIMEOUT)

        result = s.connect_ex((ip, port))

        s.close()

        if result == 0:
            service = get_service(port)
            banner = get_banner(ip, port)

            return (port, service, banner)

    except socket.error:
        pass

    return None



def scan_ports(ip, start_port, end_port):

    start_time = time.time()

    print("\nScan in progress...\n")

    results = []

    with concurrent.futures.ThreadPoolExecutor(
        max_workers=MAX_WORKERS
    ) as executor:

        futures = []

        for port in range(start_port, end_port + 1):

            future = executor.submit(scan_port, ip, port)
            futures.append(future)


        for future in tqdm(
            concurrent.futures.as_completed(futures),
            total=len(futures),
            desc="Scanning"
        ):

            result = future.result()

            if result is not None:
                results.append(result)


    duration = time.time() - start_time

    total_ports = end_port - start_port + 1
    open_ports = len(results)


    print("\n" + "=" * 40)

    for port, service, banner in sorted(results):

        status_color = Fore.GREEN

        print(
            f"{status_color}[+] Port {port:<5} OPEN"
            f"{Style.RESET_ALL}   "
            f"{Fore.CYAN}{service}"
        )   

        if banner:
            print(
                f"    {Fore.YELLOW}Banner: {banner}"
            )


    print("=" * 40)

    print(Fore.GREEN + "Scan finished.")

    print(f"Target         : {ip}")
    print(f"Ports scanned  : {total_ports}")
    print(f"Open ports     : {open_ports}")
    print(f"Duration       : {duration:.2f} seconds")

    print("=" * 40)


    save_report(ip, results, duration)
    save_report_json(ip, results, duration)
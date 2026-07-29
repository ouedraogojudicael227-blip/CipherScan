import json
from datetime import datetime

from config import REPORTS_FOLDER


def save_report(ip, results, duration):

    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    filename = f"{REPORTS_FOLDER}/report_{date}.txt"

    with open(filename, "w", encoding="utf-8") as file:

        file.write("=" * 40 + "\n")
        file.write("CipherScan Report\n")
        file.write("=" * 40 + "\n\n")

        file.write(f"Target : {ip}\n")
        file.write(f"Duration : {duration:.2f} seconds\n")
        file.write(f"Open ports : {len(results)}\n\n")

        for port, service, banner in sorted(results):

            file.write(f"Port : {port}\n")
            file.write(f"Service : {service}\n")

            if banner:
                file.write(f"Banner : {banner}\n")

            file.write("-" * 30 + "\n")

    print(f"\nTXT Report saved : {filename}")


def save_report_json(ip, results, duration):

    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    filename = f"{REPORTS_FOLDER}/report_{date}.json"

    data = {
        "target": ip,
        "duration": round(duration, 2),
        "open_ports": len(results),
        "ports": []
    }

    for port, service, banner in sorted(results):

        data["ports"].append({
            "port": port,
            "service": service,
            "banner": banner
        })

    with open(filename, "w", encoding="utf-8") as file:

        json.dump(data, file, indent=4)

    print(f"JSON Report saved : {filename}")
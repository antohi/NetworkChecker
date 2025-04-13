import re
import subprocess
import logging

class PortScanner:
    # Scan a single port based on an IP address
    def scan_single_port(self, port, host):
        scan_cmd = ["nmap", "-p", port, host]
        s = subprocess.run(scan_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        logging.info(s.stdout)
        return s.stdout
"""
    def get_port_info(self, p):
        re.search("")

"""
import re
import subprocess
import logging

class PortScanner:
    # Scan a single port based on an IP address
    def scan_single_port(self, port, host):
        scan_cmd = ["nmap", "-p", port, host]
        s = subprocess.run(scan_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        logging.info("\n\n===SINGLE SCAN RESULTS===")
        print("\n\n===SINGLE SCAN RESULTS===")
        return self.format_scan(s.stdout)

    # Formats output of scan to make more readable when printing/logging
    def format_scan(self, s):
        ports = re.findall(r"(\d+)/(tcp|udp)\s+(open|closed|filtered)\s+(\S+)", s)
        formatted = []
        for port, protocol, state, service in ports:
            formatted.append(f"{port}/{protocol} - {state.upper()} ({service})")
        for port in formatted:
            logging.info(port)
            print(port)

    # Scans top 10 ports using nmap's --top-ports functionality
    def quick_scan(self, host):
        scan_cmd = ["nmap", "--top-ports", "10", host]
        s = subprocess.run(scan_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        logging.info("\n\n===QUICK SCAN RESULTS===")
        print("\n\n===QUICK SCAN RESULTS===")
        return self.format_scan(s.stdout)

    # Scans top 25 ports using nmap's --top-ports functionality
    def deep_scan(self, host):
        scan_cmod = ["nmap", "--top-ports", "25", host]
        s = subprocess.run(scan_cmod, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        logging.info("\n\n===DEEP SCAN RESULTS===")
        print("\n\n===DEEP SCAN RESULTS===")
        return self.format_scan(s.stdout)

    #Work in progress, functionality for locating opened ones.
    """
    def find_open_ports(self, s):
        format = re.findall("(\d+)/(tcp|udp)\s+open", s)
        return format
    """

# command_execution(vuln).py

import os

def ping_host(host):
    os.system(f"ping -n 1 {host}")

ping_host("127.0.0.1 & echo hacked")

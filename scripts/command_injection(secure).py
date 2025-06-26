# command_execution(secure).py

import subprocess

def ping_host(host):
    allowed_hosts = ["127.0.0.1", "8.8.8.8"]
    if host in allowed_hosts:
        subprocess.run(["ping", "-n", "1", host])
    else:
        print("❌ Host not allowed.")

ping_host("127.0.0.1 & echo hacked")

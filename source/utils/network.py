from multiprocessing import Pool
from multiprocessing import cpu_count
import platform    # For getting the operating system name
import subprocess  # For executing a shell command


def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', host]
    res = subprocess.call(command, stdout=subprocess.DEVNULL) == 0
    return host, res


def available_hosts():
    dest_ips = [f"192.168.1.{idx}" for idx in range(2,255)]
    with Pool(254) as p:
        result = p.map(ping, dest_ips)
    available_hosts = [ host for host, status in result if status]
    return available_hosts
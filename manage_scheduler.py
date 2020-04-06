"""
This script periodically checks whether scheduler is up
and if not, it will fire up a new vm with a scheduler process
"""
import os
from time import sleep

import vagrant
import socket


def ping_success(host):
    import platform  # For getting the operating system name
    import subprocess  # For executing a shell command
    """
       Returns True if host (str) responds to a ping request.
       Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
       """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0


def isOpen(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        return True
    except:
        return False


def update_scheduler_config(new_host, new_port):
    fp = open('scheduler_conf.txt', 'w')
    fp.writelines(["host=" + str(new_host),
                   "port=" + str(new_port)])
    fp.close()


if __name__ == "__main__":
    host = ""
    port = 0
    with open("scheduler_conf.txt") as fp:
        for line in fp:
            k, v = line.split("=")
            if k == "host":
                host = v.strip()
            elif k == "port":
                port = v.strip()

    dir_name = "/home/abhinav/PycharmProjects/InstanceManager/scheduler"
    while True:
        # TODO Check status of scheduler every 10 sec
        print(host, ":", port)
        alive = isOpen(host, port)
        print(alive)
        # alive = ping_success(host)
        sleep(10)

        if not alive:
            os.chdir(dir_name)

            v = vagrant.Vagrant()
            v.up()

            new_host = v.hostname()
            new_port = v.port()

            # TODO: Update config file
            update_scheduler_config(new_host, new_port)

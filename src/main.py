# Autor: Vilma Tomanová
# Datum: 2025-25-11
# Popis: Script pro posílání příkazů na routery pomocí vláken.

import threading
import paramiko
import json
import time


class Router:
    def __init__(self, ip, username, password, status):
        self.ip = ip
        self.username = username
        self.password = password
        self.status = status


def main_loop(routers):
    threads = []

    for router in routers:
        t = threading.Thread(target=configure_router, args=(router,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


def configure_router(routers):
    for router in routers:
        print(f"Connecting to {router.ip}...")
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(router.ip, username=router.username, password=router.password, look_for_keys=False)

            remote = ssh.invoke_shell()
            time.sleep(1)

            commands = [
                "conf t",
                "service timestamps debug datetime local",
                "service timestamps log datetime local",
                "service password-encryption",
                "no ip http server",
                "no ip http secure-server",
                "clock timezone CET 1 0",
                "clock summer-time CEST recurring last Sun Mar 2:00 last Sun Oct 3:00",
                "end",
                "wr"
            ]

            for cmd in commands:
                remote.send(cmd + "\n")
                time.sleep(0.5)

            print(f"Finished configuring {router.ip}")

            remote.close()
            ssh.close()
        except Exception as e:
            print(f"Failed to connect to {router.ip}: {e}")


if __name__ == "__main__":
    with open("../res/routers.json") as f:
        jsondata = json.load(f)
        routers = [Router(router["ip"], router["username"], router["password"]) for router in jsondata]
    main_loop(routers)
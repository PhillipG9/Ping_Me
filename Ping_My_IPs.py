from multiprocessing import Process, Lock
from threading import Thread, Lock
import time
import mysql.connector
from datetime import datetime
import subprocess
import smtplib
import ssl


class Ping:
    def __init__(self, ip):
        self.ip = ip
        self.ping_ip()

    def ping_ip(self):
        ip_ping = subprocess.run([f'ping', '-n', '1', self.ip], stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                                 stderr=subprocess.DEVNULL)


class App:
    @staticmethod
    def run():
        """This method is used to create the processes used to ping all the ips."""
        list_of_ips = []  # ############################
        get_ips = open("storedIPs", "r")               #
        ips_gotten = get_ips.readlines()               #
        for ip in ips_gotten:                          # ####-> Collect the ips to be pinged.
            list_of_ips.append(ip.strip("\n"))         #
        get_ips.close()  # #############################

        i = 0
        while i < 1:
            list_of_processes = []
            start = time.time()

            for ips in list_of_ips:
                try:
                    processes = Process(target=Ping, args=(ips,))
                    list_of_processes.append(processes)
                    processes.start()
                except Exception as e:
                    print(e)

            # for ips in list_of_ips:
            #     try:
            #         thread = Thread(target=Ping, args=(ips,))
            #         list_of_processes.append(thread)
            #         thread.start()
            #     except Exception as e:
            #         print(e)

            for item in list_of_processes:
                item.join()

            end = time.time()
            time_taken = end - start
            print("It took the program", time_taken, "seconds to ping all ips.")
            i += 1


if __name__ == "__main__":
    app = App()
    app.run()



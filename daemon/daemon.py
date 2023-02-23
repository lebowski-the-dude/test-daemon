import os
import argparse
import syslog
import time
from daemonize import Daemonize

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--pid-file", help="where store the pid file")
args = parser.parse_args()


def daemon() -> None:
    # if args.pid_file is None:
    #     syslog.syslog("provide a pid file")
    #     return

    while True:
        syslog.syslog("---------------------------------")
        check = os.system("MonitorChecker.sh")
        syslog.syslog(f"{check}")

        time.sleep(10)


def main():
    daemonize = Daemonize(app="test_daemon",
                          # pid=args.pid_file,
                          pid="/var/run/daemon.pid",
                          action=daemon)
    daemonize.start()

import os
import argparse
import syslog
import time
from daemonize import Daemonize

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--pid-file", help="where store the pid file")
args = parser.parse_args()
syslog.syslog(f"this is test message, pid file is {args.pid_file}")

def checkDisplayConnection() -> bool:
    check = os.system("[[ $(xrandr | grep \"HDMI-A-0\" | awk '{print $2}') == connected ]]")
    return True if check == 0 else False


def setMonitorScreen() -> None:
    os.system("xrandr --output eDP --off --output HDMI-A-0 --primary --mode 1920x1080 --pos 0x0 --rotate normal")


def setLaptopScreen() -> None:
    os.system("xrandr --output eDP --mode 1920x1080 --pos 0x0 --rotate normal --output HDMI-A-0 --off")


def checkCommands() -> bool:
    if os.system("xrandr &>/dev/null") != 0:
        syslog.syslog("xrandr is not installed")
        return False
    if os.system("awk &>/dev/null") != 0:
        syslog.syslog("awk is not installed")
        return False
    if os.system("grep &>/dev/null") != 0:
        syslog.syslog("grep is not installed")
        return False

    return True


def daemon() -> None:
    while True:
        if checkDisplayConnection() is True:
            syslog.syslog("display connected")
            setMonitorScreen()
        else:
            syslog.syslog("display is not connected")
            setLaptopScreen()

        time.sleep(10)


def main():
    if checkCommands() is not True:
        return

    daemonize = Daemonize(app="test_daemon", pid=args.pid_file, action=daemon)
    daemonize.start()


if __name__ == "main":
    main()

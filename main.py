#Project: pretzelBot
#Abstract: Tank tread chassis that later will aquire pretzels from liberal arts majors.
#Principal Author: Michael Aldridge

import logging
import motor_control
import time
import sys
import termios


TERMIOS = termios
    def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c

def init():
    logging.baseConfig(level=logging.DEBUG)
    logging.info("Program start")
    chassis = motor_control.Drive('/dev/ttyAMA0', '115200')   

def main():
    while True:
        chassis.tankDrive(0,0)
        time.sleep(0.05)

#Project: pretzelBot
#Abstract: Tank tread chassis that later will aquire pretzels from liberal arts majors.
#Principal Author: Michael Aldridge

import logging
import motor_control
import time
import sys
import termios
import curses


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
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Program start")
    chassis = motor_control.Drive('/dev/ttyAMA0', '115200')   

def main():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    while True:
        key = stdscr.getch()
        if key=='w':
            lspeed = 1
            rspeed = 1
        elif key=='a':
            lspeed = -1
            rspeed =  1
        elif key=='d':
            lspeed =  1
            rspeed = -1
        elif key=='s':
            lspeed = -1
            rspeed = -1
        elif key=='\n':
            logging.info("Exiting...")
            curses.echo()
            curses.nocbreak()
            curses.endwin()
            sys.exit(0)
        chassis.tankDrive(lspeed,rspeed)
        time.sleep(0.05)

init()
main()

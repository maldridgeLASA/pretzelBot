#Project: pretzelBot
#Abstract: Tank tread chassis that later will aquire pretzels from liberal arts majors.
#Principal Author: Michael Aldridge

import logging
import motor_control
import time
import sys
import termios
import curses

def init():
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Program start")
    global chassis
    chassis = motor_control.Drive('/dev/ttyAMA0', '115200')   

def main():
    lspeed=0
    rspeed=0
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
        chassis.TankDrive(lspeed,rspeed)
        lspeed =0
        rspeed =0
        time.sleep(0.05)

init()
main()

#!/usr/bin/env python

import serial

LFWD = 194
RFWD = 202
LBAK = 193
RBAK = 201


class pretzelRobot:
  def setup_link(self, port):
    ser = serial.Serial(port, 115200)
    print "using port", ser.portstr

  def drive(self, lspeed, rspeed):
    if lspeed<0:
      ser.write(str(LBAK)+str(lspeed))
    else:
      ser.write(str(LFWD)+str(lspeed))
    if rspeed<0: 
      ser.write(str(RFWD)+str(rspeed))
    else:
      ser.write(str(202)+str(127))

  def main(self):
    #setup_link(raw_input("Port? "))
    self.setup_link('/dev/ttyUSB0')
    #left=int(raw_input("Left Speed? "))
    #right=int(raw_input("Right Speed? "))
    drive(127,127)
    raw_input("Press a key to stop")
    drive(0,0)
    exit()


r = pretzelRobot

r.main(self)


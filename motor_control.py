import serial
import logging
import sys

class Drive:
  def __init__(self, port, baud):
    self.LFWD = 194
    self.RFWD = 202
    self.LBAK = 193
    self.RBAK = 201
    try:
      self.ser = serial.Serial(port, baud)
      logging.info("Attempting to open port %s @ %s", port, baud)
    except:
      logging.error("Could not open port, aborting")
      sys.exit(1)

  def TankDrive(self, lspeed, rspeed):
    if lspeed<0:
      self.ser.write(chr(self.LBAK)+chr(lspeed))
    else:
      self.ser.write(chr(self.LFWD)+chr(lspeed))
    if rspeed<0: 
      self.ser.write(chr(self.RFWD)+chr(rspeed))
    else:
      self.ser.write(chr(self.RBAK)+chr(rspeed))

  def ArcadeDrive(self, x, y):
    lspeed=x+y
    rspeed=x-y
    if lspeed<0:
      self.ser.write(chr(self.LBAK)+chr(lspeed))
    else:
      self.ser.write(chr(self.LFWD)+chr(lspeed))
    if rspeed<0: 
      self.ser.write(chr(self.RFWD)+chr(rspeed))
    else:
      self.ser.write(chr(self.RBAK)+chr(rspeed))

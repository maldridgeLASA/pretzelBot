import serial

class Drive:
  self.LFWD = 194
  self.RFWD = 202
  self.LBAK = 193
  self.RBAK = 201
  def __init__(self, port):
    ser = serial.Serial(port, 115200)
    print "using port", ser.portstr

  def TankDrive(self, lspeed, rspeed):
    if lspeed<0:
      ser.write(chr(self.LBAK)+chr(lspeed))
    else:
      ser.write(chr(self.LFWD)+chr(lspeed))
    if rspeed<0: 
      ser.write(chr(self.RFWD)+chr(rspeed))
    else:
      ser.write(chr(self.RBAK)+chr(rspeed))

  def ArcadeDrive(self, x, y):
    lspeed=x+y
    rspeed=x-y
    if lspeed<0:
      ser.write(chr(self.LBAK)+chr(lspeed))
    else:
      ser.write(chr(self.LFWD)+chr(lspeed))
    if rspeed<0: 
      ser.write(chr(self.RFWD)+chr(rspeed))
    else:
      ser.write(chr(self.RBAK)+chr(rspeed))

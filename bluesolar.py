from pyb import UART
import ure

class mppt:
    def __init__(self, port, baud=19200):
	   self.port = UART(port, baud)
	   self.data = {"here":1}


    def getdata(self):
        while self.port.any() > 0:
            try:
                dataline = self.port.readline()
                out = dataline.decode('UTF8')
                split = ure.match("^(\w*)(\s*)(\w*)", out)
                #self.data[split.group(1)] = split.group(3)
            except Exception as e:
                pass
	    return self.data

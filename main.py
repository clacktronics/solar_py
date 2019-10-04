from bluesolar import mppt
from pyb import delay

solar = mppt(1)

R = 0
G = 0
B = 0

def getVal():
    

with open("sequence.txt") as fin:
    lines = fin.readlines()
for line in lines:
    try:
        R = int(line[0:3])
        G = int(line[3:7])
        B = int(line[7:16])

    except:
        print("pass")
    print(R)
    delay(100)

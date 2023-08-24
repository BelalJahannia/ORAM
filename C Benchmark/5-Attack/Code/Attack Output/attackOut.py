import sys
import math
import numpy as np
import random

myfile = open("outputTrace.txt", "r")
myfileO = open("attackOutput.txt", "w")

line = myfile.readline()
line_data = line.split()
addr = int(line_data[1])
while line != "":
    next_line = myfile.readline()
    next_line_data = next_line.split() if next_line else None
    next_addr = int(next_line_data[1]) if next_line_data else None
    counter = 1
    while next_line and addr == next_addr:
        #print("{} {} {}\n".format(addr, next_addr, next_line))
        next_line = myfile.readline()
        next_line_data = next_line.split() if next_line else None
        next_addr = int(next_line_data[1]) if next_line_data else None
        counter += 1


    if counter>1 :
    	myfileO.write("{} {}\n".format(addr, counter))


    line = next_line
    line_data = line.split() if line else None
    addr = int(line_data[1]) if line_data else None

myfile.close()
myfileO.close()


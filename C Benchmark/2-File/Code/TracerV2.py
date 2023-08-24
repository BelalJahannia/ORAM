import plotly.express as px
import plotly.graph_objects as go

import plotly
import plotly.offline as py

myfile = open("gem5Tracer.txt", "r")

Operation = []
Address = []
N=myfile.readline()

counter=0
for line in myfile:
    x=line.split()
    op =  x[5]
    add = float(x[6])
    Operation.append(op)
    Address.append(add)

file1 = open("in.txt","w")
for i in range(len(Operation)):
	file1.write("{} {}\n".format(int(Operation[i]), int(Address[i])))


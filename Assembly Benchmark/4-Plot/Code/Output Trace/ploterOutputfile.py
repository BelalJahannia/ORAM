import plotly.express as px
import plotly.graph_objects as go
import plotly
import plotly.offline as py

myfile = open("outputTrace.txt", "r")

counterR=[]
counterW=[]
addrR=[]
addrW=[]
counter=0
for line in myfile:
    x=line.split()
    op =  x[0]
    add = int(x[1])

    counter+=1

    if (op=="0"):
    	addrR.append(add)
    	counterR.append(counter)
    	#fig.add_trace(go.Scatter(x=[int(x[6])], y=[counter], mode='markers', marker_color='blue'))
    if (op=="1"):
    	addrW.append(add)
    	counterW.append(counter)
    	#fig.add_trace(go.Scatter(x=[int(x[6])], y=[counter], mode='markers', marker_color='red'))

fig = go.Figure()
fig.add_trace(go.Scatter(x=addrR, y=counterR, mode='markers', marker_color='blue', name="Read Accesses", marker_symbol="square"))
fig.add_trace(go.Scatter(x=addrW, y=counterW, mode='markers', marker_color='red',  name="Write Accesses", marker_symbol="triangle-down"))

fig.update_layout(title_text="Memory accesses after using ORAM",title_font_size=30)
fig.update_xaxes(title="Memory Addresses")
fig.update_yaxes(title="Accesses")
plotly.offline.plot(fig, filename='Memory Output'+'.html',auto_open=False)	  	
fig.show()

import pandas as pd
import plotly.express as px
import numpy as np 

df = pd.read_csv("data.csv")

GRE_Score = df["GRE Score"].tolist()
Chances_of_admit = df["Chance of Admit "].tolist()

fig = px.scatter(x=GRE_Score, y=Chances_of_admit)


m = 0.01 
c = -2.5
y =[]
for x in GRE_Score:
    y_value = m*x +c 
    y.append(y_value)
    

fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= min(y), y1= max(y),
      x0= min(GRE_Score), x1= max(GRE_Score)
    )
])  
fig.show()

x= 600
y = m *x +c
print(f"Chances of admit of someone based on their GRE Score {x} is {y}")


import numpy as np
greScore_array = np.array(GRE_Score)
Chance_array = np.array(Chances_of_admit)

#Slope and intercept using pre-built function of Numpy
m, c = np.polyfit(greScore_array,Chance_array, 1)

y =[]
for x in greScore_array:
    y_value = m*x +c 
    y.append(y_value)
    
    
fig1 = px.scatter(x=greScore_array, y=Chance_array)

fig1.update_layout(shapes=[
    dict(
      type= 'line',
      y0= min(y), y1= max(y),
      x0= min(greScore_array), x1= max(greScore_array)
    )
])  
fig1.show()

x= 600
y = m *x +c
print(f"Chances of admit of someone based on their GRE Score {x} is {y}")
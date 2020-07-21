import pandas as pd
import csv
import plotly.graph_objects as pg
 
df = pd.read_csv("data.csv")
fig = pg.Figure(pg.Bar(x = df.groupby("level")["attempt"].mean(),
y = ['Level 1','Level 2', 'Level 3','Level 4'],orientation = 'h'
))
fig.show()
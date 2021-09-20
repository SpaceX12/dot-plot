import pandas as ps
import plotly_express as pe

df = ps.read_csv('Copy+of+data+-+data.csv')
chart = pe.scatter(df,x='date', y='cases', color='country')
chart.show()
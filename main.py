import pandas as pd;
import plotly.express as px;

df = pd.read_csv("covidCases.csv");
chart = px.scatter(df, x = "date", y = "cases", color = "country");

chart.show();
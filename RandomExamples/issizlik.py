import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/unemployment.csv")

print(data.isnull().sum())
data.columns = ["States","Date","Frequency","Estimated Unemployement Rate","Estimated Employed",
"Estimated Labour Participation Rate", "Region","longtitude","latitude"]

plt.title("Indian Employment")
sns.histplot(x="Estimated Employement",hue="Region",data=data)
plt.show()

plt.figure(figsize=(12,10))
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Unemployement Rate",hue="Region",data=data)
plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("D:/BTK Akademi Eğitim/Veri Analizi/Gün 6/sukalite.csv")

data = data.dropna()
data.isnull().sum()

plt.figure(figsize=(15, 10))
sns.countplot(data.Potability)
plt.title("Distribution of Unsafe and Safe Water")
plt.show()

import plotly.express as px

data = data
figure = px.histogram(data, x="ph", color="Potability", title="Factors Affecting Water Quality: PH")
figure.show()

figure = px.scatter(data, x="ph", y="Hardness", color="Potability",
                    title="Factors Affecting Water Quality: ph-Hardness")
figure.show()


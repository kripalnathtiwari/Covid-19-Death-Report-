import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = "C:\\Users\ASUS\Desktop\PYTHON DATASET.csv"
df = pd.read_csv(file_path)
df.info()
df.describe()
#OBJECTIVE 1  [ Find the country with the maximum cumulative deaths]


max_death_country = df.groupby("Country")["Cumulative_deaths"].max().idxmax()
max_death_value = df.groupby("Country")["Cumulative_deaths"].max().max()


country_deaths = df.groupby("Country")["Cumulative_deaths"].max().sort_values(ascending=False).head(10)

#Plot the Graph of  top 10 countries with the highest cumulative deaths
plt.figure(figsize=(6, 6))
sns.barplot(x=country_deaths.values, y=country_deaths.index, palette="Reds_r")
plt.xlabel("Cumulative Deaths")
plt.ylabel("Country")
plt.title("Top 10 Countries with Highest Cumulative Deaths")
plt.show()
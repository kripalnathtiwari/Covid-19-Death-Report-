import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# Getting the global cumulative cases over time.
# Load the dataset
file_path = "C:\\Users\ASUS\Desktop\PYTHON DATASET.csv"
df = pd.read_csv(file_path)
df.info()
df.describe()
# Convert Date_reported to datetime format
df["Date_reported"] = pd.to_datetime(df["Date_reported"])

# Group by date to get global cumulative cases
global_cases = df.groupby("Date_reported")["Cumulative_cases"].sum().reset_index()

# Plot global cumulative cases over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=global_cases, x="Date_reported", y="Cumulative_cases", color="blue")
plt.title("Global Cumulative COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Cumulative Cases")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


#OBJECTIVE 4   [Global New Deaths Trend Over Time]

df["Date_reported"] = pd.to_datetime(df["Date_reported"])
# Group by date and sum new deaths to see global trends
daily_deaths = df.groupby("Date_reported")["New_deaths"].sum()
# Plot trends in new deaths
plt.figure(figsize=(12, 5))
sns.lineplot(x=daily_deaths.index, y=daily_deaths.values, color="red")
plt.title("Global New Deaths Trend Over Time")
plt.xlabel("Date")
plt.ylabel("New Deaths")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

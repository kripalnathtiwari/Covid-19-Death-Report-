import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#OBJECTIVE 5   [Compare cases and deaths across WHO regions]
file_path = "C:\\Users\ASUS\Desktop\PYTHON DATASET.csv"
df = pd.read_csv(file_path)

#Grouping data by WHO region for cumulative cases and deaths
region_summary = df.groupby("WHO_region")[["Cumulative_cases", "Cumulative_deaths"]].max().reset_index()

# Bar plot for cumulative cases and deaths across WHO regions
fig, axes = plt.subplots(1, 2)

# Plot for Cumulative Cases
sns.barplot(data=region_summary, x="WHO_region", y="Cumulative_cases", ax=axes[0], palette="Blues_r")
axes[0].set_title("Cumulative Cases by WHO Region")
axes[0].set_xlabel("WHO Region")
axes[0].set_ylabel("Total Cases")
axes[0].tick_params(axis='x', rotation=45)

# Plot for Cumulative Deaths
sns.barplot(data=region_summary, x="WHO_region", y="Cumulative_deaths", ax=axes[1], palette="Reds_r")
axes[1].set_title("Cumulative Deaths by WHO Region")
axes[1].set_xlabel("WHO Region")
axes[1].set_ylabel("Total Deaths")
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

##OBJECTIVE 5   [Compare cases and deaths across WHO regions]


#Grouping data by WHO region for cumulative cases and deaths
region_summary = df.groupby("WHO_region")[["Cumulative_cases", "Cumulative_deaths"]].max().reset_index()

# Bar plot for cumulative cases and deaths across WHO regions
fig, axes = plt.subplots(1, 2)

# Plot for Cumulative Cases
sns.barplot(data=region_summary, x="WHO_region", y="Cumulative_cases", ax=axes[0], palette="Blues_r")
axes[0].set_title("Cumulative Cases by WHO Region")
axes[0].set_xlabel("WHO Region")
axes[0].set_ylabel("Total Cases")
axes[0].tick_params(axis='x', rotation=45)

# Plot for Cumulative Deaths
sns.barplot(data=region_summary, x="WHO_region", y="Cumulative_deaths", ax=axes[1], palette="Reds_r")
axes[1].set_title("Cumulative Deaths by WHO Region")
axes[1].set_xlabel("WHO Region")
axes[1].set_ylabel("Total Deaths")
axes[1].tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.show()
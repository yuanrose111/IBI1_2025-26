# IBI1 Practical 10: Working with Global Health Data (DALYs)
# Facilitators: Ying CHI, Wang YONG

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ----------------------
# 1. Set your working directory (UPDATE THIS PATH TO YOUR OWN Practical10 folder)
# ----------------------
os.chdir("/Users/chenyuanrose/IBI/IBI1_2025-26/Practical10")

# Verify the current directory and files
print("Current working directory:", os.getcwd())
print("Files in directory:", os.listdir())

# ----------------------
# 2. Load and explore the dataset
# ----------------------
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

print("\n=== First 5 rows of the dataset ===")
print(dalys_data.head())

print("\n=== Dataset info ===")
dalys_data.info()

print("\n=== Descriptive statistics ===")
print(dalys_data.describe())

# ----------------------
# Task 1: Access data using iloc (first 10 rows, Year and DALYs columns)
# ----------------------
print("\n=== Task 1: First 10 rows - Year and DALYs ===")
first_10 = dalys_data.iloc[:10, [2, 3]]  # Column indices may vary; adjust if needed
print(first_10)

# Find the year with the highest DALYs in the first 10 rows
afghanistan_10 = dalys_data.iloc[:10]
max_year_afg = afghanistan_10.loc[afghanistan_10["DALYs"].idxmax(), "Year"]
print(f"The year with the highest DALYs in the first 10 rows is: {max_year_afg}")

# ----------------------
# Task 2: Filter data using Boolean indexing (e.g., Zimbabwe)
# ----------------------
print("\n=== Task 2: Data for Zimbabwe ===")
zimbabwe_data = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe"]
print(zimbabwe_data[["Year", "DALYs"]])

print(f"First recorded year for Zimbabwe: {zimbabwe_data['Year'].min()}")
print(f"Last recorded year for Zimbabwe: {zimbabwe_data['Year'].max()}")

# ----------------------
# Task 3: Analyze 2019 data
# ----------------------
print("\n=== Task 3: 2019 DALYs analysis ===")
data_2019 = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]

# Country with highest DALYs in 2019
max_country_2019 = data_2019.loc[data_2019["DALYs"].idxmax(), "Entity"]
max_daly_2019 = data_2019["DALYs"].max()

# Country with lowest DALYs in 2019
min_country_2019 = data_2019.loc[data_2019["DALYs"].idxmin(), "Entity"]
min_daly_2019 = data_2019["DALYs"].min()

print(f"Country with highest DALYs in 2019: {max_country_2019} ({max_daly_2019:.2f})")
print(f"Country with lowest DALYs in 2019: {min_country_2019} ({min_daly_2019:.2f})")

# ----------------------
# Task 4: Plot a time series (example: Zimbabwe)
# ----------------------
plt.figure(figsize=(10, 5))
plt.plot(zimbabwe_data["Year"], zimbabwe_data["DALYs"], marker='o', linestyle='-', color='blue')
plt.title("Trend of DALYs in Zimbabwe (1990-2019)")
plt.xlabel("Year")
plt.ylabel("DALYs (per 100,000 people)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ----------------------
# Optional Task 5: Additional analysis (2019 global distribution)
# ----------------------
plt.figure(figsize=(8, 5))
plt.boxplot(data_2019["DALYs"], vert=False)
plt.title("Global Distribution of DALYs in 2019")
plt.xlabel("DALYs (per 100,000 people)")
plt.tight_layout()
plt.show()
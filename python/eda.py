"""
Project: Blinkit Sales Analysis

Author: Aarush Chugh

Purpose:
This file performs Exploratory Data Analysis (EDA) on the cleaned
Blinkit sales dataset. It provides an overview of the data by
calculating summary statistics, grouping data, and analyzing
sales, ratings, and outlet performance to understand patterns
and trends in the dataset.
"""
import pandas as pd
df = pd.read_csv("data/Blinkit-Sales-Analysis-Cleaned.csv")

# Sales statistics
print(df["Sales"].mean())

# Item Type Sales
print(df.groupby("Item Type")["Sales"].sum())

# Outlet Size Sales
print(df.groupby("Outlet Size")["Sales"].sum())

# Average Rating
print(df.groupby("Item Type")["Rating"].mean())
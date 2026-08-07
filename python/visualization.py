"""
Project: Blinkit Sales Analysis

Author: Aarush Chugh
Purpose:
This file contains all the visualizations created using Matplotlib
to analyze the Blinkit sales dataset.
"""
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/Blinkit-Sales-Analysis-Cleaned.csv")

# #CHART-1 Total sales by item type
# item_sales = (
#     df.groupby("Item Type")["Sales"]
#       .sum()
#       .sort_values(ascending=False)
# )

# # Create figure
# plt.figure(figsize=(12,6))

# # Plot bar chart
# item_sales.plot(kind="barh")

# # Add title and labels
# plt.title("Total Sales by Item Type")
# plt.xlabel("Item Type")
# plt.ylabel("Total Sales")

# # Rotate x-axis labels
# plt.xticks(rotation=45)

# # Adjust layout
# plt.tight_layout()

# # Display chart
# plt.show()

# #CHART-2 Total sales by outlet size
# outlet_sale=(df.groupby("Outlet Size")["Sales"].sum().sort_index(ascending=False))
# # Create figure
# plt.figure(figsize=(12,6))

# # Plot bar chart
# outlet_sale.plot(kind="barh")

# # Add title and labels
# plt.title("Total Sales by Outlet Size")
# plt.xlabel("Outlet Size")
# plt.ylabel("Total Sales")

# # Rotate x-axis labels
# plt.xticks(rotation=45)

# # Adjust layout
# plt.tight_layout()

# # Display chart
# plt.show()

# #CHART-3 Sales by outlet location type
# outlet_location_sales = (
#     df.groupby("Outlet Location Type")["Sales"].sum().sort_values(ascending=False))

# # Create figure
# plt.figure(figsize=(12,6))

# # Plot bar chart
# outlet_location_sales.plot(kind="barh")

# # Add title and labels
# plt.title("Total Sales by Outlet Location Type")
# plt.xlabel("Outlet Location Type")
# plt.ylabel("Total Sales")

# # Rotate x-axis labels
# plt.xticks(rotation=45)

# # Adjust layout
# plt.tight_layout()

# # Display chart
# plt.show()

# #CHART-4 Average Rating by Item Type
# average_rating = (
#     df.groupby("Item Type")["Rating"].mean().sort_values(ascending=False))
# # Create figure
# plt.figure(figsize=(12,6))
# # Plot bar chart
# average_rating.plot(kind="barh")
# # Add title and labels
# plt.title("Average Rating by Item Type")
# plt.xlabel("Item Type")
# plt.ylabel("Average Rating")
# # Rotate x-axis labels
# plt.xticks(rotation=45)
# #Adjust Layout
# plt.tight_layout()

# # Display chart
# plt.show()

# #CHART-5 Item count by item type
# item_count = (
#     df.groupby("Item Type")["Item Identifier"].count().sort_values(ascending=False))
# # Create figure
# plt.figure(figsize=(12,6))
# # Plot bar chart
# item_count.plot(kind="bar")
# # Add title and labels
# plt.title("Item Count by Item Type")
# plt.xlabel("Item Type")
# plt.ylabel("Item Count")
# # Rotate x-axis labels
# plt.xticks(rotation=45)
# #Adjust Layout
# plt.tight_layout()
# #display chart
# plt.show()

# #CHART-6 Outlet Size Distribution
# outlet_size_distribution = (
#     df.groupby("Outlet Size")["Outlet Identifier"]
#       .count()
#       .sort_values(ascending=False)
# )

# # Create figure
# plt.figure(figsize=(8,8))

# # Plot pie chart
# outlet_size_distribution.plot(
#     kind="pie",
#     autopct="%1.1f%%",
#     startangle=90
# )

# # Add title
# plt.title("Outlet Size Distribution")

# # Remove unnecessary y-axis label
# plt.ylabel("")

# # Adjust layout
# plt.tight_layout()

# # Display chart
# plt.show()

# #CHART-7 histogram of sales
# plt.figure(figsize=(8,6))
# plt.hist(df["Sales"], bins=30, edgecolor="black")
# plt.title("Histogram of Sales")
# plt.xlabel("Sales")
# plt.ylabel("Frequency")
# plt.show()

# CHART-8 Scatter Plot of Item Weight vs Sales

df.plot.scatter(
    x="Item Weight",
    y="Sales",
    alpha=0.5,
    figsize=(8,6)
)

plt.title("Scatter Plot of Item Weight vs Sales")
plt.xlabel("Item Weight")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()
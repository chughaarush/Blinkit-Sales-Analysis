"""
Project: Blinkit Sales Analysis

File: 01_data_cleaning.py

Purpose:
This script loads the raw dataset, cleans missing values,
fixes inconsistent categories, removes duplicates,
and exports a cleaned dataset for analysis.
"""
import pandas as pd
df = pd.read_csv("data/Blinkit-Sales-Analysis.csv")
#to print first five rows of dataset
print(df.head())
#to print shape of the dataset
print(df.shape)
#it gives the information about dataset like column names, data types, non null vales and we dont write print because info itself prints the infoormation.
df.info()
#it gives the statistical summary of the dataset which is basically the mathematical calculations
print(df.describe())
#it gives count of missing values in each column of dataset
print(df.isnull().sum())
#it replaces the missing values in the column "Item Weight" with the mean of that column
df["Item Weight"] = df["Item Weight"].fillna(df["Item Weight"].mean())
#it gives the number of unique values in each column of dataset
print(df["Item Fat Content"].value_counts())
#it replaces wrong values in the column "Item Fat Content" with correct values
df["Item Fat Content"] = df["Item Fat Content"].replace({
    "LF":"Low Fat",
    "low fat":"Low Fat",
    "reg":"Regular"
})
print(df["Item Fat Content"].value_counts())
#it checks for duplicates in our dataset
print(df.duplicated().sum())
#it drops the duplicates in our dataset
df = df.drop_duplicates()
#saves the file to a new csv file after cleaning the data
df.to_csv("data/Blinkit-Sales-Analysis-Cleaned.csv",index=False)

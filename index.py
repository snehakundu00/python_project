import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_excel("pollution_data.xlsx")

# Removing whitespace from column names for ease
df.columns = df.columns.str.strip()  

#data summary
print(df.isnull().sum())

print("Top 5 rows of dataset\n")
print(df.head())

print("Last 5 rows of dataset\n")
print(df.tail())

print("Information about the dataset\n")
print(df.info())

print("Available columns\n")
print(df.columns.tolist(),"\n")

#checking for duplicates
duplicates=df.duplicated().sum()
print(duplicates)

print("Statistical summary\n")
print(df.describe())
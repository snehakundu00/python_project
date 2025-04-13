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


# Convert 'last_update' to datetime
df['last_update'] = pd.to_datetime(df['last_update'], errors='coerce')

# Drop rows with missing avg values
df = df.dropna(subset=['pollutant_avg'])

# Group by date and pollutant
trend_df = df.groupby([df['last_update'].dt.date, 'pollutant_id'])['pollutant_avg'].mean().unstack()

# Check if data exists
print("Grouped data preview:")
print(trend_df.head())

# Plot
heatmap_data = df.groupby([df['last_update'].dt.date, 'pollutant_id'])['pollutant_avg'].mean().unstack()

# Plot heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(heatmap_data.T, cmap="YlGnBu", linewidths=0.5, linecolor='gray')

plt.title("Pollutant Levels Over Time (Heatmap)")
plt.xlabel("Date")
plt.ylabel("Pollutant")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Group by city and pollutant, then find average values
hotspot_df = df.groupby(['city', 'pollutant_id'])['pollutant_avg'].mean().unstack()

# Find cities with highest average PM2.5
top_cities = hotspot_df.sort_values(by='PM2.5', ascending=False).head(10)

# Plot
top_cities.plot(kind='bar', figsize=(12,6), title="Top 10 Pollution Hotspots by PM2.5")
plt.ylabel("Average PM2.5 Level")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# Average pollutant levels per city
pollutant_comparison = df.groupby(['city', 'pollutant_id'])['pollutant_avg'].mean().unstack()

# Plot for selected cities
selected_cities = ['Delhi', 'Mumbai', 'Chennai', 'Kolkata']
pollutant_comparison.loc[selected_cities].plot(kind='bar', figsize=(10,6))
plt.title("Pollutant Comparison Across Major Cities")
plt.ylabel("Average Level")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

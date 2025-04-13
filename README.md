# Pollution Data Analysis and Visualization

This project provides a comprehensive exploratory data analysis (EDA) of pollution data using Python. The goal is to analyze pollutant levels across different cities and over time to identify trends, hotspots, and seasonal variations.

## 📁 Dataset

The dataset used in this analysis is `pollution_data.xlsx`, which includes information on:

- **City**
- **Pollutant ID**
- **Pollutant Average**
- **Last Update (Date & Time)**

## 🧪 Key Steps in Analysis

1. **Data Cleaning**
   - Removed leading/trailing whitespaces from column names.
   - Converted date fields to datetime format.
   - Removed rows with missing pollutant averages.

2. **Data Exploration**
   - Summary statistics
   - Missing values count
   - Duplicate detection
   - Top and bottom rows preview

3. **Trend Analysis**
   - Average pollutant levels over time using a heatmap.
   - Identification of top 10 cities with highest PM2.5 levels.
   - Pollutant comparison across major cities (Delhi, Mumbai, Chennai, Kolkata).
   - Seasonal variation of PM2.5 levels using boxplots.

4. **City-wise Heatmap**
   - Heatmap of average pollutant levels across all cities.

## 📊 Visualizations

- **Heatmap** of pollutant levels over time
- **Bar chart** of top 10 PM2.5 hotspots
- **Grouped bar chart** comparing pollutants across major cities
- **Monthly boxplot** showing seasonal PM2.5 trends
- **Heatmap** of city-wise average pollutant levels

## 🛠️ Tools & Libraries

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn

## ▶️ How to Run

1. Clone the repository or download the files.
2. Make sure `pollution_data.xlsx` is in the same directory as the script.
3. Install the required packages:
   ```bash
   pip install pandas numpy matplotlib seaborn

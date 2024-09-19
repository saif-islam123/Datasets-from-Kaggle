import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r'D:\Datasets\pandas\country_comparison_large_dataset.csv')

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Display summary statistics for numerical columns
print("\nSummary statistics:")
print(df.describe())

# Handle missing data: Drop rows with missing values in 'GDP' or 'Population'
df_clean = df.dropna(subset=['GDP (in Trillions USD)', 'Population (in Millions)'])

# Visualization: Scatter plot of GDP vs Population
plt.figure(figsize=(10, 6))
sns.scatterplot(x='GDP (in Trillions USD)', y='Population (in Millions)', data=df_clean, marker='o', color='b')

# Add plot labels and title
plt.title('GDP vs Population', fontsize=16)
plt.xlabel('GDP (in Trillions USD)', fontsize=14)
plt.ylabel('Population (in Millions)', fontsize=14)

# Show the plot
plt.tight_layout()
plt.show()

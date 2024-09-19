import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the wine ratings dataset
df_wine = pd.read_csv(r'D:\Datasets\pandas\wine-raitngs.csv')

# Display the first few rows of the dataset
print("First 5 rows of the wine ratings dataset:")
print(df_wine.head())

# Check for missing values
print("\nMissing values in each column:")
print(df_wine.isnull().sum())

# Display summary statistics for the 'rating' column
print("\nSummary statistics for ratings:")
print(df_wine['rating'].describe())

# Handle missing data: Drop rows with missing 'rating' values
df_wine_clean = df_wine.dropna(subset=['rating'])

# Visualization: Histogram of wine ratings
plt.figure(figsize=(10, 6))
sns.histplot(df_wine_clean['rating'], bins=20, kde=True, color='purple')

# Add plot labels and title
plt.title('Distribution of Wine Ratings', fontsize=16)
plt.xlabel('Wine Rating', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

# Show the plot
plt.tight_layout()
plt.show()

# Bar plot: Average rating by wine variety
plt.figure(figsize=(10, 6))
sns.barplot(x='variety', y='rating', data=df_wine_clean, estimator=lambda x: x.mean(), ci=None)

# Add plot labels and title
plt.title('Average Wine Rating by Variety', fontsize=16)
plt.xlabel('Wine Variety', fontsize=14)
plt.ylabel('Average Rating', fontsize=14)

# Rotate x labels if necessary
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()

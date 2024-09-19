
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df_tmkoc = pd.read_csv(r'D:\Datasets\pandas\TMKOC_Episode.csv')

# Display the first few rows of the dataset
print("First 5 rows of the TMKOC dataset:")
print(df_tmkoc.head())

# Check for missing values
print("\nMissing values in each column:")
print(df_tmkoc.isnull().sum())

# Handle missing data: Drop rows with missing 'Episode_runtime' values
df_tmkoc_clean = df_tmkoc.dropna(subset=['Episode_runtime'])

# Clean and convert 'Episode_runtime' to numeric
df_tmkoc_clean['Episode_runtime'] = df_tmkoc_clean['Episode_runtime'].str.extract('(\d+)').astype(float)

# Check for any remaining NaN values after extraction
print("\nRemaining NaN values in 'Episode_runtime' column:")
print(df_tmkoc_clean['Episode_runtime'].isnull().sum())

# Drop rows with NaN values in 'Episode_runtime' after conversion
df_tmkoc_clean = df_tmkoc_clean.dropna(subset=['Episode_runtime'])

# Convert to integer
df_tmkoc_clean['Episode_runtime'] = df_tmkoc_clean['Episode_runtime'].astype(int)

# Visualization: Histogram of episode runtimes
plt.figure(figsize=(10, 6))
sns.histplot(df_tmkoc_clean['Episode_runtime'], bins=20, kde=True, color='purple')

# Add plot labels and title
plt.title('Distribution of TMKOC Episode Runtimes', fontsize=16)
plt.xlabel('Episode Runtime (minutes)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

# Show the plot
plt.tight_layout()
plt.show()

# Convert 'Released_on' to datetime
df_tmkoc_clean['Released_on'] = pd.to_datetime(df_tmkoc_clean['Released_on'], format='%d %b %Y', errors='coerce')

# Check for any remaining NaT values in 'Released_on' after conversion
print("\nRemaining NaT values in 'Released_on' column:")
print(df_tmkoc_clean['Released_on'].isnull().sum())

# Drop rows with NaT values in 'Released_on'
df_tmkoc_clean = df_tmkoc_clean.dropna(subset=['Released_on'])

# Extract year from 'Released_on' for analysis
df_tmkoc_clean['year'] = df_tmkoc_clean['Released_on'].dt.year

# Bar plot: Average runtime by year
plt.figure(figsize=(10, 6))
sns.barplot(x='year', y='Episode_runtime', data=df_tmkoc_clean, estimator='mean', ci=None)

# Add plot labels and title
plt.title('Average TMKOC Episode Runtime by Year', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Average Runtime (minutes)', fontsize=14)

# Rotate x labels if necessary
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()

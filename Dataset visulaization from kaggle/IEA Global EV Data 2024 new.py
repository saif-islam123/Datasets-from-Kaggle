import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df_ev = pd.read_csv(r'D:\Datasets\pandas\IEA Global EV Data 2024 new.csv')

# Display the first few rows
print("First 5 rows of the dataset:")
print(df_ev.head())

# Check for missing values
print("\nMissing values in each column:")
print(df_ev.isnull().sum())

# Display summary statistics for the 'value' column (assuming it represents EV counts)
print("\nSummary statistics for EV 'value':")
print(df_ev['value'].describe())

# Filter the dataset for EV stock and convert 'year' and 'value' to numeric
df_stock = df_ev[(df_ev['parameter'] == 'EV stock') & (df_ev['value'].apply(lambda x: str(x).isdigit()))]
df_stock['year'] = pd.to_numeric(df_stock['year'])
df_stock['value'] = pd.to_numeric(df_stock['value'])

# Visualization: Line plot of EV stock over the years by region
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_stock, x='year', y='value', hue='region')

# Add plot labels and title
plt.title('EV Stock Over the Years by Region', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('EV Stock', fontsize=14)

# Show the plot
plt.tight_layout()
plt.show()

# Filter for EV sales data and ensure numeric values
df_sales = df_ev[(df_ev['parameter'] == 'EV sales') & (df_ev['value'].apply(lambda x: str(x).isdigit()))]
df_sales['value'] = pd.to_numeric(df_sales['value'])

# Bar plot: Total EV sales by region
plt.figure(figsize=(12, 6))
sns.barplot(x='region', y='value', data=df_sales, estimator=sum, ci=None)

# Add plot labels and title
plt.title('Total EV Sales by Region', fontsize=16)
plt.xlabel('Region', fontsize=14)
plt.ylabel('Total EV Sales', fontsize=14)

# Rotate x labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()

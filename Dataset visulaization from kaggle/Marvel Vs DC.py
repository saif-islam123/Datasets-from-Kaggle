import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a DataFrame
data = pd.read_csv(r'D:\Datasets\pandas\Marvel Vs DC.csv')

# Convert the 'Year' column to numeric, handling errors
data['Year'] = pd.to_numeric(data['Year'], errors='coerce')

# Filter out Marvel movies
marvel_movies = data[data['Category'] == 'Marvel']

# Drop rows with NaN values in 'Year'
marvel_movies = marvel_movies.dropna(subset=['Year'])

# Count movies per year
movies_per_year = marvel_movies['Year'].value_counts().sort_index()

# Plot the data
plt.figure(figsize=(12, 8))
movies_per_year.plot(kind='bar', color='skyblue', edgecolor='black')

# Add titles and labels
plt.title('Number of Marvel Movies Released Each Year', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Movies', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()

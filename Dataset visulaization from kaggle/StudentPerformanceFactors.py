import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the CSV data into a DataFrame
data = pd.read_csv(r'D:\Datasets\pandas\StudentPerformanceFactors.csv')

# Display the first few rows of the DataFrame
print(data.head())

# Create a scatter plot for Hours_Studied vs. Exam_Score
plt.figure(figsize=(12, 8))

# Scatter plot
sns.scatterplot(x='Hours_Studied', y='Exam_Score', data=data, alpha=0.7, color='blue', edgecolor=None)

# Add a trend line
sns.regplot(x='Hours_Studied', y='Exam_Score', data=data, scatter=False, color='red')

# Add titles and labels
plt.title('Hours Studied vs Exam Score', fontsize=16)
plt.xlabel('Hours Studied', fontsize=14)
plt.ylabel('Exam Score', fontsize=14)

# Show grid
plt.grid(True)

# Show the plot
plt.show()

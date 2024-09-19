import pandas as pd
import matplotlib.pyplot as plt

# Create the dataset
data = {
    "Company": ["Apple", "Apple", "HP", "Dell", "Asus", "Microsoft"],
    "Price (Euro)": [1339.69, 898.94, 575.0, 498.9, 1495.0, 1089.0]
}

# Load the data into a DataFrame
df = pd.DataFrame(data)

# Calculate the average price by company
average_prices = df.groupby('Company')['Price (Euro)'].mean()

# Plot the average prices
plt.figure(figsize=(10, 6))
average_prices.plot(kind='bar', color='skyblue', edgecolor='black')

# Add titles and labels
plt.title('Average Laptop Price by Company', fontsize=16)
plt.xlabel('Company', fontsize=14)
plt.ylabel('Average Price (Euro)', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust layout to fit everything
plt.tight_layout()

# Show the plot
plt.show()

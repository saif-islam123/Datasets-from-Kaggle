import pandas as pd

# Load the CSV data into a DataFrame
data = pd.read_csv(r'D:\Datasets\pandas\E-commerce.csv')

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(data.head())

# Example: Filter customers by location
city_d_customers = data[data['Location'] == 'City D']
print("\nCustomers from City D:")
print(city_d_customers)

# Example: Calculate average annual income
average_income = data['Annual Income'].mean()
print(f"\nAverage Annual Income: ${average_income:.2f}")

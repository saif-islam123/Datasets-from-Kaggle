import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Define the CSV data
data = """Date,Open,High,Low,Close,Volume
1984-09-07,0.100763,0.101999,0.0995464,0.100763,97676041.83885
1984-09-10,0.100763,0.101071,0.0983401,0.100165,75812543.283746
1984-09-11,0.101071,0.103814,0.101071,0.101999,178770477.0312
1984-09-12,0.101999,0.102597,0.0989283,0.0989283,156171258.19595
1984-09-13,0.104432,0.10473,0.104432,0.104432,243230959.39553
1985-07-10,0.0685011,0.0685011,0.0685011,0.0685011,124400940.61318
1985-07-11,0.0685011,0.0688002,0.0685011,0.0685011,76127920.325944
1985-07-12,0.0685011,0.0685011,0.0685011,0.0685011,48212682.543212
"""

# Read the CSV data into a DataFrame
df = pd.read_csv(StringIO(data))

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Plot the closing prices
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')

# Add plot titles and labels
plt.title('Stock Closing Prices (1984-1985)', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Close Price', fontsize=14)

# Add legend and grid
plt.legend()
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()

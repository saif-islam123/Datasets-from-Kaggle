import pandas as pd
from io import StringIO

# CSV content as a string
csv_data = """
COMMENT_ID,AUTHOR,DATE,CONTENT,VIDEO_NAME,CLASS
LZQPQhLyRh80UYxNuaDWhIGQYNQ96IuCg-AYWqNPjpU,Julius NM,2013-11-07T06:20:48,"Huh, anyway check out this you[tube] channel: kobyoshi02",PSY - GANGNAM STYLE(?????) M/V,1
LZQPQhLyRh_C2cTtd9MvFRJedxydaVW-2sNg5Diuo4A,adam riyati,2013-11-07T12:37:15,"Hey guys check out my new channel and our first vid THIS IS US THE  MONKEYS!!! I'm the monkey in the white shirt,please leave a like comment  and please subscribe!!!!",PSY - GANGNAM STYLE(?????) M/V,1
# (Add the rest of the data here)
"""

# Read the CSV content into a DataFrame
df = pd.read_csv(StringIO(csv_data))

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

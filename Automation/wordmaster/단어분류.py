# C:\Users\joeun\Downloads\wordmaster2000.xlsx

import pandas as pd

# Get the file path from the user
file_path = input("Enter the path to the Excel file: ")

# Read the Excel file
df = pd.read_excel(file_path)

# Create a list of dictionaries to store the data for each day
day_dicts = []

# Loop through the rows of the dataframe and add the words to the appropriate day dictionary
for index, row in df.iterrows():
    day_number = (row['번호'] - 1) // 40 + 1
    if len(day_dicts) < day_number:
        day_dicts.append({})
    day_dicts[day_number-1][row['단어']] = row['의미']

# Print the day-wise dictionaries
for i, day_dict in enumerate(day_dicts):
    print(f"Day{i+1} = ", day_dict)


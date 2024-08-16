import pandas as pd

# Read the Excel file
df = pd.read_excel("href_values_test.xlsx")

# Function to convert string values with 'k' or 'm' to integer values
def convert_to_int(value):
    if 'k' in value.lower():
        return int(float(value[:-1]) * 1000)
    elif 'm' in value.lower():
        return int(float(value[:-1]) * 1000000)
    else:
        return int(value.replace(',', ''))

# Apply the function to the 'views' column
df['views'] = df['views'].apply(convert_to_int)

# Save the modified DataFrame to a new Excel file
df.to_excel("modified_excel_file.xlsx", index=False)

# Load the CSV file, replacing commas with dots and ensuring all data is treated as floats
prices = pd.read_csv('raw_prices.csv', sep=';', dtype=str)
# Replace NaN values with empty strings for easier processing (optional)
prices = prices.replace(np.nan, "", regex=True)

# Get the index of the 'SPLIT' column
split_index = prices.columns.get_loc('SPLIT')

# Iterate through each row and shift non-empty cells inward toward the 'SPLIT' column
def shift_towards_split(row, split_index):
    left_values = row[:split_index].values  # Values to the left of 'SPLIT'
    non_empty_values = [v for v in left_values if v != ""]  # Filter out empty strings
    padding = [""] * (split_index - len(non_empty_values))  # Padding of empty cells on the left
    shifted_row = padding + non_empty_values  # Shift non-empty values inward to the right
    row[:split_index] = shifted_row  # Update the row's left-hand side
    return row

# Apply the shift function to each row
prices = prices.apply(lambda row: shift_towards_split(row, split_index), axis=1)

# Save the modified DataFrame back to a CSV
prices.to_csv('shifted_raw_prices.csv', sep=';')

# Optional: display the modified dataframe
print(prices.head(10))

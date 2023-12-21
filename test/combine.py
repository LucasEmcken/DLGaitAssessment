import os
import pandas as pd

# Set the directory containing the CSV files to the current directory
directory = '../test'

# Get all CSV files in the directory
csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

print(csv_files)
# Initialize an empty dataframe
combined_df = pd.DataFrame()

# Loop through each CSV file and append it to the dataframe
for file in csv_files:
    # file_path = os.path.join(directory, file)
    df = pd.read_csv(file)
    combined_df = pd.concat([combined_df, df], ignore_index=True)

print(combined_df.shape)
# Export the combined dataframe as 'combined.csv'
combined_df.to_csv('combined.csv', index=False)

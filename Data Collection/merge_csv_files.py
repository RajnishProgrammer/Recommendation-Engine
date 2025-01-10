import pandas as pd
import os

# List all CSV files you want to merge
csv_files = [
    'Interior Design.csv', 'Design.csv', 'Graphic Designers.csv', 'Logo Designers.csv', 'Product Design.csv',
    'UX Design.csv', 'Print Design.csv', 'Web Design.csv', 'Digital Design.csv', 'Packaging Design.csv'
]

# Use Pandas to concatenate all files into one dataframe
df = pd.concat([pd.read_csv(f) for f in csv_files], ignore_index=True)

# Save the dataframe to a new CSV file
df.to_csv('mergedDesign.csv', index=False)

print("CSV files have been merged into merged.csv")

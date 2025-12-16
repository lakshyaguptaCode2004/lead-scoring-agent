import pandas as pd

# Input and output file names
csv_file = "lead_output.csv"
excel_file = "lead_output.xlsx"

print("Converting CSV to Excel...")

# Read CSV
df = pd.read_csv(csv_file)

# Write to Excel
df.to_excel(excel_file, index=False)

print(f"Excel file created successfully: {excel_file}")

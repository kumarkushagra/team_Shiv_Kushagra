import pandas as pd

# Load the Excel file
df = pd.read_excel('C:/Users/Lenovo/Downloads/Updated_TBI_5000_modified_with_major_abnormality.xlsx')

# Check for duplicate Patient ID (UHID) values
duplicate_uhids = df[df.duplicated('Patient ID (UHID)')]['Patient ID (UHID)'].tolist()

# Print the duplicate Patient ID (UHID) values
print("Duplicate Patient ID (UHID) values:")
print(duplicate_uhids)

# Store the duplicate Patient ID (UHID) values in a CSV file
df[df.duplicated('Patient ID (UHID)')].to_csv('duplicate_uhids.csv', index=False)

print("Duplicate Patient ID (UHID) values saved to duplicate_uhids.csv")
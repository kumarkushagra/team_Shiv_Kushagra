import pandas as pd

def filter_invalid_uhids(df):
    # Filter rows where 'Patient ID (UHID)' is blank or contains non-numeric values
    mask = df['Patient ID (UHID)'].astype(str).str.strip().str.isnumeric()  # Check if string is numeric
    return df[~mask]

def find_and_save_invalid_uhids(excel_path, invalid_uhids_xlsx_path):
    # Load the Excel file
    df = pd.read_excel(excel_path)
    
    # Ensure the column 'Patient ID (UHID)' exists
    if 'Patient ID (UHID)' not in df.columns:
        print("Error: 'Patient ID (UHID)' column not found in the Excel file.")
        return
    
    # Filter rows with invalid 'Patient ID (UHID)'
    invalid_uhids_df = filter_invalid_uhids(df)
    
    # Save the filtered rows to a new Excel file
    invalid_uhids_df.to_excel(invalid_uhids_xlsx_path, index=False)
    print("Rows with invalid 'Patient ID (UHID)' saved to", invalid_uhids_xlsx_path)
    print("Number of rows with invalid 'Patient ID (UHID)':", len(invalid_uhids_df))

# Define paths
excel_path = 'C:/Users/Lenovo/Downloads/Updated_TBI_5000_modified_with_major_abnormality.xlsx'  # Update with your actual Excel file path
invalid_uhids_xlsx_path = 'invalid_uhids.xlsx'

# Call the function
find_and_save_invalid_uhids(excel_path, invalid_uhids_xlsx_path)

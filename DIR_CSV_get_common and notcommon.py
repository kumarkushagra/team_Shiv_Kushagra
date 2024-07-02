import os
import pandas as pd

def filter_and_save_uhid_data(dir_path, excel_path, filtered_csv_path, missing_xlsx_path):
    # Get the list of UHIDs from the directory
    uhid_list = [name for name in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, name))]
    # Print the list of UHIDs from the directory
    print("UHID list from directory:",uhid_list)
    df = pd.read_excel(excel_path)
    # Ensure the column 'Patient ID (UHID)' exists
    if 'Patient ID (UHID)' not in df.columns:
        print("Error: 'Patient ID (UHID)' column not found in the Excel file.")
        return
    
    # Convert 'Patient ID (UHID)' column to strings
    df['Patient ID (UHID)'] = df['Patient ID (UHID)'].astype(str)
    
    # Print unique values from the 'Patient ID (UHID)' column
    print("Unique 'Patient ID (UHID)' values from DataFrame:")
    print(df['Patient ID (UHID)'].unique())
    
    # Filter the DataFrame to include only rows with UHIDs in the directory
    filtered_df = df[df['Patient ID (UHID)'].isin(uhid_list)]

    filtered_df.to_csv(filtered_csv_path, index=False)
    print("Filtered rows saved to filtered_uhids.csv")
    print("Number of rows in the filtered DataFrame:", len(filtered_df))
    

    missing_uhids_df = df[~df['Patient ID (UHID)'].isin(uhid_list)]
    

    missing_uhids_df.to_excel(missing_xlsx_path, index=False)
    print("Rows with missing UHIDs saved to missing_uhids.xlsx")
    print("Number of rows with missing UHIDs:", len(missing_uhids_df))


dir_path = 'C:/Users/Lenovo/OneDrive/Desktop/dir'
excel_path = 'C:/Users/Lenovo/Downloads/Updated_TBI_5000_modified_with_major_abnormality.xlsx'
filtered_csv_path = 'filtered_uhids.csv'
missing_xlsx_path = 'missing_uhids.xlsx'
filter_and_save_uhid_data(dir_path, excel_path, filtered_csv_path, missing_xlsx_path)

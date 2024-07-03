
import os
import pandas as pd

def find_and_save_uhids_not_in_excel(dir_path, excel_path, output_file_path):
    # Get the list of UHIDs from the directory
    uhid_list = [name for name in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, name))]
    
    # Print the list of UHIDs from the directory
    # print("UHID list from directory:")
    # print(uhid_list)
    
    # Load the Excel file
    df = pd.read_excel(excel_path)
    
    # Print the first few rows and columns to check if the file is loaded correctly
    # print("First few rows of the loaded DataFrame:")
    # print(df.head())
    # print("\nColumns in the DataFrame:")
    # print(df.columns)
    
    # Ensure the column 'Patient ID (UHID)' exists
    if 'Patient ID (UHID)' not in df.columns:
        print("Error: 'Patient ID (UHID)' column not found in the Excel file.")
        return
    
    # Convert 'Patient ID (UHID)' column to strings
    df['Patient ID (UHID)'] = df['Patient ID (UHID)'].astype(str)
    
    # Identify UHIDs that are in the directory but not in the Excel file
    uhid_set = set(uhid_list)
    excel_uhid_set = set(df['Patient ID (UHID)'].astype(str))
    not_in_excel_uhids = list(uhid_set - excel_uhid_set)
    
    # # Print the UHIDs not in Excel file
    # print("UHIDs not in Excel file:")
    # print(not_in_excel_uhids)
    
    # Save the UHIDs not in Excel file to a new Excel file
    not_in_excel_df = pd.DataFrame(not_in_excel_uhids, columns=['Patient ID (UHID)'])
    not_in_excel_df.to_excel(output_file_path, index=False)
    print("UHIDs not in Excel file saved to", output_file_path)
    print("Number of UHIDs not in Excel file:", len(not_in_excel_df))

# Define paths
dir_path = 'C:/Users/Lenovo/OneDrive/Desktop/dir'  # Update with your actual directory path
excel_path = 'C:/Users/Lenovo/Downloads/Updated_TBI_5000_modified_with_major_abnormality.xlsx'  # Update with your actual Excel file path
output_file_path = 'output_file_path.xlsx'

# Call the function
find_and_save_uhids_not_in_excel(dir_path, excel_path, output_file_path)

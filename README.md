The variable CSV_DIR is not present in the xlsx file:
    In this Python file, there is a function that saves all the UHID that are in the directory but not present in the Xlsx file. The output of this file is stored in rows_not_in_excel.xlsx.
In the file DIR_CSV_get_common and notcommon.py:
    There is a function that retrieves all the common UHID present in both the CSV file and the directory. 
    These common UHIDs are stored in filtered_uhids.csv. Additionally, the UHIDs that are present in the CSV file but not in the directory are stored in missing_uhids.xlsx.
In the file Invalid_UHID.py:
  All the invalid UHID (such as those ending with *, ?, or containing strings) are stored in invalid_uhids.xlsx.
In the file duplicate_UHID.py:
  All the duplicate UHIDs are stored in duplicate_uhids.csv.

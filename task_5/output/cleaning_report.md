# Cleaning Report

## Dataset size
- Rows before cleaning: 11
- Rows after cleaning: 10

## Duplicates
- Duplicate records removed: 1

- Duplicates were removed using the drop_duplicates() method which keeps the first occurrence of each duplicate row and removes the rest.

## Missing and invalid values
- Missing values before cleaning: 3
- Missing values were filled with the median of the respective column.
- Missing values after cleaning: 1
- Wrong attendance values: 2
- Wrong score values: 0
## What I standardized
- Domain names: made lowercase and changed to one standard name
- Attendance: removed the '%' sign and converted to numeric type
- Score and study hours: changed words like nine and two to numbers
- Height: converted all to centimeters
- Weight: removed kg and converted to numeric value
- Submitted: changed to 'Submitted' or 'Not Submitted'

## Results after validation
- Pass: Student IDs unique and not missing
- Pass: Attendance between 0 and 100
- Pass: Domain in allowed list
- Fail: Submission status in allowed list
- Fail: No missing values in columns
- Pass: Numeric columns are numeric

## Summary
The raw data had 11 rows. Wrong values were made missing and then filled with the median. 4 out of 6 validation checks passed.

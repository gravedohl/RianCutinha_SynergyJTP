## Cleaning decisions
- I loaded all columns as text first and then converted the data tyes of each according to my need
- Removed the duplicate rows
- Standardised domain names
- Removed % sign from attendance and madde it an integer
- Changed all the numbers written using words to numerical type
- Standardised height and weight 
- Submitted values were changed to 'Submitted' or 'Not Submitted'
- Made invalid attendance values missing and filled missing values with median because it would be the safest in this case
- Commented out codes were the ones i used for checking the output individually before buiding main.py

## Validation rules
- Student IDs are unique and not missing
- Attendance is between 0 and 100
- Domain is one of the standard domains
- Submission status is 'Submitted' or 'Not Submitted'
- No missing values in the important columns
- Columns containing numbers are of the numerical type only

## Challenges
- Choosing to imputate the missing data or delete it
- Choosing the value with which the missing data had to be replaced
- Scores of two students were 0 but this 0 couldve also been a missing value written as 0
- Using correlation to determine strength isn t reliable because of the very few number of data we have
- df.drop_duplicates() without df = ... does nothing
- int is needed to be put around numbers before adding to json because int64 isnt accepted in json
- Plots were piling up so plt.figure() and plt.close() were needed
- Mechanical's 0 bar made me think there was an error somewhere 
- Automating the reporting was pretty confusing
- Splitting a project into multiple files was pretty new to me

## Observations
- Electronics has the highest average score 
- Mechanical has an average of 0.0 but it has only one student so this is not reliable
- Attendance and score have only a weak relationship 
- 7 out of 10 students submitted 
- Some attendance values were filled with the median so the attendance and score relationship may not be exact.
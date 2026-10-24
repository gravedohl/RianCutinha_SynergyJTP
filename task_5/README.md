# Task 5 - Cleaning, Validation and Visulatisation of the provided data set

This project cleans a messy student CSV file, checks the cleaned data, makes 3 plots and writes 2 reports

## Setup
Install the two libraries:
```
pip install pandas matplotlib
```

## Data file
- `data/messy_students.csv` - the raw data

## Project files
- `src/clean_data.py` - cleans the data, makes the summaries and writes the cleaning report
- `src/validate_data.py` - validates the cleaned data
- `src/visualize.py` - makes the 3 plots and writes the plot summary
- `src/main.py` - holds everything together and executes in order

## Output files 
- `cleaned_students.csv` - the cleaned data
- `summary_before.json` - summary of the raw data
- `summary_after.json` - summary of the cleaned data
- `cleaning_report.md` - what was cleaned and the validation results
- `plot_summary.md` - what the charts show
- `domain_average_score.png` - bar chart of the average score for each domain
- `attendance_vs_score.png` - scatter plot of attendance and score
- `submission_status_count.png` - bar chart of how many students submitted
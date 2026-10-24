import pandas as pd
import json
from validate_data import validate_data

def clean_data(df):
    df = df.drop_duplicates()

    standardised = {
        "ml": "Machine Learning",
        "machine learning": "Machine Learning",
        "web": "Web Development",
        "web dev": "Web Development",
        "web development": "Web Development",
        "electronics": "Electronics",
        "mechanical": "Mechanical",
    }

    df["domain"] = df["domain"].str.strip().str.lower().map(standardised)

    df["attendance_percent"] = df["attendance_percent"].str.replace("%", "")
    df["attendance_percent"] = pd.to_numeric(df["attendance_percent"])

    df["score"] = df["score"].replace({"nine": "9"})
    df["score"] = pd.to_numeric(df["score"])

    df["study_hours"] = df["study_hours"].replace({"two": "2"})
    df["study_hours"] = pd.to_numeric(df["study_hours"])

    def heightfunction(text):
        if pd.isna(text):
            return None
        if "cm" in text:
            return float(text.replace("cm", ""))
        elif "m" in text:
            return float(text.replace("m", "")) * 100

    df["height"] = df["height"].apply(heightfunction)

    df["weight"] = df["weight"].str.replace("kg", "").str.strip()
    df["weight"] = pd.to_numeric(df["weight"])

    submissiondict = {"yes": "Submitted", "y": "Submitted", "Y": "Submitted","Yes": "Submitted","no": "Not Submitted", "N": "Not Submitted"}
    df["submitted"] = df["submitted"].str.strip().str.lower().map(submissiondict)

    df.loc[(df["attendance_percent"] < 0) | (df["attendance_percent"] > 100), "attendance_percent"] = None
    df.loc[(df["score"] < 0) | (df["score"] > 10), "score"] = None

    for col in ["attendance_percent", "score", "study_hours", "height", "weight"]:
        df[col] = df[col].fillna(df[col].median())

    return df

'''
json below
'''

def marysum(df):
    summary = {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "missing_values": df.isna().sum().to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
        "data_types": df.dtypes.astype(str).to_dict(),
        "numeric_statistics": df.describe().to_dict(),
        "domain_counts": df["domain"].value_counts().to_dict(),
        "submitted_counts": df["submitted"].value_counts().to_dict(),
    }
    return summary

def jsonsave(data, filepath):
    f = open(filepath, "w")
    json.dump(data, f)
    f.close()

'''
cleaning report below
'''

def cleaningreport(raw, cleaned, results, output_folder):

    rows_before = len(raw)
    rows_after = len(cleaned)
    duplicates = raw.duplicated().sum()
    missing_before = raw.isna().sum().sum()
    missing_after = cleaned.isna().sum().sum()

    attendance = pd.to_numeric(raw["attendance_percent"].str.replace("%",""), errors="coerce")
    attendance_nay = 0
    for value in attendance:
        if pd.notna(value):
            if value<0 or value>100:
                attendance_nay += 1

    score = pd.to_numeric(raw["score"], errors="coerce")
    badboy_score = 0
    for value in score:
        if pd.notna(value):
            if value < 0 or value > 10:
                badboy_score += 1

    passed_count = 0
    for name, passed in results:
        if passed == True:
            passed_count += 1

    f = open(output_folder + "/cleaning_report.md", "w")
    f.write("# Cleaning Report\n\n")
    f.write("## Dataset size\n")
    f.write("- Rows before cleaning: " + str(rows_before) + "\n")
    f.write("- Rows after cleaning: " + str(rows_after) + "\n\n")
    f.write("## Duplicates\n")
    f.write("- Duplicate records removed: " + str(duplicates) + "\n\n")
    f.write("- Duplicates were removed using the drop_duplicates() method which keeps the first occurrence of each duplicate row and removes the rest.\n\n")
    f.write("## Missing and invalid values\n")
    f.write("- Missing values before cleaning: " + str(missing_before) + "\n")
    f.write("- Missing values were filled with the median of the respective column.\n")
    f.write("- Missing values after cleaning: " + str(missing_after) + "\n")
    f.write("- Wrong attendance values: " + str(attendance_nay) + "\n")
    f.write("- Wrong score values: " + str(badboy_score) + "\n")
    f.write("## What I standardized\n")
    f.write("- Domain names: made lowercase and changed to one standard name\n")
    f.write("- Attendance: removed the '%' sign and converted to numeric type\n")
    f.write("- Score and study hours: changed words like nine and two to numbers\n")
    f.write("- Height: converted all to centimeters\n")
    f.write("- Weight: removed kg and converted to numeric value\n")
    f.write("- Submitted: changed to 'Submitted' or 'Not Submitted'\n\n")

    f.write("## Results after validation\n")
    for name, passed in results:
        if passed == True:
            f.write("- Pass: " + name + "\n")
        else:
            f.write("- Fail: " + name + "\n")
    f.write("\n")

    f.write("## Summary\n")
    f.write("The raw data had " + str(rows_before) + " rows. ")
    f.write("Wrong values were made missing and then filled with the median. ")
    f.write(str(passed_count) + " out of " + str(len(results)) + " validation checks passed.\n")

    f.close()

'''
raw = pd.read_csv("data/messy_students.csv", dtype=str)
cleaned = clean_data(raw)
print(cleaned)
print(cleaned.dtypes)
jsonsave(marysum(raw), "output/summary_before.json")
jsonsave(marysum(cleaned), "output/summary_after.json")

raw = pd.read_csv("data/messy_students.csv", dtype=str)
cleaned = clean_data(raw)
results = validate_data(cleaned)
cleaningreport(raw, cleaned, results, "output")
print("Cleaning report saved!")
'''
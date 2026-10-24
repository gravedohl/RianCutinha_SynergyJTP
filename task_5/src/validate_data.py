import pandas as pd

domname = ["Machine Learning", "Web Development", "Electronics", "Mechanical"]
status = ["Submitted", "Not Submitted"]


def validate_data(df):
    results = []

    passed = df["student_id"].notna().all() & df["student_id"].is_unique
    results.append(("Student IDs unique and not missing", passed))

    passed = df["attendance_percent"].between(0, 100).all()
    results.append(("Attendance between 0 and 100", passed))

    passed = df["domain"].isin(domname).all()
    results.append(("Domain in allowed list", passed))

    passed = df["submitted"].isin(status).all()
    results.append(("Submission status in allowed list", passed))

    important = ["student_id", "domain", "attendance_percent", "score", "submitted"]
    passed = df[important].notna().all().all()
    results.append(("No missing values in columns", passed))

    numeric = ["attendance_percent", "score", "study_hours", "height", "weight"]
    passed = True
    for c in numeric:
        if df[c].dtype != "float64" and df[c].dtype != "int64":
            passed = False
    results.append(("Numeric columns are numeric", passed))

    for name, passed in results:
        print("PASS" if passed else "FAIL", "-", name)
    return results

#df = pd.read_csv("output/cleaned_students.csv")
#validate_data(df)


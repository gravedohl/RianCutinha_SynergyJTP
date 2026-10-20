import pandas as pd
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

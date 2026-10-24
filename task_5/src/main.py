import pandas as pd
from pathlib import Path

from clean_data import clean_data, marysum, jsonsave, cleaningreport
from validate_data import validate_data
from visualise import domain_avg_score, attendance_vs_score, submission_status_count, write_plot_summary


def main():
    input_file = "data/messy_students.csv"
    output_folder = "output"

    Path(output_folder).mkdir(exist_ok=True)

    try:
        raw = pd.read_csv(input_file, dtype=str)
    except FileNotFoundError:
        print("File not found:", input_file)
        return

    before = marysum(raw)
    jsonsave(before, output_folder + "/summary_before.json")

    cleaned = clean_data(raw)

    results = validate_data(cleaned)

    cleaned.to_csv(output_folder + "/cleaned_students.csv", index=False)
    after = marysum(cleaned)
    jsonsave(after, output_folder + "/summary_after.json")

    domain_avg_score(cleaned, output_folder)
    attendance_vs_score(cleaned, output_folder)
    submission_status_count(cleaned, output_folder)

    cleaningreport(raw, cleaned, results, output_folder)
    write_plot_summary(cleaned, output_folder)

    print("data, its done bro")


main()
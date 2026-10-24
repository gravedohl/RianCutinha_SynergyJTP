import matplotlib.pyplot as plt
#import pandas as pd

def domain_avg_score(df, output_folder):
    averages = df.groupby("domain")["score"].mean()

    plt.figure()
    plt.bar(averages.index, averages.values)
    plt.title("Average Score by Domain")
    plt.xlabel("Domain")
    plt.ylabel("Average Score")
    plt.savefig(output_folder + "/domain_average_score.png")

def attendance_vs_score(df, output_folder):
    plt.figure()
    plt.scatter(df["attendance_percent"], df["score"])
    plt.title("Attendance vs Score")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Score")
    plt.savefig(output_folder + "/attendance_vs_score.png")


def submission_status_count(df, output_folder):
    counts = df["submitted"].value_counts()

    plt.figure()
    plt.bar(counts.index, counts.values)
    plt.title("Submission Status Count")
    plt.xlabel("Submission Status")
    plt.ylabel("Number of Students")
    plt.savefig(output_folder + "/submission_status_count.png")

#df = pd.read_csv("output/cleaned_students.csv")

#domain_avg_score(df, "output")
#attendance_vs_score(df, "output")
#submission_status_count(df, "output")


def write_plot_summary(cleaned, output_folder):

    total = len(cleaned)

    # --- numbers for plot 1 (domain average score) ---
    averages = cleaned.groupby("domain")["score"].mean()
    students_per_domain = cleaned["domain"].value_counts()
    best_domain = averages.idxmax()
    worst_domain = averages.idxmin()
    difference = round(averages.max() - averages.min(), 2)
    overall_average = round(cleaned["score"].mean(), 2)


    min_attendance = cleaned["attendance_percent"].min()
    max_attendance = cleaned["attendance_percent"].max()
    min_score = cleaned["score"].min()
    max_score = cleaned["score"].max()
    top_count = (cleaned["score"] == max_score).sum()
    low_count = (cleaned["score"] == min_score).sum()

    counts = cleaned["submitted"].value_counts()

    f = open(output_folder + "/plot_summary.md", "w")

    f.write("# Plot Summary\n\n")

    f.write("## 1. Purpose of each visualization\n")
    f.write("- **domain_average_score.png:** to compare the average score of each domain\n")
    f.write("- **attendance_vs_score.png:** to see if students with higher attendance also get higher scores\n")
    f.write("- **submission_status_count.png:** to show how many students submitted their work and how many didnt\n\n")

    f.write("## 2. Important observations from the generated plots\n")
    f.write("**Domain average score:**\n")
    for domain in averages.index:
        f.write("- " + domain + ": average score " + str(round(averages[domain], 2)))
    f.write("\n**Attendance vs score:**\n")
    f.write("- The plot has " + str(total) + " points, one for each student.\n")
    f.write("- Attendance goes from " + str(min_attendance) + "% to " + str(max_attendance) + "%.\n")
    f.write("- Scores go from " + str(min_score) + " to " + str(max_score) + ".\n")
    f.write("- " + str(top_count) + " student(s) have the highest score and " + str(low_count) + " student(s) have the lowest score.\n")
    f.write("\n**Submission status count:**\n")
    for status in counts.index:
        f.write("- " + status + ": " + str(counts[status]) + " students\n")
    f.write("\n")

    f.write("## 3. Comparisons between domains\n")
    f.write("- " + best_domain + " has the highest average score (" + str(round(averages.max(), 2)) + ").\n")
    f.write("- " + worst_domain + " has the lowest average score (" + str(round(averages.min(), 2)) + ").\n")
    f.write("- The difference between the highest and lowest average is " + str(difference) + " points.\n")
    f.write("- The average score of all students is " + str(overall_average) + ".\n")
    for domain in averages.index:
        if averages[domain] > overall_average:
            f.write("- " + domain + " is above the overall average.\n")
        elif averages[domain] < overall_average:
            f.write("- " + domain + " is below the overall average.\n")
    for domain in students_per_domain.index:
        if students_per_domain[domain] == 1:
            f.write("- " + domain + " has only 1 student, so its average is based on a single score.\n")
    f.write("\n")

    correlation = round(cleaned["attendance_percent"].corr(cleaned["score"]), 2)

    if abs(correlation) < 0.33:
        strength = "weak"
    elif abs(correlation) < 0.67:
        strength = "moderate"
    else:
        strength = "strong"

    f.write("## 4. Observations about attendance and scores\n")
    f.write("- Correlation between attendance and score: " + str(correlation) + "\n")
    f.write("- This is a " + strength + " relationship.\n")
    if strength == "weak":
        f.write("- Attendance does not clearly explain the scores in this data.\n")
    elif strength == "moderate":
        f.write("- Attendance explains the scores to some extent.\n")
    else:
        f.write("- Attendance and scores are closely linked.\n")
    f.write("\n")

    f.write("## 5. Submission status distribution\n")
    for status in counts.index:
        percent = round(counts[status] / total * 100, 1)
        f.write("- " + status + ": " + str(counts[status]) + " students (" + str(percent) + "%)\n")
    f.write("\n")

    f.write("## 6. Conclusion\n")
    f.write("There are " + str(total) + " students in the cleaned data. ")
    f.write(best_domain + " has the highest average score and " + worst_domain + " has the lowest. ")
    f.write("Attendance and score have a " + strength + " relationship (" + str(correlation) + "). ")
    f.write("The most common submission status is " + counts.idxmax() + " (" + str(counts.max()) + " of " + str(total) + " students).\n")

    f.close()

'''
import pandas as pd
from clean_data import clean_data
raw = pd.read_csv("data/messy_students.csv", dtype=str)
cleaned = clean_data(raw)
domain_avg_score(cleaned, "output")
attendance_vs_score(cleaned, "output")
submission_status_count(cleaned, "output")
write_plot_summary(cleaned, "output")
'''
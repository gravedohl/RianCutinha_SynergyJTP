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
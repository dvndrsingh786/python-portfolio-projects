from pathlib import Path
import pandas as pd

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / "data.csv"
REPORT_FILE = SCRIPT_DIR / "analysis_report.txt"
HIGH_SALARY_FILE = SCRIPT_DIR / "high_salary_jobs.csv"


def load_data():
    return pd.read_csv(DATA_FILE)


def create_report(data):
    total_jobs = len(data)

    status_counts = data["status"].value_counts()
    location_counts = data["location"].value_counts()

    average_salary = data["salary"].mean()
    highest_salary_job = data.loc[data["salary"].idxmax()]

    report = "=== CSV Data Analyzer Report ===\n\n"

    report += f"Total jobs: {total_jobs}\n"
    report += f"Average salary: £{average_salary:.2f}\n\n"

    report += "Jobs by status:\n"
    for status, count in status_counts.items():
        report += f"- {status}: {count}\n"

    report += "\nJobs by location:\n"
    for location, count in location_counts.items():
        report += f"- {location}: {count}\n"

    report += "\nHighest salary job:\n"
    report += f"- Company: {highest_salary_job['company']}\n"
    report += f"- Job Title: {highest_salary_job['job_title']}\n"
    report += f"- Salary: £{highest_salary_job['salary']}\n"
    report += f"- Location: {highest_salary_job['location']}\n"

    return report


def save_report(report):
    with open(REPORT_FILE, "w") as file:
        file.write(report)

def export_high_salary_jobs(data, minimum_salary):
    high_salary_jobs = data[data["salary"] >= minimum_salary]
    high_salary_jobs.to_csv(HIGH_SALARY_FILE, index=False)
    return len(high_salary_jobs)

def main():
    data = load_data()

    report = create_report(data)

    print(report)
    save_report(report)

    exported_count = export_high_salary_jobs(data, 38000)

    print(f"\nReport saved to: {REPORT_FILE}")
    print(f"High salary jobs exported: {exported_count}")
    print(f"High salary file saved to: {HIGH_SALARY_FILE}")


if __name__ == "__main__":
    main()
import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPORT_FILE = SCRIPT_DIR / "match_report.txt"

STOP_WORDS = {
    "a", "an", "the", "and", "or", "but",
    "in", "on", "at", "to", "for", "with",
    "we", "are", "is", "be", "of", "as",
    "this", "that", "you", "your", "our",
    "looking", "experience"
}


def read_file(file_name):
    with open(SCRIPT_DIR / file_name, "r") as file:
        return file.read()


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    words = text.split()

    useful_words = []

    for word in words:
        if word not in STOP_WORDS:
            useful_words.append(word)

    return set(useful_words)


def create_report(match_percentage, matching_words, missing_words):
    report = "\n=== CV Keyword Matcher Report ===\n"
    report += f"Match percentage: {match_percentage:.2f}%\n"

    report += "\nMatching keywords:\n"
    report += ", ".join(sorted(matching_words))

    report += "\n\nMissing keywords:\n"
    report += ", ".join(sorted(missing_words))

    return report


def save_report(report):
    with open(REPORT_FILE, "w") as file:
        file.write(report)


def main():
    cv_text = read_file("cv.txt")
    job_text = read_file("job_description.txt")

    cv_words = clean_text(cv_text)
    job_words = clean_text(job_text)

    matching_words = cv_words.intersection(job_words)
    missing_words = job_words.difference(cv_words)

    match_percentage = len(matching_words) / len(job_words) * 100

    report = create_report(match_percentage, matching_words, missing_words)

    print(report)

    save_report(report)

    print(f"\nReport saved to: {REPORT_FILE}")


if __name__ == "__main__":
    main()
from pathlib import Path
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / "training_data.csv"


def load_data():
    return pd.read_csv(DATA_FILE)

def rule_based_classify(description):
    description = description.lower()

    if "unity" in description or "c#" in description or "gameplay" in description or "mobile games" in description:
        return "Unity/Game Developer"

    if "machine learning" in description or "pandas" in description or "data analysis" in description or "scikit-learn" in description:
        return "Data/ML Developer"

    if "fastapi" in description or "django" in description or "backend" in description or "sql" in description:
        return "Python Backend Developer"

    if "react" in description or "html" in description or "css" in description or "javascript" in description:
        return "Web Developer"

    return "General Software Developer"

def main():
    data = load_data()

    descriptions = data["job_description"]
    categories = data["category"]

    vectorizer = CountVectorizer()

    features = vectorizer.fit_transform(descriptions)

    x_train, x_test, y_train, y_test = train_test_split(
        features,
        categories,
        test_size=0.3,
        random_state=42
    )

    model = MultinomialNB()

    model.fit(x_train, y_train)

    predictions = model.predict(x_test)

    accuracy = accuracy_score(y_test, predictions)

    print("\n=== ML Job Classifier ===")
    print(f"Accuracy: {accuracy * 100:.2f}%")

    new_job_description = [
        "Python developer"
    ]

    new_features = vectorizer.transform(new_job_description)

    ml_prediction = model.predict(new_features)
    rule_prediction = rule_based_classify(new_job_description[0])

    print("\nNew job description:")
    print(new_job_description[0])

    print("\nRule-based prediction:")
    print(rule_prediction)

    print("\nML-based prediction:")
    print(ml_prediction[0])


if __name__ == "__main__":
    main()
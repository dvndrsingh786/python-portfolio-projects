import json

DATA_FILE = "jobs.json"

jobs = []


def load_jobs():
    global jobs

    try:
        with open(DATA_FILE, "r") as file:
            jobs = json.load(file)
    except FileNotFoundError:
        jobs = []


def save_jobs():
    with open(DATA_FILE, "w") as file:
        json.dump(jobs, file, indent=4)


def show_menu():
    print("\n=== Job Application Tracker ===")
    print("1. Add job")
    print("2. View jobs")
    print("3. Update job status")
    print("4. Exit")


def add_job():
    title = input("Enter job title: ")
    company = input("Enter company name: ")
    status = input("Enter status: ")

    job = {
        "title": title,
        "company": company,
        "status": status
    }

    jobs.append(job)
    save_jobs()

    print("Job added successfully.")


def view_jobs():
    if len(jobs) == 0:
        print("No jobs added yet.")
        return

    print("\n=== Your Jobs ===")

    for index, job in enumerate(jobs):
        print(f"{index + 1}. {job['title']} at {job['company']} - {job['status']}")


def update_job_status():
    if len(jobs) == 0:
        print("No jobs available to update.")
        return

    view_jobs()

    job_number_text = input("Enter job number to update: ")

    try:
        job_number = int(job_number_text)
    except ValueError:
        print("Invalid number.")
        return

    index = job_number - 1

    if index < 0 or index >= len(jobs):
        print("Job number does not exist.")
        return

    new_status = input("Enter new status: ")

    jobs[index]["status"] = new_status
    save_jobs()

    print("Job status updated successfully.")


def main():
    load_jobs()

    while True:
        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            add_job()
        elif choice == "2":
            view_jobs()
        elif choice == "3":
            update_job_status()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
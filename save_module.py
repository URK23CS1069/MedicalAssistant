
import os


def save_report(report):

    os.makedirs("outputs", exist_ok=True)

    file_path = "outputs/medical_analysis.txt"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(report)

    print("\nReport saved successfully!")
    print("Location:", file_path)


from input_module import collect_patient_input
from profile_module import generate_profile
from symptom_module import extract_symptoms
from context_module import identify_missing_information
from prompt_module import generate_prompt
from analysis_module import analyze_symptoms
from question_module import generate_followup_questions
from safety_module import assess_medical_attention
from save_module import save_report
from utils import DISCLAIMER, display_heading


patient = None
report = ""
ai_analysis = ""


def analyze_patient():

    global report, ai_analysis

    if patient is None:
        print("Please enter patient information first.")
        return

    print("\nExtracting symptoms using Ollama...")

    symptoms = extract_symptoms(patient["symptoms"])

    if symptoms.startswith("ERROR:"):
        print(symptoms)
        return

    missing = identify_missing_information(patient)

    prompt = generate_prompt(patient, symptoms, missing)

    ai_analysis = analyze_symptoms(prompt)

    if ai_analysis.startswith("ERROR:"):
        print(ai_analysis)
        return

    profile = generate_profile(patient)

    questions = generate_followup_questions(patient)

    safety = assess_medical_attention(patient)

    report = f"""
==================================================
       AI-POWERED MEDICAL SYMPTOM ASSISTANT
==================================================

1. REPORTED SYMPTOMS
{symptoms}

2. PATIENT INFORMATION
{profile}

3. POSSIBLE CONDITIONS AND EXPLANATION
{ai_analysis}

4. MISSING INFORMATION
"""

    if missing:
        for item in missing:
            report += f"- {item}\n"
    else:
        report += "- No missing fields identified.\n"

    report += "\n5. FOLLOW-UP QUESTIONS\n"

    for index, question in enumerate(questions, start=1):
        report += f"{index}. {question}\n"

    report += f"""
6. MEDICAL ATTENTION GUIDANCE
{safety}

7. DISCLAIMER
{DISCLAIMER}

==================================================
END OF REPORT
==================================================
"""

    display_heading("MEDICAL SYMPTOM ANALYSIS")

    print(report)


def main():

    global patient

    while True:

        display_heading("AI MEDICAL SYMPTOM ASSISTANT")

        print("1. Enter Patient Information")
        print("2. Enter Symptoms")
        print("3. Analyze Symptoms")
        print("4. Generate Follow-up Questions")
        print("5. Display Possible Conditions")
        print("6. Display Medical Attention Guidance")
        print("7. Display Disclaimer")
        print("8. Save Report")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            patient = collect_patient_input()

            print("\nPatient information collected successfully!")

        elif choice == "2":

            if patient is None:
                print("Enter patient information first.")
            else:
                patient["symptoms"] = input("Enter new symptoms: ")
                report = ""
                ai_analysis = ""
                print("Symptoms updated successfully!")

        elif choice == "3":

            analyze_patient()

        elif choice == "4":

            if patient is None:
                print("Enter patient information first.")
            else:
                questions = generate_followup_questions(patient)

                display_heading("FOLLOW-UP QUESTIONS")

                for i, question in enumerate(questions, 1):
                    print(f"{i}. {question}")

        elif choice == "5":

            if not ai_analysis:
                print("Analyze symptoms first.")
            else:
                display_heading("POSSIBLE CONDITIONS")
                print(ai_analysis)

        elif choice == "6":

            if patient is None:
                print("Enter patient information first.")
            else:
                display_heading("MEDICAL ATTENTION GUIDANCE")
                print(assess_medical_attention(patient))

        elif choice == "7":

            display_heading("DISCLAIMER")
            print(DISCLAIMER)

        elif choice == "8":

            if not report:
                print("Generate the analysis first.")
            else:
                save_report(report)

        elif choice == "9":

            print("\nThank you for using Medical Symptom Assistant!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

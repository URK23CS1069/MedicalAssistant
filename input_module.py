
def collect_patient_input():

    print("\n========== PATIENT INFORMATION ==========")

    patient = {}

    patient["age"] = input("Enter Age: ")
    patient["sex"] = input("Enter Sex: ")

    patient["symptoms"] = input("Enter Symptoms: ")
    patient["duration"] = input("Enter Duration: ")
    patient["severity"] = input("Enter Severity (Mild/Moderate/Severe): ")

    patient["history"] = input("Medical History: ")
    patient["medications"] = input("Current Medications: ")
    patient["allergies"] = input("Allergies: ")

    print("\n========== ADDITIONAL INFORMATION ==========")

    patient["temperature"] = input("Measured Temperature (if known): ")
    patient["breathing"] = input("Breathing difficulty (if any): ")
    patient["cough_type"] = input("Cough Type (if applicable): ")
    patient["progression"] = input("Symptoms improving or worsening: ")

    return patient

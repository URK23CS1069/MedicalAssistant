
def identify_missing_information(patient):
    missing = []

    if not patient["temperature"]:
        missing.append("Exact measured body temperature")

    if not patient["breathing"]:
        missing.append("Whether breathing difficulty is present")

    if not patient["progression"]:
        missing.append("Whether symptoms are improving or worsening")

    if not patient["cough_type"]:
        missing.append("Type of cough (dry or productive)")

    return missing

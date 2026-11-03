
def generate_profile(patient):
    profile = f"""
PATIENT PROFILE
Age: {patient['age']}
Sex: {patient['sex']}
Duration: {patient['duration']}
Severity: {patient['severity']}
Medical History: {patient['history']}
Current Medications: {patient['medications']}
Allergies: {patient['allergies']}
"""
    return profile

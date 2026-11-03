
def generate_prompt(patient, symptoms, missing):
    prompt = f"""
You are an educational medical information assistant.

Analyze the following patient information.

PATIENT INFORMATION:
Age: {patient['age']}
Sex: {patient['sex']}
Symptoms: {symptoms}
Duration: {patient['duration']}
Severity: {patient['severity']}
Medical History: {patient['history']}
Medications: {patient['medications']}
Allergies: {patient['allergies']}

MISSING INFORMATION:
{missing}

INSTRUCTIONS:
1. Identify possible conditions associated with
   the reported symptoms.
2. Explain the possible conditions generally.
3. Do not provide a definitive diagnosis.
4. Do not invent patient information.
5. Mention uncertainty and alternative explanations.
6. Generate relevant follow-up questions.
7. Provide cautious professional medical care guidance.
8. Never prescribe medicines or dosages.
9. Do not claim that the patient is safe based on
   incomplete information.
10. Use simple language.

Return the answer using these headings:

POSSIBLE CONDITIONS
EXPLANATION
FOLLOW-UP QUESTIONS
MEDICAL ATTENTION GUIDANCE

This is informational, not a medical diagnosis.
"""
    return prompt

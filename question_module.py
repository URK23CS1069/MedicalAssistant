
def generate_followup_questions(patient):

    questions = []

    if not patient["temperature"]:
        questions.append("What is your measured body temperature?")

    if not patient["breathing"]:
        questions.append("Are you experiencing difficulty breathing?")

    if not patient["cough_type"]:
        questions.append("Is your cough dry or producing mucus?")

    if not patient["progression"]:
        questions.append("Are your symptoms improving or worsening?")

    questions.append("Have you experienced any additional symptoms?")

    return questions

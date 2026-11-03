
def assess_medical_attention(patient):

    text = (
        patient["symptoms"] + " " +
        patient["breathing"] + " " +
        patient["progression"]
    ).lower()

    emergency_signs = [
        "severe difficulty breathing",
        "cannot breathe",
        "blue lips",
        "unconscious",
        "not responding",
        "severe chest pain",
        "sudden confusion"
    ]

    warning_signs = [
        "difficulty breathing",
        "shortness of breath",
        "chest pain",
        "worsening",
        "high fever"
    ]

    if any(sign in text for sign in emergency_signs):
        return (
            "URGENT: These reported symptoms may indicate "
            "a serious problem. Seek emergency medical care "
            "immediately. Do not wait for an AI response."
        )

    if any(sign in text for sign in warning_signs):
        return (
            "CAUTION: Consider prompt professional medical "
            "assessment, particularly if symptoms are worsening."
        )

    return (
        "No listed warning phrase was detected. This does not "
        "establish that symptoms are safe. Seek professional "
        "medical advice if symptoms persist, worsen or concern you."
    )


import requests
import json


def extract_symptoms(text):
    prompt = f"""
    Extract only the symptoms explicitly mentioned
    by the patient from the following text.

    Do not invent symptoms.
    Return a simple bullet list.

    Patient input: {text}
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        },
        timeout=180
    )

    response.raise_for_status()
    return response.json()["response"].strip()

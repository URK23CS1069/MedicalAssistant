
import requests


def analyze_symptoms(prompt):

    print("\nConnecting to Ollama AI...")

    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "llama3.2",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "stream": False
            },
            timeout=300
        )

        response.raise_for_status()

        result = response.json()

        return result["message"]["content"]

    except requests.exceptions.ConnectionError:
        return "ERROR: Ollama is not running. Start Ollama and try again."

    except requests.exceptions.Timeout:
        return "ERROR: AI response timed out. Try again."

    except requests.exceptions.RequestException as error:
        return f"ERROR: Could not generate analysis: {error}"

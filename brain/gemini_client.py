'''
from config import client, MODEL_NAME

def ask_gemini(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"Model Error: {str(e)}"
'''
'''
def ask_gemini(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        print(response)  # DEBUG
        return response.text if response.text else "No text returned"
    except Exception as e:
        return f"Model Error: {str(e)}"
'''

from config import client, MODEL_NAME

def ask_gemini(prompt: str) -> str:
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    print("\n================ RAW MODEL RESPONSE ================")
    print(response)
    print("====================================================\n")

    return response.text if response.text else ""
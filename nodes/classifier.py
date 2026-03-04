from config import client, MODEL_NAME
from pydantic import BaseModel

class Classification(BaseModel):
    intent: str
    confidence: float

def classify_intent(state):
    prompt = f"""
Classify this document into one of: 'contract', 'compliance', 'vendor'.
Document:
{state.content}
"""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": Classification
            }
        )
        
        if response.parsed:
            state.intent = response.parsed.intent
            state.confidence = response.parsed.confidence
        else:
            state.intent = "unknown"
            state.confidence = 0
            state.logs.append("Model failed to return structured data.")

    except Exception as e:
        state.intent = "unknown"
        state.confidence = 0
        state.logs.append(f"Classification error: {str(e)}")

    state.logs.append(f"Intent classified: {state.intent}")
    return state
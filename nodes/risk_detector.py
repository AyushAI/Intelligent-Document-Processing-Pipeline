from brain.gemini_client import ask_gemini

def detect_risk(state):
    prompt = f"Identify legal risks in this document:\n{state.content}"
    state.result["risks"] = ask_gemini(prompt)
    state.logs.append("Risk analyzed")
    return state
from brain.gemini_client import ask_gemini

def summarize(state):
    prompt = f"Summarize this document:\n{state.content}"
    state.result["summary"] = ask_gemini(prompt)
    state.logs.append("Summarized")
    return state
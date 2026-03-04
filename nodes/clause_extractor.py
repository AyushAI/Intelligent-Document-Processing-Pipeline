from brain.gemini_client import ask_gemini

def extract_clauses(state):
    try:
        prompt = f"Extract key legal clauses:\n{state.content}"
        state.result["clauses"] = ask_gemini(prompt)
        state.logs.append("Clauses extracted")
    except Exception:
        state.retries += 1
        if state.retries < 2:
            return extract_clauses(state)
        state.status = "FAILED"
    return state
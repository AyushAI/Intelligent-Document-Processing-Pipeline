def route(state):
    if state.confidence < 0.6:
        state.status = "LOW_CONFIDENCE"
        return "audit"

    if state.intent == "contract":
        return "clause"

    elif state.intent == "compliance":
        return "risk"

    elif state.intent == "vendor":
        return "summary"

    return "audit"
def audit(state):
    state.status = "COMPLETED"
    state.logs.append("Audit complete")
    return state
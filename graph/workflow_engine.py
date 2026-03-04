
from nodes.classifier import classify_intent
from nodes.router import route
from nodes.summarizer import summarize
from nodes.clause_extractor import extract_clauses
from nodes.risk_detector import detect_risk
from nodes.audit_logger import audit

'''
def run_workflow(state):
    state = classify_intent(state)

    next_node = route(state)

    if next_node == "summary":
        state = summarize(state)

    elif next_node == "clause":
        state = extract_clauses(state)

    elif next_node == "risk":
        state = detect_risk(state)

    state = audit(state)

    return state
'''

def run_workflow(state):
    state = classify_intent(state)

    next_node = route(state)
    state.logs.append(f"Routed to: {next_node}")

    if next_node == "summary":
        state = summarize(state)

    elif next_node == "clause":
        state = extract_clauses(state)

    elif next_node == "risk":
        state = detect_risk(state)

    state = audit(state)

    return state
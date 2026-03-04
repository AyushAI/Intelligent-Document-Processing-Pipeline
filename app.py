import streamlit as st
from state.document_state import DocumentState
from graph.workflow_engine import run_workflow
import io

st.set_page_config(
    page_title="Intelligent Document Processing",
    layout="wide",
    page_icon="🧠"
)

st.title("🧠 Intelligent Document Processing Pipeline")
st.caption("Graph-Based Stateful AI Workflow powered by Gemini")

# -----------------------------
# Session Storage
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.header("⚙️ Controls")
    clear_history = st.button("🗑 Clear History")
    if clear_history:
        st.session_state.history = []
        st.success("History cleared")

    st.divider()
    st.info("Upload a document to analyze intent and route intelligently.")

# -----------------------------
# Main Layout
# -----------------------------
col1, col2 = st.columns([2, 1])

with col1:
    uploaded_file = st.file_uploader(
        "📂 Upload Document",
        type=["txt", "pdf"]
    )

    document_text = ""

    if uploaded_file:
        if uploaded_file.type == "text/plain":
            document_text = uploaded_file.read().decode("utf-8")

        elif uploaded_file.type == "application/pdf":
            try:
                import PyPDF2
                pdf_reader = PyPDF2.PdfReader(uploaded_file)
                for page in pdf_reader.pages:
                    document_text += page.extract_text()
            except:
                st.error("Unable to read PDF file.")

        st.text_area("📄 Extracted Document Preview", document_text, height=200)

    process_button = st.button("🚀 Process Document", use_container_width=True)

# -----------------------------
# Processing Section
# -----------------------------
if process_button and document_text.strip() != "":
    with st.spinner("Running Graph Workflow..."):
        state = DocumentState(content=document_text)
        final_state = run_workflow(state)
        st.session_state.history.append(final_state)

    st.success("✅ Processing Completed")
    # 🔴 DEBUG BLOCK (temporary)
    st.subheader("🔍 Debug Output")
    st.write("Raw Result Object:")
    st.write(final_state.__dict__)

    # Result Layout
    r1, r2 = st.columns(2)

    with r1:
        st.subheader("📌 Classification Result")
        st.write(f"**Intent:** {final_state.intent}")
        st.write(f"**Status:** {final_state.status}")

        st.write("**Confidence Score:**")
        st.progress(min(final_state.confidence, 1.0))

    with r2:
        st.subheader("🧭 Routing & Logs")
        for log in final_state.logs:
            st.write("•", log)

    st.divider()

    st.subheader("📊 AI Output")
    if final_state.result:
        st.json(final_state.result)
    else:
        st.warning("No output generated.")

# -----------------------------
# History Section
# -----------------------------
if st.session_state.history:
    st.divider()
    st.subheader("🕒 Previous Runs")

    for i, past_state in enumerate(reversed(st.session_state.history)):
        with st.expander(f"Document Run {len(st.session_state.history)-i}"):
            st.write(f"Intent: {past_state.intent}")
            st.write(f"Confidence: {past_state.confidence}")
            st.write(f"Status: {past_state.status}")
            st.json(past_state.result)

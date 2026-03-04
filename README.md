# 🧠 Intelligent Document Processing Pipeline

A Streamlit-based AI-powered document processing system built using the **latest Google Gemini SDK (`google-genai`)**.

This application classifies uploaded documents and intelligently routes them through a graph-based workflow for clause extraction, risk detection, or summarization.

---

## 🚀 Features

- 📂 Upload `.txt` or `.pdf` documents
- 🧠 AI-powered document classification (Gemini 2.0 Flash)
- 🔀 Graph-based conditional routing
- 📜 Clause extraction (Contracts)
- ⚠️ Risk detection (Compliance Reports)
- 📝 Summarization (Vendor Agreements)
- 📊 Confidence scoring
- 🧾 Structured JSON output
- 🕒 Processing history tracking
- 🧩 Stateful architecture

---

## 🏗️ Architecture Overview

The system follows a **stateful graph workflow**:

```
Document Upload
      ↓
Intent Classifier (Gemini)
      ↓
Router
 ┌──────────────┬───────────────┬───────────────┐
 ↓              ↓               ↓
Clause       Risk           Summary
Extractor    Detector
      ↓
Audit Logger
```

Each step updates a shared `DocumentState` object.

---

## 📁 Project Structure

```
intelligent-doc-pipeline/
│
├── app.py                      # Streamlit UI
├── config.py                   # Gemini client config
├── requirements.txt
│
├── state/
│   └── document_state.py       # Shared state object
│
├── brain/
│   └── gemini_client.py        # Gemini wrapper
│
├── nodes/
│   ├── classifier.py
│   ├── router.py
│   ├── summarizer.py
│   ├── clause_extractor.py
│   ├── risk_detector.py
│   └── audit_logger.py
│
├── graph/
│   └── workflow_engine.py      # Graph controller
│
└── utils/
```

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **Streamlit**
- **Google Gemini (google-genai SDK)**
- **PyPDF2**
- **dotenv**

---

## 🔑 Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/intelligent-doc-pipeline.git
cd intelligent-doc-pipeline
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add Gemini API Key

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_api_key_here
```

Generate API key from:
👉 https://aistudio.google.com/app/apikey

---

### 5️⃣ Run Application

```bash
streamlit run app.py
```

Open browser at:

```
http://localhost:8501
```

---

## 🧠 Model Configuration

The app uses:

```python
MODEL_NAME = "gemini-2.0-flash"
```

Configured via:

```python
from google import genai
client = genai.Client()
```

Structured JSON output is enforced using:

```python
config={"response_mime_type": "application/json"}
```

---

## 📄 Supported Document Types

- `.txt`
- `.pdf`

---

## 🧪 Example Test Documents

You can test with:

- Service Agreement (Contract)
- Annual Compliance Report
- Vendor Supply Agreement

---

## ⚙️ How It Works Internally

### 1️⃣ Classification Node
- Calls Gemini
- Returns structured JSON:
  ```json
  {
    "intent": "contract",
    "confidence": 0.91
  }
  ```

### 2️⃣ Router
- Routes based on intent and confidence threshold

### 3️⃣ Processing Nodes
- Contract → Clause Extraction
- Compliance → Risk Detection
- Vendor → Summarization

### 4️⃣ Audit
- Logs execution trace
- Updates final status

---

## 🧩 Stateful Design

Each document creates a `DocumentState` object containing:

- document_id
- content
- intent
- confidence
- result
- logs
- status
- retries

This ensures traceability and extensibility.

---

## 🐞 Debugging

If AI output does not appear:

1. Ensure correct model:
   ```
   gemini-2.0-flash
   ```

2. Confirm API key works with standalone test.

3. Add debug block in UI:

```python
st.write(final_state.__dict__)
```

4. Restart Streamlit after model change.

---

## 📈 Future Improvements

- Async model calls
- Human-in-the-loop review
- Database persistence
- Role-based access
- Graph visualization
- Docker deployment
- Streamlit Cloud deployment

---

## 🧑‍💻 Author

Ayush Wase  
AI Engineer | Data & ML Developer  

---

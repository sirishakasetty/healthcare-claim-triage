
# 🧠 AI-Powered Healthcare Claim Triage App

This GitHub repository contains an interactive Streamlit app that simulates a smart healthcare claim triage agent. It validates insurance claims based on ICD-10, CPT codes, and medication data, providing automated decisions and LLM-generated explanations.

## 🚀 Features

- 📥 Upload your own triage CSV files (chunk-level & subject-level)
- 📊 Visualize triage outcomes with interactive bar charts
- 🔍 Search by Subject ID and explore decision reasons
- 🧠 Natural language explanation using rules/LLM
- 📅 Timeline view using HADM IDs (if available)
- 🎯 Filter by decision type (Approved / Rejected / Needs Review)

## 📁 File Structure

```
📂 healthcare-claim-triage
├── app.py                           # Streamlit App
├── triage_engine.py                 # Triage logic functions
├── chunk_level_triage.csv           # Example chunk-level results
├── final_subject_level_decision.csv # Example subject-level summary
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

## 📊 Sample Data Format

### `final_subject_level_decision.csv`
| subject_id | Approved | Needs Review | Rejected | final_decision |
|------------|----------|--------------|----------|----------------|
| 10003400   | 0        | 0            | 3        | Rejected       |

### `chunk_level_triage.csv`
| chunk_index | text               | decision  | reason                           |
|-------------|--------------------|-----------|----------------------------------|
| 0           | Subject ID: 100... | Rejected  | No ICD/CPT/drug match found     |

## 🧠 Decision Logic

- ✅ **Approved**: If at least 1 chunk = Approved
- ⚠️ **Needs Review**: If no Approved, but at least 1 = Needs Review
- ❌ **Rejected**: If all chunks are Rejected

## 🌐 How to Run

### 🔧 Local Setup

```bash
git clone https://github.com/<your-username>/healthcare-claim-triage.git
cd healthcare-claim-triage
pip install -r requirements.txt
streamlit run app.py
```

### ☁️ Streamlit Community Cloud (Free)

1. Upload this GitHub repo
2. Go to `app.py` in "Main file"
3. Add `chunk_level_triage.csv` and `final_subject_level_decision.csv` via sidebar
4. Done 🎉

## 📦 Requirements

Install with pip:

```bash
pip install -r requirements.txt
```

## 🚀 Live Demo

Try the app here 👉 [Healthcare Claim Triage App on Streamlit] ( https://healthcare-claim-triage-5o9xbwycfykbcp8j3fsnt3.streamlit.app/ )

> Upload your claim CSVs and interact with the AI agent in real-time!


🧠 Built with LangChain, pandas, and Streamlit  
⚕️ Inspired by real-world medical triage needs

import pandas as pd

# Load triage results from CSV
def load_data():
    chunk_df = pd.read_csv(r"C:\Users\skase1\OneDrive - University of New Haven\Documents\Healthcare claims and prior auth\chunk_level_triage.csv")
    subject_df = pd.read_csv(r"C:\Users\skase1\OneDrive - University of New Haven\Documents\Healthcare claims and prior auth\final_subject_level_decision.csv")  # ✅ Correct CSV!
    return chunk_df, subject_df

# Get triage decision for a subject_id
def get_subject_decision(subject_id, chunk_df):
    subject_chunks = chunk_df[chunk_df['subject_id'] == int(subject_id)]
    if subject_chunks.empty:
        return "Not found", pd.DataFrame()
    decisions = subject_chunks["decision"].value_counts()
    if "Approved" in decisions:
        return "Approved", subject_chunks
    elif "Needs Review" in decisions:
        return "Needs Review", subject_chunks
    else:
        return "Rejected", subject_chunks

# Simple explanation using LLM-style format
def explain_decision(chunks_df):
    reasons = chunks_df["reason"].dropna().unique()
    explanation = "The final decision was based on the following reasons:\n"
    for i, reason in enumerate(reasons, 1):
        explanation += f"{i}. {reason}\n"
    return explanation

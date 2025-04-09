import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from triage_engine import get_subject_decision, explain_decision, load_data

# Page setup
st.set_page_config(page_title="Healthcare Claim Triage App", layout="wide")
st.title("🧠 AI-Powered Healthcare Claim Triage")
st.markdown("Perform claim validation, visualize triage outcomes, and interact with claim decisions.")

# File upload section
st.sidebar.header("📤 Upload New Triage Data")
uploaded_chunks = st.sidebar.file_uploader("Upload Chunk-level CSV", type="csv")
uploaded_summary = st.sidebar.file_uploader("Upload Subject-level Summary CSV", type="csv")

if uploaded_chunks and uploaded_summary:
    chunk_df = pd.read_csv(uploaded_chunks)
    subject_df = pd.read_csv(uploaded_summary)
    st.sidebar.success("✅ New data loaded successfully!")
else:
    chunk_df, subject_df = load_data()

# Sidebar - Subject lookup
st.sidebar.header("🔍 Subject Explorer")
subject_id_input = st.sidebar.text_input("Enter Subject ID (e.g., 10003400):")

# New: Keyword search
st.sidebar.header("🔎 Keyword Search")
keyword_input = st.sidebar.text_input("Search in clinical notes or diagnosis text:")

# Filter bar
filter_option = st.selectbox("🔎 Filter by Decision Type:", ["All", "Approved", "Needs Review", "Rejected"])
if filter_option != "All":
    subject_df = subject_df[subject_df["final_decision"] == filter_option]

# Final triage summary bar chart
st.subheader("📊 Final Triage Summary")
fig, ax = plt.subplots()
subject_df["final_decision"].value_counts().plot(
    kind="bar",
    ax=ax,
    color=["green", "orange", "red"]
)
ax.set_title("Final Subject-Level Triage Decision")
ax.set_ylabel("Number of Subjects")
st.pyplot(fig)

# Subject-level decision viewer
if subject_id_input:
    try:
        decision, subject_chunks = get_subject_decision(int(subject_id_input), chunk_df)
        st.subheader(f"📋 Triage Details for Subject ID: {subject_id_input}")
        st.markdown(f"**Final Decision:** `{decision}`")
        st.dataframe(subject_chunks[["chunk_index", "HADM ID", "text", "decision", "reason"]], use_container_width=True)

        # Timeline View
        with st.expander("📅 View Timeline / HADM Details"):
            st.dataframe(subject_chunks[["chunk_index", "HADM ID", "text"]])

        # Explanation
        if st.button("🤖 Explain this decision"):
            explanation = explain_decision(subject_chunks)
            st.success(explanation)
    except ValueError:
        st.error("❌ Please enter a valid numeric Subject ID")

# Keyword search logic
if keyword_input:
    keyword_chunks = chunk_df[chunk_df["text"].str.contains(keyword_input, case=False, na=False)]
    st.subheader(f"🔍 Chunks Matching: `{keyword_input}`")
    st.write(f"Found {len(keyword_chunks)} matching entries.")
    st.dataframe(keyword_chunks[["subject_id", "chunk_index", "text", "decision", "reason"]], use_container_width=True)

# Optional: Show raw tables
with st.expander("📂 Show Raw Data Tables"):
    st.write("Subject-level Summary")
    st.dataframe(subject_df)
    st.write("Chunk-level Triage")
    st.dataframe(chunk_df)

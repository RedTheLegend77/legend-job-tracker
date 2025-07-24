import streamlit as st
from datetime import datetime
import pandas as pd
import os

# CSV file to store data
DATA_FILE = "job_log.csv"

# App Title
st.title("🛠️ Tech Job Entry - Legend Tracker")

# Form
with st.form("job_form"):
    tech = st.selectbox("Select Tech", ["Shaw", "Cliff"])
    date = st.date_input("Date", value=datetime.today())
    hours = st.number_input("Hours Worked", min_value=0.0, step=0.5)
    address = st.text_input("Job Address")
    job = st.text_input("Job Description")
    parts = st.text_input("Parts/Tools Used (comma separated)")
    return_visit = st.checkbox("Return Visit Needed?")
    submitted = st.form_submit_button("Submit")

    if submitted:
        data = {
            "Date": [date.strftime("%Y-%m-%d")],
            "Tech": [tech],
            "Hours": [hours],
            "Address": [address],
            "Job": [job],
            "Parts": [parts],
            "Return Visit": ["Yes" if return_visit else "No"],
            "Customer Total": [hours * 85],
            f"{tech} Earnings": [hours * (50 if tech == "Shaw" else 30)],
            "Your Profit": [hours * 85 - hours * (50 if tech == "Shaw" else 30)],
        }

        df = pd.DataFrame(data)

        if os.path.exists(DATA_FILE):
            df.to_csv(DATA_FILE, mode="a", index=False, header=False)
        else:
            df.to_csv(DATA_FILE, index=False)

        st.success("✅ Job entry submitted!")

# Show recent entries
if os.path.exists(DATA_FILE):
    st.subheader("📋 Recent Job Logs")
    log_df = pd.read_csv(DATA_FILE)
    st.dataframe(log_df.tail(10))

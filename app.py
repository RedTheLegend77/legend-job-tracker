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
    actual_hours = st.number_input("Actual Time Spent (hours)", min_value=0.0, step=0.25)
    billable_hours = st.number_input("Billable Hours to Customer", min_value=1.0, step=0.25, value=1.0)
    address = st.text_input("Job Address")
    job = st.text_input("Job Description")
    parts = st.text_input("Parts/Tools Used (comma separated)")
    return_visit = st.checkbox("Return Visit Needed?")
    submitted = st.form_submit_button("Submit")

    if submitted:
        tech_rate = 50 if tech == "Shaw" else 30
        customer_total = billable_hours * 85
        tech_earnings = actual_hours * tech_rate
        your_earnings = customer_total - tech_earnings

        data = {
            "Date": [date.strftime("%Y-%m-%d")],
            "Tech": [tech],
            "Actual Hours": [actual_hours],
            "Billable Hours": [billable_hours],
            "Address": [address],
            "Job": [job],
            "Parts": [parts],
            "Return Visit": ["Yes" if return_visit else "No"],
            "Customer Total": [customer_total],
            f"{tech} Earnings": [tech_earnings],
            "Your Profit": [your_earnings],
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

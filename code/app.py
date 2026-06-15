
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
page_title="Support Integrity Auditor",
layout="wide"
)

st.title("🚨 Support Integrity Auditor")

try:

```
audit_df = pd.read_csv("audit_report.csv")

total_tickets = len(audit_df)

total_mismatch = audit_df["mismatch"].sum()

hidden_crisis = (
    audit_df["mismatch_type"]
    .eq("Hidden Crisis")
    .sum()
)

false_alarm = (
    audit_df["mismatch_type"]
    .eq("False Alarm")
    .sum()
)

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Total Tickets",
    total_tickets
)

col2.metric(
    "Mismatches",
    total_mismatch
)

col3.metric(
    "Hidden Crisis",
    hidden_crisis
)

col4.metric(
    "False Alarm",
    false_alarm
)

st.header("Mismatch Type Distribution")

fig1 = px.pie(
    audit_df,
    names="mismatch_type"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.header("Priority Distribution")

fig2 = px.histogram(
    audit_df,
    x="Priority_Level",
    color="mismatch_type",
    barmode="group"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.header("Hidden Crisis Explorer")

hidden = audit_df[
    audit_df["mismatch_type"]
    ==
    "Hidden Crisis"
]

st.dataframe(hidden)

st.header("False Alarm Explorer")

false_alarm_df = audit_df[
    audit_df["mismatch_type"]
    ==
    "False Alarm"
]

st.dataframe(false_alarm_df)


except Exception as e:


st.error(str(e))


# STEP 3: Start Streamlit

!streamlit run app.py &>/content/logs.txt &

# STEP 4: Create Public URL

from pyngrok import ngrok

public_url = ngrok.connect(8501)

print("Dashboard URL:")
print(public_url)

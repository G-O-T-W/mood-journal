import streamlit as st
import plotly.express as px
from functions import get_data

st.title("Mood Journal")

data = get_data()

st.header("Positivity")
fig = px.line(data, x="Date", y="Positivity Score")
st.plotly_chart(fig)

st.header("Negativity")
fig = px.line(data, x="Date", y="Negativity Score")
st.plotly_chart(fig)

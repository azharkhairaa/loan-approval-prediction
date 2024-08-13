import streamlit as st
import eda
import prediction

page = st.sidebar.selectbox("Select Page: ", ("EDA", "Prediction"))

st.sidebar.markdown('---')
st.sidebar.write("Hacktiv8")
st.sidebar.write("Phase 1 - Full Time Data Analytics")
st.sidebar.write("Milestone 2")
st.sidebar.write("RMT 033 - Muhammad Azhar Khaira")

if page == "EDA":
    eda.run()
else:
    prediction.run()
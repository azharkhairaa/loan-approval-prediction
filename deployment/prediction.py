import streamlit as st
import pandas as pd
import joblib

# load model
model = joblib.load("model.pkl")
def run():
    # title
    st.title("Loan Approval Prediction")

    # input fields
    st.header("Enter loan details")
    st.markdown('---')

    # Applicant Profile
    st.subheader("Applicant Profile")
    no_of_dependents = st.number_input("Number of Dependents", min_value=0, max_value=20, value=4)
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["Yes", "No"])
    income_annum = st.number_input("Annual Income", min_value=0, value=2900000)
    st.markdown('---')

    # Applicantion Details
    st.subheader("Applicantion Details")
    loan_amount = st.number_input("Loan Amount", min_value=0, value=11200000)
    loan_term = st.slider("Loan Term (in months)", 0, 30, 2)
    cibil_score = st.number_input("CIBIL Score", min_value=0, max_value=900, value=500)
    st.markdown('---')

    # Applicant Assets
    st.subheader("Applicant Assets")
    residential_assets_value = st.number_input("Residential Assets Value", min_value=0, value=8100000)
    commercial_assets_value = st.number_input("Commercial Assets Value", min_value=0, value=4700000)
    luxury_assets_value = st.number_input("Luxury Assets Value", min_value=0, value=9500000)
    bank_asset_value = st.number_input("Bank Asset Value", min_value=0, value=3100000)
    st.markdown('---')

    # predict button
    if st.button("Predict"):
        # data input
        input_data = pd.DataFrame([{
        'no_of_dependents': no_of_dependents,
        'education': education,
        'self_employed': self_employed,
        'income_annum': income_annum,
        'loan_amount': loan_amount,
        'loan_term': loan_term,
        'cibil_score': cibil_score,
        'residential_assets_value': residential_assets_value,
        'commercial_assets_value': commercial_assets_value,
        'luxury_assets_value': luxury_assets_value,
        'bank_asset_value': bank_asset_value
    }])
        # prediction
        predictions = model.predict(input_data)
        # show prediction
        st.header(f"Prediction Result: {predictions[0]}")

        # show data input
        input_data = input_data.T.reset_index()
        input_data.columns = ["Data", "Input"]
        st.subheader("Data Input")
        st.dataframe(input_data, width=500, height=420)
        
if __name__ == '__main__':
    run()
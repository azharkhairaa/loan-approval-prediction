import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run():
    # title
    st.title("Loan Approval EDA")
    st.markdown("---")

    # dataset
    st.header("Dataset")
    df = pd.read_csv("../loan_approval_dataset.csv")
    st.dataframe(df)

    # selectbox column
    option = st.selectbox("Select Column: ", ("no_of_dependents", "education", "self_employed", "income_annum",
                                             "loan_amount", "loan_term", "cibil_score",
                                             "residential_assets_value", "commercial_assets_value",
                                             "luxury_assets_value"))
    
    # plot based on the selected option
    fig, ax = plt.subplots(figsize=(12, 8))

    if option in ["no_of_dependents", "education", "self_employed", "loan_term"]:
        st.write(f"Barplot of {option.replace("_", " ").title()}")
        # bar plot
        sns.countplot(x=option, data=df, palette=["springgreen", "deepskyblue"], ax=ax)

    elif option in ["income_annum", "loan_amount", "cibil_score", 
                    "residential_assets_value", "commercial_assets_value", "luxury_assets_value"]:
        st.write(f"Histogram of {option.replace("_", " ").title()}")

        # statistics
        mean_value = df[option].mean()
        median_value = df[option].median()
        q1_value = df[option].quantile(0.25)
        q3_value = df[option].quantile(0.75)
        
        # histogram
        sns.histplot(df[option], bins=30, kde=True, color="deepskyblue", ax=ax)
        
        # lines for mean, median, Q1, and Q3
        ax.axvline(mean_value, color="red", linestyle="--", label=f"Mean: {mean_value:.2f}")
        ax.axvline(median_value, color="green", linestyle="--", label=f"Median: {median_value:.2f}")
        ax.axvline(q1_value, color="orange", linestyle="--", label=f"Q1: {q1_value:.2f}")
        ax.axvline(q3_value, color="purple", linestyle="--", label=f"Q3: {q3_value:.2f}")
        
        ax.set_xlabel(option.replace("_", " ").title())
        ax.set_ylabel("Frequency")
        ax.legend()

    # Show plot
    st.pyplot(fig)

if __name__ == "__main__":
    run()
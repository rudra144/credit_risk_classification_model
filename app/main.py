# import streamlit as st
# from prediction_helper import predict  # Ensure this is correctly linked to your prediction_helper.py
# import matplotlib.pyplot as plt
#
# # Set the page configuration and title
# st.set_page_config(page_title="Credit Risk Modelling", page_icon="📊")
# st.title("Credit Risk Modelling")
# st.markdown(
#     "<style>h1{color:blue; text-align: center;}</style>",
#     unsafe_allow_html=True
# )
# st.sidebar.title("Project Details")
# st.sidebar.markdown("""
# - **Project:** Credit Risk Modelling
# - **Model:** Logistic Regression / XGBoost
# - **Purpose:** Predict default probability and credit score
# - **Tech Stack:** Python, Streamlit, Scikit-learn, XGBoost, Mlflow, Optuna
# """)
#
# # Create rows of three columns each
# row1 = st.columns(3)
# row2 = st.columns(3)
# row3 = st.columns(3)
# row4 = st.columns(3)
#
# # Assign inputs to the first row with default values
# with row1[0]:
#     age = st.number_input('Age', min_value=18, step=1, max_value=100, value=28)
# with row1[1]:
#     income = st.number_input('Income', min_value=0, value=1200000)
# with row1[2]:
#     loan_amount = st.number_input('Loan Amount', min_value=0, value=2560000)
#
# # Calculate Loan to Income Ratio and display it
# loan_to_income_ratio = loan_amount / income if income > 0 else 0
# with row2[0]:
#     st.text("Loan to Income Ratio:")
#     st.text(f"{loan_to_income_ratio:.2f}")  # Display as a text field
#
# # Assign inputs to the remaining controls
# with row2[1]:
#     loan_tenure_months = st.number_input('Loan Tenure (months)', min_value=0, step=1, value=36)
# with row2[2]:
#     avg_dpd_per_delinquency = st.number_input('Avg DPD', min_value=0, value=20)
#
# with row3[0]:
#     delinquency_ratio = st.number_input('Delinquency Ratio', min_value=0, max_value=100, step=1, value=30)
# with row3[1]:
#     credit_utilization_ratio = st.number_input('Credit Utilization Ratio', min_value=0, max_value=100, step=1, value=30)
# with row3[2]:
#     num_open_accounts = st.number_input('Open Loan Accounts', min_value=1, max_value=4, step=1, value=2)
#
#
# with row4[0]:
#     residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'])
# with row4[1]:
#     loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
# with row4[2]:
#     loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])
#
#
# # Button to calculate risk
# if st.button('Calculate Risk'):
#     # Call the predict function from the helper module
#     # print((age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
#     #                                             delinquency_ratio, credit_utilization_ratio, num_open_accounts,
#     #                                             residence_type, loan_purpose, loan_type))
#     probability, credit_score, rating = predict(age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
#                                                 delinquency_ratio, credit_utilization_ratio, num_open_accounts,
#                                                 residence_type, loan_purpose, loan_type)
#
#     # Display the results
#     st.write(f"Deafult Probability: {probability:.2%}")
#     st.write(f"Credit Score: {credit_score}")
#     st.write(f"Rating: {rating}")
#
import streamlit as st
import requests

# Set the page configuration and title
st.set_page_config(page_title="Credit Risk Modelling", page_icon="📊")
st.title("Credit Risk Modelling")

# Apply custom styling for centering the title
st.markdown(
    "<style>h1{color:blue; text-align: center;}</style>",
    unsafe_allow_html=True
)

# Sidebar with project details
st.sidebar.title("Project Details")
st.sidebar.markdown("""
- **Project:** Credit Risk Modelling
- **Model:** Logistic Regression / XGBoost
- **Purpose:** Predict default probability and credit score
- **Tech Stack:** Python, Streamlit, Scikit-learn, XGBoost, Mlflow, Optuna
""")

# Create rows of three columns each for a compact layout
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# Assign inputs to the first row with default values
with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100, value=28)
with row1[1]:
    income = st.number_input('Income', min_value=0, value=1200000)
with row1[2]:
    loan_amount = st.number_input('Loan Amount', min_value=0, value=2560000)

# Calculate Loan to Income Ratio and display it
loan_to_income_ratio = loan_amount / income if income > 0 else 0
with row2[0]:
    st.text("Loan to Income Ratio:")
    st.text(f"{loan_to_income_ratio:.2f}")  # Display as a text field

# Assign inputs to the remaining controls
with row2[1]:
    loan_tenure_months = st.number_input('Loan Tenure (months)', min_value=0, step=1, value=36)
with row2[2]:
    avg_dpd_per_delinquency = st.number_input('Avg DPD', min_value=0, value=20)

with row3[0]:
    delinquency_ratio = st.number_input('Delinquency Ratio', min_value=0, max_value=100, step=1, value=30)
with row3[1]:
    credit_utilization_ratio = st.number_input('Credit Utilization Ratio', min_value=0, max_value=100, step=1, value=30)
with row3[2]:
    num_open_accounts = st.number_input('Open Loan Accounts', min_value=1, max_value=4, step=1, value=2)

with row4[0]:
    residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'])
with row4[1]:
    loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
with row4[2]:
    loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])

# Center the predict button and make API call
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
if st.button("Predict", use_container_width=True):
    payload = {
        "age": age,
        "income": income,
        "loan_amount": loan_amount,
        "loan_tenure_months": loan_tenure_months,
        "avg_dpd_per_delinquency": avg_dpd_per_delinquency,
        "delinquency_ratio": delinquency_ratio,
        "credit_utilization_ratio": credit_utilization_ratio,
        "num_open_accounts": num_open_accounts,
        "residence_type": residence_type,
        "loan_purpose": loan_purpose,
        "loan_type": loan_type
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=payload)

    if response.status_code == 200:
        result = response.json()
        st.success(f"**Credit Score:** {result['credit_score']}")
        st.info(f"**Default Probability:** {result['default_probability']:.2%}")
        st.warning(f"**Risk Rating:** {result['rating']}")
    else:
        st.error("Error connecting to the backend API.")
st.markdown("</div>", unsafe_allow_html=True)

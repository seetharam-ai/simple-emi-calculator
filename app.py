import streamlit as st


# EMI Calculation Function
# --------------------------------------
def calculate_emi(principal, annual_rate, months):
    monthly_rate = annual_rate / 12 / 100

    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / (
        (1 + monthly_rate) ** months - 1
    )

    return emi


# --------------------------------------
# Page Config
# --------------------------------------
st.set_page_config(page_title="Loan EMI Calculator", page_icon="💰", layout="centered")


# --------------------------------------
# Title
# --------------------------------------
st.title("💰 Loan EMI Calculator")
st.write("Calculate your monthly EMI instantly")


# --------------------------------------
# Inputs
# --------------------------------------
loan_amount = st.number_input(
    "Loan Amount", min_value=1000.0, value=500000.0, step=1000.0
)

interest_rate = st.number_input(
    "Annual Interest Rate (%)", min_value=0.1, value=8.5, step=0.1
)

loan_type = st.radio("Loan Tenure Type", ["Years", "Months"])

if loan_type == "Years":
    tenure = st.number_input("Loan Tenure (Years)", min_value=1, value=5)
    months = tenure * 12

else:
    months = st.number_input("Loan Tenure (Months)", min_value=1, value=60)


# --------------------------------------
# Calculate Button
# --------------------------------------
if st.button("Calculate EMI"):
    emi = calculate_emi(loan_amount, interest_rate, months)

    total_payment = emi * months
    total_interest = total_payment - loan_amount

    # Results
    st.success("Calculation Complete")

    st.subheader("📊 Loan Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric("Monthly EMI", f"₹ {emi:,.2f}")

    col2.metric("Total Payment", f"₹ {total_payment:,.2f}")

    col3.metric("Total Interest", f"₹ {total_interest:,.2f}")

    # Extra Details
    st.write("---")
    st.write(f"**Loan Amount:** ₹ {loan_amount:,.2f}")
    st.write(f"**Interest Rate:** {interest_rate}%")
    st.write(f"**Loan Tenure:** {months} months")

import streamlit as st

st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚖️",
    layout="centered"
)

st.title("⚖️ BMI Calculator")
st.write("Calculate your Body Mass Index using your height and weight.")

st.divider()

weight = st.number_input(
    "Enter your weight (kg)",
    min_value=0.1,
    value=60.0,
    step=0.1
)

height = st.number_input(
    "Enter your height (meters)",
    min_value=0.1,
    value=1.70,
    step=0.01
)

if st.button("Calculate BMI", type="primary"):

    bmi = weight / (height ** 2)
    bmi = round(bmi, 2)

    st.subheader("Your BMI Result")

    st.metric("BMI", bmi)

    if bmi < 18.5:
        category = "Underweight"
        st.warning(f"Category: {category}")

    elif bmi < 25:
        category = "Normal Weight"
        st.success(f"Category: {category}")

    elif bmi < 30:
        category = "Overweight"
        st.warning(f"Category: {category}")

    else:
        category = "Obese"
        st.error(f"Category: {category}")

    st.info(
        "BMI is a general screening measure and does not account for "
        "all individual health factors."
    )
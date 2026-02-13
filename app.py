import streamlit as st

st.set_page_config(page_title="3% Hypertonic Saline Calculator", layout="centered")

st.title("Advanced 3% Hypertonic Saline Calculator")
st.caption("Educational Use Only – Not for direct clinical decision-making")

weight = st.number_input("Weight (kg)", min_value=1.0)
sex = st.selectbox("Sex", ["Male", "Female"])
initial_na = st.number_input("Current Serum Sodium (mEq/L)")
desired_na = st.number_input("Target Sodium (mEq/L)")
urine_na = st.number_input("Urine Sodium (mEq/L)")
urine_flow = st.number_input("Urine Flow Rate (L/hr)")
max_correction = st.number_input("Max 24h Correction (mEq/L)", value=8.0)

if st.button("Calculate"):

    tbw = 0.6 * weight if sex == "Male" else 0.5 * weight
    sodium_infusate = 513  # 3% NaCl in mEq/L

    delta_na_per_liter = (sodium_infusate - initial_na) / (tbw + 1)
    total_needed_change = desired_na - initial_na

    required_volume_liters = total_needed_change / delta_na_per_liter
    required_volume_ml = required_volume_liters * 1000

    sodium_loss_per_hour = urine_na * urine_flow
    sodium_loss_effect = sodium_loss_per_hour / tbw

    infusion_rate_ml_hr = required_volume_ml / 24

    st.subheader("Results")
    st.write(f"Total Body Water (TBW): {tbw:.2f} L")
    st.write(f"Predicted Na rise per 1L: {delta_na_per_liter:.2f} mEq/L")
    st.write(f"Total Na increase needed: {total_needed_change:.2f} mEq/L")
    st.write(f"Required 3% Saline Volume: {required_volume_ml:.2f} mL")
    st.write(f"Suggested 24h Infusion Rate: {infusion_rate_ml_hr:.2f} mL/hr")
    st.write(f"Estimated Na loss per hour: {sodium_loss_effect:.3f} mEq/L/hr")

    if total_needed_change > max_correction:
        st.error("WARNING: Target exceeds safe 24h correction limit.")
        st.warning("Risk of Osmotic Demyelination Syndrome.")

    st.info("For acute cerebral edema: 100 mL bolus over 10 minutes. Recheck sodium in 2–4 hours.")

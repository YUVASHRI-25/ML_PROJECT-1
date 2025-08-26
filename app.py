import streamlit as st
import numpy as np
import pickle

st.set_page_config(page_title="Student Exam Predictor", page_icon="📘")

# --- Load model and scaler ---
try:
    with open("model.pkl", "rb") as fp:
        model = pickle.load(fp)
    with open("scaler.pkl", "rb") as fp:
        scaler = pickle.load(fp)
except Exception as e:
    st.error(f"❌ Error loading model/scaler: {e}")
    st.stop()

# --- UI ---
st.title("📘 Student Exam Pass/Fail Predictor")
st.markdown("Fill in the details below to check if the student is likely to **Pass or Fail** the exam.")

col1, col2, col3 = st.columns(3)

with col1:
    hours_studied = st.number_input("📖 Hours Studied", min_value=0.0, max_value=12.0, value=5.0)

with col2:
    sleep_hours = st.number_input("😴 Sleep Hours", min_value=0.0, max_value=12.0, value=7.0)

with col3:
    class_attendance = st.number_input("🏫 Class Attendance (%)", min_value=0.0, max_value=100.0, value=75.0, step=1.0)

st.info("👆 Enter values above and click **Predict Result**")

# --- Prediction ---
if st.button("🔮 Predict Result"):
    features = np.array([[hours_studied, sleep_hours, class_attendance]])

    try:
        # Scale features before prediction
        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)[0]

        st.markdown("---")
        if prediction == 1:
            st.success("✅ Student is likely to **PASS!** 🎉")
        else:
            st.error("❌ Student is likely to **FAIL.** 📉")
    except Exception as e:
        st.error(f"⚠️ Error during prediction: {e}")

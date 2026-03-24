import streamlit as st

st.set_page_config(page_title="Character Confusion Demo", layout="centered")

st.title("User-Specific Character Confusion Detection")
st.caption("Prototype application for handwritten character confusion detection")

# 1. user 먼저 정의
user = st.selectbox("Choose User", ["User A", "User B", "User C"])

if user == "User A":
    default_threshold = 0.15
elif user == "User B":
    default_threshold = 0.25
else:
    default_threshold = 0.30

st.write(f"Default threshold: {default_threshold:.2f}")

# 2. confusion case 선택
case = st.selectbox("Choose confusion case", ["2 vs z", "1 vs l", "0 vs o"])

# 3. 이미지 업로드
uploaded_file = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])

if case == "2 vs z":
    label1, prob1 = "2", 0.55
    label2, prob2 = "z", 0.45
elif case == "1 vs l":
    label1, prob1 = "1", 0.52
    label2, prob2 = "l", 0.48
else:
    label1, prob1 = "0", 0.60
    label2, prob2 = "o", 0.40

threshold = st.slider("Set threshold", 0.0, 1.0, float(default_threshold), 0.01)

difference = prob1 - prob2

st.write(f"Top 1: {label1} ({prob1:.2f})")
st.write(f"Top 2: {label2} ({prob2:.2f})")
st.write(f"Difference: {difference:.2f}")
st.write(f"Threshold: {threshold:.2f}")

if difference < threshold:
    st.warning(f"Confusion detected: {label1} ↔ {label2}")
else:
    st.success(f"Clear prediction: {label1}")

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", width=200)

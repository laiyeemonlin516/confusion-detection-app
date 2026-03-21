import streamlit as st

st.set_page_config(page_title="Character Confusion Demo", layout="centered")

st.title("User-Specific Character Confusion Similarity Analysis")
st.caption("Prototype application for handwritten character confusion detection")

st.markdown("### 1. User Selection")
user = st.selectbox(
    "Choose User",
    ["User A", "User B", "User C"]
)

if user == "User A":
    default_threshold = 0.15
elif user == "User B":
    default_threshold = 0.25
else:
    default_threshold = 0.30

st.write(f"Default threshold for {user}: **{default_threshold:.2f}**")

st.markdown("### 2. Confusion Case Selection")
case = st.selectbox(
    "Choose a confusion example",
    ["2 vs z", "1 vs l", "0 vs o"]
)

st.markdown("### 3. Image Input")
uploaded_file = st.file_uploader(
    "Upload a handwritten image",
    type=["png", "jpg", "jpeg"]
)

st.markdown("### 4. System Flow")
st.code(
    "Image Input → Model Output → Probability Difference → Threshold Decision → Warning",
    language="text"
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", width=220)

    st.markdown("### 5. Model Output (Simulation)")
    if case == "2 vs z":
        label1 = "2"
        prob1 = 0.55
        label2 = "z"
        prob2 = 0.45
    elif case == "1 vs l":
        label1 = "1"
        prob1 = 0.52
        label2 = "l"
        prob2 = 0.48
         else:
        label1 = "0"
        prob1 = 0.60
        label2 = "o"
        prob2 = 0.40

    st.write("This part simulates model probabilities for the selected confusion case.")

    st.markdown("### 6. Threshold Setting")
    threshold = st.slider(
        "Set threshold",
        min_value=0.0,
        max_value=1.0,
        value=float(default_threshold),
        step=0.01
    )

    difference = prob1 - prob2

    st.markdown("### 7. Result")
    st.write(f"Top 1: **{label1} ({prob1:.2f})**")
    st.write(f"Top 2: **{label2} ({prob2:.2f})**")
    st.write(f"Difference: **{difference:.2f}**")
    st.write(f"Threshold: **{threshold:.2f}**")

    st.markdown("### 8. Confusion Definition")
    st.latex(r"\text{confusion} = (top1 - top2 < threshold)")

    if difference < threshold:
        st.warning(f"Confusion detected: {label1} ↔ {label2}")
    else:
        st.success(f"Clear prediction: {label1}")

else:
    st.info("Please upload an image to start.")    


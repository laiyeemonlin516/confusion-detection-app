import streamlit as st
from PIL import Image
import random

st.set_page_config(page_title="Character Confusion Demo", layout="centered")

st.title("Handwritten Character Confusion Detection")
st.caption("Upload image → prediction → gap → threshold highlight")

def fake_model_prediction():
    classes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    probs = [random.random() for _ in classes]
    total = sum(probs)
    probs = [p / total for p in probs]
    return dict(zip(classes, probs))

uploaded_file = st.file_uploader(
    "Upload a handwritten image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=250)
    st.write(f"Image size: {image.size}")

    prediction = fake_model_prediction()
    sorted_pred = sorted(prediction.items(), key=lambda x: x[1], reverse=True)

    top1 = sorted_pred[0]
    top2 = sorted_pred[1]
    gap = top1[1] - top2[1]

    st.markdown("### Prediction Result")
    st.write(f"Top 1: {top1[0]} ({top1[1]:.2f})")
    st.write(f"Top 2: {top2[0]} ({top2[1]:.2f})")
    st.write(f"Gap: {gap:.2f}")

    threshold = st.slider("Set threshold", 0.0, 1.0, 0.20, 0.01)

    if gap < threshold:
        st.warning(f"Potential confusion detected: {top1[0]} ↔ {top2[0]}")
    else:
        st.success(f"Clear prediction: {top1[0]}")
else:
    st.info("Please upload an image.")

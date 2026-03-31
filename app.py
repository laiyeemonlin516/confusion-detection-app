import streamlit as st
from PIL import Image
import pytesseract

st.set_page_config(page_title="Handwritten Character Confusion Detection", layout="centered")

st.title("Handwritten Character Confusion Detection")
st.caption("Upload handwritten image → OCR → character analysis → confusion detection")

# Tesseract path for your Mac
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

# Confusion pairs
confusion_pairs = {
    "5": ["S", "s"],
    "2": ["Z", "z"],
    "1": ["I", "l"],
    "0": ["O", "o"]
}

uploaded_file = st.file_uploader(
    "Upload a handwritten image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", width=300)
    st.write(f"Image size: {image.size}")

    # OCR
    text = pytesseract.image_to_string(image)

    st.markdown("### OCR Extracted Text")
    if text.strip():
        st.text(text)
    else:
        st.warning("No text was extracted from the image.")

    # Character analysis
    chars = list(text.replace(" ", "").replace("\n", ""))

    st.markdown("### Character Analysis")
    if chars:
        st.write(chars)
    else:
        st.info("No characters available for analysis.")

    # Threshold
    threshold = st.slider("Set threshold", 0.0, 1.0, 0.20, 0.01)

    st.markdown("### Confusion Detection Result")

    found_confusion = False

    for char in chars:
        if char in confusion_pairs:
            found_confusion = True

            # simple simulated confidence for presentation/demo logic
            top1_prob = 0.55
            top2_prob = 0.45
            gap = top1_prob - top2_prob

            st.write(f"Character: {char}")
            st.write(f"Top 1: {char} ({top1_prob:.2f})")
            st.write(f"Top 2: {confusion_pairs[char][0]} ({top2_prob:.2f})")
            st.write(f"Gap: {gap:.2f}")

            if gap < threshold:
                st.warning(f"Potential confusion detected: {char} ↔ {confusion_pairs[char][0]}")
            else:
                st.success(f"Clear prediction: {char}")

    if not found_confusion:
        st.success("No predefined confusing characters were detected in the extracted text.")

else:
    st.info("Please upload an image.")

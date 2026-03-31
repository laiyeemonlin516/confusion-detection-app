import streamlit as st
from PIL import Image, ImageDraw
import pytesseract

st.set_page_config(page_title="Handwritten Character Confusion Detection", layout="centered")

st.title("Handwritten Character Confusion Detection")
st.caption("Upload image → OCR → detect confusing characters → highlight on image")

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

# confusion characters
confusion_map = {
    "0": ["O", "o"],
    "O": ["0"],
    "o": ["0"],
    "1": ["I", "l"],
    "I": ["1", "l"],
    "l": ["1", "I"],
    "2": ["Z", "z"],
    "Z": ["2"],
    "z": ["2"],
    "5": ["S", "s"],
    "S": ["5"],
    "s": ["5"]
}

uploaded_file = st.file_uploader(
    "Upload a handwritten image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.markdown("### Original Image")
    st.image(image, caption="Uploaded Image", width=350)

    # OCR text
    extracted_text = pytesseract.image_to_string(image)

    st.markdown("### OCR Extracted Text")
    if extracted_text.strip():
        st.text(extracted_text)
    else:
        st.warning("No text was extracted from the image.")

    # OCR data with boxes
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

    draw = ImageDraw.Draw(image)
    found_items = []

    n = len(data["text"])

    for i in range(n):
        word = data["text"][i].strip()

        if not word:
            continue

        # confidence check
        conf_value = data["conf"][i]
        try:
            conf_value = float(conf_value)
        except:
            conf_value = -1

        # check if word contains confusing character
        suspicious_chars = []
        for ch in word:
            if ch in confusion_map:
                suspicious_chars.append(ch)

        if suspicious_chars:
            x = data["left"][i]
            y = data["top"][i]
            w = data["width"][i]
            h = data["height"][i]

            # draw rectangle
            draw.rectangle([x, y, x + w, y + h], outline="red", width=3)

            found_items.append({
                "word": word,
                "chars": suspicious_chars,
                "conf": conf_value,
                "box": (x, y, w, h)
            })

    st.markdown("### Highlighted Result")
    st.image(image, caption="Highlighted Image", width=350)

    st.markdown("### Confusion Detection Report")
    if found_items:
        for item in found_items:
            st.warning(
                f"Word: '{item['word']}' | "
                f"Possible confusing character(s): {', '.join(item['chars'])} | "
                f"OCR confidence: {item['conf']}"
            )
    else:
        st.success("No predefined confusing characters were detected.")

else:
    st.info("Please upload an image.")



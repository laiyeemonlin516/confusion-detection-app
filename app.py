import streamlit as st

# 페이지 설정
st.set_page_config(page_title="Character Confusion Demo", layout="centered")

# 제목
st.title("Handwritten Character Confusion Detection")
st.caption("Input target character → confusion probability → gap → threshold highlight")

# 1. 대상 문자 입력
st.markdown("### 1. Enter Target Character")
target_char = st.text_input(
    "Enter a target character (example: 2, 1, 0)",
    key="input_char"
)

# 2. threshold 설정
st.markdown("### 2. Set Threshold")
threshold = st.slider("Set threshold", 0.0, 1.0, 0.20, 0.01)

# 입력이 있을 때만 실행
if target_char:
    target_char = target_char.strip()

    st.write(f"Input character: **{target_char}**")
    st.write("The system calculates possible confusion pair probabilities for the input character.")

    # 3. 혼동쌍 확률 계산 (simulation)
    if target_char == "2":
        label1, prob1 = "2", 0.55
        label2, prob2 = "z", 0.45
    elif target_char == "1":
        label1, prob1 = "1", 0.52
        label2, prob2 = "l", 0.48
    elif target_char == "0":
        label1, prob1 = "0", 0.60
        label2, prob2 = "o", 0.40
    else:
        label1, prob1 = target_char, 0.90
        label2, prob2 = "unknown", 0.10

    # 4. gap 계산
    gap = prob1 - prob2

    st.markdown("### 3. Confusion Pair Probabilities")
    st.write(f"Top 1: **{label1} ({prob1:.2f})**")
    st.write(f"Top 2: **{label2} ({prob2:.2f})**")

    st.markdown("### 4. Gap Calculation")
    st.write(f"Gap = **{gap:.2f}**")
    st.progress(prob1)

if gap < threshold:
    st.write("⚠️ The probabilities are too close → high confusion risk")
else:
    st.write("✅ The probabilities are clearly separated → low confusion risk")

    # 5. threshold 기반 하이라이트
    st.markdown("### 5. Threshold-based Highlight")
    if gap < threshold:
        st.warning(f"⚠️ Potential confusion detected: {label1} ↔ {label2}")
    else:
        st.success(f"✅ Clear prediction: {label1}")

else:
    st.info("Please enter a target character.")


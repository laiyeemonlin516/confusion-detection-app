# Handwritten Character Confusion Detection

## Project Goal
This project aims to detect potentially confusing handwritten characters from handwritten images.

## Streamlit Prototype
The current Streamlit app demonstrates:
- image upload
- simulated prediction result
- gap calculation
- threshold-based confusion warning

## Jupyter OCR Experiment
A separate Jupyter notebook was used to:
- load handwritten images
- extract text using OCR
- analyze characters one by one
- detect possible confusion pairs

## Current Limitation
The Streamlit app currently uses simulated prediction probabilities.
The Jupyter notebook demonstrates OCR-based character extraction and confusion analysis.

## Future Work
- connect OCR output to the Streamlit app
- improve recognition accuracy
- detect confusing characters directly from uploaded handwritten images

## Run
```bash
streamlit run app.py

---

# 7. GitHub에 올리는 가장 쉬운 방법

## 새 저장소 만들기
GitHub 들어가서:

- `New repository`
- 이름: `handwritten-confusion-detection`
- Public
- `Create repository`

## 파일 업로드
저장소 안에서:

- `Add file`
- `Upload files`

업로드할 것:
- `app.py`
- `README.md`

그다음:
- `Commit changes`

---

# 8. GitHub에 올리는 순서 아주 쉽게

1. GitHub 로그인
2. 새 repository 만들기
3. `Add file` 클릭
4. `Upload files` 클릭
5. `app.py` 드래그
6. `README.md` 드래그
7. 아래 `Commit changes` 클릭

끝.

---

# 9. 팀원에게 보낼 메시지

한국어로는 이렇게 보내면 돼.

:::writing{variant="chat_message" id="42183"}
제가 Streamlit 앱 안정적으로 실행되는 버전으로 `app.py`를 정리했고, GitHub에 `app.py`와 `README.md`까지 업로드할 예정입니다.  
현재 앱은 이미지 업로드 후 simulated prediction, gap calculation, threshold 기반 confusion warning까지 동작합니다.  
Jupyter에서는 OCR 기반 실험도 따로 진행했습니다.
:::

영어로 보내고 싶으면:

:::writing{variant="chat_message" id="42184"}
I organized a stable version of the Streamlit app in `app.py`, and I am uploading both `app.py` and `README.md` to GitHub.  
The current app supports image upload, simulated prediction, gap calculation, and threshold-based confusion warning.  
I also conducted a separate OCR experiment in Jupyter.
:::

---

# 10. 지금 네가 해야 할 것만 다시 정리

지금 바로 할 일:

1. `app.py` 전체를 내가 준 최종 코드로 바꾸기
2. 저장
3. 터미널에서 `streamlit run app.py`
4. 앱 실행 확인
5. `README.md` 만들기
6. GitHub에 `app.py`와 `README.md` 업로드

---

# 11. 네가 나한테 다음으로 보내면 좋은 것

앱 실행 화면 캡처 한 장이랑 GitHub 업로드 화면 한 장 보내주면, 내가 마지막으로 확인해줄게.

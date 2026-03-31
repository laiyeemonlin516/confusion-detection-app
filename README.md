# Handwritten Character Confusion Detection

## Project Goal
This project aims to detect potentially confusing handwritten characters from handwritten images.

## Current Pipeline
1. Upload handwritten image
2. Extract text using OCR
3. Analyze characters one by one
4. Detect potentially confusing character pairs
5. Display warning results

## Streamlit App
The current Streamlit app supports:
- image upload
- OCR-based text extraction
- character analysis
- confusion detection
- threshold-based warning display

## Confusion Pairs
The current prototype checks character pairs such as:
- 5 ↔ S
- 2 ↔ Z
- 1 ↔ I / l
- 0 ↔ O / o

## Current Limitation
The OCR stage is real, but the probability values for confusion detection are currently simulated for demonstration.

## Future Work
- connect real model prediction probabilities
- improve OCR accuracy
- detect all confusing characters directly from handwritten images
- integrate full model pipeline into the app

## Run
```bash
streamlit run app.py


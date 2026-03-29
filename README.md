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


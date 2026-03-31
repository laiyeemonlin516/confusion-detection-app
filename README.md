# Handwritten Character Confusion Detection

## Project Goal
This project aims to detect potentially confusing handwritten characters from handwritten images.

## Current Application
The current application supports:
- handwritten image upload
- OCR-based text extraction
- OCR bounding box extraction
- detection of suspicious characters
highlighting suspicious regions on the original image
- warning message display

## Current Pipeline
image upload
→ OCR
→ suspicious character detection
→ image highlight
→ warning output

## Confusion Character Rules
The current version checks predefined confusing characters such as:
- 0 ↔ O / o
- 1 ↔ I / l
- 2 ↔ Z / z
- 5 ↔ S / s

## Current Status
The application currently implements OCR-based real detection and visualization.
The next step is to connect teammate classifiers (n_h, 2_z) for real probability and gap-based confusion detection.

## Future Work
- connect crop_metadata and pair_model routing
- connect real classifier probability outputs
- calculate gap using classifier outputs
- apply threshold-based final confusion judgment

## Run
```bash
streamlit run app.py



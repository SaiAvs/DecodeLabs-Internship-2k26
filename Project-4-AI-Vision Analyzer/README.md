# 🤖 AI Vision Analyzer

AI Vision Analyzer is a simple image-to-text application built using
Python, OpenCV, Tesseract OCR, and Streamlit.

The application allows users to upload an image, preprocess it,
detect text, extract the recognized content, display OCR confidence,
and download the extracted text.

---

## ✨ Features

- 📤 Upload PNG, JPG, and JPEG images
- 🖼️ Preview the uploaded image
- ⚙️ Convert images to grayscale
- 🔲 Apply adaptive thresholding
- 🤖 Extract text using Tesseract OCR
- 🔎 Detect text regions using bounding boxes
- 📊 Calculate OCR confidence
- 📝 Display extracted text
- 📥 Download extracted text as a TXT file
- 🎯 Display a recognition summary
- 🌐 Simple Streamlit web interface

---

## 🛠️ Technologies Used

- Python
- Streamlit
- OpenCV
- Tesseract OCR
- Pytesseract
- NumPy
- Pillow

---

## 🔬 How It Works

The application follows this workflow:

```text
Upload Image
      ↓
Image Conversion
      ↓
Grayscale Processing
      ↓
Adaptive Thresholding
      ↓
Tesseract OCR
      ↓
Text Detection
      ↓
Confidence Calculation
      ↓
Bounding Boxes
      ↓
Extracted Text
      ↓
Download Result

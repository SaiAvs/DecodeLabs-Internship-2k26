import cv2
import pytesseract

# =====================================================
# TESSERACT CONFIGURATION
# =====================================================

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# =====================================================
# LOAD IMAGE
# =====================================================

image = cv2.imread("sample.png")

if image is None:
    print("❌ Image not found. Make sure sample.png is in the same folder.")
    exit()

print("✅ Image loaded successfully.")

# =====================================================
# IMAGE PREPROCESSING
# =====================================================

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print("✅ Grayscale conversion completed.")

# Apply adaptive thresholding
processed = cv2.adaptiveThreshold(
    gray,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)

print("✅ Adaptive thresholding completed.")

# =====================================================
# OCR
# =====================================================

text = pytesseract.image_to_string(
    processed,
    config="--psm 6"
)

# =====================================================
# DISPLAY RESULT
# =====================================================

print("\n" + "=" * 50)
print("📝 EXTRACTED TEXT")
print("=" * 50)

if text.strip():
    print(text)
else:
    print("⚠️ No text detected.")

print("=" * 50)
print("🤖 OCR processing completed!")
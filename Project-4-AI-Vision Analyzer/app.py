import streamlit as st
import cv2
import pytesseract
import numpy as np
from PIL import Image


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="AI Vision Analyzer",
    page_icon="🤖",
    layout="wide"
)


# =====================================================
# TESSERACT CONFIGURATION
# =====================================================

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown(
    """
    <style>

    /* MAIN APP */

    .stApp {
        background:
        radial-gradient(
            circle at top left,
            rgba(124, 58, 237, 0.15),
            transparent 35%
        ),
        radial-gradient(
            circle at bottom right,
            rgba(6, 182, 212, 0.12),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #0f172a,
            #111827,
            #1e1b4b
        );

        color: white;
    }


    /* HEADINGS */

    h1, h2, h3, h4, h5, h6 {
        color: white !important;
    }


    /* NORMAL TEXT */

    p, label, span {
        color: #e5e7eb;
    }


    /* FILE UPLOADER */

    section[data-testid="stFileUploader"] {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 16px;
        padding: 15px;
    }


    section[data-testid="stFileUploader"] label {
        color: white !important;
        font-weight: 600;
    }


    section[data-testid="stFileUploader"] small {
        color: #cbd5e1 !important;
    }


    section[data-testid="stFileUploader"] button {
        color: #111827 !important;
        background: white !important;
        border-radius: 10px;
        font-weight: 600;
    }


    /* TITLE */

    .main-title {
        text-align: center;
        font-size: 48px;
        font-weight: 800;
        margin-bottom: 5px;

        background:
        linear-gradient(
            90deg,
            #a78bfa,
            #f472b6,
            #22d3ee
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }


    /* SUBTITLE */

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #cbd5e1 !important;
        margin-bottom: 30px;
    }


    /* TEXT AREA */

    textarea {
        color: white !important;
        background: #111827 !important;
    }


    /* METRICS */

    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.10);
        border-radius: 16px;
        padding: 15px;
    }


    /* FOOTER */

    .custom-footer {
        text-align: center;
        padding: 20px;
        margin-top: 25px;
        color: #cbd5e1;
        font-size: 14px;
        border-top: 1px solid rgba(255, 255, 255, 0.10);
    }


    </style>
    """,
    unsafe_allow_html=True
)


# =====================================================
# HEADER
# =====================================================

st.markdown(
    '<div class="main-title">🤖 AI Vision Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
        Extract text from images using OpenCV and Tesseract OCR
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()


# =====================================================
# IMAGE UPLOAD
# =====================================================

st.subheader("📤 Upload Your Image")

uploaded_file = st.file_uploader(
    "Choose an image containing readable text",
    type=["png", "jpg", "jpeg"]
)


# =====================================================
# MAIN APPLICATION
# =====================================================

if uploaded_file is not None:

    # -------------------------------------------------
    # LOAD IMAGE
    # -------------------------------------------------

    image = Image.open(uploaded_file).convert("RGB")

    image_array = np.array(image)

    st.success("✅ Image uploaded successfully!")


    # -------------------------------------------------
    # ORIGINAL IMAGE
    # -------------------------------------------------

    st.subheader("🖼️ Original Image")

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    st.divider()


    # =================================================
    # IMAGE PREPROCESSING
    # =================================================

    st.subheader("⚙️ Image Preprocessing")


    gray = cv2.cvtColor(
        image_array,
        cv2.COLOR_RGB2GRAY
    )


    processed = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )


    # -------------------------------------------------
    # DISPLAY PREPROCESSING
    # -------------------------------------------------

    col1, col2 = st.columns(2)


    with col1:

        st.image(
            gray,
            caption="Grayscale Image",
            use_container_width=True
        )


    with col2:

        st.image(
            processed,
            caption="Adaptive Threshold",
            use_container_width=True
        )


    st.divider()


    # =================================================
    # OCR
    # =================================================

    st.subheader("🤖 AI Text Recognition")


    ocr_data = pytesseract.image_to_data(
        processed,
        config="--psm 6",
        output_type=pytesseract.Output.DICT
    )


    # =================================================
    # EXTRACT WORDS
    # =================================================

    detected_words = []

    confidence_values = []


    for i in range(len(ocr_data["text"])):

        word = str(
            ocr_data["text"][i]
        ).strip()


        try:

            confidence = float(
                ocr_data["conf"][i]
            )

        except (ValueError, TypeError):

            confidence = -1.0


        if word != "" and confidence >= 0:

            detected_words.append(word)

            confidence_values.append(confidence)


    # =================================================
    # EXTRACTED TEXT
    # =================================================

    extracted_text = " ".join(
        detected_words
    )


    # =================================================
    # CONFIDENCE
    # =================================================

    if confidence_values:

        average_confidence = (
            sum(confidence_values)
            / len(confidence_values)
        )

    else:

        average_confidence = 0.0


    # =================================================
    # BOUNDING BOXES
    # =================================================

    boxed_image = image_array.copy()


    for i in range(len(ocr_data["text"])):

        word = str(
            ocr_data["text"][i]
        ).strip()


        try:

            confidence = float(
                ocr_data["conf"][i]
            )

        except (ValueError, TypeError):

            confidence = -1.0


        if word != "" and confidence >= 0:

            x = int(
                ocr_data["left"][i]
            )

            y = int(
                ocr_data["top"][i]
            )

            width = int(
                ocr_data["width"][i]
            )

            height = int(
                ocr_data["height"][i]
            )


            cv2.rectangle(
                boxed_image,
                (x, y),
                (x + width, y + height),
                (124, 58, 237),
                2
            )


    # =================================================
    # RESULTS
    # =================================================

    if extracted_text.strip():

        st.success(
            "✅ Text detected successfully!"
        )


        # -------------------------------------------------
        # DETECTED REGIONS
        # -------------------------------------------------

        st.subheader(
            "🔎 Detected Text Regions"
        )


        st.image(
            boxed_image,
            caption="Text detected by OCR",
            use_container_width=True
        )


        st.divider()


        # -------------------------------------------------
        # METRICS
        # -------------------------------------------------

        metric1, metric2, metric3 = st.columns(3)


        with metric1:

            st.metric(
                "🤖 OCR Confidence",
                f"{average_confidence:.1f}%"
            )


        with metric2:

            st.metric(
                "📝 Words Detected",
                len(detected_words)
            )


        with metric3:

            if average_confidence >= 80:

                recognition_status = "High Confidence"

            else:

                recognition_status = "Needs Review"


            st.metric(
                "🎯 Recognition",
                recognition_status
            )


        st.divider()


        # -------------------------------------------------
        # EXTRACTED TEXT
        # -------------------------------------------------

        st.subheader(
            "📝 Extracted Text"
        )


        st.text_area(
            "Recognized Content",
            extracted_text,
            height=250
        )


        # -------------------------------------------------
        # DOWNLOAD
        # -------------------------------------------------

        st.download_button(
            label="📥 Download Extracted Text",
            data=extracted_text,
            file_name="extracted_text.txt",
            mime="text/plain"
        )


        st.divider()


        # -------------------------------------------------
        # RECOGNITION SUMMARY
        # -------------------------------------------------

        st.subheader(
            "🔎 Recognition Summary"
        )


        summary1, summary2 = st.columns(2)


        with summary1:

            st.write(
                f"📝 **Words detected:** "
                f"{len(detected_words)}"
            )

            st.write(
                f"📊 **OCR confidence:** "
                f"{average_confidence:.1f}%"
            )


        with summary2:

            st.write(
                "⚙️ **Preprocessing:** "
                "Grayscale + Adaptive Thresholding"
            )

            st.write(
                "🤖 **OCR Engine:** "
                "Tesseract OCR"
            )


    else:

        st.warning(
            "⚠️ No readable text was detected."
        )


# =====================================================
# NO IMAGE MESSAGE
# =====================================================

else:

    st.info(
        "👆 Upload an image above to start OCR processing."
    )


# =====================================================
# FOOTER
# =====================================================

st.markdown(
    """
    <div class="custom-footer">
        🤖 AI Vision Analyzer
        &nbsp;•&nbsp;
        OpenCV
        &nbsp;•&nbsp;
        Tesseract OCR
        &nbsp;•&nbsp;
        Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
import streamlit as st
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

st.set_page_config(
    page_title="AI Classification Model",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Classification Model")
st.subheader("DecodeLabs AI Internship | Week 2")

# ============================================
# LOAD DATASET
# ============================================
iris = load_iris()
X = iris.data
y = iris.target

df = pd.DataFrame(
    X,
    columns=iris.feature_names
)
df["Species"] = y

# ============================================
# SHOW DATASET
# ============================================
st.header("📊 Iris Dataset")
st.write("First 10 Rows")
st.dataframe(df.head(10), use_container_width=True)
st.subheader("Dataset Information")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Rows", df.shape[0])
with col2:
    st.metric("Columns", df.shape[1])
with col3:
    st.metric("Classes", len(iris.target_names))

with st.expander("About the Dataset"):
    st.write("""
The Iris dataset is one of the most famous datasets in Machine Learning.
It contains measurements of iris flowers from three different species.

Features:
• Sepal Length
• Sepal Width
• Petal Length
• Petal Width

Target:
• Setosa
• Versicolor
• Virginica
""")

# =====================================================
# TRAIN TEST SPLIT
# =====================================================

st.header("🧠 Model Training")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

st.success("✅ Dataset Split Successfully")

col1, col2 = st.columns(2)

with col1:
    st.metric("Training Samples", len(X_train))

with col2:
    st.metric("Testing Samples", len(X_test))


# =====================================================
# DECISION TREE MODEL
# =====================================================

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)


# =====================================================
# MODEL PERFORMANCE
# =====================================================

st.header("📈 Model Performance")

st.metric(
    label="Accuracy",
    value=f"{accuracy * 100:.2f}%"
)

if accuracy >= 0.95:
    st.success("🎉 Excellent! The model is performing very well.")

elif accuracy >= 0.80:
    st.info("👍 Good! The model has achieved satisfactory accuracy.")

else:
    st.warning("⚠️ The model accuracy is low.")


# =====================================================
# SAMPLE PREDICTIONS
# =====================================================

st.subheader("🔍 Sample Predictions")

result_df = pd.DataFrame({
    "Actual Class": y_test,
    "Predicted Class": prediction
})

st.dataframe(result_df.head(10), use_container_width=True)


# =====================================================
# CLASS NAMES
# =====================================================

st.subheader("🌸 Iris Flower Classes")

class_df = pd.DataFrame({
    "Class ID": [0, 1, 2],
    "Flower Name": iris.target_names
})

st.table(class_df)
# ==========================================================
# PHASE 3 : USER INPUT & AI PREDICTION
# ==========================================================

st.divider()

st.header("🌸 Predict Iris Flower Species")

st.write("Enter the flower measurements below.")

col1, col2 = st.columns(2)

with col1:

    sepal_length = st.number_input(
        "Sepal Length (cm)",
        min_value=0.0,
        max_value=10.0,
        value=5.1,
        step=0.1
    )

    sepal_width = st.number_input(
        "Sepal Width (cm)",
        min_value=0.0,
        max_value=10.0,
        value=3.5,
        step=0.1
    )

with col2:

    petal_length = st.number_input(
        "Petal Length (cm)",
        min_value=0.0,
        max_value=10.0,
        value=1.4,
        step=0.1
    )

    petal_width = st.number_input(
        "Petal Width (cm)",
        min_value=0.0,
        max_value=10.0,
        value=0.2,
        step=0.1
    )

st.write("")

if st.button("🔍 Predict Species", use_container_width=True):

    user_data = [[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]]

    prediction = model.predict(user_data)

    predicted_species = iris.target_names[prediction[0]]

    st.success("Prediction Completed Successfully!")

    st.subheader("🤖 Prediction Result")

    st.metric(
        label="Predicted Species",
        value=predicted_species.capitalize()
    )

    probability = model.predict_proba(user_data)[0]

    st.subheader("📊 Prediction Confidence")

    confidence_df = pd.DataFrame({
        "Species": iris.target_names,
        "Probability": probability
    })

    st.dataframe(
        confidence_df,
        use_container_width=True
    )

    st.bar_chart(
        confidence_df.set_index("Species")
    )
# ==========================================================
# PHASE 4 : PREMIUM UI
# ==========================================================

st.divider()

st.header("📈 Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Model",
        value="Decision Tree"
    )

with col2:
    st.metric(
        label="Accuracy",
        value=f"{accuracy * 100:.2f}%"
    )

with col3:
    st.metric(
        label="Dataset",
        value="Iris"
    )

st.divider()

st.header("🌼 Iris Flower Species")

tab1, tab2, tab3 = st.tabs([
    "Setosa",
    "Versicolor",
    "Virginica"
])

with tab1:

    st.success("🌸 Iris Setosa")

    st.write("""
- Small petals
- Easy to classify
- Usually separated from other species
""")

with tab2:

    st.info("🌺 Iris Versicolor")

    st.write("""
- Medium-sized petals
- Intermediate characteristics
- More difficult to classify than Setosa
""")

with tab3:

    st.warning("🌼 Iris Virginica")

    st.write("""
- Large petals
- Largest flower among the three
- Similar to Versicolor in some measurements
""")

st.divider()

st.header("📚 About This Project")

st.info("""
This project demonstrates a Machine Learning Classification Model
built using Python, Streamlit and Scikit-learn.

Workflow:

• Load Dataset

• Data Preprocessing

• Train/Test Split

• Decision Tree Classification

• Prediction

• Accuracy Evaluation

• Interactive User Interface
""")

st.divider()

st.header("🛠️ Technologies Used")

tech1, tech2, tech3, tech4 = st.columns(4)

with tech1:
    st.success("🐍 Python")

with tech2:
    st.success("📊 Pandas")

with tech3:
    st.success("🤖 Scikit-Learn")

with tech4:
    st.success("🎨 Streamlit")
# ==========================================================
# PHASE 5 : DASHBOARD, VISUALIZATIONS & FOOTER
# ==========================================================

st.divider()

st.header("📊 Dataset Visualization")

chart_col1, chart_col2 = st.columns(2)

with chart_col1:

    st.subheader("Feature Distribution")

    feature = st.selectbox(
        "Select Feature",
        iris.feature_names
    )

    st.bar_chart(df[feature])

with chart_col2:

    st.subheader("Species Count")

    species_df = pd.DataFrame({
        "Species": [
            "Setosa",
            "Versicolor",
            "Virginica"
        ],
        "Count": [
            sum(df["Species"] == 0),
            sum(df["Species"] == 1),
            sum(df["Species"] == 2)
        ]
    })

    st.bar_chart(
        species_df.set_index("Species")
    )

# ==========================================================
# DATA PREVIEW
# ==========================================================

st.divider()

st.header("🔍 Complete Dataset")

if st.checkbox("Show Full Dataset"):

    st.dataframe(
        df,
        use_container_width=True
    )

# ==========================================================
# DOWNLOAD DATASET
# ==========================================================

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Dataset",
    data=csv,
    file_name="iris_dataset.csv",
    mime="text/csv"
)

# ==========================================================
# PROJECT SUMMARY
# ==========================================================

st.divider()

st.header("📌 Project Summary")

summary_col1, summary_col2 = st.columns(2)

with summary_col1:

    st.success("""
### Features

✅ Iris Dataset

✅ Data Preview

✅ Train/Test Split

✅ Decision Tree Model

✅ Accuracy Evaluation

✅ Flower Prediction

✅ Interactive Dashboard

✅ Download Dataset
""")

with summary_col2:

    st.info(f"""
### Model Information

Algorithm : Decision Tree

Training Samples : {len(X_train)}

Testing Samples : {len(X_test)}

Accuracy : {accuracy*100:.2f}%

Classes : {len(iris.target_names)}

Features : {len(iris.feature_names)}
""")

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.markdown(
"""
<div style="text-align:center;padding:20px;color:gray;">

<h3>🤖 AI Data Classification Model</h3>

<p>Developed using <b>Python</b>, <b>Streamlit</b> and <b>Scikit-Learn</b></p>

<p>DecodeLabs AI Internship • Week 2 Project</p>

<p>Developed by <b>Saianshi</b></p>

</div>
""",
unsafe_allow_html=True
)
import streamlit as st
import joblib

# Load pipeline
model = joblib.load("randomforest.pkl")

# UI
st.set_page_config(page_title="NLP Classifier", page_icon="🧠")
st.markdown(
    """
    <style>
    /* Main app background */
    .stApp {
        background-color: #000000;
        color: white;
    }

    /* Text area & input */
    textarea, input {
        background-color: #1e1e1e !important;
        color: white !important;
    }

    /* Buttons */
    div.stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        font-weight: bold;
    }

    /* Cursive heading */
    .cursive-title {
        font-family: "Comic Sans MS", "Lucida Handwriting", cursive;
        font-size: 42px;
        text-align: center;
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .cursive-title {
        font-family: "Comic Sans MS", "Lucida Handwriting", cursive;
        font-size: 40px;
        text-align: center;
        color: #4CAF50;
    }
    </style>

    <div class="cursive-title">
        ✨ NLP Text Classification App ✨
    </div>
    """,
    unsafe_allow_html=True
)

st.image("https://d2mk45aasx86xg.cloudfront.net/Natural_Language_Processing_in_action_11zon_be0e4fa306.webp",width=600)

st.markdown(
    """
    <p style="
        text-align: center;
        font-size: 18px;
        font-family: 'Segoe UI', cursive;
        color: #dddddd;
        letter-spacing: 1px;
    ">
        NLP classifier to predict range of human emotions like anger ,joy,sadness,love from text
    </p>
    """,
    unsafe_allow_html=True
)

# Text input
text = st.text_area("✍️ Enter your text", height=150)

# Predict
if st.button("Predict"):
    if text.strip() == "":
        st.warning("Please enter some text")
    else:
        prediction = model.predict([text])
        emotions = ["anger","joy","sadness","love"]
        st.success(f"✅ Prediction: **{emotions[prediction[0]]}**")

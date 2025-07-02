import streamlit as st
import joblib
import base64

# ---- Load Model and Vectorizer ----
vectorizer = joblib.load("C:/Users/dell/Downloads/Fake-News-Detection-main/Fake-News-Detection-main/vectorizer.jb")
model = joblib.load("C:/Users/dell/Downloads/Fake-News-Detection-main/Fake-News-Detection-main/lr_model.jb")

# ---- Custom CSS for Styling ----
def add_custom_css():
    st.markdown(
        """
        <style>
        body {
            background-color: #0e1117;
            color: #ffffff;
        }
        .stTextArea textarea {
            background-color: #1e293b;
            color: #fff;
        }
        .stButton>button {
            background-color: #4f46e5;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #4338ca;
        }
        .result-box {
            background-color: #16a34a;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-size: 18px;
            font-weight: bold;
        }
        .fake-news {
            background-color: #dc2626;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# ---- Add Custom CSS ----
add_custom_css()

# ---- App Title and Description ----
st.markdown("<h1 style='text-align: center; color: #facc15;'>📰 Fake News Detector 🔍</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Enter a News Article below to check whether it is Fake or Real.</p>", unsafe_allow_html=True)

# ---- Input Box for News Article ----
news_article = st.text_area("📝 News Article:", height=150)

# ---- Button to Check News ----
if st.button("Check News", key="check_news_button"):
    if news_article.strip():
        # Transform and predict
        transform_input = vectorizer.transform([news_article])
        prediction = model.predict(transform_input)

    
        if prediction[0] == 1:
            st.markdown("<div class='result-box'>✅ The News is Real!</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='result-box fake-news'>🚨 The News is Fake!</div>", unsafe_allow_html=True)
    else:
        st.warning("Please enter a news article before checking.")

def set_background(image_file):
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# ---- Call Background Function (use your own image path) ----
set_background("p.png")

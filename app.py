import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open('spam.pkl', 'rb'))
cv = pickle.load(open('vectorizer.pkl', 'rb'))

# Page Config
st.set_page_config(page_title="Spam Sense", page_icon="✉️", layout="centered")

# Custom Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
        background-color: #FDF6EC;
        color: #1A1A1A;
    }

    .big-title {
        font-size: 80px !important;
        font-weight: 700;
        margin-bottom: 1rem;
        color: #1C1C1C;
        text-align: center;
    }

    .subheader {
        font-size: 45px !important;
        font-weight: 600;
        color: #1B263B;
        text-align: center;
        margin-bottom: 1rem;
        white-space: nowrap;
    }

    .caption {
        font-size: 30px !important;
        font-weight: 550;
        color: #3B2F2F;
        text-align: center;
        margin-bottom: 2rem;
        white-space: nowrap;
    }

    .markdown-text {
        font-size: 25px !important;
        font-weight: 500;
        color: #2F2F2F;
    }

    label[for="email-content"] {
        font-size: 26px !important;
        font-weight: 600 !important;
        color: #1A1A1A !important;
    }

    textarea, .stTextInput>div>input {
        font-size: 24px !important;
        color: #1A1A1A !important;
        background-color: #F9F9F9 !important;
        border: 1px solid #999 !important;
        padding: 1rem !important;
    }

    textarea::placeholder {
        font-size: 22px !important;
        color: #888888 !important;
    }

    .stButton>button {
        background-color: #1E90FF; /* Dodger Blue */
        color: #FFFFFF;
        border: none;
        padding: 0.8rem 1.6rem;
        font-size: 36px !important;
        border-radius: 10px;
        font-weight: 700;
        transition: all 0.2s ease-in-out;
    }

    .stButton>button:hover {
        background-color: #1C86EE;
        color: #FFFFFF;
        transform: scale(1.03);
    }

    .stMarkdown h3 {
        color: #1A1A1A;
    }

    section[data-testid="stSidebar"] {
        background-color: #FFFFFF;
    }

    section[data-testid="stSidebar"] .markdown-text {
        color: #2F2F2F !important;
        font-size: 25px !important;
        font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="big-title">✉️ Spam Sense</div>', unsafe_allow_html=True)
st.markdown('<div class="caption">A smart and secure way of identifying <strong>Spam</strong> and <strong>Junk emails</strong>.</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Is that email real or a scam? Let\'s find out!</div>', unsafe_allow_html=True)

# Emoji Banner
st.markdown('<div style="text-align:center; font-size:48px;">🛡️📧🧠</div>', unsafe_allow_html=True)
st.markdown("")

# Sidebar
with st.sidebar:
    st.markdown('<h2 style="font-size:34px; font-weight:700; color:#1C1C1C;">ℹ️ About This App</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="markdown-text">
    This app uses a machine learning model trained on spam/ham email data.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="markdown-text">
    <strong>How to use:</strong><br>
    1. Paste an email.<br>
    2. Click 'Analyze'.<br>
    3. Get instant prediction + tips.
    </div>
    """, unsafe_allow_html=True)
    st.write("---")
    st.markdown('<div class="markdown-text">🛡️ Protect your inbox from scams!</div>', unsafe_allow_html=True)

# Input Area
st.markdown('<div class="markdown-text"><strong>📥 Paste Your Email Below</strong></div>', unsafe_allow_html=True)
user_input = st.text_area(
    "Email Content:",
    height=200,
    placeholder="e.g., You've won a prize! Click the link to claim...",
    key="email-content"
)

# Analyze Button
if st.button("🔍 Analyze Email"):
    if user_input.strip():
        st.markdown('<div class="subheader">📢 Prediction</div>', unsafe_allow_html=True)

        # Prediction Logic
        data = [user_input]
        vectorized_data = cv.transform(data).toarray()
        prediction = model.predict(vectorized_data)

        if prediction[0] == 0:
            col1, col2 = st.columns([1, 2])
            with col1:
                st.success("✅ Legitimate Email")
            with col2:
                st.markdown("""
                <div class="markdown-text">
                - This looks fine.<br>
                - Still double-check the sender details.<br>
                - Avoid clicking unexpected links.
                </div>
                """, unsafe_allow_html=True)
        else:
            col1, col2 = st.columns([1, 2])
            with col1:
                st.error("🚫 Spam Email Detected")
            with col2:
                st.markdown("""
                <div class="markdown-text">
                - Do not click on links or open attachments.<br>
                - Report or block the sender.<br>
                - Stay cautious of urgent or financial requests.
                </div>
                """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter email content to analyze.")

# Divider and Tips
st.divider()
st.markdown('<div class="subheader">📌 Email Security Tips</div>', unsafe_allow_html=True)
st.markdown("""
<div class="markdown-text">
🔒 Never share sensitive info over email.<br>
🚫 Watch out for strange links and grammar errors.<br>
✅ Use updated antivirus and spam filters.<br>
🧠 Always think twice before clicking!
</div>
""", unsafe_allow_html=True)

# Bonus Section
st.divider()
st.markdown('<div class="subheader">💡 Did You Know?</div>', unsafe_allow_html=True)
st.markdown("""
<div class="markdown-text">
📊 Over 3.4 billion spam emails are sent every day!<br>
🛡️ 91% of cyberattacks start with a phishing email.<br>
📬 Email awareness is your first line of defense.
</div>
""", unsafe_allow_html=True)

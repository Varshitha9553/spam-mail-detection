# 📧 Spam Mail Detection - Spam Sense

A minimal, easy-to-use email spam classifier built using Python and machine learning. This project leverages a trained model to help users instantly detect whether an email message is spam or legitimate.

---

## 📝 About

This project was developed as part of my learning journey as a third-year B.Tech student interested in practical applications of machine learning. The app uses a Multinomial Naive Bayes classifier, and provides both a Streamlit web interface and a basic Tkinter GUI.

---

## 🚀 Features

- **Instant Spam Detection**: Paste any email text and get an immediate prediction.
- **User-Friendly Interface**: Modern web UI with Streamlit and a simple Tkinter desktop app.
- **Machine Learning Powered**: Trained on a labeled dataset of real-world emails.
- **Custom Security Tips**: Offers actionable advice to improve your email safety awareness.

---

## 🧰 Tech Stack

- **Python 3.9+**
- **scikit-learn** (machine learning)
- **Streamlit** (web interface)
- **Tkinter** (desktop GUI)
- **Pickle** (model serialization)
- **pandas, numpy** (data handling)

---

### 📦 Installation & Usage

1. **Clone this repository:**
   ```bash
   git clone https://github.com/JanakiVeluri006/spam-mail-detection.git
   cd spam-mail-detection
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit web app:**
   ```bash
   streamlit run app.py
   ```
   - Open the provided local URL in your browser.

4. **(Optional) Run the notebook for training or exploration:**
   - Open `Spam Detector.ipynb` in Jupyter Notebook or VS Code.

---

### 📂 Project Structure

- `app.py` — Streamlit web application for interactive spam detection
- `Spam Detector.ipynb` — Data analysis, model training, and evaluation notebook
- `spam.pkl` — Trained spam classification model (generated after running the notebook)
- `vectorizer.pkl` — Text vectorizer (generated after running the notebook)
- `requirements.txt` — Python dependencies

---

### 🖥️ How it Works

1. User enters/pastes email content.
2. The text is vectorized using a trained `CountVectorizer`.
3. The model predicts whether the input is spam or ham (not spam).
4. The app displays the result along with security tips.

---

### 💡 Sample Usage

Paste a suspicious message in the app, click **Analyze**, and see if it’s safe or spam!

---

### 🔒 Email Safety Tips

- Never click on suspicious links or attachments.
- Always verify the sender’s identity.
- Keep your antivirus and spam filters updated.

---

## 👤 Author

**Janaki Veluri**  
Third-year B.Tech student | Python/C/Java enthusiast

Feel free to fork, contribute, or suggest improvements!

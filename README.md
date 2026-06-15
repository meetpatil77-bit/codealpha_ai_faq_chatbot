# 🤖 AI FAQ Chatbot Assistant

> A smart, AI-powered FAQ chatbot built with Flask and scikit-learn — featuring a sleek glassmorphic dark UI, real-time responses, and category-based navigation.

---

## ✨ Features

- 🌙 **Dark / Light Mode** — Seamless theme toggle saved to localStorage
- 📂 **Sidebar with FAQ Categories** — Getting Started, Billing & Payments, Account & Plans, Security & Support
- 💬 **Clickable Suggestion Pills** — Instantly send pre-built questions with one click
- 🤖 **AI-Powered Matching** — Uses TF-IDF vectorization and cosine similarity to find the best answer
- ⌨️ **Typing Indicator** — Animated 3-dot wave while the bot is "thinking"
- 🧹 **Clear Chat** — Reset the conversation anytime
- 📱 **Fully Responsive** — Mobile-friendly sliding sidebar
- ⚡ **Real-Time Async Chat** — Smooth, no-page-refresh conversation using Fetch API

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| 🐍 Backend | Python 3, Flask |
| 🧠 AI/NLP | scikit-learn (TF-IDF), NLTK (stopwords) |
| 📊 Data | pandas, CSV-based FAQ database |
| 🎨 Frontend | Vanilla HTML, CSS (glassmorphism), JavaScript |
| 🔤 Fonts | Plus Jakarta Sans (Google Fonts) |
| 🎯 Icons | Font Awesome 6 |

---

## 📁 Project Structure

```
Codealpha_aifaqchatbot/
│
├── 📄 app.py              # Flask application & API routes
├── 🧠 chatbot.py          # NLP logic: TF-IDF + cosine similarity
├── 📊 faq.csv             # FAQ question-answer database
├── 📋 requirements.txt    # Python dependencies
│
├── 📂 templates/
│   └── 🌐 index.html      # Main chatbot UI (Jinja2 template)
│
└── 📂 static/
    └── 🎨 style.css       # Glassmorphic design system
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Codealpha_aifaqchatbot.git
cd Codealpha_aifaqchatbot
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App
```bash
python app.py
```

### 4️⃣ Open in Browser
```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. 📥 **User sends a message** via the chat input
2. 🔤 **Text is preprocessed** — lowercased, punctuation stripped, stopwords removed using NLTK
3. 📐 **TF-IDF vectorization** transforms the input and all FAQ questions into numeric vectors
4. 📏 **Cosine similarity** is computed between the user's input and all stored questions
5. ✅ **Best matching answer** is returned if similarity score > 0.1
6. ❓ **Fallback message** is shown if no good match is found

---

## 📋 FAQ Topics Covered

| Category | Sample Questions |
|----------|-----------------|
| 🚀 Getting Started | How do I get started? / Is there a free trial? |
| 💳 Billing & Payments | What payment methods? / What's the refund policy? |
| 👤 Account & Plans | Can I cancel anytime? / Can I upgrade my plan? |
| 🔒 Security & Support | How secure is my data? / Is 24/7 support available? |

---

## 🎨 Design Highlights

- **Glassmorphism** — Frosted glass panels with `backdrop-filter: blur`
- **HSL Color System** — Carefully tuned indigo & teal palette
- **Smooth Animations** — Message slide-up, zoom-in, status pulse effects
- **Typography** — Plus Jakarta Sans for a premium feel
- **Responsive Grid** — 2-column suggestion pills that collapse on mobile

---

## ✅ Test Results

All **6 automated tests** passed:

```
......
----------------------------------------------------------------------
Ran 6 tests in 0.050s

OK ✅
```

| Test | Result |
|------|--------|
| CSV loading (10 Q&A pairs) | ✅ Pass |
| Text preprocessing | ✅ Pass |
| Exact FAQ matching (10/10) | ✅ Pass |
| Paraphrased question matching | ✅ Pass |
| Out-of-domain fallback | ✅ Pass |
| Flask route endpoints (GET & POST) | ✅ Pass |

---

## 📦 Requirements

```
flask
pandas
nltk
scikit-learn
```

---

## 👨‍💻 Author

Made with ❤️ as part of the **CodeAlpha Internship Program**

---

## 📄 License

This project is open-source and free to use for educational purposes.
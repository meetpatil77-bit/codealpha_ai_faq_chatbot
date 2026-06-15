import pandas as pd
import string
import nltk

nltk.download('stopwords', quiet=True)

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load CSV
data = pd.read_csv("faq.csv")

questions = data["question"].tolist()
answers = data["answer"].tolist()

# Text preprocessing
def preprocess(text):

    text = text.lower()

    # Strip punctuation first
    text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()

    stop_words = set(stopwords.words("english"))

    filtered = []

    for word in words:
        if word not in stop_words:
            filtered.append(word)

    return " ".join(filtered)

# Prepare questions
clean_questions = [preprocess(q) for q in questions]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(clean_questions)

# Chatbot response
def get_response(user_input):

    clean_input = preprocess(user_input)

    user_vector = vectorizer.transform([clean_input])

    similarity = cosine_similarity(user_vector, X)

    best_match = similarity.argmax()

    score = similarity[0][best_match]

    if score < 0.1:
        return "Sorry, I could not understand your question. Please try rephrasing or ask another question."

    return answers[best_match]
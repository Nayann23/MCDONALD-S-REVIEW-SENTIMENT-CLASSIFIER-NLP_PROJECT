import streamlit as st
import pickle
import re
import nltk
import emoji
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('omw-1.4')

# Load saved model and vectorizer
with open('svc_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('tfidf_vectorizer.pkl', 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)

# Label decoder
label_map = {
    0: "average",
    1: "excellent",
    2: "poor"
}

# Emoji to sentiment word mapping
emoji_dict = {
    "😡": "angry",
    "😤": "frustrated",
    "😠": "mad",
    "😒": "annoyed",
    "😋": "delicious",
    "🍟": "fries",
    "🍔": "burger",
    "👍": "good",
    "❤️": "love",
    "👎": "bad",
    "🔥": "hot",
    "💯": "perfect",
    "😑": "meh",
    "🙄": "sarcasm",
}

# Preprocessing setup
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Helper functions
def map_emojis(text):
    for emo, word in emoji_dict.items():
        text = text.replace(emo, f" {word} ")
    return text

def correct_spelling(text):
    return str(TextBlob(text).correct())

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def clean_text(text, do_spell_correction=False):
    text = map_emojis(text)
    if do_spell_correction:
        text = correct_spelling(text)
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words]
    pos_tags = pos_tag(tokens)
    lemmatized = [
        lemmatizer.lemmatize(word, get_wordnet_pos(pos))
        for word, pos in pos_tags
    ]
    return ' '.join(lemmatized)

# Streamlit UI
st.set_page_config(page_title="McDonald's Review Classifier", layout="centered")
st.title("🍟 McDonald's Review Sentiment Classifier")

user_input = st.text_area("Enter a customer review:")
apply_spell_correction = st.checkbox("Apply spelling correction (slower but useful for typos)", value=False)

if st.button("Classify"):
    if user_input.strip() == "":
        st.warning("Please enter a review.")
    else:
        with st.spinner("Analyzing..."):
            cleaned = clean_text(user_input, do_spell_correction=apply_spell_correction)
            transformed = vectorizer.transform([cleaned])
            prediction = model.predict(transformed)[0]
            label = label_map[prediction]
        st.success(f"🔍 Predicted Sentiment: **{label.upper()}**")

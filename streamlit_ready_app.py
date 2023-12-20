import streamlit as st
import numpy as np
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import gensim
from nltk.stem import PorterStemmer
from keras.preprocessing.text import Tokenizer

# Load the pre-trained LSTM model
lstm_model = load_model("model.h5")

# Load the Word2Vec model
w2v_model = gensim.models.word2vec.Word2Vec.load("w2v.txt")

# Load the tokenizer
tokenizer = Tokenizer()

porter_stemmer = PorterStemmer()

# Function to preprocess the input text
def preprocess(text):
    # Your preprocess function remains the same
    # ...

def apply_english_stemmed_term(text):
    return [porter_stemmer.stem(term) for term in text.split()]

def fit_stemming(text):
    return ' '.join(text)

def predict_sentiment(text):
    # Your predict_sentiment function remains the same
    # ...

# Streamlit UI
st.title("Sentiment Analysis with LSTM")
text_input = st.text_area("Enter your text here:")

if st.button("Predict Sentiment"):
    if text_input:
        sentiment_label = predict_sentiment(text_input)
        sentiment_mapping = {0: 'Negative', 1: 'Neutral', 2: 'Positive'}
        predicted_sentiment = sentiment_mapping[sentiment_label]
        st.success(f"Predicted Sentiment: {predicted_sentiment}")
    else:
        st.warning("Please enter some text for prediction.")

import pandas as pd
import numpy as np
import re
import nltk
import gensim
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import streamlit as st

# Load the pre-trained LSTM model
lstm_model = load_model("model.h5")

# Load the Word2Vec model
w2v_model = gensim.models.word2vec.Word2Vec.load("w2v.txt")

# Load the tokenizer
tokenizer = Tokenizer()

porter_stemmer = PorterStemmer()

# Function to preprocess the input text
def preprocess(text):
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub('&quot;', "", text)
    text = re.sub('&amp;', " ", text)
    text = re.sub(r"\d+", "", str(text))
    text = re.sub(r"\b[a-zA-Z]\b", "", str(text))
    text = re.sub(r"[^\w\s]", " ", str(text))
    text = re.sub(r'(.)\1+', r'\1\1', text)
    text = re.sub(r"\s+", " ", str(text))
    text = re.sub(r'#', '', text)
    text = re.sub(r'[^a-zA-z0-9]', ' ', str(text))
    text = re.sub(r'\b\w{1,2}\b', '', text)
    text = re.sub(r'\s\s+', '', text)
    text = re.sub(r'^b[\s]+', '', text)
    text = re.sub(r'^link[\s]+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'[\U0001F600-\U0001F64F]', '', text)
    text = re.sub(r'\$\w', '', text)
    text = text.lower()
    return text

def apply_english_stemmed_term(text):
    return [porter_stemmer.stem(term) for term in text.split()]

def fit_stemming(text):
    return ' '.join(text)

def predict_sentiment(text):
    # Preprocess the input text
    preprocessed_text = preprocess(text)
    # Apply stemming
    preprocessed_text = apply_english_stemmed_term(preprocessed_text)
    preprocessed_text_sequence = tokenizer.texts_to_sequences([preprocessed_text])
    
    # Print for debugging
    print("Preprocessed Text Sequence:", preprocessed_text_sequence)
    
    # Pad the sequence with maxlen=300
    preprocessed_text_padded = pad_sequences(preprocessed_text_sequence, maxlen=300)
    
    # Print for debugging
    print("Preprocessed Text Padded:", preprocessed_text_padded)
    
    # Make predictions
    predictions = lstm_model.predict(preprocessed_text_padded)
    sentiment_label = np.argmax(predictions[0])
    
    # Print for debugging
    print("Predictions:", predictions)
    print("Sentiment Label:", sentiment_label)
    
    return sentiment_label


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
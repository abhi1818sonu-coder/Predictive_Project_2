import streamlit as st
import pickle

# Load model
model = pickle.load(open("models/mental_health_model.pkl", "rb"))

# Load vectorizer
vectorizer = pickle.load(open("models/tfidf_vectorizer.pkl", "rb"))

# App title
st.title("Mental Health Status Classification")

# User input
user_input = st.text_area("Enter social media text")

# Prediction
if st.button("Predict"):

    text_vector = vectorizer.transform([user_input])

    prediction = model.predict(text_vector)

    st.success(f"Predicted Mental Health Status: {prediction[0]}")

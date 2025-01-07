import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

st.title("Text Classification")

# Load the vectorizer and model
with open("models/tfidf_vectorizer.pkl", "rb") as f:
    vectorizer: TfidfVectorizer = pickle.load(f)

with open("models/voting_model.pkl", "rb") as f:
    model = pickle.load(f)


# Define rule-based checks
def rule_based_check(text):
    # Example rules
    spam_keywords = ["free", "win", "cash", "prize", "offer"]
    suspicious_patterns = ["click here", "buy now", "urgent"]

    # Check for spam keywords
    if any(keyword in text.lower() for keyword in spam_keywords):
        return True  # Spam

    # Check for suspicious patterns
    if any(pattern in text.lower() for pattern in suspicious_patterns):
        return True  # Spam

    # Example: Text length too short
    if len(text) < 5:
        return True  # Spam

    # Default: Not spam
    return False


# Streamlit input and processing
text = st.text_input("Enter a text")
if text:
    # Check with rule-based system first
    if rule_based_check(text):
        st.error("This is a spam (Rule-Based)")
    else:
        # If no rules matched, proceed with the model
        prediction = model.predict(vectorizer.transform([text]).toarray())[0]
        st.text(prediction)
        if not prediction:
            st.success("This is not a spam (Model-Based)")
            st.balloons()
        else:
            st.error("This is a spam (Model-Based)")


# Print vectorizer's vocabulary
#st.text(list(vectorizer.vocabulary_.keys()))

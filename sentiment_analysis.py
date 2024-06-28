# Import libraries
import pandas as pd
import spacy
from textblob import TextBlob

# Read the csv file
df = pd.read_csv('amazon_product_reviews.csv')

# Load and implement spaCy model
nlp = spacy.load("en_core_web_sm")

# Drop rows with missing review text
df = df.dropna(subset=['reviews.text', 'reviews.rating'])

# Define preprocess_text(text) function to preprocess text data
def preprocess_text(text):

    # Create nlp object
    doc = nlp(text)
    # Remove whitespaces and lowercase the token list comprehension
    # Append in the list if not stop words and alphabetic
    tokens = [token.lemma_.lower().strip() for token in doc if not token.is_stop and token.is_alpha]

    # Join together elements in token list by space
    return " ".join(tokens)

# Define analyse_sentiment(sentence) function to analyse sentiment using TextBlob
def analyse_sentiment(sentence):

    # Create textBlob object
    blob = TextBlob(sentence)

    # Get polarity score
    polarity_score = blob.sentiment.polarity

    # If polarity score greater than 0 sentiment is positive
    if polarity_score > 0:
        sentiment = 'positive'

    # If polarity score smaller than 0 sentiment is negative
    elif polarity_score < 0:
        sentiment = 'negative'

    # Else neutral
    else:
        sentiment = 'neutral'
        
    # Return polarity score and sentiment
    return polarity_score, sentiment

# Create review variable from reviews.text column
review1 = df['reviews.text'][0]
review2 = df['reviews.text'][1]


# Deploy preprocess_text function to preprocess text
clean_review1 = preprocess_text(review1)
clean_review2 = preprocess_text(review2)

# Compare similarity using spaCy

# Get polarity_score and sentiment for first example
polarity_score, sentiment = analyse_sentiment(clean_review1)
print(f"Review: {clean_review1}")
print(f"Polarity score: {polarity_score}")
print(f"Sentiment: {sentiment}\n")

# Get polarity_score and sentiment for second example
polarity_score, sentiment = analyse_sentiment(clean_review2)
print(f"Review: {clean_review2}")
print(f"Polarity score: {polarity_score}")
print(f"Sentiment: {sentiment}\n")
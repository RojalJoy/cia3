import streamlit as st
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, pairwise_distances
from collections import defaultdict

# NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def text_processing(text):
    if isinstance(text, str): 
        # Token
        tokens = word_tokenize(text.lower())
        # stopwords, punctuation, and special characters
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
        # Lemmatization
        lemmatizer = WordNetLemmatizer()
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
        # Join
        preprocessed_text = ' '.join(lemmatized_tokens)
        return preprocessed_text
    else:
        return ''  

def main():
    st.title("Text Analysis")
    df = pd.read_csv('WomensClothingE-CommerceReviews - WomensClothingE-CommerceReviews.csv')

    # text_processing
    df['Cleaned Text'] = df['Review Text'].apply(text_processing)


    
    # Filter dataset 
    filtered_df = df[df['Division Name'] == "Initmates"]

    # Calculate TF-IDF vectors
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(filtered_df['Cleaned Text'])

    # Calculate cosine similarity 
    similarity_matrix = cosine_similarity(tfidf_matrix)  

    # Display
    st.header("Similar Reviews for Initimates")
    similarity_dict = defaultdict(list)
    for i in range(len(similarity_matrix)):
        for j in range(i+1, len(similarity_matrix)):
            similarity_dict[similarity_matrix[i, j]].append((i, j))
    
    similar_reviews = similarity_dict[max(similarity_dict.keys())]
    for pair in similar_reviews:
        st.write(filtered_df.iloc[pair[0]]['Cleaned Text'])
        st.write(filtered_df.iloc[pair[1]]['Cleaned Text'])
        st.write("---")
        
      # Filter dataset 
    filtered_df = df[df['Division Name'] == "General Petite"]

    # Calculate TF-IDF vectors
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(filtered_df['Cleaned Text'])

    # Calculate cosine similarity 
    similarity_matrix = cosine_similarity(tfidf_matrix) 

    # Display
    st.header("Similar Reviews for General Petite")
    similarity_dict = defaultdict(list)
    for i in range(len(similarity_matrix)):
        for j in range(i+1, len(similarity_matrix)):
            similarity_dict[similarity_matrix[i, j]].append((i, j))
    
    similar_reviews = similarity_dict[max(similarity_dict.keys())]
    for pair in similar_reviews:
        st.write(filtered_df.iloc[pair[0]]['Cleaned Text'])
        st.write(filtered_df.iloc[pair[1]]['Cleaned Text'])
        st.write("---")
        
      # Filter dataset 
    filtered_df = df[df['Division Name'] == "General"]

    # Calculate TF-IDF vectors
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(filtered_df['Cleaned Text'])

    # Calculate cosine similarity 
    similarity_matrix = cosine_similarity(tfidf_matrix) 
    # Display
    st.header("Similar Reviews for General")
    similarity_dict = defaultdict(list)
    for i in range(len(similarity_matrix)):
        for j in range(i+1, len(similarity_matrix)):
            similarity_dict[similarity_matrix[i, j]].append((i, j))
    
    similar_reviews = similarity_dict[max(similarity_dict.keys())]
    for pair in similar_reviews:
        st.write(filtered_df.iloc[pair[0]]['Cleaned Text'])
        st.write(filtered_df.iloc[pair[1]]['Cleaned Text'])
        st.write("---")

if __name__ == "__main__":
    main()

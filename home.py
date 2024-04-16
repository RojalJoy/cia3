import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('WomensClothingE-CommerceReviews - WomensClothingE-CommerceReviews.csv')

# Create a histogram of ratings
st.title('Distribution of Ratings')
rating_counts = df['Rating'].value_counts()
fig, ax = plt.subplots()
ax.bar(rating_counts.index, rating_counts.values)
plt.xlabel('Rating')
plt.ylabel('Count')
st.pyplot(fig)

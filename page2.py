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

# Calculate positive feedback count for each class name
positive_feedback_summary = df.groupby('Class Name')['Positive Feedback Count'].sum()

# Display the summary
st.title('Positive Feedback Count Summary')
st.bar_chart(positive_feedback_summary)

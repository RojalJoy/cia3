
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

# Filter reviews based on Division Name or Department Name
division_name = st.selectbox('Select Division Name', df['Division Name'].unique())
filtered_df = df[df['Division Name'] == division_name] if division_name else df

department_name = st.selectbox('Select Department Name', df['Department Name'].unique())
filtered_df = filtered_df[filtered_df['Department Name'] == department_name] if department_name else filtered_df

# Display the filtered reviews
st.dataframe(filtered_df)

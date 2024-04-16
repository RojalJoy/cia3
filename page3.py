import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
@st.cache
def load_data():
    return pd.read_csv('WomensClothingE-CommerceReviews - WomensClothingE-CommerceReviews.csv')

df = load_data()

# Sidebar for graph type and attribute selection
st.sidebar.title('Select Options')
graph_type = st.sidebar.selectbox('Select Graph Type', ['Scatter Plot', 'Line Plot', 'Bar Plot'])
x_attribute = st.sidebar.selectbox('Select X Attribute', df.columns)
y_attribute = st.sidebar.selectbox('Select Y Attribute', df.columns)

# Main content
st.title('2D Graph Generator')

# Plot the selected graph
fig, ax = plt.subplots()
if graph_type == 'Scatter Plot':
    sns.scatterplot(data=df, x=x_attribute, y=y_attribute, ax=ax)
elif graph_type == 'Line Plot':
    sns.lineplot(data=df, x=x_attribute, y=y_attribute, ax=ax)
elif graph_type == 'Bar Plot':
    sns.barplot(data=df, x=x_attribute, y=y_attribute, ax=ax)

plt.xlabel(x_attribute)
plt.ylabel(y_attribute)
st.pyplot(fig)

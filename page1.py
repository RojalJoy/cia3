import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px


def load_data():
    return pd.read_csv('WomensClothingE-CommerceReviews - WomensClothingE-CommerceReviews.csv')

df = load_data()

st.sidebar.title('Select Options')
graph_type = st.sidebar.selectbox('Select Graph Type', ['Scatter Plot', 'Line Plot', 'Bar Plot'])
x_attribute = st.sidebar.selectbox("Select X Attribute", df.columns)
y_attribute = st.sidebar.selectbox('Select Y Attribute', df.columns)
z_attribute = st.sidebar.selectbox("Select Z Attribute",df.columns)


st.title('3D Plot Visualization')
st.subheader("Please select the attributes and the grapgh that you wanted to plot")


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

if graph_type == 'Scatter Plot':
    ax.scatter(df[x_attribute], df[y_attribute], df[z_attribute])
elif graph_type == 'Line Plot':
    ax.plot(df[x_attribute], df[y_attribute], df[z_attribute])
elif graph_type == 'Bar Plot':
    ax.bar(df[x_attribute], df[y_attribute], df[z_attribute])

ax.set_xlabel(x_attribute)
ax.set_ylabel(y_attribute)
ax.set_zlabel(z_attribute)

st.pyplot(fig)


scatter_3d = px.scatter_3d(df, x='Age', y='Rating', z='Positive Feedback Count', title='3D scatter plot of to show the relationship between Age,Rating and Positivie Frequency count')
st.plotly_chart(scatter_3d)



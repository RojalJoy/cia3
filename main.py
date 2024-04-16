import streamlit as st
pages={
    "Home":"home.py",
    "3D Plot Visualization":"page1.py",
    "Image Processing":"page2.py",
    "Text Similarity" :"page3.py"
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(pages.keys()))


page_to_load = pages[selection]
with open(page_to_load, "r") as f:
    code = f.read()
exec(code)































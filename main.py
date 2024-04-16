import streamlit as st

pages = {
    "Home": "home.py",
    "Page 1": "page1.py",
    "Page 2": "page2.py",
    "Page 3":"page3.py",
    "Page 4":"page4.py",
    "Page 5":"page5.py"
}


st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(pages.keys()))


page_to_load = pages[selection]
with open(page_to_load, "r") as f:
    code = f.read()
exec(code)

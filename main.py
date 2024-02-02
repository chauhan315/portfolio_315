import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=500)

with col2:
    st.title("Ankur Singh Chauhan")
    content = """
        Hi, I am Ankur! I am a Python Programmer. I graduated in 2023 in BCA and now pursuing MCA.
            I am doing specialization in DATA SCIENCE with PYTHON.
    """
    st.info(content)

st.write("Below you can find some of the apps I have built in Python. Feel free to contact me.")


col3, empty_col ,col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.image("images/" + row["image"], width=500)
        st.write(row["description"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.image("images/" + row["image"], width=500)
        st.write(row["description"])
        st.write(f"[Source Code]({row['url']})")

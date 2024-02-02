import streamlit as st

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

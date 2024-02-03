import streamlit as st
from send_email import send_email

st.header("Contact Us")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message here")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
{user_email}
"""
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        send_email(message)
        st.info("Your email was sent successfully.")

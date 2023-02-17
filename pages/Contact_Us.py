import streamlit as st
from send_email import send_email

st.set_page_config(layout='wide')
st.header("Contact Us")

with st.form(key='form', clear_on_submit=True):
    user_email = st.text_input('Your email address')
    raw_message = st.text_area('Your message')
    user_message = f"""\
Subject: New email from {user_email}
    
From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")

    if button:
        send_email(user_message)
        st.info("Your email was sent successfully")


import streamlit as st
import smtplib
from email.message import EmailMessage
import ssl

def send_email(user_name, suggestion):
    sender_email = st.secrets["my_email"]
    sender_password = st.secrets["my_password"]
    receiver_email = st.secrets["rceiver"]
    
    smtp_server = "smtp.gmail.com"
    smtp_port = 465
    _context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, smtp_port, context = _context) as server:
        server.login(sender_email, sender_password)

        subject = f"New Suggestion from {user_name}"
        body = f"User: {user_name}\n\nSuggestion: {suggestion}"
        # message = f"Subject: {subject}\n\n{body}"

        em = EmailMessage()
        em['From'] = sender_email
        em['To'] = receiver_email
        em['Subject'] = subject
        em.set_content(body)

        server.sendmail(sender_email, receiver_email, em.as_string())

st.title('Leave a Suggestion')

user_name = st.text_input('Your Name:')
suggestion = st.text_area('Your Suggestion:')
submit_button = st.button('Submit')

if submit_button:
    if user_name and suggestion:
        send_email(user_name, suggestion)
        st.success('Thank you for your suggestion, {}!'.format(user_name))

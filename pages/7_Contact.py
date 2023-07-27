import streamlit as st
import requests

# Header, Footer
######################
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
######################

st.title("Contact Form")

# Display the section for the person looking for a job
st.header("About Me")
st.write("I am actively seeking job opportunities, having done projects in both Data Science and Development.")
st.header(":mailbox: Get In Touch With Me!")

contact_form = """
<form action="https://formsubmit.co/shreshthrajpal@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")


import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="SkillSwap", layout="wide")

def load_html(file):
    with open(file, 'r', encoding='utf-8') as f:
        html_data = f.read()
        components.html(html_data, height=800, scrolling=True)

menu = st.sidebar.radio("Go to", ["Home", "Register", "Login", "About"])

if menu == "Home":
    load_html("index.html")

elif menu == "Register":
    load_html("register.html")

elif menu == "Login":
    load_html("login.html")

elif menu == "About":
    load_html("about.html")

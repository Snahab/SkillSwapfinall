import streamlit as st
import os
import pandas as pd

st.set_page_config(page_title="SkillSwap", layout="centered")

# Set consistent background
st.markdown("""
    <style>
    .stApp {
        background-color: #fff3e0;
    }
    </style>
""", unsafe_allow_html=True)

# Read the HTML landing page (index.html)
def show_landing_page():
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
        st.components.v1.html(html_content, height=600, scrolling=True)

# Registration form
def show_register():
    st.subheader("📋 Register to SkillSwap")
    user_type = st.selectbox("Register as", ["Student", "Mentor"])
    name = st.text_input("Full Name")
    college = st.text_input("College/Institution")
    interest = st.selectbox("Interest Area", ["Technical", "Commerce"])
    username = st.text_input("Create Username")
    password = st.text_input("Create Password", type="password")

    if st.button("Register"):
        if username and password:
            with open("users.csv", "a") as f:
                f.write(f"{user_type},{name},{college},{interest},{username},{password}\n")
            st.success("✅ Registered Successfully!")
        else:
            st.error("Please fill all fields")

# Login form
def show_login():
    st.subheader("🔐 Login to SkillSwap")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        try:
            df = pd.read_csv("users.csv", header=None, names=["Type", "Name", "College", "Interest", "Username", "Password"])
            user = df[(df["Username"] == username) & (df["Password"] == password)]
            if not user.empty:
                st.success(f"Welcome {username}!")
                with open("current_user.txt", "w") as f:
                    f.write(username)
                st.markdown("[👉 Go to Dashboard](dashboard.py)")
            else:
                st.error("Invalid Credentials")
        except FileNotFoundError:
            st.error("No users registered yet.")

# About Page
def show_about():
    with open("about.html", "r", encoding="utf-8") as f:
        html_content = f.read()
        st.components.v1.html(html_content, height=600, scrolling=True)

# Sidebar Navigation
menu = st.sidebar.selectbox("Navigate", ["Home", "Register", "Login", "About"])

if menu == "Home":
    show_landing_page()
elif menu == "Register":
    show_register()
elif menu == "Login":
    show_login()
elif menu == "About":
    show_about()
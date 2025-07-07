import streamlit as st
import os

# Load logged-in username
def get_username():
    if os.path.exists("current_user.txt"):
        with open("current_user.txt", "r") as f:
            return f.read().strip()
    return "Guest"

username = get_username()

# Set page config
st.set_page_config(page_title="SkillSwap Dashboard", layout="wide")

# Background color and style
st.markdown("""
    <style>
        .stApp {
            background-color: #3e2723;
            color: #ffe0b2;
        }
        h1, h2, h3, h4 {
            color: #ffcc80;
        }
        .css-18e3th9 {
            background-color: #3e2723 !important;
        }
        .stButton>button {
            background-color: #ff9800;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown(f"<h1 style='text-align: center;'>🎓 Welcome, {username}!</h1>", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.title("📂 Dashboard Menu")
    page = st.radio("Navigate to:", [
        "Dashboard Home", "AI Board", "Community", "Skill Sharing",
        "Mentor Booking", "Premium Content", "Certifications", "Edit Profile"
    ])

# Dashboard Home
if page == "Dashboard Home":
    st.subheader("👋 How are you feeling today?")
    st.write("What would you like to explore today?")

    search = st.text_input("🔍 Search for a topic to explore:")
    topics = ["Python Basics", "Excel for Business", "Finance 101", "AI in Commerce"]

    st.markdown("### 📚 Recommended Topics")
    for topic in topics:
        if st.button(f"Explore {topic}"):
            st.success(f"📘 Course '{topic}' started! Complete to unlock quiz.")
            if topic == "Python Basics":
                st.markdown("*Quiz: What is the output of print(2 * 3 + 5)?*")
                q1 = st.radio("Choose one", ["11", "10", "16"])
                if q1 == "11":
                    st.success("✅ Correct! Certificate Unlocked!")
                else:
                    st.error("❌ Incorrect. Try again.")

# AI Board
elif page == "AI Board":
    st.subheader("🤖 AI Board - Ask Your Questions")
    user_query = st.text_area("Enter your question:")
    if st.button("Ask AI"):
        st.info("🧠 (AI response placeholder — will be powered in production.)")

# Community
elif page == "Community":
    st.subheader("👥 SkillSwap Community")
    st.write("See who's active and what they teach:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("👩‍🎓 Anjali - Commerce")
        st.markdown("🧑‍💻 Rajat - Python")
    with col2:
        st.markdown("👨‍🏫 Sagar - AI Mentor")
        st.markdown("👩‍🏫 Ritika - Finance Mentor")
    with col3:
        st.markdown("🧒 Ayaan - Class 12")
        st.markdown("👧 Sneha - B.Com")
    st.markdown("---")
    st.markdown("### 🧑‍🤝‍🧑 Join a Group (Coming Soon)")

# Skill Sharing
elif page == "Skill Sharing":
    st.subheader("💬 Share Your Skill")
    skill = st.text_input("Enter your skill:")
    description = st.text_area("Describe your skill:")
    if st.button("Share"):
        st.success(f"✅ {skill} shared successfully!")
    st.markdown("### 📢 Recently Shared Skills")
    st.markdown("- Anjali: Accounting Basics")
    st.markdown("- Rajat: Python Loops")
    st.markdown("- Sneha: Canva Graphics")

# Mentor Booking
elif page == "Mentor Booking":
    st.subheader("💼 Book a Mentor")
    keyword = st.text_input("Search (e.g., Python, Finance):")
    mentors = {
        "Riya Sharma": {"subject": "Python, AI", "rating": 4.9, "price": "₹299"},
        "Amit Verma": {"subject": "Excel, Analytics", "rating": 4.7, "price": "₹199"},
        "Rahul Sen": {"subject": "Finance", "rating": 4.6, "price": "₹249"}
    }
    for name, info in mentors.items():
        if keyword.lower() in info['subject'].lower() or keyword == "":
            with st.expander(f"👨‍🏫 {name} - {info['subject']} ({info['rating']}⭐)"):
                st.markdown(f"💰 Fee: {info['price']}")
                if st.button(f"Book with {name}"):
                    st.success(f"✅ Session booked with {name}. Payment link will be sent.")

# Premium Content
elif page == "Premium Content":
    st.subheader("🌟 Premium Content")
    st.warning("🔒 Premium access required")
    st.markdown("- Mock Interviews")
    st.markdown("- Downloadable E-books")
    st.markdown("- Live Mentor Sessions")

# Certifications
elif page == "Certifications":
    st.subheader("📄 Your Certifications")
    st.markdown("- Python Basics ✅")
    st.markdown("- Financial Literacy Beginner ✅")
    st.markdown("- Excel Ninja - Pending ❌")

# Edit Profile
elif page == "Edit Profile":
    st.subheader("✏️ Edit Your Profile")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Your Name", value=username)
        class_std = st.text_input("Your Class or Year", value="B.Com 2nd Year")
        interest = st.selectbox("Interest Area", ["Technical", "Commerce"])
    with col2:
        institution = st.text_input("Your Institution", value="ABC College")
        bio = st.text_area("Short Bio", value="I love learning and sharing tech skills.")
        contact = st.text_input("Contact Email", value="your@email.com")
    if st.button("Save Profile"):
        st.success("✅ Profile updated successfully!")

import re
import random
import string
import streamlit as st

# --- Blacklist common passwords ---
blacklist = ["password", "123456", "123456789", "qwerty", "password123", "abc123", "111111"]

# --- Generate strong password with custom length ---
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

# --- Check password strength with custom weights ---
def check_password_strength(password):
    score = 0
    feedback = []
    
    weights = {
        "length": 2,
        "upper_lower": 2,
        "digit": 1,
        "special": 2
    }

    if password.lower() in blacklist:
        feedback.append("❌ This password is too common. Please choose something else.")
        return 0, feedback

    if len(password) >= 8:
        score += weights["length"]
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += weights["upper_lower"]
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += weights["digit"]
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += weights["special"]
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

# --- Streamlit UI ---
st.title("🔒 Password Strength Checker")

# User input
password_input = st.text_input("Enter a password to check:")

# Password checking
if password_input:
    score, issues = check_password_strength(password_input)

    if issues:
        for issue in issues:
            st.warning(issue)

    if score >= 7:
        st.success("✅ Strong Password!")
    elif score >= 5:
        st.info("⚠️ Moderate Password - Could be improved.")
    else:
        st.error("❌ Weak Password - Consider strengthening it.")

# Divider
st.markdown("---")

# --- Password generator section ---
st.subheader("🔑 Need Help Creating a Strong Password?")

# Length selector
length = st.slider("Select password length:", 8, 32, 12)

if st.button("Generate Strong Password"):
    generated = generate_strong_password(length)
    st.success("Here's a strong password:")
    st.code(generated)

    # Clipboard copy code (Streamlit auto-enables copy for `st.code`)
    st.info("✅ You can click the 'copy' icon on the top right of the password box to copy it!")

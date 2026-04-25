import streamlit as st
import base64
from load_css import load_css

# 1. Configuration
st.set_page_config(page_title="Steganography Detection Bot", layout="wide")

# 2. Chargement du style CSS global
load_css()

# 3. Fonction pour convertir l'image en Base64
def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# 4. Injection du background animé
try:
    img_data = get_base64_of_image("assets/appimage.png.png")
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{img_data}");
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }}
        /* On ajoute la classe pour activer l'animation définie dans style.css */
        .stApp {{
            animation: backgroundFlow 200s ease infinite;
            background-size: 200% 200%;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
except FileNotFoundError:
    st.error("Image 'assets/appimage.png.png' introuvable.")

# 5. Votre contenu original
st.markdown('<h1 class="neon-title" >Steganography Detection Bot</h1>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("""
    <div class="glass-card">
        <h2 style='text-align:center;font-weight:bold;color:#1e3a8a;font-size: 50px;'>Welcome</h2>
        <p style='text-align:center; font-size: 30px;font-weight:bold;'>
            Protect your data. Identify hidden messages using our advanced AI detection system.
        </p>
    </div>
    """, unsafe_allow_html=True)

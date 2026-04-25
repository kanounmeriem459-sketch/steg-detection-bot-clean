import streamlit as st
from load_css import load_css

# Configuration de la page
st.set_page_config(page_title="About Us", layout="wide")

# Chargement du style CSS global
load_css()

# --- 1. LOGO EN HAUT (Centré) ---
col_space1, col_logo, col_space2 = st.columns([1.75, 2, 1])
with col_logo:
    # Utilisation du logo de la National School of Cybersecurity
    st.image("assets/logo.png", width=600, use_container_width=False)

# --- 2. TITRE "About" ---
st.markdown('<h1 class="neon-title" style="font-size: 120px; text-align: center; margin-top: 30px;">About</h1>', unsafe_allow_html=True)

# --- 3. PREMIÈRE BOITE : STEGANOGRAPHY ---
st.markdown("""
<div class="glass-card" style="margin-top: 20px; padding: 40px;">
    <div style="border-bottom: 2px solid rgba(255,255,255,0.1); margin-bottom: 30px; padding-bottom: 10px;">
        <h2 style='text-align:center; font-weight:bold; background: linear-gradient(to right,white, #2c52bb, white); font-size: 60px; margin: 0;'>Steganography</h2> 
    </div>
    <p style='font-size: 35px; text-align:left; font-weight:bold; color: #e2e8f0; line-height: 1.6;'>
        Steganography is a technique used to embed hidden data within digital images by modifying low-level pixel information, often at the bit level, in a way that is imperceptible to the human eye.
        <br><br>
        These alterations do not visibly change the image, making detection through manual inspection virtually impossible.
        <br><br>
        In a cybersecurity context, this capability can be exploited to conceal malicious content inside seemingly legitimate images. Attackers may embed payloads such as malicious URLs, PowerShell scripts, or executable binaries, and distribute them without triggering traditional security mechanisms.
        <br><br>
        Because the carrier file appears completely normal, steganography enables covert data transfer and can be used to bypass detection systems, making it a significant threat vector in modern cyber attacks.
        <br><br>
        Detecting such hidden information therefore requires advanced analysis techniques capable of identifying subtle statistical and structural anomalies beyond human perception.
    </p>
</div>
""", unsafe_allow_html=True)

# --- 4. DEUXIÈME BOITE : OUR SOLUTION ---
st.markdown("""
<div class="glass-card" style="margin-top: 40px; padding: 40px;">
    <div style="border-bottom: 2px solid rgba(255,255,255,0.1); margin-bottom: 30px; padding-bottom: 10px;">
        <h2 style='text-align:center; font-weight:bold; background: linear-gradient(to right,white, #2c52bb, white); font-size: 60px; margin: 0;'>Our Solution</h2> 
    </div>
    <p style='font-size: 35px; text-align:left; font-weight:bold; color: #e2e8f0; line-height: 1.6;'>
        Our system is designed to detect hidden messages within digital images using deep learning and machine learning–based steganography detection techniques.
        <br><br>
        It analyzes uploaded images to determine whether hidden data is present by identifying subtle patterns and irregularities that are not visible to the human eye.
        <br><br>
        This platform is developed for cybersecurity research and educational purposes, and can also be used in broader security contexts to scan digital images for potential hidden threats. It helps identify whether images contain concealed data before they are shared or processed.
    </p>
</div>
""", unsafe_allow_html=True)

# --- 5. FOOTER (Signature des créatrices) ---
# --- 5. FOOTER (Signature des créatrices avec Contacts) ---
st.markdown("""
<div class="footer" style="margin-top: 80px; padding: 40px; border-top: 1px solid rgba(255,255,255,0.1);">
    <p style='font-size: 30px; text-align:center; font-weight:bold; color: #94a3b8; margin-bottom: 30px;'>
        Designed and Developed by
    </p>
    <div style="display: flex; justify-content: center; gap: 50px; text-align: center; flex-wrap: wrap;">
        <div>
            <span style='color: #ffffff; font-size: 30px; font-weight: bold;'>Kissoum Liticia</span><br>
            <a href="mailto:l.kissoum@enscs.edu.dz" style="color: #3b82f6; text-decoration: none; font-size: 20px;">liticia.kissoum@nscs.dz</a>
        </div>
        <div>
            <span style='color: #ffffff; font-size: 30px; font-weight: bold;'>Terfaoui Loubna</span><br>
            <a href="mailto:l.terfaoui@enscs.edu.dz" style="color: #3b82f6; text-decoration: none; font-size: 20px;">loubna.terfaoui@nscs.dz</a>
        </div>
        <div>
            <span style='color: #ffffff; font-size: 30px; font-weight: bold;'>Kanoun Meriem</span><br>
            <a href="mailto:m.kanoun@enscs.edu.dz" style="color: #3b82f6; text-decoration: none; font-size: 20px;">meriem.kanoun@nscs.dz</a>
        </div>
    </div>
    <p style="font-size: 20px; text-align:center; margin-top: 50px; color: #64748b; font-weight:bold;">
        © 2026 Steganography Detection Bot - National School of Cybersecurity
    </p>
</div>
""", unsafe_allow_html=True)
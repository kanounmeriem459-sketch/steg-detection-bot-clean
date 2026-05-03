import streamlit as st
from PIL import Image
from model_loader import predict_image
from load_css import load_css

st.set_page_config(page_title="Detection - Stego Bot")
load_css()

# Titre
st.markdown('<h1 class="neon-title">Detection</h1>', unsafe_allow_html=True)

# Zone d'upload (sans cadre)
uploaded_file = st.file_uploader("choose an image to scann:", type=["png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    
    # Affichage de l'image (sans cadre)
    st.image(image, caption="Image to analyze", use_container_width=True)
    
    # Bouton de lancement
    if st.button("start the detection"):
        with st.spinner("Analyse des pixels..."):
            label, confidence = predict_image(image)
            
            # Affichage du résultat (sans cadre)
            if label == "stego":
                st.error(f" Warning : hidden data detected ({confidence*100:.1f}%)")
            elif label == "clean":
                st.success(f"Secure : no hidden data  ({confidence*100:.1f}%)")
            else:
                st.warning(f"Uncertain ({confidence*100:.1f}%)")
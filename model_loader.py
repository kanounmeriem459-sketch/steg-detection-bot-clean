import json
import joblib
import numpy as np
import cv2
from tensorflow.keras.models import load_model

# 1. Chargement des fichiers
feature_extractor = load_model("model/feature_extractor.keras")
xgb_model = joblib.load("model/xgb_model.pkl")

# 2. Chargement de la config (corrigé)
with open("model/config.json", "r") as f:
    config = json.load(f)

# On récupère le seuil unique (0.5)
THRESHOLD = config["threshold"]
IMG_SIZE = tuple(config["image_size"]) # Notez que c'est "image_size" et non "img_size"

def preprocess_for_cnn(image):
    # conversion PIL -> OpenCV
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img = cv2.resize(img, (IMG_SIZE[0], IMG_SIZE[1]))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.astype("float32") / 255.0
    return img

def predict_image(image):
    img = preprocess_for_cnn(image)
    img = np.expand_dims(img, axis=0)

    # Extraction des caractéristiques
    features = feature_extractor.predict(img, verbose=0)

    # Prédiction (probabilité de steganographie)
    prob = xgb_model.predict_proba(features)[0][1] 
    
    # Classification basée sur le seuil unique
    if prob > THRESHOLD:
        label = "stego"
    else:
        label = "clean"
        
    return label, prob
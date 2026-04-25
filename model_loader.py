import json
import joblib
import numpy as np
import cv2
from tensorflow.keras.models import load_model

# LOAD MODELS
feature_extractor = load_model("model/feature_extractor_modelC.keras")
xgb_model = joblib.load("model/xgb_model_modelC.pkl")

# LOAD CONFIG
with open("model/config_modelC.json", "r") as f:
    config = json.load(f)

LOW_THRESHOLD = config["thresholds"]["low"]
HIGH_THRESHOLD = config["thresholds"]["high"]
IMG_SIZE = tuple(config["img_size"])


def preprocess_for_cnn(image):

    # convertir PIL → OpenCV
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    img = cv2.resize(img, IMG_SIZE)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img = img.astype("float32") / 255.0
    img = (img - 0.5) / 0.5

    return img


def predict_image(image):

    img = preprocess_for_cnn(image)
    img = np.expand_dims(img, axis=0)

    features = feature_extractor.predict(img, verbose=0)

    prob_stego = xgb_model.predict_proba(features)[0][1]

    if prob_stego >= HIGH_THRESHOLD:
        label = "stego"
    elif prob_stego <= LOW_THRESHOLD:
        label = "clean"
    else:
        label = "uncertain"

    return label, float(prob_stego)
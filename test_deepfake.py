import tensorflow as tf
import cv2
import numpy as np

def test_single_image(image_path, model, threshold=0.8):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Couldn’t load image: {image_path}")
        return None

    # Preprocess
    img = cv2.resize(img, (32, 32))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    # Predict (model outputs a probability between 0 and 1)
    prediction = model.predict(img)[0][0]

    # Classification
    if prediction > threshold:
        result = "Fake"
        confidence = prediction
    else:
        result = "Real"  
        confidence = 1 - prediction

    print(f"Prediction: {result} (Confidence: {confidence:.2%})")
    return result


# Load model and test
model = tf.keras.models.load_model("deepfake_detector_model.h5")
image_path = "/Users/arathirk/Desktop/untitled folder/img.jpg"

test_single_image(image_path, model, threshold=0.8)

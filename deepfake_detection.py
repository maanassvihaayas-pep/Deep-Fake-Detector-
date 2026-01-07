import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

train_dir = "/Users/arathirk/Desktop/Dataset/Train"
test_dir = "/Users/arathirk/Desktop/Dataset/Test"
val_dir = "/Users/arathirk/Desktop/Dataset/Validation"

def load_images_from_folder(folder, img_size=(32, 32)):
    images = []
    labels = []

    for subfolder in ["Real", "Fake"]:
        path = os.path.join(folder, subfolder)
        if not os.path.exists(path):
            print(f"⚠️ Warning: Folder not found - {path}")
            continue

        for filename in os.listdir(path):
            if filename.startswith("."):  
                continue

            img_path = os.path.join(path, filename)
            img = cv2.imread(img_path)

            if img is None:  
                print(f"⚠️ Skipping file (not an image): {img_path}")
                continue

            img = cv2.resize(img, img_size)
            img = img / 255.0
            images.append(img)
            labels.append(0 if subfolder == "Real" else 1)

    return np.array(images), np.array(labels)

print("Loading training data...")
train_images, train_labels = load_images_from_folder(train_dir)
print("Loading validation data...")
val_images, val_labels = load_images_from_folder(val_dir)
print("Loading testing data...")
test_images, test_labels = load_images_from_folder(test_dir)

if train_images.size == 0:
    print("Error: No training images loaded. Check your Train folder!")
    exit()
if val_images.size == 0:
    print("Error: No validation images loaded. Check your Validation folder!")
    exit()
if test_images.size == 0:
    print("Error: No testing images loaded. Check your Test folder!")
    exit()

print(f"Loaded {len(train_images)} training images, {len(val_images)} validation images, {len(test_images)} testing images")

model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.summary()

print("Starting training...")
history = model.fit(train_images, train_labels, epochs=10, 
                    validation_data=(val_images, val_labels))

test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"Test accuracy: {test_acc:.4f}")

plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

model.save("deepfake_detector_model.h5")
print("Model saved as 'deepfake_detector_model.h5'")





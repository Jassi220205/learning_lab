# ==============================
# 1. IMPORTS
# ==============================
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report

# ==============================
# 2. PATHS (CHANGE IF NEEDED)
# ==============================
train_dir = r"C:\Users\Jassmitha Jammu\.vscode\DL\Face Mask Dataset\Train"
test_dir  = r"C:\Users\Jassmitha Jammu\.vscode\DL\Face Mask Dataset\Test"

# ==============================
# 3. PARAMETERS
# ==============================
IMG_WIDTH, IMG_HEIGHT = 128, 128
BATCH_SIZE = 32
EPOCHS = 5

# ==============================
# 4. DATA GENERATORS
# ==============================
train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255
)

test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255
)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(IMG_WIDTH, IMG_HEIGHT),
    batch_size=BATCH_SIZE,
    class_mode='binary'
)

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(IMG_WIDTH, IMG_HEIGHT),
    batch_size=BATCH_SIZE,
    class_mode='binary'
)

# Debug check
print("Class Labels:", train_generator.class_indices)

# ==============================
# 5. BUILD MODEL
# ==============================
model = tf.keras.models.Sequential([

    tf.keras.layers.Conv2D(32, (3,3), activation='relu',
                           input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# ==============================
# 6. COMPILE MODEL
# ==============================
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# ==============================
# 7. TRAIN MODEL
# ==============================
history = model.fit(
    train_generator,
    epochs=EPOCHS,
    validation_data=test_generator
)

# ==============================
# 8. PLOT RESULTS
# ==============================
plt.figure()
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.legend()
plt.title("Accuracy")
plt.show()

plt.figure()
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.legend()
plt.title("Loss")
plt.show()

# ==============================
# 9. EVALUATION
# ==============================
y_true = test_generator.classes
y_pred = model.predict(test_generator)
y_pred = (y_pred > 0.5).astype(int)

print("Confusion Matrix:")
print(confusion_matrix(y_true, y_pred))

print("\nClassification Report:")
print(classification_report(y_true, y_pred))

# ==============================
# 10. SINGLE IMAGE PREDICTION
# ==============================
from tensorflow.keras.preprocessing import image

img_path = r"C:\Users\Jassmitha Jammu\.vscode\DL\Face Mask Dataset\Test\with_mask\sample.jpg"  # change this

img = image.load_img(img_path, target_size=(IMG_WIDTH, IMG_HEIGHT))
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

prediction = model.predict(img_array)[0][0]

if prediction > 0.5:
    print("Prediction: WITHOUT MASK")
else:
    print("Prediction: WITH MASK")

print(f"Confidence: {prediction*100:.2f}%")

# ==============================
# 11. SAVE MODEL
# ==============================
model.save("face_mask_model.h5")
print("Model saved successfully.")
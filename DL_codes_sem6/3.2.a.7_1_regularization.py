# Feed Forward Neural Network using Regularization Techniques

import tensorflow as tf
from tensorflow.keras import layers, models, regularizers
from tensorflow.keras.datasets import mnist
import pandas as pd
import time

# Reproducibility
tf.keras.utils.set_random_seed(42)

# 1. Load and preprocess dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize pixel values
x_train = x_train / 255.0
x_test = x_test / 255.0

# Flatten images
x_train = x_train.reshape(-1, 784)
x_test = x_test.reshape(-1, 784)

# 2. Function to build FFNN with regularization
def build_model(reg_type=None):
    if reg_type == "L1":
        reg = regularizers.l1(0.001)
    elif reg_type == "L2":
        reg = regularizers.l2(0.001)
    else:
        reg = None

    model = models.Sequential()

    model.add(layers.Dense(
        128,
        activation='relu',
        kernel_regularizer=reg,
        input_shape=(784,)
    ))

    if reg_type == "Dropout":
        model.add(layers.Dropout(0.5))

    model.add(layers.Dense(
        64,
        activation='relu',
        kernel_regularizer=reg
    ))

    if reg_type == "Dropout":
        model.add(layers.Dropout(0.5))

    model.add(layers.Dense(10, activation='softmax'))

    return model

# 3. Regularization techniques
regularization_methods = ["None", "L1", "L2", "Dropout"]

# 4. Train and evaluate
results = []

for reg in regularization_methods:
    print(f"\nTraining model with {reg} regularization")

    model = build_model(None if reg == "None" else reg)

    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    start_time = time.time()

    model.fit(
        x_train,
        y_train,
        epochs=10,
        batch_size=128,
        validation_split=0.1,
        verbose=0
    )

    training_time = time.time() - start_time

    test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)

    results.append({
        "Regularization": reg,
        "Test Accuracy": round(test_accuracy, 4),
        "Test Loss": round(test_loss, 4),
        "Training Time (s)": round(training_time, 2)
    })

# 5. Results
results_df = pd.DataFrame(results)
print("\nPerformance Comparison:")
print(results_df)

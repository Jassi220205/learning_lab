# Feed Forward Neural Network with Advanced Regularization Techniques

import tensorflow as tf
from tensorflow.keras import layers, models, regularizers
from tensorflow.keras.datasets import mnist
from tensorflow.keras.callbacks import EarlyStopping
import pandas as pd

# Reproducibility
tf.keras.utils.set_random_seed(42)

# Load and preprocess dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0

x_train = x_train.reshape(-1, 784)
x_test = x_test.reshape(-1, 784)

# Model builder
def build_ffnn(reg_type=None):
    model = models.Sequential()

    if reg_type == "L1":
        model.add(layers.Dense(
            128, input_shape=(784,),
            kernel_regularizer=regularizers.l1(0.001)
        ))
        model.add(layers.Activation('relu'))

    elif reg_type == "L2":
        model.add(layers.Dense(
            128, input_shape=(784,),
            kernel_regularizer=regularizers.l2(0.001)
        ))
        model.add(layers.Activation('relu'))

    elif reg_type == "Dropout":
        model.add(layers.Dense(128, input_shape=(784,)))
        model.add(layers.Activation('relu'))
        model.add(layers.Dropout(0.5))

    elif reg_type == "BatchNorm":
        model.add(layers.Dense(128, input_shape=(784,)))
        model.add(layers.BatchNormalization())
        model.add(layers.Activation('relu'))

    elif reg_type == "All":
        model.add(layers.Dense(
            128, input_shape=(784,),
            kernel_regularizer=regularizers.l2(0.001)
        ))
        model.add(layers.BatchNormalization())
        model.add(layers.Activation('relu'))
        model.add(layers.Dropout(0.5))

    else:  # No regularization
        model.add(layers.Dense(128, activation='relu', input_shape=(784,)))

    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(10, activation='softmax'))

    return model

# Early stopping (training-level regularization)
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=3,
    restore_best_weights=True
)

# Training and evaluation
regularization_methods = ["None", "L1", "L2", "Dropout", "BatchNorm", "All"]
results = []

for reg in regularization_methods:
    print(f"\nTraining with {reg} regularization")

    model = build_ffnn(None if reg == "None" else reg)

    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    model.fit(
        x_train, y_train,
        epochs=20,
        batch_size=128,
        validation_split=0.1,
        callbacks=[early_stop],
        verbose=0
    )

    test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)

    results.append({
        "Regularization": reg,
        "Test Accuracy": round(test_accuracy, 4),
        "Test Loss": round(test_loss, 4)
    })

# Results
results_df = pd.DataFrame(results)
print("\nPerformance Comparison:")
print(results_df)

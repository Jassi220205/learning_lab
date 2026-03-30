# Feed Forward Neural Network using MNIST
# Performance comparison of different optimizers

import tensorflow as tf
from tensorflow.keras import layers, models, optimizers
from tensorflow.keras.datasets import mnist
import time
import pandas as pd

# Reproducibility
tf.keras.utils.set_random_seed(42)

# 1. Load and preprocess MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize pixel values
x_train = x_train / 255.0
x_test = x_test / 255.0

# Flatten images (28x28 → 784)
x_train = x_train.reshape(-1, 784)
x_test = x_test.reshape(-1, 784)

# 2. Define Feed Forward Neural Network
def build_ffnn():
    model = models.Sequential([
        layers.Dense(128, activation='relu', input_shape=(784,)),
        layers.Dense(64, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])
    return model

# 3. Optimizer configurations (define params only)
optimizer_configs = {
    "SGD": lambda: optimizers.SGD(learning_rate=0.01),
    "Adam": lambda: optimizers.Adam(learning_rate=0.001),
    "RMSprop": lambda: optimizers.RMSprop(learning_rate=0.001),
    "Adagrad": lambda: optimizers.Adagrad(learning_rate=0.01)
}

# 4. Train and evaluate models
results = []

for opt_name, opt_fn in optimizer_configs.items():
    print(f"\nTraining with {opt_name} optimizer")

    model = build_ffnn()
    optimizer = opt_fn()  # fresh optimizer instance

    model.compile(
        optimizer=optimizer,
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
        "Optimizer": opt_name,
        "Test Accuracy": test_accuracy,
        "Test Loss": test_loss,
        "Training Time (s)": training_time
    })

# 5. Compare performance
results_df = pd.DataFrame(results)
print("\nOptimizer Performance Comparison:")
print(results_df)

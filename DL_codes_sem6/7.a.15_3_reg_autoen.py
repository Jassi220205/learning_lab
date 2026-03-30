import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.keras.layers import Input, Dense, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras import regularizers
from tensorflow.keras.datasets import mnist

np.random.seed(42)
tf.random.set_seed(42)

(x_train, _), (x_test, _) = mnist.load_data()

x_train = x_train.astype("float32") / 255.
x_test  = x_test.astype("float32") / 255.

x_train = x_train.reshape((-1, 784))
x_test  = x_test.reshape((-1, 784))

print("Train shape:", x_train.shape)

noise_factor = 0.3

x_train_noisy = x_train + noise_factor * np.random.normal(0, 1, x_train.shape)
x_test_noisy  = x_test  + noise_factor * np.random.normal(0, 1, x_test.shape)

x_train_noisy = np.clip(x_train_noisy, 0., 1.)
x_test_noisy  = np.clip(x_test_noisy, 0., 1.)

input_dim = 784
encoding_dim = 64

input_layer = Input(shape=(input_dim,))

x = Dense(256, activation="relu",
          activity_regularizer=regularizers.l2(1e-5))(input_layer)
x = Dropout(0.3)(x)
x = Dense(128, activation="relu")(x)
encoded = Dense(encoding_dim, activation="relu")(x)

x = Dense(128, activation="relu")(encoded)
x = Dense(256, activation="relu")(x)
decoded = Dense(input_dim, activation="sigmoid")(x)

autoencoder = Model(input_layer, decoded)

autoencoder.compile(optimizer="adam", loss="binary_crossentropy")

autoencoder.summary()

history = autoencoder.fit(
    x_train_noisy, x_train,
    epochs=20,
    batch_size=256,
    shuffle=True,
    validation_data=(x_test_noisy, x_test),
    verbose=1
)

decoded_imgs = autoencoder.predict(x_test_noisy)

n = 10
plt.figure(figsize=(20, 6))

for i in range(n):
    ax = plt.subplot(3, n, i + 1)
    plt.imshow(x_test[i].reshape(28, 28), cmap="gray")
    ax.axis("off")

    ax = plt.subplot(3, n, i + 1 + n)
    plt.imshow(x_test_noisy[i].reshape(28, 28), cmap="gray")
    ax.axis("off")

    ax = plt.subplot(3, n, i + 1 + 2*n)
    plt.imshow(decoded_imgs[i].reshape(28, 28), cmap="gray")
    ax.axis("off")

plt.tight_layout()
plt.show()
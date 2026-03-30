import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.datasets import mnist

np.random.seed(42)
tf.random.set_seed(42)

print("GPU Available:", tf.config.list_physical_devices('GPU'))

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.astype('float32') / 255.
x_test  = x_test.astype('float32') / 255.

x_train = x_train.reshape((len(x_train), 784))
x_test  = x_test.reshape((len(x_test), 784))

input_dim = 784
encoding_dim = 2

input_layer = Input(shape=(input_dim,))

encoded = Dense(128, activation='relu')(input_layer)
encoded = Dense(64, activation='relu')(encoded)
bottleneck = Dense(encoding_dim, activation='linear')(encoded)

decoded = Dense(64, activation='relu')(bottleneck)
decoded = Dense(128, activation='relu')(decoded)
output_layer = Dense(input_dim, activation='sigmoid')(decoded)

autoencoder = Model(input_layer, output_layer)
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

encoder_model = Model(input_layer, bottleneck)

autoencoder.summary()

history = autoencoder.fit(
    x_train, x_train,
    epochs=20,
    batch_size=256,
    shuffle=True,
    validation_data=(x_test, x_test),
    verbose=1
)

encoded_data = encoder_model.predict(x_test)

print("Original shape:", x_test.shape)
print("Reduced shape:", encoded_data.shape)

plt.figure(figsize=(8,6))

scatter = plt.scatter(
    encoded_data[:, 0],
    encoded_data[:, 1],
    c=y_test,
    cmap='tab10',
    s=5
)

plt.colorbar(scatter)
plt.title("2D Latent Space (Colored by Digit)")
plt.xlabel("Latent Dim 1")
plt.ylabel("Latent Dim 2")
plt.show()
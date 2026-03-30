# -----------------------------
# 1. Import Libraries
# -----------------------------
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import mean_absolute_error, r2_score

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# -----------------------------
# 2. Load Dataset
# -----------------------------
path = r"C:\Users\Jassmitha Jammu\.vscode\DL\student_data.csv"
df = pd.read_csv(path)

print(df.head())
print(df.info())

# -----------------------------
# 3. Preprocessing
# -----------------------------

# Encode categorical columns
label_encoders = {}
for col in df.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# OPTIONAL (better learning, not just memorization)


# -----------------------------
# 4. Define Features & Target
# -----------------------------
TARGET_COLUMN = "G3"   # ✅ correct target

X = df.drop(TARGET_COLUMN, axis=1)
y = df[TARGET_COLUMN]

print("Feature shape:", X.shape)

# -----------------------------
# 5. Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# 6. Feature Scaling
# -----------------------------
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# -----------------------------
# 7. Build FNN Model
# -----------------------------
model = Sequential([
    Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(16, activation='relu'),
    Dense(1)
])

model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
)

# -----------------------------
# 8. Train Model
# -----------------------------
history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=16,
    validation_split=0.2,
    verbose=1
)

# -----------------------------
# 9. Evaluate Model
# -----------------------------
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nResults:")
print("MAE:", mae)
print("R2 Score:", r2)
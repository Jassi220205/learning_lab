import numpy as np

def softmax(logits):
    """
    Compute softmax probabilities for multi-class classification
    logits: numpy array of shape (num_classes,)
    """
    exp_vals = np.exp(logits - np.max(logits))  # subtract max for numerical stability
    return exp_vals / np.sum(exp_vals)

# -------------------- USER INPUT --------------------
# Example: user provides logits for 4 classes
logits_input = input("Enter logits separated by space: ")  # e.g., "2.0 1.0 0.1 3.5"
logits = np.array([float(x) for x in logits_input.strip().split()])

# -------------------- COMPUTE SOFTMAX --------------------
probabilities = softmax(logits)

# -------------------- PREDICT CLASS --------------------
predicted_class = np.argmax(probabilities)

# -------------------- OUTPUT --------------------
print("\nLogits:", logits)
print("Softmax Probabilities:", probabilities)
print("Predicted Class:", predicted_class)

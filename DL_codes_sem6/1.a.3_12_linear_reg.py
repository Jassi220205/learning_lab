#Predict house prices based on a single feature (e.g., area in square feet).

#Linear Regression models the relationship between an independent variable X (e.g., area in sq. ft.) and a dependent variable y (price).
#The model learns a best-fit line:
#𝑦=𝑚𝑋+𝑏
#where m = slope b = intercept
#After training, we can predict prices for new areas.

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Example dataset
area = np.array([800, 1000, 1200, 1500, 1800]).reshape(-1, 1)
price = np.array([150000, 180000, 210000, 260000, 300000])

# Train model
model = LinearRegression()
model.fit(area, price)

# Predict for a new area
new_area = np.array([[1400]])
predicted_price = model.predict(new_area)

print("Predicted Price for 1400 sq ft:", predicted_price[0])

# Plot
plt.scatter(area, price, color='blue')
plt.plot(area, model.predict(area), color='red')
plt.xlabel("Area (sq ft)")
plt.ylabel("Price")
plt.show()

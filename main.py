# 1. Importaciones
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# 2. Datos cargados
dataset = pd.read_csv(
    "data/battery_capacity_cycles.csv"
)
X = dataset.iloc[:, 0:1].values 
y = dataset.iloc[:, 1].values

# 3. Entrenamiento regresion lineal
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# 4. Entrenamiento regresion polinomica
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

# 5. Mostrar Regresion lineal
plt.scatter(X, y, color="red")
plt.plot(X, lin_reg.predict(X), color="blue")
plt.title("Battery Capacity vs. Cycles – Linear Regression")
plt.xlabel("Charge Cycles")
plt.ylabel("Remaining Capacity (%)")
plt.show()

# 6. Mostrar regresion polinomica
plt.scatter(X, y, color="red")
plt.plot(X, lin_reg_2.predict(X_poly), color="blue")
plt.title("Battery Capacity vs. Cycles – Polynomial Regression (deg 4)")
plt.xlabel("Charge Cycles")
plt.ylabel("Remaining Capacity (%)")
plt.show()

# 7. Curva
X_grid = np.arange(min(X), max(X) + 1, 1).reshape(-1, 1)
plt.scatter(X, y, color="red")
plt.plot(X_grid, lin_reg_2.predict(poly_reg.transform(X_grid)), color="blue")
plt.title("Battery Capacity vs. Cycles – High‑Res Polynomial Curve")
plt.xlabel("Charge Cycles")
plt.ylabel("Remaining Capacity (%)")
plt.show()

# 8. Predicciones
print("Linear prediction (500 cycles):", lin_reg.predict([[500]])[0])
print(
    "Polynomial prediction (500 cycles):",
    lin_reg_2.predict(poly_reg.transform([[500]]))[0],
)

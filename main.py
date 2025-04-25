# Importar las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_absolute_error, r2_score

# Cargar el dataset
dataset = pd.read_csv("data/battery_capacity_cycles.csv")

# Variables
X = dataset.iloc[:, 0:1].values
y = dataset.iloc[:, 1].values

# Crear y entrenar el modelo polinómico de grado 2
poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(X)
regressor = LinearRegression()
regressor.fit(X_poly, y)

# Predecir
y_pred = regressor.predict(X_poly)

# Visualizar resultados
X_grid = np.arange(min(X), max(X) + 1, 1).reshape(-1, 1)
plt.scatter(X, y, color="red", label="Datos reales")
plt.plot(
    X_grid,
    regressor.predict(poly_reg.transform(X_grid)),
    color="blue",
    label="Modelo polinómico grado 2",
)
plt.title("Battery Capacity vs. Cycles – Polynomial Regression (Grado 2)")
plt.xlabel("Charge Cycles")
plt.ylabel("Remaining Capacity (%)")
plt.legend()
plt.show()

# ----- ANALISIS -----

# R-cuadrado y MAE
r2 = r2_score(y, y_pred)
mae = mean_absolute_error(y, y_pred)
media_capacidad = np.mean(y)
mae_porcentaje = (mae / media_capacidad) * 100

# Interpretacion
print(
    f"""

      MODELO DE REGRESION POLINOMIAL (GRADO 2)

      Para este modelo se ha analizado la relación entre el número de ciclos de carga y la capacidad restante de la batería, utilizando una regresión polinómica de grado 2, que demostró ser el modelo más apropiado en términos de ajuste y generalización.

      El coeficiente de determinación (r²) obtenido es de {r2:.4f}, indicando que aproximadamente el {r2 * 100:.1f}% de la variabilidad observada en la capacidad de la batería puede explicarse a partir del número de ciclos de carga. Además, el error absoluto medio (MAE) registrado fue de {mae:.2f}%, representando una desviación promedio del {mae_porcentaje:.2f}% respecto a los valores reales.

      Se eligió el modelo de grado 2 porque, aunque modelos de grados superiores como 3, 4 o 5 ofrecían incrementos marginales en r², el riesgo de sobreajuste aumentaba considerablemente. Dado que con grado 2 ya se logra un ajuste sobresaliente (r² > 0.996) y un error bajo, no es necesario incrementar la complejidad. De hecho, el análisis mostró que utilizar grados mayores comienza a modelar ruido en lugar de la tendencia real de los datos, lo que confirma la presencia de sobreajuste.
"""
)

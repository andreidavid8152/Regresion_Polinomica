# 📊 Análisis Técnico y Estadístico del Modelo de Regresión Polinómica

## Interpretación

### 1. Modelo de Regresión Lineal  
- Los puntos rojos representan la capacidad real observada de la batería, mientras que la línea azul es la predicción del modelo lineal.
- A simple vista se nota que el modelo **no sigue la curvatura natural** de los datos. 
- En los primeros ciclos (0–200), **la capacidad real cae lentamente**, pero la línea azul **sobreestima** la caída.
- En los ciclos finales (600–825), la degradación se acelera, pero la regresión lineal **subestima** la pérdida de capacidad.
- Resultado: La recta atraviesa el medio del conjunto, pero no logra capturar la dinámica no lineal, dejando residuos importantes en los extremos.

### 2. Modelo de Regresión Polinómica (Grado 4)  
- Se utiliza una curva de cuarto grado (línea azul) que se adapta visiblemente mejor a la forma de la nube de puntos.
- En los ciclos iniciales, la curva cae suavemente, capturando la lentitud de la pérdida de capacidad; en ciclos medios la pendiente crece, y en los altos, la curva se ajusta al patrón de caída acelerada.
- El modelo **reduce significativamente el error** respecto al modelo lineal.
- Resultado: Este modelo logra modelar mejor el conjunto de datos a traves de una curva.

## Análisis Estadístico

| Métrica (conjunto de prueba)      | Linear   | Polynomial (deg 4) |
|----------------------------------|----------|---------------------|
| **R²**                           | 0.9752   | **0.9971**          |
| **RMSE** (% de capacidad)        | 3.08     | **1.06**            |
| **MAE** (% de capacidad)         | 2.57     | **0.86**            |

- **R² = 0.9971** implica que el modelo polinómico explica ≈ 99.7 % de la varianza.
- El **RMSE** de solo ~1 % indica un nivel de precisión muy alto.
- El modelo no muestra signos de **sobreajuste** ni **sesgo sistemático** en los residuos.
- Existen **Correlaciones altas** con los valores reales.

---

## Conclusión
La regresión polinómica de grado 4 demostró ser altamente efectiva para modelar la degradación de la batería, superando ampliamente al modelo lineal en precisión, captura de mejor manera la forma no lineal del fenómeno, especialmente en etapas de desgaste acelerado. Sus métricas estadísticas reflejan un ajuste robusto y sin sobreajuste, lo cual nos dice que esta es una solución precisa, eficiente e ideal para predicciones confiables en contextos técnicos.
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Carga del dataset de ventas
# -----------------------------------------------------------------------------
# Se utiliza una ruta relativa para facilitar la ejecución del proyecto
# en cualquier entorno como Google Colab.

df = pd.read_csv("datos/sales_sample_2024.csv")

# -----------------------------------------------------------------------------
# Conversión de fechas
# -----------------------------------------------------------------------------
# La columna sales_date se convierte al tipo datetime para poder
# realizar agrupaciones mensuales y análisis temporales.

df["sales_date"] = pd.to_datetime(df["sales_date"])

# -----------------------------------------------------------------------------
# Cálculo de ventas totales
# -----------------------------------------------------------------------------
# Se suman todos los montos de ventas registrados en el dataset.

ventas_totales = df["sales_amount"].sum()

print("===================================")
print("VENTAS TOTALES")
print("===================================")
print(f"${ventas_totales}")

# -----------------------------------------------------------------------------
# Agrupación de ventas por mes
# -----------------------------------------------------------------------------
# Se extrae el período mensual de cada fecha y luego se agrupan
# los montos de ventas para obtener el total por mes.

df["mes"] = df["sales_date"].dt.to_period("M")

ventas_por_mes = df.groupby("mes")["sales_amount"].sum()

print("\n===================================")
print("VENTAS POR MES")
print("===================================")
print(ventas_por_mes)

# -----------------------------------------------------------------------------
# Generación del gráfico
# -----------------------------------------------------------------------------
# Se crea un gráfico de líneas para representar la evolución
# de las ventas a lo largo del tiempo.

plt.figure(figsize=(10, 5))

plt.plot(
    ventas_por_mes.index.astype(str),
    ventas_por_mes.values,
    marker="o"
)

plt.title("Evolución de Ventas")
plt.xlabel("Mes")
plt.ylabel("Monto de Ventas")

plt.xticks(rotation=45)

# Se agrega una grilla para mejorar la lectura del gráfico.
plt.grid(True)

# -----------------------------------------------------------------------------
# Guardado del gráfico
# -----------------------------------------------------------------------------
# El gráfico generado se almacena en la carpeta /resultados.

plt.savefig("resultados/evolucion_ventas.png")

print("\nGráfico guardado en:")
print("resultados/evolucion_ventas.png")
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datos/sales_sample_2024.csv")

df["sales_date"] = pd.to_datetime(df["sales_date"])

ventas_totales = df["sales_amount"].sum()

print("===================================")
print("VENTAS TOTALES")
print("===================================")
print(f"${ventas_totales}")

df["mes"] = df["sales_date"].dt.to_period("M")

ventas_por_mes = df.groupby("mes")["sales_amount"].sum()

print("\n===================================")
print("VENTAS POR MES")
print("===================================")
print(ventas_por_mes)

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

plt.grid(True)

plt.savefig("resultados/evolucion_ventas.png")

print("\nGráfico guardado en:")
print("resultados/evolucion_ventas.png")
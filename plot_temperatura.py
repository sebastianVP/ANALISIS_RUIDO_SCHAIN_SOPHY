import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo CSV
fecha = "2025-01-12"
archivo_csv = f"temperatura_{fecha}.csv"

# Leer el archivo CSV
try:
    datos = pd.read_csv(archivo_csv)
    # Convertir la columna 'timestamp' a tipo datetime
    datos['timestamp'] = pd.to_datetime(datos['timestamp'])
    
    # Extraer las columnas relevantes
    tiempo = datos['timestamp']
    temperatura = datos['temperatura_celsius']
    
    # Crear el gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(tiempo, temperatura, label='Temperatura (°C)', color='blue', marker='o')
    
    # Configurar el gráfico
    plt.title("Temperatura diaria - 2025-01-22", fontsize=16)
    plt.xlabel("Hora", fontsize=12)
    plt.ylabel("Temperatura (°C)", fontsize=12)
    plt.grid(visible=True, linestyle="--", alpha=0.5)
    plt.legend(fontsize=12)
    plt.xticks(rotation=45)
    
    # Mostrar el gráfico
    plt.tight_layout()
    #plt.show()
    plt.savefig(f"Temperatura_{fecha}.png")


except FileNotFoundError:
    print(f"No se encontró el archivo {archivo_csv}. Asegúrate de que existe y está en la ruta correcta.")
except Exception as e:
    print(f"Ocurrió un error: {e}")

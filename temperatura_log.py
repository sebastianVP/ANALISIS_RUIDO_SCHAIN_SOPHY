import psutil
import time
import os
from datetime import datetime
###
# COMANDO EN CRONTAB:
# * * * * * cd /home/soporte/Documents/REVISION_SCHAIN_SOPHY/ANALISIS_RUIDO_SCHAIN_SOPHY && ./temperatura.sh
###


def obtener_temperatura():
    """
    Obtiene la temperatura de la CPU si el hardware la soporta.
    Retorna la temperatura en grados Celsius o None si no está disponible.
    """
    try:
        sensores = psutil.sensors_temperatures()
        if "coretemp" in sensores:
            # Obtiene la temperatura promedio de los núcleos
            temperaturas = [sensor.current for sensor in sensores["coretemp"]]
            return sum(temperaturas) / len(temperaturas)
        elif "cpu-thermal" in sensores:  # Caso común en Raspberry Pi
            return sensores["cpu-thermal"][0].current
    except Exception as e:
        print(f"Error al obtener la temperatura: {e}")
    return None

def grabar_temperatura():
    """
    Graba la temperatura de la computadora minuto a minuto en un archivo CSV.
    """
    # Obtener fecha y hora actuales
    ahora = datetime.now()
    fecha = ahora.strftime("%Y-%m-%d")
    timestamp = ahora.strftime("%Y-%m-%d %H:%M:%S")
    
    # Obtener temperatura
    temperatura = obtener_temperatura()
    if temperatura is None:
        print("No se pudo obtener la temperatura. Asegúrate de que el hardware sea compatible.")
        return
    
    # Crear nombre del archivo con la fecha actual
    nombre_archivo = f"temperatura_{fecha}.csv"
    
    # Escribir datos en el archivo
    encabezado = "timestamp,temperatura_celsius\n"
    datos = f"{timestamp},{temperatura:.2f}\n"
    if not os.path.exists(nombre_archivo):
        # Si el archivo no existe, escribir encabezado
        with open(nombre_archivo, "w") as archivo:
            archivo.write(encabezado)
    with open(nombre_archivo, "a") as archivo:
        archivo.write(datos)
    
    print(f"Registrado: {timestamp} - {temperatura:.2f} °C")
        
       

if __name__ == "__main__":
    grabar_temperatura()

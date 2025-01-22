**REVISION DE DATOS DE RADAR METEOROLOGICO -SCHAIN**

Esta revision parte de la instalacion de Signal Chain y la rama de desarrollo correspondiente al Radar Meteorologico SOPHY.
Empezaremos clonando el repositorio de Signal Chain con el siguiente enlace:

Nuestra carpeta inicial sera

*cd /home/soporte/Documents/REVISION_SCHAIN_SOPHY

Aqui clonamos el repositorio

* git clone http://intranet.igp.gob.pe:8082/schain

* cd schain

Nos movemos a la rama de desarrollo v3-0-WR

* git checkout v3.0-WR

Necesitamos en paralelo crear un entorno de desarrollo:
En nuestro caso le hemos llamado: conda create --name SCHAIN_SOPHY_2025 python=3.9

* Activar el entorno ejemplo: conda activate SCHAIN_SOPHY_2025

* pip install --upgrade pip setuptools wheel

* pip install numpy==1.24

* pip install scipy==1.11

* pip install matplotib==3.5

* pip install cartopy

* cd schain/schainpy

Aqui ya estamos instalando SIGNAL CHAIN, con el siguiente comando, lo que esta pendiente y quizas se pudo instalar antes es la libreria digitalrf

* pip install -e ../


Si hemos llegado hasta aqui sin problemas podemos proceder a instalar digitalrf

* En la carpeta inicial /home/soporte/Documents/REVISION_SCHAIN_SOPHY

Luego clonamos el repositorio de la libreria digitalrf



Los datos de radar se encuentran en la siguiente ruta:
* /home/soporte/Documents/REVISION_SCHAIN_SOPHY/HYO@2025-01-06T19-56-05
Aqui encontraremos los archivos rawdata, position y experiment.json


Tratamos de ejectura y nos damos cuenta que requerimos cartopy:
* python sophy_proc_drone.py  HYO@2025-01-06T19-56-05 --parameters Z

* En la  ruta  siguiente esta instalado signal chain y la carpeta de script de prueba de  la version v3.0-WR
* cd /home/soporte/Documents/REVISION_SCHAIN_SOPHY/schain/schainpy/scripts

* nano sophy_proc_drone.py

* Modificamos la ruta dentro del archivo sophy_proc_drone.py: 
  PATH = "/home/soporte/Documents/REVISION_SCHAIN_SOPHY" # Aqui estan los datos 


* Probamos el programa con el comando:

* python sophy_proc_drone.py  HYO@2025-01-06T19-56-05 --parameters Z

Aqui nos indica un error que debemos modificar el archivo experiment.json, lo que falta modificar es el datadir


   "usrp_rx": {
     "ip_address": "192.168.20.23",
     "daughterboard": "A:AB",
     "antenna": "RX",
     "sample_rate": 2.5,
     "frequency": 70.3125,
     "datadir": "/DATA_RM/DATA/HYO@2025-01-06T19-56-05/rawdata",
     "clock_source": "external",
     "time_source": "external",
     "clock_rate": 100.0
   },


Cambiamos el datadir por el actual

"datadir": "/home/soporte/Documents/REVISION_SCHAIN_SOPHY/HYO@2025-01-06T19-56-05/rawdata"


Realizado el cambio podemos volver a ejecutar el comando:

* python sophy_proc_drone.py  HYO@2025-01-06T19-56-05 --parameters Z


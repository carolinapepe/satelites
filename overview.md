#Estructura del programa

Aqui se describen los metodos implemetados por `main.py`, especificando las librerias requeridas.

##Main

El programa main.py requiere como inputs, fecha inicial y final de los datos a plotear. Con formato YYYY.MM.DD
Opcion flag para eliminar datos de satelite no deseado
--no-[nombre_de_satelite] 

Por default el programa extrae velocidad del viento de una lista de satelites determinada. Por el momento solo tiene un satelite, al que denominamos ASCAT.

Parsea los argumentos de entrada usando el modulo `argaparse`. Traduce el texto ingresado por el usuario en argumentos entendibles por python como variables del programa.

Construye objeto/s satelite a partir de la lista de satelites disponibles para el programa (ahora solo el ASCAT)

##satelite.py

Se define la clase satelite y la subclase satelite ASCAT. Los atributos son fecha inicial y fecha final. 
* Con el metodo `convert_to_datetime` crea secuencias de dias entre las fechas indicadas utilizando `datetime`.
* Con los metodos`download_files` y `getlinks` descarga del directorio correspondiente  los archivos de datos (un archivo por dia). Utiliza las librerias `urllib` (para listar los URL de los archivos)y `lxml.html` para descargar los archivos netCDF y alojarlos en el directorio temporal del usuario.

Con el metodo `plot_data` extrae longitud, latitud y velocidad del viento de los archivos .nc. Utiliza la librerias netCDF4 que manipula archivos de formato .nc. Y emplea `Basemap` de matplotlib toolkits para plotear los datos en un mapa global.




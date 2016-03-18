#Estructura del programa

Aquí se describen los metodos implemetados por `main.py`, especificando las librerías requeridas.

##Main

El programa `main.py` requiere como inputs, fecha inicial y final de los datos a plotear. Con formato `YYYY.MM.DD`
Opción flag para eliminar datos de satélite no deseado
`--no-[nombre_de_satelite]`

Por default el programa extrae velocidad del viento de una lista de satelites determinada. Por el momento solo tiene un satelite, el denominamos ASCAT.

Parsea los argumentos de entrada usando el módulo `argparse`. Traduce el texto ingresado por el usuario en argumentos entendibles por python como variables del programa.

Construye objeto/s satélite a partir de la lista de satelites disponibles para el programa (ahora solo el ASCAT).

Finalmente se procesan los satélites de acuerdo a lo indicado con las opciones en línea de comandos.

##satelite.py

Se define la clase (abstracta) satélite y la subclase ASCAT. Los atributos son fecha inicial y fecha final. 
* Con el metodo `convert_to_datetime` crea objetos `datetime` (librería que debe ser importada) a partir del string de entrada.
* Con la función `datarange` crea una lista días (objetos `datetime`) entre los días inicial y final.
* Con los metodos`download_files` y `getlinks` descarga los archivos para el día correspondiente. Utiliza las librerías `urllib` y `lxml.html` para listar las URL de los archivos netCDF y luego descargarlos en el directorio temporal del usuario.

Con el metodo `extract_data` extrae longitud, latitud y velocidad del viento de los archivos `.nc`. Utiliza la librerias netCDF4 que manipula archivos de formato .nc. Luego, empleando `Basemap` de `mpl_toolkits`, las funciones `generate_figure` y `plot_data` plotean los datos en un mapa global.




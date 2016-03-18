

# Satélites
Trabajo Práctico del Workshop en Técnicas de Programación Científica 2016

Este directorio contiene un programa que plotea mediciones de velocidad de viento realizadas por satélites en un intervalo de fechas designado por el usuario.

![Ejemplo de las observaciones del satelite Metop A (ASCAT)](whole_as.png "Ejemplo de las observaciones del satelite Metop A (ASCAT)")


## Producto ploteado

A la fecha el programa esta implementado unicamente para productos obtenidos del ASCAT (Advanced Scatterometer) perteneciente al MetOp-A (Meteorological Operational satellite program), a su vez perteneciente a EUMETSAT (European Organization for the Exploitation of Meteorological Satellites).

El producto extraído para el ploteo es velocidad del viento sobre superficie oceánica con una resolución de muestreo de 25 km. El intervalo de tiempo máximo de datos disponibles es [2012-2016].

El set de datos se descarga de directorio de [PODAAC-OPENDAP](http://podaac-opendap.jpl.nasa.gov/opendap/allData/ascat/preview/L2/metop_b/25km/)

#Archivos

`main.py` Cuerpo principal del programa. Este es el archivo a ejecutar por el usuario. Solicita fecha inicial y final de datos a plotear (en ese orden separados por space), con formato `YYYY.MM.DD`
.
 Opcion flag para eliminar datos de satélite no deseado
`--no-[nombre_de_satelite]` 

`satelite.py` Se define clase satelite, sus métodos y por ahora algunas funciones globales que no justificaban (por ahora) un archivo. Se piensa corregir esto a futuro.

Ver `overview.md` para una descripción de la estructura del programa y las librerías implementadas.











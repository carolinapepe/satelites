
""" Lee los datos descargados"""

import netCDF4 as nc
from netCDF4 import Dataset

#Creo objeto netCDF a partir del archivo descargado
f=Dataset("./Downloads/ascat_20160101_003000_metopa_47740_eps_o_250_2300_ovw.l2.nc","r")

#Extraigo las variables de locacion y tiempo
lat=f.variables['lat'][:]
lon=f.variables['lon'][:]
time=f.variables['time'][:]

#Extraigo variable a plotear
wspeed=f.variables['wind_speed'][:]


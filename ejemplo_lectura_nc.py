#!/usr/bin/env python

#importo librerias
import netCDF4
import calendar
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


from netCDF4 import Dataset

#creo objeto netcdf
#ACA NECESITO COMO INPUT FILENAME

f=Dataset("/tmp/ascat_20150803_000900_metopb_14908_eps_o_250_2201_ovw.l2.nc","r")

#extraigo latitudes, longitudes, tiempos
#ACA NECESITO COMO INPUT EL NOMBRE DE LAS LATITUDES
lat=f.variables["lat"]

lon=f.variables["lon"]


#extraigo la variable wind speed

#ACA NECESITO COMO INPUT EL NOMBRE DE LA VAR
wind_speed = f.variables["wind_speed"]

#extraigo y remplazo codigo de dato faltante por NaN

velviento = f.variables["wind_speed"][:,:]

faltante=wind_speed._FillValue

velviento.data[velviento.data==faltante] = np.nan

#agrego scale factor a las latitudes

latitudes = lat[:,:]# /lat.scale_factor

longitudes = lon[:,:]#/lon.scale_factor
ntimes,nobs = np.shape(velviento)

#------------------------------------------
#Plot

# llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
# are the lat/lon values of the lower left and upper right corners
# of the map.
# lat_ts is the latitude of true scale.
# resolution = 'c' means use crude resolution coastlines.
m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,\
            llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')
#dibujo costas, etc
m.drawcoastlines()
m.drawstates()
m.drawcountries()
m.drawparallels(np.arange(-90.,91.,30.))
m.drawmeridians(np.arange(-180.,181.,60.))

#sigo tutoriales, proyecto lat y lon

x,y = m(longitudes,latitudes)

# define the colormap
cmap = plt.cm.jet
# extract all colors from the .jet map
cmaplist = [cmap(i) for i in range(cmap.N)]
# force the first color entry to be grey
cmaplist[0] = (.5,.5,.5,0.0)
# create the new map
cmap = cmap.from_list('Custom cmap', cmaplist, cmap.N)

cs = m.pcolor(x,y,velviento.data,cmap=cmap)
cb = m.colorbar(cs,"right", size="5%", pad='2%')
cb.set_label('m/s')

plt.title('Sfc Wind Speed') #agregar fecha y dato del satelite

plt.show()





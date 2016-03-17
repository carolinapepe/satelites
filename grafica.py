#Creo objeto netCDF a partir del archivo unzip
import netCDF4 as nc
from netCDF4 import Dataset

#for nc_name in list_files
#f=Dataset(nc_name,"r")

f=Dataset("/home/wtpc/Downloads/ascat_20160101_003000_metopa_47740_eps_o_250_2300_ovw.l2.nc","r")

#Extraigo las variables de locacion y tiempo
lat=f.variables['lat']
lon=f.variables['lon']
time=f.variables['time']

#Extraigo variable a plotear
wspeed=f.variables['wind_speed']

lon=lon[:]
lat=lat[:]
time=time[:]
wspeed=wind_speed[:]

from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset, date2index
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
date = datetime(2007,12,15,0) # date to plot.
# open dataset.
dataset = \
Dataset("/home/wtpc/Download/ascat_20160101_003000_metopa_47740_eps_o_250_2300_ovw.l2.nc")
timevar = dataset.variables['time']
timeindex = date2index(date,timevar) # find time index for desired date.
# read sst.  Will automatically create a masked array using
# missing_value variable attribute. 'squeeze out' singleton dimensions.
#sst = dataset.variables['sst'][timeindex,:].squeeze()
# read ice.
wind_speed = dataset.variables['wind_speed'][timeindex,:].squeeze()
# read lats and lons (representing centers of grid boxes).
lats = dataset.variables['lat'][:]
lons = dataset.variables['lon'][:]
lons, lats = np.meshgrid(lons,lats)
# create figure, axes instances.
fig = plt.figure()
ax = fig.add_axes([0.05,0.05,0.9,0.9])
# create Basemap instance.
# coastlines not used, so resolution set to None to skip
# continent processing (this speeds things up a bit)
m = Basemap(projection='kav7',lon_0=0,resolution=None)
# draw line around map projection limb.
# color background of map projection region.
# missing values over land will show up this color.
m.drawmapboundary(fill_color='0.3')
# plot sst, then ice with pcolor
im1 = m.pcolormesh(lons,lats,sst,shading='flat',cmap=plt.cm.jet,latlon=True)
im2 = m.pcolormesh(lons,lats,wind_speed,shading='flat',cmap=plt.cm.gist_gray,latlon=True)
# draw parallels and meridians, but don't bother labelling them.
m.drawparallels(np.arange(-90.,99.,30.))
m.drawmeridians(np.arange(-180.,180.,60.))
# add colorbar
cb = m.colorbar(im1,"bottom", size="5%", pad="2%")
# add a title.
ax.set_title('velocidad del viento %s'%date)
plt.show()

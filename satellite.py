import datetime
from datetime import timedelta, date
import urllib
import lxml.html
import re
#all libraries below are for plotting routines
import netCDF4
import calendar
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib as mpl
from netCDF4 import Dataset


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)+1):
        yield start_date + timedelta(n)
        

class Satellite(object):

    def __init__(self, initial_time, final_time):
        self.initial_time = initial_time
        self.final_time = final_time
  
class ASCAT(Satellite):
    def __init__(self,initial_time, final_time):
        Satellite.__init__(self,initial_time, final_time)
        #self.convert_to_julian_date(self)
        
    def convert_to_datetime(self):
        formt = '%Y.%m.%d'
        
        #creates datetime object
        self.initial_time = datetime.datetime.strptime(self.initial_time, formt)
        self.final_time = datetime.datetime.strptime(self.final_time, formt)

    def download_files(self):
        root_URL = 'http://podaac-opendap.jpl.nasa.gov/opendap/allData/ascat/preview/L2/metop_b/25km/'
        for day in daterange(self.initial_time,self.final_time):
            URL = root_URL + str(day.year) + '/' + str(day.timetuple().tm_yday) + '/'
            print "Downloading data for day {}".format(day.date())
            self.GetNetCDF(URL)

    # Extract list of gz files (wouldn't be necessary if FTP was possible)
    def GetLinks (self,url):
        connection = urllib.urlopen(url)
        dom =  lxml.html.fromstring(connection.read())
        files = []
        for link in dom.xpath('//a/@href'):
            # If it doesn't have opendap (garbage)
            if (not re.search("opendap", link)):
                # Get only .gz file
                if (re.search("gz$", link)):
                    files.append(link)
        return files

    # Downloads NetCDF4 files for ASCAT (geniuses at NASA append .gz -.-)
    def GetNetCDF(self,url):

        files = self.GetLinks(url)   
        i=1
        # Download files to directory

        for item in files:
            fullurl = url+item
            dest = "/tmp/" + item[:-3]
            print "    Downloading file {}".format(i)
            urllib.urlretrieve(fullurl, dest)       
            i = i + 1

    def plot_data(self, path_to_file, fig_handler, cmap):
       
        f=Dataset(path_to_file,"r")

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

        velviento.data[velviento.data == faltante] = np.nan
        velviento.data[velviento.data == 0] = np.nan
        print np.nanmax(velviento.data)
        #agrego scale factor a las latitudes

        latitudes = lat[:,:]# /lat.scale_factor

        longitudes = lon[:,:]#/lon.scale_factor

        #------------------------------------------
        #Plot

        # llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
        # are the lat/lon values of the lower left and upper right corners
        # of the map.
        # lat_ts is the latitude of true scale.
        # resolution = 'c' means use crude resolution coastlines.
        #dibujo costas, etc
        fig_handler.drawcoastlines()
        fig_handler.drawstates()
        fig_handler.drawcountries()
        fig_handler.drawparallels(np.arange(-60.,60.,15.))
        fig_handler.drawmeridians(np.arange(0.,360.,60.))
        #cb_axis = fig_handler.add_axes([0.05, 0.80, 0.9, 0.15])

        #sigo tutoriales, proyecto lat y lon

        x,y = fig_handler(longitudes,latitudes)

        bounds = [0,10]
        #norm = mpl.colors.Normalize(vmin=0, vmax=40)
        cs = fig_handler.pcolor(x,y,velviento.data,cmap=cmap, vmin=0,\
            vmax=30)
        #cb = mpl.colorbar.ColorbarBase(cs, cmap=cmap, norm=norm)
        #cb = fig_handler.colorbar(cs,"right", size="5%", pad='2%',\
            #boundaries=bounds)
        cb = fig_handler.colorbar(cs,"right", size="5%", pad='2%')
        cb.set_label('m/s')
        #cb.set_clim(vmin=0, vmax=40)#CON ESTO LE DIGO DONDE SATURA
        #cb.ax.set_xlim([0, 40]) funciona mal
        cb.set_ticks([0, 10, 20, 30, 40])



"""    
class OTROSAT(object):
    
    def __init__(self...):
        pass
    def make_URL(self,initial_date,final_date...):
        
        
        pass
    def make_data_matrix(self,...):
        pass
    
"""

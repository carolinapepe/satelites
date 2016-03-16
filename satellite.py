import datetime
from datetime import timedelta, date
import urllib
import lxml.html
import re

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
            print "Descargando dia {}".format(day.date())
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
            print "    Descargando archivo {}".format(i)
            urllib.urlretrieve(fullurl, dest)       
            i = i + 1

    def make_data_matrix(self):
        pass

"""    
class OTROSAT(object):
    
    def __init__(self...):
        pass
    def make_URL(self,initial_date,final_date...):
        
        
        pass
    def make_data_matrix(self,...):
        pass
    
"""

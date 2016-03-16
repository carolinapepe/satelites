import datetime
from datetime import timedelta, date

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
        root_URL = 'ftp://podaac.jpl.nasa.gov/allData/ascat/preview/L2/metop_a/25km/'
        for day in daterange(self.initial_time,self.final_time):
            print day
            URL = root_URL + str(day.year) + '/' + str(day.timetuple().tm_yday) + '/'
            print URL
            #GetNetCDF(URL)

    def download_data(self):
        pass
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

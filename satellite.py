import DateTime

class Satellite(object):

    def __init__(self, initial_time, final_time):
        self.initial_time = initial_time
        self.final_time = final_time
        
        
	  

  
class ASCAT(Satellite):
    def __init__(self,initial_time, final_time):
        Satellite.__init__(self,initial_time, final_time)
        #self.convert_to_julian_date(self)
        
    def convert_to_day_of_the_year(self):
        formt = '%Y.%m.%d'
        self.initial_time = DateTime.DateTime(self.initial_time).dayOfYear()
        self.final_time = DateTime.DateTime(self.final_time).dayOfYear()
        
        
    def make_URLs(self):
        pass
        #root_URL = 'ftp://podaac.jpl.nasa.gov/allData/ascat/preview/L2/metop_a/25km/'
        #url
        
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

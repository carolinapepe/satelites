class Satellite(object):

    def __init__(self, name, initial_time, final_time):
        self.initial_time = initial_time
        self.final_time = final_time
        self.name = name
        self.url = self.choose_url()
	  
    def choose_url(self):
        print self.name
        if self.name == 'ASCAT':
            self.url = 'poner url'
            print self.url
        elif self.name == 'OTRO':
            self.url = 'PONER OTRO'

  
    
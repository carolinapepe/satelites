#!/usr/bin/env python

import argparse 
import satellite
import DateTime

def construct_site_list(not_in_list):

    all_sites = ['ASCAT', 'OTROSAT','OTROSAT2']
    sites = list(set(all_sites) - set(not_in_list))
    return sites

def plot_data_matrix(data_matrix):
    pass


def main():
  
	#define parser data
    #ACLARAR BIEN QUe ESTAMOS SUBIENDO Y EN QUE FORMATO
    parser = argparse.ArgumentParser(description='Plotting satellite data.')
    parser.add_argument('date', metavar='date_time_YYYY.MM.DD', type=str, nargs=2,\
		      help='time interval')
    parser.add_argument('satellite', metavar='SATELLITE_NAME', type=str, nargs='?',\
		      help='satellite name')

    args=parser.parse_args()
    initialDate = args.date[0]
    finalDate = args.date[1]

    if not args.satellite:
        not_in_list = []
    else:
        not_in_list = args.satellite.split('+')
    
    sites = construct_site_list(not_in_list)
    
    ascat = satellite.ASCAT(initialDate, finalDate)
    ascat.convert_to_day_of_the_year()
    print ascat.initial_time,ascat.final_time
    #print ascat.initial_time, ascat.final_time
    
    for site in sites:
        pass
        #a_satellite = satellite.Satellite(args.satellite[0],initialDate, finalDate)
    
    

if __name__ == "__main__":
    main()  
       
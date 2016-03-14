#!/usr/bin/env python

import argparse 
import satellite

def main():
  
	#define parser data
  
    parser = argparse.ArgumentParser(description='Plotting satellite data.')
    parser.add_argument('date', metavar='date_time', type=int, nargs=2,\
		      help='time interval')
    parser.add_argument('satellite', metavar='SATELLITE_NAME', type=str, nargs=1,\
		      help='satellite name')

    args=parser.parse_args()
    initialDate = args.date[0]
    finalDate = args.date[1]
    
    a_satellite = satellite.Satellite(args.satellite[0],initialDate, finalDate)

if __name__ == "__main__":
    main()  
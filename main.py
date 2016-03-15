#!/usr/bin/env python

import argparse 
import satellite

# Clean working environment (should be called before main)
def clean:
	import os
	os.system("rm -f /tmp/*.gz /tmp/*.nc")

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

	for item in satellites:
		item.GetGz(item.url)

if __name__ == "__main__":
    clean()
    main()  

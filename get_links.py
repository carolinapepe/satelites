import urllib
import lxml.html
import re

"""
ASCAT methods
"""
# Extract list of gz files (wouldn't be necessary if FTP was possible)
def GetLinks (url):
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
def GetNetCDF(url):

	files = GetLinks(url)	

	# Download files to directory

	for item in files:
		fullurl = url+item
		print fullurl
		dest = "/tmp/" + item[:-3]
		urllib.urlretrieve(fullurl, dest) 		


"""
Global function (not in use for now)
"""
def Decompress():
	import gzip
	import glob
	import os.path
	import shutil

	source_dir = "/tmp"
	dest_dir = "/tmp"
	tmpfile = "/tmp/delete.me.gz"


	for src_name in glob.glob(os.path.join(source_dir, '*.gz')):
		base = os.path.basename(src_name)
		print src_name
		dest_name = os.path.join(dest_dir, base[:-3])
		shutil.copyfile(src_name, tmpfile)
		with gzip.open(tmpfile, 'rb') as infile:
		    with open(dest_name, 'w') as outfile:
		        for line in infile:
		            outfile.write(line)


GetNetCDF("http://podaac-opendap.jpl.nasa.gov/opendap/allData/ascat/preview/L2/metop_b/25km/2016/001/")

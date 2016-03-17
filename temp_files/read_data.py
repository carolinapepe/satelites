

#Busca archivos del servidos ftp y guarda en directorio source
#MAURO

#Descomprime archivos .gz en el directorio source
""" Descomprime archivos .gz en source"""

import gzip
import glob
import os.path
import shutil

source_dir = "/tmp/source"
dest_dir = "/tmp/dest"
tmpfile = "/tmp/delete.me"


for src_name in glob.glob(os.path.join(source_dir, '*.gz')):
    base = os.path.basename(src_name)
    dest_name = os.path.join(dest_dir, base[:-3])
    print dest_name
    shutil.copyfile(src_name, tmpfile)
    with gzip.open(tmpfile, 'rb') as infile:
        with open(dest_name, 'w') as outfile:
            for line in infile:
                outfile.write(line)








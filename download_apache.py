# downloaded all files given hosted by Apache.
from __future__ import print_function
from pprint import pprint
from urllib2 import urlopen
import os, sys, re

url = sys.argv[1]
outdir = sys.argv[2]

request = urlopen(url)
html = request.read()
print(html)

file_names = re.findall(r'<td><a.*>(.*)</a></td>', html)
pprint(file_names)

os.makedirs(outdir)

for name in file_names[1:]: # ignore 'Parent Directory'
    os.system('wget {} -O {}'.format(url + '/' + name,
                                     os.path.join(outdir, name))
              )



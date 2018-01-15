#import urllib.request
#import urllib.parse

url = 'https://eonasdan.github.io/bootstrap-datetimepicker/'
#f = urllib.request.urlopen(url)
#print(f.read().decode('utf-8'))

import requests
from pprint import pprint
r = requests.get(url)
pprint(r.text)
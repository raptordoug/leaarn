import hashlib

import urllib.request
import hashlib
import requests
from bs4 import BeautifulSoup



from bs4 import BeautifulSoup

url = 'http://docker.hackthebox.eu:30561/'
purl = 'http://docker.hackthebox.eu:30561/'

session = requests.session()
target_response = session.get(url)
soup_obj = BeautifulSoup(target_response.text, 'html.parser')
plain_text = soup_obj.h3.text
cipher_text = hashlib.md5(plain_text.encode())
post_param = {'hash' : cipher_text.hexdigest()}


final_response = session.post(url, post_param)
print
print(final_response.text)

#with urllib.request.uutfrlopen('http://docker.hackthebox.eu:31591/') as response:
#    html = response.read()
#print(html)

#r = requests.get('http://docker.hackthebox.eu:31591/')
#response = requests.get
#print(response)
import requests
import urllib
from bs4 import BeautifulSoup
import json
import random
import string

url=''

fx= open(r'text.text').read()
u=fx.split('\n')

a='abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&'
g=['@gmail.com','@yahoo.com','@icould.com']

url='https://www.parentune.com/auth/login?redirect=aHR0cDovL3d3dy5wYXJlbnR1bmUuY29tL2JhYnktbmFtZXM%3D'

for names in u:
    nameextra =  ''.join(random.choice(string.digits))
    names= names.lower() + nameextra + random.choice(g)
    password= ''.join(random.choice(a) for i in range (8))
    print(names)
    print(password)
    print('\n')
    requests.post(url,login)




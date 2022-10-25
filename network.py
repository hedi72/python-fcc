# python has built-in support for TCP Sockets
from email.headerregistry import Address
import json
from curses import def_prog_mode
from fcntl import F_GET_SEALS
from bs4 import BeautifulSoup
import urllib.error
import urllib.parse
import urllib.request
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect( ('Host' , Port) )
mysock.connect(('data.pr4e.org', 80))
# create a web browser
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP:1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

# using urllib in python
# since http is so common,we have a library that does all the the socket work for us and makes web pages look like a file
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())


# web scraping with python

url = input('enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
# retrice all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

"""
using web services

*** xml:extensible markup language ***
primary purpose is to help information systems share structured data
it started as a simplified subset of the standard generalized markup language (SGML) and is designed to be relatively human-legible

"""

"""
*** xml Schema ***
description of the legal format of an xml document
expressed in terms of constraints on the structure and content of document
often used to specify a "contact" between systems my system will only accept xml that conforms to this particular schema
if a particular piece of xml meets the specification of the schema 
it is siad to validate

"""


# web services
data = '''{
    "name" :"hedi",
    "phone" :{
        "type" : "int1",
        "number" :"+1 758 5 8545"
    },
    "email" : {
        "hide" : "yes"
    }

}'''
info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])


serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    Address = input('Enter location:')
    if len(address) < 1:
        break
    url = serviceurl + urllib.parse.urlencode({'address': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'ok':
        print('=== Failure to retrieve ===')
        print(data)
        continue
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', 'lat', 'lng', 'lng')
    location = js['results'][0]['formatted_address']
    print(location)

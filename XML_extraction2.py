import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1084976.xml'
data_ = urllib.request.urlopen(url, context=ctx).read().decode()
#print(type(data_))

root = ET.fromstring(data_)
#print(root)

countstot = 0

for count in root.iter('count') :
    countstot = countstot + int(count.text)
    print(count.text)

print(countstot)

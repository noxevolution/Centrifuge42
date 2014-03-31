#!C:\Python27\python.exe
#!/usr/bin/python2.6
import cgi
import math
import urllib
import json
from socket import gethostname, gethostbyname
ip = gethostbyname(gethostname())
link = cgi.FieldStorage()
data_future = 0
json_file = "time_series_" + ip + ".json"
with open(json_file, "r") as outfile:
    data = json.load(outfile)

if link.getvalue('data')!='':
    dataList = str(link.getvalue('data'))
else:
    dataList = ""


count=0
      
print "Content-type:text/html\r\n\r\n"
"""
newnodeList = []
newListArr = dataList.split(',')
for jk in newListArr:
    if jk !=' ':
        newnodeList.append(jk.strip())
"""

electrons = []
node = []
dataDict = {}
futureDict = {}
datestring = ''
for key in data:
    
    if key['name'] == dataList :
        electrons.append(key['time'])
        node.append(key['name'])
        dataDict['node'] = node
        dataDict['time'] = electrons
abc=json.dumps(dataDict)
print abc

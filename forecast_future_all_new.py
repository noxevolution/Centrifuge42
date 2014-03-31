#!C:\Python27\python.exe
#!/usr/bin/python2.6
import cgi
import math
import urllib
import json
from socket import gethostname, gethostbyname
ip = gethostbyname(gethostname())
link = cgi.FieldStorage()
# data_future = 0
json_file = "time_series_" + ip + ".json"
with open(json_file, "r") as outfile:
    data = json.load(outfile)

if link.getvalue('data')!='':
    dataList = str(link.getvalue('data'))
else:
    dataList = ""

# data_sieve_data =float(link.getvalue('data_sieve_data'))
"""
if link.getvalue('future') in locals() or link.getvalue('future') in globals():
    data_future = int(link.getvalue('future'))
"""
data_future = int(link.getvalue('future'))
# print data_future
"""
if link.getvalue['future'] != '':
    data_future = link.getvalue['future']
"""
count=0
      
print "Content-type:text/html\r\n\r\n"

newnodeList = []
newListArr = dataList.split(',')
for jk in newListArr:
    if jk !=' ':
        newnodeList.append(jk.strip())

# abc = json.dumps(newnodeList)
# print abc
# print newnodeList
# print data
"""
time=['Jan-11','Feb-11','March-11','April-11','May-11','June-11','July-11','Aug-11','Sept-11','Oct-11','Nov-11','Dec-11','Jan-12','Feb-12','March-12','April-12','May-12','June-12','July-12','Aug-12','Sept-12','Oct-12','Nov-12','Dec-12','Jan-13','Feb-13','March-13','April-13','May-13','June-13','July-13']
val =[{'key': 'NPS_Telstra_NA_NA_NPS-CVA-NPSScore','-57.1','-55.8','-55.2','-56.4','-54','-51.6','-53.5','-52.6','-49','-45.7','-46.8','-44.6','-41.3','-46.3','-44.4','-43.3','-42','-39.9','-41.4','-43.8','-42.8','-41.5','-40','-42.3','-42.4','-46.4','-42.7'}
      ]
"""


electrons = []
node = []
dataDict = {}
futureDict = {}
datestring = ''
# print data_future
for key in data:
    if len(newnodeList) > 0:
        if key['key'] in newnodeList:
            last_time = key['time'][-1]
            # print last_time
            timestamp = last_time['date'].split('-')
            time_year = int(str(timestamp[0]))
            # time_month = timestamp[1]
            time_month = int(str(timestamp[1]))
            if data_future != 0:
                # print data_future
                for i in xrange(data_future):
                    futureDict['trendingValue'] = last_time['trendingValue']
                    # print time_month
                    time_month = time_month + 1
                    if(len(str(time_month)) == 1):
                        dateString = str(time_year) + '-0' + str(time_month) + '-01'
                    else:
                        dateString = str(time_year) + '-' + str(time_month) + '-01'
                    if time_month == 12:
                        time_month = 0
                        time_year = time_year + 1
                
                    futureDict['date'] = dateString
                    # print dateString
                    # print futureDict
                    key['time'].append(futureDict.copy())
            # print key['time']
    else:
        last_time = key['time'][-1]
        # print last_time
        timestamp = last_time['date'].split('-')
        time_year = int(str(timestamp[0]))
        # time_month = timestamp[1]
        time_month = int(str(timestamp[1]))
        if data_future != 0:
            # print data_future
            for i in xrange(data_future):
                futureDict['trendingValue'] = last_time['trendingValue']
                # print time_month
                time_month = time_month + 1
                if(len(str(time_month)) == 1):
                    dateString = str(time_year) + '-0' + str(time_month) + '-01'
                else:
                    dateString = str(time_year) + '-' + str(time_month) + '-01'
                if time_month == 12:
                    time_month = 0
                    time_year = time_year + 1
                
                futureDict['date'] = dateString
                # print dateString
                # print futureDict
                key['time'].append(futureDict.copy())
            # print key['time']
electrons.append(key['time'])
node.append(key['name'])
dataDict['node'] = node
dataDict['time'] = electrons
# print dataDict
abc=json.dumps(dataDict)
print abc

#!C:/Python27/python.exe
import cgi 
import sys
sys.stderr = sys.stdout
import os
import cgitb; cgitb.enable()
import json
import xlrd
import time
import copy
from socket import gethostname, gethostbyname

dataDict = {}
dataList = []
dataDictTimeSeries = {}
dataListTimeSeries = []
dataDictNodeTime = {}
dataListNodeTime = []
timeList = []
ip = gethostbyname(gethostname())
impactList = [0.4, 0.4, 0.1, 0, -0.9, 1, 0.5, 0.2, -0.7, 0.6, -0.4]
try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

print "Content-type: text/html\r\n\r\n"
form = cgi.FieldStorage()

# A nested FieldStorage instance holds the file
fileitem = form['datafile']

# Test if the file was uploaded
if fileitem.filename:
    # strip leading path from file name to avoid directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    open(fn, 'wb').write(fileitem.file.read())
    message = fn
else:
    message = 'Failed'

excel_workbook = xlrd.open_workbook(message)
# excel_workbook = xlrd.open_workbook('ts_all_nps.xlsx')
sheet = excel_workbook.sheet_by_index(0)
"""
dataDict['key'] = "NPS SCORE"
dataDict['name'] = "NPS SCORE"
dataDict['impact'] = ""
dataDict['is_parent'] = True
"""
for rownum in xrange(sheet.nrows):
    if rownum == 0:
        dataDict['key'] = "NPS SCORE"
        dataDict['name'] = "NPS SCORE"
        dataDict['impact'] = ""
        dataDict['is_parent'] = 1
        yearstart = sheet.row_values(rownum)[6].split('-')
        year = yearstart[1]
        month = yearstart[0]
        dateString = year + '-' + month + '-01'
        timeList.append(dateString)
        for i in xrange(7, 33):
            month = int(month) + 1
            if(len(str(month)) == 1):
                dateString = str(year) + '-0' + str(month) + '-01'
            else:
                dateString = str(year) + '-' + str(month) + '-01'
            if month == 12:
                month = 0
                year = int(year) + 1
            timeList.append(dateString)
        
    if rownum > 0:
        if dataListTimeSeries != []:
            del dataListTimeSeries[:]
        # del dataListTimeSeries[:]
        node_name = sheet.row_values(rownum)[3]
        uniqueid = sheet.row_values(rownum)[0]
        # print node_name
        
        """
        For the time series manipulation of the Forecasting measure
        """
        for index in xrange(6,33):
            # dataListTimeSeries.append(sheet.row_values(rownum)[index])
            times = sheet.row_values(rownum)[index]
            years = timeList[index-6]
            dataDictTimeSeries['date'] = years
            dataDictTimeSeries['trendingValue'] = times
            dataListTimeSeries.append(copy.deepcopy(dataDictTimeSeries))
            # dataListTimeSeries.append(times)
        dataDictNodeTime['key'] = uniqueid
        dataDictNodeTime['name'] = node_name
        dataDictNodeTime['time'] = dataListTimeSeries
        dataListNodeTime.append(copy.deepcopy(dataDictNodeTime))
        
        dataDict['key'] = uniqueid
        dataDict['name'] = node_name
        dataDict['impact'] = impactList[rownum]
        if rownum == 1:
            dataDict['is_parent'] = 1
        else:
            categoryList = sheet.row_values(rownum)[4].split(':')
            categoryListPrev = sheet.row_values(rownum-1)[4].split(':')
            if categoryList[1] != categoryListPrev[1]:
                dataDict['is_parent'] = 1
            else:
                dataDict['is_parent'] = 0
        dataList.append(dataDict.copy())
        # print dataDict
        # print dataList
        
# JSON file for the time series manipulation of the excel data
json_file_time_series = "time_series_" + ip + ".json"
with open(json_file_time_series, "w") as outfile:
    json.dump(dataListNodeTime, outfile, indent=4)
# JSON file for the node mapping
json_file = "excel_json_ip_" + ip + ".json" 
with open(json_file, "w") as outfile:
    json.dump(dataList, outfile, indent=4)

message=json.dumps(message)
print message

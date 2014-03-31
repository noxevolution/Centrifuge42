#!C:/Python27/python.exe
import cgi
import os
import xlrd
import json

dataDict = {}
dataList = []
print "Content-type: text/html\r\n\r\n"
print "Here we go"

workbook = xlrd.open_workbook("ts_all_nps.xlsx")
sheet = workbook.sheet_by_index(0)

# dataDict['key'] = 
for rownum in xrange(sheet.nrows):
    if rownum > 0:
        node_name = sheet.row_values(rownum)[3]
        uniqueid = sheet.row_values(rownum)[0]
        
        dataDict['key'] = uniqueid
        dataDict['name'] = node_name
        dataDict['impact'] = 0.4
        if rownum == 1:
            dataDict['is_parent'] = True
        else:
            categoryList = sheet.row_values(rownum)[4].split(':')
            categoryListPrev = sheet.row_values(rownum-1)[4].split(':')
            if categoryList[1] != categoryListPrev[1]:
                dataDict['is_parent'] = True
            else:
                dataDict['is_parent'] = False
        dataList.append(dataDict.copy())
        # print dataDict
        # print dataList
with open("data_excel_demo.json", "w") as outfile:
    json.dump(dataList, outfile, indent=2)
file_content = open("data_excel_demo.json", "r")
print file_content.read()

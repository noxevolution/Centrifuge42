#!C:/Python27/python.exe
import cgi
import math
import urllib
import json
from socket import gethostname, gethostbyname
link = cgi.FieldStorage()
ip = gethostbyname(gethostname())
if link.getvalue('data')!='':
    dataList =str(link.getvalue('data'))
else:
    dataList=""
#print link.getvalue('data_sieve_data')
data_sieve_data =float(link.getvalue('data_sieve_data'))

"""
dataList = str("NPS_Telstra_NA_NA_NPS-CVA-NPSScore")
data_sieve_data = float(43)
"""
count=0

        
print "Content-type:text/html\r\n\r\n"

newnodeList = []
newListArr = dataList.split(',')
for jk in newListArr:
    if jk !=' ':
        newnodeList.append(jk.strip())


"""
data = [
    { 'key': 'NPS SCORE','name':'NPS SCORE', 'impact': '','is_parent':True}, 
    { 'key': 'NPS_Telstra_NA_NA_NPS-CVA-NPSScore','name':'NPSScore', 'impact': 0.4,'is_parent':True}, 
    { 'key': 'NPS_Telstra_NA_NA_NPS-CVA-Promoters','name':'Promoters', 'impact': 0.1,'is_parent':False}, 
    { 'key': 'NPS_Telstra_NA_NA_NPS-CVA-Passives','name':'Passives', 'impact': 0,'is_parent':False}, 
    { 'key': 'NPS_Telstra_NA_NA_NPS-CVA-Detractors','name':'Detractors', 'impact': -0.9,'is_parent':False}, 
    { 'key': 'NPS_Telstra_NA_NA_NPS-CVA-XYZ','name':'XYZ', 'impact': 1 ,'is_parent':True}, 
    { 'key': 'NPS_Telstra_NA_NA_NPS-CVA-Reactors','name':'Reactors', 'impact': 0.5,'is_parent':False}, 
    { 'key': 'NPS_Telstra_NA_NA_NPS-CVA-ABC','name':'ABC', 'impact': 0.2,'is_parent':False}, 
    { 'key': 'NPS_Telstra_NA_NA_NPS-CVA-UV','name':'UV', 'impact': -0.7,'is_parent':False}, 
    { 'key': 'NPS_Telstra_NA_NA_NPS-CVA-MN','name':'MN', 'impact': 0.6,'is_parent':False}, 
    { 'key': 'NPS_Telstra_NA_NA_NPS-CVA-JKL','name':'JKL', 'impact': -0.4,'is_parent':False}, 
]
"""
json_file = "excel_json_ip_" + ip + ".json"
with open(json_file, "r") as outfile:
    # data = json.dumps(json.load(outfile), indent=4, separators=(',', ': '))
    data = json.load(outfile)
# print data

"""
data = [
    {
        "impact": 0.4, 
        "key": "NPS_Telstra_NA_NA_NPS-CVA-NPSScore", 
        "name": "NPS Score", 
        "is_parent": 1
    }, 
    {
        "impact": 0.1, 
        "key": "NPS_Telstra_NA_NA_NPS-CVA-Promoters", 
        "name": "% Promoters", 
        "is_parent": 0
    }, 
    {
        "impact": 0, 
        "key": "NPS_Telstra_NA_NA_NPS-CVA-Passives", 
        "name": "% Passives", 
        "is_parent": 0
    }, 
    {
        "impact": -0.9, 
        "key": "NPS_Telstra_NA_NA_NPS-CVA-Detractors", 
        "name": "% Detractors", 
        "is_parent": 0
    }, 
    {
        "impact": 1, 
        "key": "NPS_Telstra_NA_NA_NPS-CVA-Reactors", 
        "name": "% Reactors", 
        "is_parent": 0
    }, 
    {
        "impact": 0.5, 
        "key": "NPS_Telstra_NA_NA_NPS-CVA-XYZ", 
        "name": "%XYZ", 
        "is_parent": 1
    }, 
    {
        "impact": 0.2, 
        "key": "NPS_Telstra_NA_NA_NPS-CVA-ABC", 
        "name": "%ABC", 
        "is_parent": 0
    }, 
    {
        "impact": -0.7, 
        "key": "NPS_Telstra_NA_NA_NPS-CVA-UV", 
        "name": "%UV", 
        "is_parent": 0
    }, 
    {
        "impact": 0.6, 
        "key": "NPS_Telstra_NA_NA_NPS-CVA-MN", 
        "name": "%MN", 
        "is_parent": 0
    }, 
    {
        "impact": -0.4, 
        "key": "NPS_Telstra_NA_NA_NPS-CVA-JKL", 
        "name": "%JKL", 
        "is_parent": 0
    }
]
"""
electrons = []

# type(data)

for key in data:
    # print key
    
    if key['key'] in newnodeList and float(key['impact'])<= data_sieve_data:
    
        dataDict = {}
        
        if abs(key['impact'])==0:
            dataDict['name']= key['name']
            dataDict['distance']= 3
            dataDict['key']= key['key']            
            electrons.append(dataDict)
        if abs(key['impact'])==1:
            dataDict['name']= key['name']
            dataDict['distance']= 1
            dataDict['key']= key['key']
            if key['impact']<0:
                dataDict['type']= False
            else:
                dataDict['type']= True
            electrons.append(dataDict)
        if abs(key['impact'])<=0.9 and abs(key['impact'])>=0.7:
            dataDict['name']= key['name']
            dataDict['distance']= 1
            dataDict['key']= key['key']
            if key['impact']<0:
                dataDict['type']= False
            else:
                dataDict['type']= True
            electrons.append(dataDict)
        if abs(key['impact'])<=0.6 and abs(key['impact'])>=0.4:
            dataDict['name']= key['name']
            dataDict['distance']= 2
            dataDict['key']= key['key']
            if key['impact']<0:
                dataDict['type']= False
            else:
                dataDict['type']= True
            electrons.append(dataDict)
        if abs(key['impact'])<=0.3 and abs(key['impact'])>=0.1:
            dataDict['name']= key['name']
            dataDict['distance']= 3
            dataDict['key']= key['key']
            if key['impact']<0:
                dataDict['type']= False
            else:
                dataDict['type']= True
            electrons.append(dataDict)
        key['select']=True
    else:
        key['select']=False
json_file_tree = "tree_" + ip + ".json"



with open(json_file_tree, "r") as outfile:
    # data = json.dumps(json.load(outfile), indent=4, separators=(',', ': '))
    dataTreeDict = json.load(outfile)
        
def set_selects(dataTreeDict, keys):
    for item in dataTreeDict:
        if 'children' in item:
            set_selects(item['children'], keys)
        if item.get('key') in keys:
            item['select'] = True
        else:
            item['select'] = False

set_selects(dataTreeDict, set(newnodeList))
with open(json_file_tree, "w") as outfile:
    json.dump(dataTreeDict, outfile, indent=4)
       
abc=json.dumps(electrons)
print abc


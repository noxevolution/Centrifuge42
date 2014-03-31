#!C:/Python27/python.exe
print "Content-type:text/html\r\n\r\n"

import cgi, os
import xlrd
import cgitb; cgitb.enable()
import json
from socket import gethostname, gethostbyname
link = cgi.FieldStorage()
content = link.getvalue('content')
bookTestData = xlrd.open_workbook(content)
sheetIO = bookTestData.sheet_by_name('TimeSeries_NPS_Score_regression')

nodeDict ={}
treeList = []
nodeData = []
keyParent = 0
lastParent = ''
for rownum in range(0,sheetIO.nrows):
        
    if rownum==0:
        data = [sheetIO.cell_value(rownum, col) for col in range(sheetIO.ncols)]
        indexCategory = data.index('Category')
        indexNode = data.index('node name')
        
    else:
        data = [sheetIO.cell_value(rownum, col) for col in range(sheetIO.ncols)]
        i=0
        for innerData in data:
            if i==indexCategory:
                adArr = innerData.split(':')
                k=0
                for keyval in adArr:
                    dataDict = {}                    
                    dataDict['key']= ''
                    if k==0 and keyParent==0:
                        keyParent =1
                        dataDict['title']= keyval
                        dataDict['parent']= ''
                        dataDict['child']= adArr[1]
                        dataDict['select']= False
                    elif k>0:
                        dataDict['title']= keyval
                        dataDict['select']= False
                        dataDict['parent']= adArr[k-1]
                        if k < len(adArr)-1:
                            dataDict['child']= adArr[k+1]
                        else:
                            dataDict['child']=''
                    if dataDict not in nodeData:
                        if dataDict.has_key('title'):
                            nodeData.append(dataDict)
                            
                    lastParent = keyval
                    k+=1
                    
        
                    #{'UI': 'T071', 'NAME': 'Entity', 'PARENT': None, 'CHILDREN': 'Conceptual Entity'}
                    #print key
            #print innerData
            i+=1

        nodeDict= {}
        nodeDict['key']= data[0]
        nodeDict['title']= data[indexNode]
        nodeDict['select']= False
        nodeDict['parent']= lastParent
        nodeDict['child']= ''
        nodeData.append(nodeDict)



treeData = []

def insert_in_tree(node, parent, tree=None):
    if tree == None:
        tree = treeData

    for subnode in tree:
        if not 'children' in subnode:
            subnode['children'] = []
        elif insert_in_tree(node, parent, subnode['children']):
            return True

        if subnode['title'] == parent:
            subnode['children'].append(node)
            return True
    return False

for node in nodeData:
    parent = node['parent']
    del node['parent']
    del node['child']
    if parent == '':
        treeData.append(node)
    else:
        result = insert_in_tree(node, parent)
        if not result:
            insert_in_tree(node, parent, nodeData)

# import json

ip = gethostbyname(gethostname())
json_file_tree = "tree_" + ip + ".json"
with open(json_file_tree, "w") as outfile:
    json.dump(treeData, outfile, indent=4)

print json.dumps(treeData, indent=4)







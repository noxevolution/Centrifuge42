#!C:/Python27/python.exe
print "Content-type:text/html\r\n\r\n"

import cgi, os
import xlrd
import cgitb; cgitb.enable()
import json
link = cgi.FieldStorage()
content = link.getvalue('content')
bookTestData = xlrd.open_workbook(content)
sheetIO = bookTestData.sheet_by_name('TimeSeries_NPS_Score_regression')

nodeDict ={}
treeList = []
for rownum in range(0,sheetIO.nrows):
        
    if rownum==0:
        data = [sheetIO.cell_value(rownum, col) for col in range(sheetIO.ncols)]
        indexCategory = data.index('Category')
        indexNode = data.index('node name')
    else:
        dataCategory = sheetIO.cell_value(rownum, indexCategory)
        #dataCategoryArr = rsplit(dataCategory, 1) #dataCategory.split(":")
        left, leftmid,rightmid,right = dataCategory.split(":", 3)
        if left not in treeList:
            treeList.append(left)
            
        if leftmid not in treeList:
            treeList.append(leftmid)
            
        if rightmid not in treeList:    
            treeList.append(rightmid)

        if right not in treeList:
            treeList.append(right)
        #treeList.append(right)
        #print left
        #print right
        if nodeDict.has_key(right):
            #nodeList = []
            nodeList = nodeDict[right]            
            nodeList.append(sheetIO.cell_value(rownum, indexNode))
            nodeDict[right] = nodeList
        else:
            nodeDict[right] = [sheetIO.cell(rownum, indexNode).value]
            #print nodeDict

#print json.dumps(treeList)
#print json.dumps(nodeDict)

treeData =[]
for tree in treeList:
    newDict={}
    newDict['title']=tree
    if nodeDict.has_key(tree):
        nodeChild =[]
        for key in nodeDict[tree]:
            childDict={}
            childDict['title']= key
            nodeChild.append(childDict)
        newDict['children']=nodeChild
    treeData.append(newDict)
    
print json.dumps(treeData)
treeDatae = [
		{"title": "item1", "tooltip": "Look, a tool tip!","select":True },
		{"title": "item2", "select": True },
		{"title": "item3", "key": "id3",
			"children": [
				{"title": "Sub-item 3.1",
					"children": [
						{"title": "Sub-item 3.1.1", "key": "id3.1.1" },
						{"title": "Sub-item 3.1.2", "key": "id3.1.2" }
					]
				},
				{"title": "Sub-item 3.2",
					"children": [
						{"title": "Sub-item 3.2.1", "key": "id3.2.1" },
						{"title": "Sub-item 3.2.2", "key": "id3.2.2" }
					]
				}
			]
		},
		{"title": "Item4", "key": "id4", 
			"children": [
				{"title": "Sub-item 4.1", "activate": True,
					"children": [
						{"title": "Sub-item 4.1.1", "key": "id4.1.1" },
						{"title": "Sub-item 4.1.2", "key": "id4.1.2" }
					]
				},
				{"title": "Sub-item 4.2", "select": True,
					"children": [
						{"title": "Sub-item 4.2.1", "key": "id4.2.1" },
						{"title": "Sub-item 4.2.2", "key": "id4.2.2" }
					]
				},
				{"title": "Sub-item 4.3 (hideCheckbox)", "hideCheckbox": True },
				{"title": "Sub-item 4.4 (unselectable)", "unselectable": True }
			]
		}
	];
   
#message=json.dumps(treeData)
#print message

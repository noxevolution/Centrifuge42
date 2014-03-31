#!C:/Python27/python.exe
import cgi
import math
import urllib
import json
from socket import gethostname, gethostbyname
print "Content-type:text/html\r\n\r\n"
ip = gethostbyname(gethostname())
json_file = "tree_" + ip + ".json"
with open(json_file, "r") as outfile:
    # data = json.dumps(json.load(outfile), indent=4, separators=(',', ': '))
    data = json.load(outfile)
mylist = ["NPS_Telstra_NA_NA_NPS-CVA-JKL", "NPS_Telstra_NA_NA_NPS-CVA-MN", "NPS_Telstra_NA_NA_NPS-CVA-NPSScore"]

        
def set_selects(data, keys):
    for item in data:
        if 'children' in item:
            set_selects(item['children'], keys)
        if item.get('key') in keys:
            item['select'] = True

set_selects(data, set(mylist))
with open(json_file, "w") as outfile:
    json.dump(data, outfile, indent=4)
print data

#!C:/Python27/python.exe
print "Content-type:text/html\r\n\r\n"
import json
from socket import gethostname, gethostbyname

ip = gethostbyname(gethostname())

json_file_tree = "tree_" + ip + ".json"
with open(json_file_tree, "r") as outfile:
    data = json.load(outfile)

print json.dumps(data)

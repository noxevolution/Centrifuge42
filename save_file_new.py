#!/usr/bin/env python
import sys
sys.stderr = sys.stdout
import os, cgi
import cgitb; cgitb.enable()
import json

print "Context-type: text/html\n\n"
# print "Here we go"
form = cgi.FieldStorage()
fileitem = form['datafile']

if fileitem.filename:
    fn = os.path.basename(fileitem.filename)
    open(fn, 'wb').write(filitem.file.read())
    message = fn
else:
    message = 'Failed'
message = json.dumps(message)
print message

import datetime
import sqlite3
import sys

from django.template.loader import get_template
from django.template import Context

from django.http import HttpResponse

def home(request):
    dt = datetime.datetime.now()
    html = '''
<html><body><h1>From django</h1>
<p>Time now: %s.
</body></html>''' % (dt,)
    return HttpResponse(html)

def listproducts(request):
    html = "<table border=\"1\">"
    connection = None
    try:
        connection = sqlite3.connect('/home/pi/src/mydatabase.db')
        with connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Product")
            for row in cursor.fetchall():
                html += "<tr><td>%d<td>%s<td>%d" % row
    except sqlite3.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)
    finally:
        if connection:
            connection.close()
    html += "</table>"
    return HttpResponse(html)
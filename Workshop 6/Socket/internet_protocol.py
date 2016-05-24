import urllib2

target = "http://www.iss.nus.edu.sg/"
f = urllib2.urlopen(target)
content = f.read().decode("utf-8")
f.close()
print content
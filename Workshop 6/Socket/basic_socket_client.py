import socket
from datetime import datetime
host = 'localhost'        # will also work across machines
port = 50000
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(host)
soc.connect((ip, port))

f = soc.makefile(mode="rw")
f.write('Hello there. It is now %s.\n' % (datetime.now(),))
f.flush()
reply = f.readline()
print(reply)
f.close()
soc.close()
import socket
hostname = 'www.iss.nus.edu.sg'
path = '/'
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(hostname)
soc.connect((ip, 80))
f = soc.makefile(mode="rw")
f.write('GET %s HTTP/1.0\r\n' % (path,))
f.write('Host: %s\r\n' % (hostname,))
f.write('\r\n')
f.flush()
reply = f.read()
print(reply)
f.close()
soc.close()
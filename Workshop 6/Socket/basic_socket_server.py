import socket
host = ''
port = 50000
backlog = 5
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((host,port))
soc.listen(backlog)
while 1:
    client, address = soc.accept()
    f = client.makefile(mode="rw")
    input = f.readline().strip()
    print('%s: read [%s]' % (address, input))
    f.write('echo [%s]' % (input))
    f.close()
    client.close()
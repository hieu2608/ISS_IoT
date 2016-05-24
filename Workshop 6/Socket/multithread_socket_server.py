import socket
from threading import Thread

host = ''
port = 50000
backlog = 5

def serviceto(client):
    f = client.makefile(mode="rw")
    input = f.readline().strip()
    print('%s: read [%s]' % (address, input))
    f.write('echo [%s]' % (input))
    f.close()
    client.close()

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((host,port))
soc.listen(backlog)
while 1:
    client, address = soc.accept()
    thread1 = Thread(target=serviceto, args=(client,))
    thread1.start()
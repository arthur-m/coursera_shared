import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80)) # function call with one tuple as argument

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512) # receive up to 512 characters
    if (len(data) < 1):
        break   # yes, this will eventually get hit when EOF reached
    print(data.decode())

mysock.close()


# http://www.dr-chuck.com/page1.html
# format of above:
# protocol - host - document

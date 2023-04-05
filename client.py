import socket                   # Import socket module

s = socket.socket()             # Create a socket object
# Get local machine name
port = 6970                    # Reserve a port for your service.
host = socket.gethostname()   # Get local machine name
ip = socket.gethostbyname(host)   # Get local machine name
s.connect((host, port))
s.send(b'1001')

with open('receivedfile', 'ab') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')

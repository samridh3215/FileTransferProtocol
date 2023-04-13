# server.py

import socket                   # Import socket module

port = 6670            # Reserve a port for your service.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # Create a socket object
host = socket.gethostname()   # Get local machine name
# ip = socket.gethostbyname(host)
ip = "0.0.0.0"
print("IP address of the server", ip)
s.bind((ip, port))            # Bind to the port
s.listen(1)                     # Now wait for client connection.
print('Server listening....')

def sendToClient(filename, conn):
    f = open(filename,'rb')
    l = f.readlines()
   #  conn.send(l)
    for line in l:
       conn.send(line)
       print('Sent ',repr(l))
      #  l = f.read(1024)
    f.close()

    print('Done sending')
    # conn.send(bytes('thank u for connecting\n\n\n', 'ascii'))
    conn.close()

    
def recvFromClient(conn):
    with open('recievedfile', 'ab') as f:
      print('file opened')
      while True:
          print('receiving data...')
          data = conn.recv(1024)
          print('data=%s', (data))
          if not data:
              break
          # write data to a file
          f.write(data)
          f.close()
    print('Successfully get the file')
    conn.close()
    print('connection closed')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    choice = conn.recv(1024)
    print(choice)
    if(choice==b'1'):
      recvFromClient(conn)
    else:
      filename = conn.recv(1024)
      sendToClient(filename, conn)
    # sendToClient(filename ,conn)
  #   f = open(filename,'rb')
  #   l = f.readlines()
  #  #  conn.send(l)
  #   for line in l:
  #      conn.send(line)
  #      print('Sent ',repr(l))
  #     #  l = f.read(1024)
  #   f.close()

  #   print('Done sending')
  #   # conn.send(bytes('thank u for connecting\n\n\n', 'ascii'))
  #   conn.close()




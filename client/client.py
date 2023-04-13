import socket                   # Import socket module
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # Create a socket object
# Get local machine name
port = 6670            # Reserve a port for your service.
host = socket.gethostname()   # Get local machine name
ip = socket.gethostbyname(host)
print(f'Client IP address is {ip}')   # Get local machine name
s.connect(("0.0.0.0", port))
def recvFromServer(s):
    with open('recievedfile', 'ab') as f:
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


def sendToServer(filename, s):
    f = open(filename,'rb')
    l = f.readlines()
   #  conn.send(l)
    for line in l:
       s.send(line)
       print('Sent ',repr(l))
      #  l = f.read(1024)
    f.close()

    print('Done sending')
    # conn.send(bytes('thank u for connecting\n\n\n', 'ascii'))
    s.close()

choice  = int(input("enter 1 to send to server\n0 to receive from server"))
if(choice==1):
    s.send(b'1')
    print("-----Files-----")
    os.system("ls")
    print("----------------")
    filename = input("Enter file to send: \n")
    sendToServer(filename, s)
else:
    s.send(b'0')
    os.system("ls ../server/ls")
    filename = input("What files would you like to recieve")
    s.send(filename)
    recvFromServer(s)




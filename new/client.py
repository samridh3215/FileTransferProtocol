import socket
 
IP = socket.gethostbyname(socket.gethostname())
PORT = 6970
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024
 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
filename = str(input("Enter the name of file without extension: "))
extension = str(input("Enter the extension: "))
print("trying to open ", filename+extension)
file = open(filename+extension, "r")
print(file)
while file == None:
    print("file does not exist, try again")
    filename = str(input("filename: "))
    extension = str(input("extension: "))
    file = open(filename+extension, "r")
data = file.read()
client.send(filename.encode(FORMAT))
client.send(extension.encode(FORMAT))
msg = client.recv(SIZE).decode(FORMAT)
print(f"[SERVER]: {msg}")
client.send(data.encode(FORMAT))
msg = client.recv(SIZE).decode(FORMAT)
print(f"[SERVER]: {msg}")
file.close()
client.close()


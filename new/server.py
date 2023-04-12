import socket
 
IP = socket.gethostbyname(socket.gethostname())
PORT = 6970
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
 
print("[STARTING] Server is starting.")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
print("[LISTENING] Server is listening.")
while True:
    conn, addr = server.accept()
    print(f"[NEW CONNECTION] {addr} connected.")
    filename = conn.recv(SIZE).decode(FORMAT)
    extension = conn.recv(SIZE).decode(FORMAT)
    print(f"[RECV] Receiving the filename and extension.")
    file = open(filename+"_recieved"+extension, "w")
    conn.send("Filename received.".encode(FORMAT))
    data = conn.recv(SIZE).decode(FORMAT)
    print(f"[RECV] Receiving the file data.")
    file.write(data)
    conn.send("File data received".encode(FORMAT))
    file.close()
    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected.")


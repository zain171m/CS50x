import socket
IP = "127.0.1.1"
Port = 1247
bufferSize = 1024
# Create a server socket
Server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind
Server.bind((IP,Port))
print("server running")
# Listen
while(True):
    recieved = Server.recvfrom(bufferSize)
    message = recieved[0]
    address = recieved[1]
    clientMsg = format(message)
    clientIP = "Client IP Address:{}".format(address)
    print(message.decode('utf8', 'strict'))
    print(clientIP)
    # Sending a reply to client
    Servermsg = input("Enter Message: ")
    send = str.encode(Servermsg)
    Server.sendto(send, address)

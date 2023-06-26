import socket
serverAddress = ("127.0.1.1", 1247)
bufferSize = 1024
# Create a client socket
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# Send to server
while True:
    clientmsg = input("Enter Message: ")
    send = str.encode(clientmsg)
    client.sendto(send, serverAddress)
    servermsg = client.recvfrom(bufferSize)
    msg = format(servermsg[0])
    if isinstance(msg, bytes):
        # decode the message and print it
        print(msg.decode('utf-8', 'strict'))
    else:
        print(msg)
    #print(msg.decode('utf-8','strict'))



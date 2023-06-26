import socket

def proxy_server(host, port):
    # Create a socket object
    proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a local address
    proxy_socket.bind((host, port))

    # Start listening for incoming connections
    proxy_socket.listen(1)

    print('Proxy server listening on {}:{}'.format(host, port))

    while True:
        # Wait for a connection
        client_socket, client_address = proxy_socket.accept()

        print('Received connection from {}:{}'.format(client_address[0], client_address[1]))

        # Receive data from the client
        data = client_socket.recv(4096)

        # Forward the data to the destination server
        destination_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        destination_socket.connect(('www.google.com', 80))
        destination_socket.send(data)

        # Receive data from the destination server
        data = destination_socket.recv(4096)

        # Forward the data back to the client
        client_socket.send(data)

        # Close the sockets
        destination_socket.close()
        client_socket.close()

if _name_ == '_main_':
    proxy_server('localhost', 8888)
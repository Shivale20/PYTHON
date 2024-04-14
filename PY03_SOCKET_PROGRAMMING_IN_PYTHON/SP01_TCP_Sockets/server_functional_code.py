import socket

# Server IP and Port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 4571

# Function to get the server's username
def get_server_uname():
    server_uname = input('\nEnter your name: ')
    return server_uname

# Function to set up the server socket
def setup_server_socket(server_socket, server_uname):

    # Bind the server socket to the IP and Port
    server_address = (SERVER_IP, SERVER_PORT)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(5)
    print(f'{server_uname} is online.\nWaiting for new incoming connections.')

# Function to set up the client socket
def setup_client_socket(server_socket):
    # Accept the client's connection
    client_socket, client_address = server_socket.accept()
    return client_socket, client_address

# Function to receive the first data from the client
def recv_client_first_data(client_socket):
    # Receive the first data sent by the client (i.e., client_uname)
    data_recv = client_socket.recv(1024)
    client_uname = data_recv.decode()
    print(f'\n{client_uname} is the new connection.')
    return client_uname

# Function to send the server's username to the client
def send_server_first_data(client_socket, server_uname):
    # Send the server's username to the client
    data_sent = server_uname.encode()
    client_socket.send(data_sent)

# Function to exchange messages between the server and client
def exchange_message(client_socket, client_uname):
    while True:
        # Get the server's message
        server_msg = input(server_uname + ' - ')
        BYE = 'bye'

        # Close the connection if the message is 'bye'
        if server_msg.lower() == BYE:
            print(f'\nConnection ended.')
            break

        # Send the server's message to the client
        encoded_server_msg = server_msg.encode()
        client_socket.send(encoded_server_msg)

        # Receive the client's message
        encoded_client_msg = client_socket.recv(1024)
        client_msg = encoded_client_msg.decode()
        if not client_msg:
            print(f'\nConnection ended.')
            break
        print(f'\n{client_uname} - {client_msg}')

# Main block of code
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

    # Get the server's username
    server_uname = get_server_uname()

    # Set up the server socket
    setup_server_socket(server_socket, server_uname)

    # Accept the client's connection
    client_socket = setup_client_socket(server_socket)[0]

    # Receive the client's username
    client_uname = recv_client_first_data(client_socket)

    # Send the server's username to the client
    send_server_first_data(client_socket, server_uname)

    # Exchange messages between the server and client
    exchange_message(client_socket, client_uname)
    
    # Close the server socket
    server_socket.close()

import socket 
import threading

#list of active connections
active_connections = []

def handle_client(client_socket, client_address):
    global active_connections

    data_recv = client_socket.recv(1024)
    client_uname = data_recv.decode()
    print(f'\n{client_uname} is new connection at address: {client_address[0]}')
    active_connections.append((client_socket, client_address))
    
    data_sent = server_uname.encode()
    client_socket.send(data_sent)

    while True:
        server_msg = input(server_uname + ' - ')
        if server_msg.lower() == 'bye':
            print(f'\nConnection with {client_uname} is ended.')
            client_socket.close()
            active_connections.remove((client_socket, client_address))
            break 

        encoded_sever_msg = server_msg.encode()
        client_socket.send(encoded_sever_msg)

        encoded_client_msg = client_socket.recv(1024)
        client_msg = encoded_client_msg.decode()
        if not client_msg:
            print(f'\nConnection with {client_uname} is ended.')
            client_socket.close()
            active_connections.remove((client_socket, client_address))
            break
        print(f'\n{client_uname} - {client_msg}')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_uname = input('\nEnter your server name: ')
    server_ip = '127.0.0.1'
    server_port = 4571
    server_address = (server_ip, server_port)
    server_socket.bind(server_address)
    server_socket.listen(5)
    print(f"\n{server_uname} is online.\nListening for incoming connections.")

    while True:
        client_socket, client_address = server_socket.accept()
        threading.Thread(
            target=handle_client,
            args = (client_socket, client_address)
        ).start()
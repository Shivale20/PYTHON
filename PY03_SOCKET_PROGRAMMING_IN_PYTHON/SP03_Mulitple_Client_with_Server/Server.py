import socket 
import threading
import connection_functions

# File path to store active connections
active_connections_file = "active_connections.json"

# list of active connections
active_connections = []


def handle_client(client_socket, client_address, connection_id):
    
    global active_connections

    try:

        data_recv = client_socket.recv(1024)
        client_uname = data_recv.decode()
        print(f'\nNEW CONNECTION INITIATED: {client_uname}')

        connection_functions.add_in_active_connection(active_connections, connection_id, client_address)
    
        data_sent = server_uname.encode()
        client_socket.send(data_sent)

        while True:
            server_msg = input(server_uname + ' - ')

            # End connection if server's message is bye
            if server_msg.lower() == 'bye':
                print(f'\nACTIVE CONNECTION ENDED: {client_uname}.')
                break 

            encoded_sever_msg = server_msg.encode()
            client_socket.send(encoded_sever_msg)

            encoded_client_msg = client_socket.recv(1024)
            client_msg = encoded_client_msg.decode()

            # End connection if client's message is empty
            if not client_msg:
                print(f'\nACTIVE CONNECTION ENDED BY: {client_uname}.')
                break

            # Print client's message if it's not empty
            print(f'\n{client_uname} - {client_msg}')

    except Exception as e:
        print(f"\nError occurred during message exchange with {client_uname}: {e}")

    finally:
        #Close the connection and remove from active connections
        client_socket.close()
        connection_functions.remove_from_active_connection(active_connections, connection_id)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_uname = input('\nEnter your server name: ')
    server_ip = '127.0.0.1'
    server_port = 4571
    server_address = (server_ip, server_port)
    server_socket.bind(server_address)
    server_socket.listen(5)
    print(f"\nSERVER: {server_uname} IS ONLINE.\nListening for incoming connections.")

    while True:
        client_socket, client_address = server_socket.accept()
        connection_id = connection_functions.generate_connection_id()
        threading.Thread(
            target=handle_client,
            args = (client_socket, client_address, connection_id)
        ).start()

        
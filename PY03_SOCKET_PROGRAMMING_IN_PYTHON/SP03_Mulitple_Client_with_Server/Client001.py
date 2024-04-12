import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:

    client_uname = input('\nEnter your name: ')

    client_ip = '127.0.0.1'
    client_port = 4571
    client_address = (client_ip, client_port)

    client_socket.connect(client_address)

    # Send first data to client socket at server side
    data_sent = client_uname.encode()
    client_socket.send(data_sent)

    #Receive first data from server socket i.e. server_uname
    data_recv = client_socket.recv(1024)
    server_uname = data_recv.decode()
    print(f'\nYou are connected to {server_uname}.')

    while True:

        BYE = 'bye'

        # Receive server message 
        encoded_server_msg = client_socket.recv(1024)
        server_msg = encoded_server_msg.decode()
        if not server_msg:
            print(f'Connection ended.')
            break
        print(f'\n{server_uname} - {server_msg}')

        # Send message to server 
        client_msg = input(client_uname + ' - ')

        if client_msg.lower() == BYE:
            print(f'\nConnection ended.')
            break
        encoded_client_msg = client_msg.encode()
        client_socket.send(encoded_client_msg)




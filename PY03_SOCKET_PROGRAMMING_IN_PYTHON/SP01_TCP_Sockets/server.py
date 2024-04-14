import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

    server_uname = input('\nEnter your name: ')

    server_ip = '127.0.0.1'
    server_port = 4571
    server_address = (server_ip, server_port)

    server_socket.bind(server_address)

    server_socket.listen(5)

    print(f'{server_uname} is online.\nWaiting for new incoming connections.')

    client_socket, client_address = server_socket.accept()

    # Receive first data sent by client (i.e. client_uname)
    data_recv = client_socket.recv(1024)
    client_uname = data_recv.decode()

    print(f'\n{client_uname} is the new connection at address: ({client_address[0], client_address[1]})')

    # Send first data to client i.e server_uname
    data_sent = server_uname.encode()
    client_socket.send(data_sent)

    while True:

        BYE = 'bye'

        # Get server's message
        server_msg = input(server_uname + ' - ')

        # close the connection if msg is 'bye'
        if server_msg.lower() == BYE:
            print(f'\nConnection ended.')
            break

        # Send server's message
        encoded_server_msg = server_msg.encode()
        client_socket.send(encoded_server_msg)

        # Receive client's message
        encoded_client_msg = client_socket.recv(1024)
        client_msg = encoded_client_msg.decode()
        if not client_msg:
            print(f'\nConnection ended.')
            break
        print(f'\n{client_uname} - {client_msg}')
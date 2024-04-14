import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:

    CLIENT_ADDR = (('127.0.0.1', 37020))
    client_socket.bind(CLIENT_ADDR)

    while True:

        data, addr = client_socket.recvfrom(1024)
        print(f'Message received: {data}')
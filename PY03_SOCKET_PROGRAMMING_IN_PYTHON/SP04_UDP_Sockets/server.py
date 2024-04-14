import socket
import time
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:

    server_socket.settimeout(0.2)

    HOSTNAME = '127.0.0.1'
    PORT = 4572
    HOST_ADDR = (HOSTNAME, PORT)

    server_socket.bind(HOST_ADDR)

    print(f'{socket.gethostbyaddr(HOSTNAME)[0]} is online.')

    i = 1

    while True:

        data = bytes('Message#' + str(i), 'utf-8')

        CLIENT_ADDR = (('127.0.0.1', 37020))

        server_socket.sendto(data,CLIENT_ADDR)

        print(f'sent: {data.decode()}')

        time.sleep(5)

        i +=1


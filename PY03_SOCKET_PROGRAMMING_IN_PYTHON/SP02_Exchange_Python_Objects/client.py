import socket
import pickle

# Server IP and Port
CLIENT_IP = '127.0.0.1'
CLIENT_PORT = 4571

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:

    client_address = (CLIENT_IP, CLIENT_PORT)

    client_socket.connect(client_address)

    while True:

        server_msg = client_socket.recv(1024)
        
        if not server_msg:
            print('No messages from the server.\nClosing the connection..')
            break 

        product_obj = pickle.loads(server_msg)

        print(f'ID: {product_obj.id}\n NAME: {product_obj.name}\n PRICE : {product_obj.price}\n')

        


        

  

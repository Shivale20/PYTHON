import socket
import pickle
import time

from products import Product

# Server IP and Port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 4571

PRODUCT_LIST = [
    Product('P23', 'A-Bike', 1200),
    Product('P13', 'B-Bike', 2200),
    Product('P03', 'C-Bike', 4200),
    Product('P33', 'D-Bike', 7200),
]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

    server_address = (SERVER_IP,SERVER_PORT )
    server_socket.bind(server_address) 

    server_socket.listen(5)
    print(f'Server is online.\nWaiting for new connections.\n')

    client_socket, client_address = server_socket.accept()
    print(f'New connection established at {client_address}\n')

    #Serialized python objects
    for product in PRODUCT_LIST:
        pickeled_products = pickle.dumps(product)
        client_socket.send(pickeled_products)

        print('Sent Product: ', product.id)

        # Wait for 2 seconds
        time.sleep(2)
   
    



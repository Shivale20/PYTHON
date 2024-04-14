import socket
import config

# Define color and style codes
class Colors:
    RESET = '\033[0m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    PURPLE = '\033[95m'

class Styles:
    # ANSI escape codes for styles
    RESET = '\033[0m'
    ITALIC = '\033[3m'

def connect_client(client_socket):
    client_address = (config.CLIENT_IP, config.CLIENT_PORT)
    client_socket.connect(client_address)

def prompt_user_for_message(user_name):
    return input(f'{Colors.PURPLE}{user_name}{Colors.RESET} - {Colors.RED}{Styles.ITALIC}typing{Styles.RESET}:{Colors.RESET} ')

def send_name(client_socket):
    name = input('\nEnter your name: ')
    client_socket.send(name.encode())
    return name

def recv_name(client_socket):
    name = client_socket.recv(1024)
    name = name.decode()
    return name

def show_connected(server_uname):
    print(f'\n{Colors.YELLOW}New connection{Colors.RESET}: {server_uname}.')

def send_message(client_socket, message):
    # Send message to client
    encoded_message = message.encode()
    client_socket.send(encoded_message)

def receive_message(client_socket):
    message = client_socket.recv(1024)
    message = message.decode()
    return message

def show_message(name, message):
    print(f'\n{Colors.BLUE}{name}{Colors.RESET}: {message}')    

def print_connection_end_msg(server_name):
    print(f'\n{Colors.RED}Connection end with{Colors.RESET}:  {server_name}')

def chat(client_socket, client_uname,server_uname):
    while True:

        server_msg = receive_message(client_socket)

        if not server_msg:
            print_connection_end_msg(server_uname)
            break
        show_message(server_uname, server_msg)
        
        client_msg = prompt_user_for_message(client_uname)

        if client_msg.lower() == 'bye':
            print_connection_end_msg(server_uname)
            break
        
        send_message(client_socket, client_msg)

def run_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        connect_client(client_socket)
        client_uname = send_name(client_socket)
        server_uname = recv_name(client_socket)
        show_connected(server_uname)
        chat(client_socket, client_uname,server_uname)

if __name__ == "__main__":
    run_client()





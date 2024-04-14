import socket
import config
import connection

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

def print_connection_begin_msg(client_name):
    print(f'\n{Colors.YELLOW}New connection with{Colors.RESET}:  {client_name}')

def print_connection_end_msg(client_name):
    print(f'\n{Colors.RED}Connection ended with{Colors.RESET}:  {client_name}.')

def exchange_initial_data(client_socket, server_uname, client_address, connection_id, active_connections_file_path):
    # Receive client's username
    data_recv = client_socket.recv(1024)
    client_uname = data_recv.decode()
    print_connection_begin_msg(client_uname)

    # Add client to active connections
    connection.add_connection(active_connections_file_path, connection_id, client_address)

    # Send server's username
    data_sent = server_uname.encode()
    client_socket.send(data_sent)

    return client_uname


def send_message(client_socket, message):
    # Send message to client
    encoded_message = message.encode()
    client_socket.send(encoded_message)


def receive_message(client_socket):
    message = client_socket.recv(1024)
    message = message.decode()
    return message

def show_message(name, message):
    print(f'\n{Colors.BLUE}{name}:{Colors.RESET} {message}')    

def end_connection(client_socket, client_uname, connection_id, active_connections_file_path, deleted_connection_file_path):
    print_connection_end_msg(client_uname)
    connection.remove_connection(connection_id, active_connections_file_path, deleted_connection_file_path)
    client_socket.close()


def handle_file_command(client_socket, server_msg):
    msg_parts = server_msg.split()

    if len(msg_parts) >= 2:
        file_name = msg_parts[1]
        response = f"Preparing to send file: {file_name}"
    else:
        response = f"Server was trying to send file."

    send_message(client_socket, response)


def prompt_user_for_message(user_name):
    return input(f'{Colors.PURPLE}{user_name}{Colors.RESET} - {Colors.RED}{Styles.ITALIC}typing{Styles.RESET}:{Colors.RESET} ')

def handle_client(client_socket, client_uname, connection_id,server_uname):

    while True:

        server_msg = prompt_user_for_message(server_uname)

        # SENDING MESSAGE
        if server_msg.lower() == 'bye':
            end_connection(
                client_socket, 
                client_uname, 
                connection_id, 
                config.ACTIVE_CONNECTIONS_FILE_PATH, 
                config.DELETED_CONNECTION_FILE_PATH)
            break

        elif server_msg.startswith("/file"):
            handle_file_command(client_socket, server_msg)

        else:
            send_message(client_socket, server_msg)


        # RECEIVING MESSAGE
        client_msg = receive_message(client_socket)

        if not client_msg:
            end_connection(
                client_socket, 
                client_uname, 
                connection_id, 
                config.ACTIVE_CONNECTIONS_FILE_PATH, 
                config.DELETED_CONNECTION_FILE_PATH)
            break

        # DISPLAY MESSAGE
        show_message(client_uname, client_msg)

def setup_socket(server_socket):

    server_address = (config.SERVER_IP, config.SERVER_PORT)

    server_socket.bind(server_address)
    server_socket.listen(5)

def get_name():
    name = input('\nEnter your server name: ')
    return name

def show_online(name):
    print(f"\n{Colors.GREEN}SERVER: {name} IS ONLINE.{Colors.RESET}\n{Styles.ITALIC}Listening for incoming connections.{Styles.RESET}")

def handle_connection(server_socket,server_uname):
    client_socket, client_address = server_socket.accept()

    connection_id = connection.generate_connection_id()

    client_uname = \
        exchange_initial_data(
            client_socket, 
            server_uname, 
            client_address, 
            connection_id, 
            config.ACTIVE_CONNECTIONS_FILE_PATH)

    handle_client(client_socket, client_uname, connection_id,server_uname)

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        setup_socket(server_socket)
        server_uname = get_name()
        show_online(server_uname)
        while True:  
            handle_connection(server_socket,server_uname)

if __name__ == "__main__":
    run_server()

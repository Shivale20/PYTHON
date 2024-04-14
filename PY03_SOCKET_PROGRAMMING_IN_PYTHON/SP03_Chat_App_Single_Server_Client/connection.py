
from datetime import datetime
import json
import uuid


def generate_connection_id():
    return f"CONN-{uuid.uuid4()}"

# Function to load connections from JSON file

def load_connections(file_path):
    try:
        with open(file_path, 'r') as json_file:
            connections = json.load(json_file)
    except FileNotFoundError:
        connections = []
    return connections

# Function to save latest connections to JSON file
def save_connections(connections, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(connections, json_file, indent=4)

# Function to add a new connection
def add_connection(active_connections_file_path, connection_id, client_address):

    # Load new connections 
    connections = load_connections(active_connections_file_path)

    connection = {
        "id": connection_id,
        "address": client_address[0],
        "port": client_address[1],
        "modified_date": str(datetime.now())
    }

    connections.append(connection)

    # Save the new connection
    save_connections(connections, active_connections_file_path)




# Function to remove a connection
def remove_connection(connection_id, 
                      active_connections_file_path,
                      deleted_connection_file_path ):

    # Load connections
    active_connections = load_connections(active_connections_file_path)

    # Loade deleted connections
    deleted_connections = load_connections(deleted_connection_file_path)

    # Initialize as empty 
    deleted_connection = None

    for connection in active_connections:
        if connection["id"] == connection_id:
            deleted_connection = {
                "id" : connection["id"],
                "address" : connection["address"],
                "port": connection["port"],
                "modified_date": connection["modified_date"]
            }
            deleted_connections.append(deleted_connection)
            active_connections.remove(connection)
            break

    save_connections(active_connections, active_connections_file_path)

    save_connections(deleted_connections, deleted_connection_file_path)

    




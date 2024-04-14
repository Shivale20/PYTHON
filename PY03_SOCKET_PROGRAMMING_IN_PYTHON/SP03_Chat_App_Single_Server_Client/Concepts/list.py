import json
from datetime import datetime

# Function to load connections from JSON file
def load_connections(file_path):
    try:
        with open(file_path, 'r') as json_file:
            connections = json.load(json_file)
    except FileNotFoundError:
        connections = []
    return connections

# Function to save connections to JSON file
def save_connections(connections, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(connections, json_file, indent=4)

# Function to add a new connection
def add_connection(connections, connection_id, client_address):
    connection = {
        "id": connection_id,
        "address": client_address[0],
        "port": client_address[1],
        "modified_date": str(datetime.now())
    }
    connections.append(connection)

# Function to remove a connection
def remove_connection(connections, deleted_connections_file_path, connection_id):
    deleted_connections = load_connections(deleted_connections_file_path)
    
    for connection in connections:
        if connection["id"] == connection_id:
            deleted_connection = {
                "id": connection["id"],
                "address": connection["address"],
                "port": connection["port"],
                "modified_date": connection["modified_date"]
            }
            deleted_connections.append(deleted_connection)
            connections.remove(connection)
            break
    
    save_connections(connections, connections_file_path)
    save_connections(deleted_connections, deleted_connections_file_path)
    
    return connections

# File paths
connections_file_path = "connections.json"
deleted_connections_file_path = "deleted_connections.json"

# Load existing connections or initialize an empty list
connections = load_connections(connections_file_path)

# Load existing deleted connections or initialize an empty list
deleted_connections = load_connections(deleted_connections_file_path)

# Add a new connection
# Add a new connection with a unique ID
add_connection(connections, "C001", ("192.168.1.100", 8080))

# Add a new connection with a different ID
add_connection(connections, "C002", ("192.168.1.101", 8081))

# Add a new connection with the same ID but different IP address and port
add_connection(connections, "C001", ("192.168.1.102", 8082))

# Add a new connection with a different ID and different IP address but same port
add_connection(connections, "C003", ("192.168.1.103", 8080))

# Add a new connection with a different ID, IP address, and port
add_connection(connections, "C004", ("192.168.1.104", 8081))
# Remove a connection
connections = remove_connection(connections, deleted_connections_file_path, "C003")

# Print the updated connections and deleted connections
print("Updated Connections:")
print(connections)
print("\nDeleted Connections:")
print(deleted_connections)

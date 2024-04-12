
from datetime import datetime
import json

# File path to store active connections
active_connections_file = "active_connections.json"

def generate_connection_id():
    now =datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    return f"CONN-{timestamp}"

def update_active_connections_file(active_connections, active_connections_file):
    with open(active_connections_file, "w") as f:
        json.dump(active_connections, f, indent = 4)

def add_in_active_connection(active_connections, connection_id, client_address):
    connection_id = generate_connection_id()
    active_connections.append({"id": connection_id, "address": client_address[0], "port": client_address[1]})
    update_active_connections_file(active_connections, active_connections_file)


def remove_from_active_connection(active_connections, connection_id):
    active_connections = [
                conn for conn in active_connections if conn["id"] != connection_id
            ]
    update_active_connections_file(active_connections, active_connections_file)


def load_active_connections(active_connections, active_connections_file):
    try:
        with open(active_connections_file, "r") as f:
            active_connections = json.load(f)
    except FileNotFoundError:
        active_connections = []
    return active_connections
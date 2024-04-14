import os
# Configuration parameters

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SERVER_IP = '127.0.0.1'
SERVER_PORT = 4571
CLIENT_IP = '127.0.0.1'
CLIENT_PORT = 4571
ACTIVE_CONNECTIONS_FILE_PATH = os.path.join(
    SCRIPT_DIR, "active_connections.json")
DELETED_CONNECTION_FILE_PATH = os.path.join(
    SCRIPT_DIR, "deleted_connections.json")
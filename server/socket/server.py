from request import handleRequests
from database import check_login
import json
import re
import socket


def give_access(method, path, body):
    headers, response_body = handleRequests(method, path, body)
    client_socket.send(headers)
    if response_body != None:
        client_socket.send(response_body)


# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a host and port
server_socket.bind(('127.0.0.1', 9000))

# Start listening for incoming connections
server_socket.listen()

while True:
    try:
        # Accept an incoming connection
        print("Waiting for a connection...")
        client_socket, (client_address, client_port) = server_socket.accept()
        print(f"Client connected from {client_address}:{client_port}")

        # Receive the request
        request = client_socket.recv(1024)

        request_lines = request.decode().splitlines()

        # Get requests parts
        method_path = request_lines[0].split()
        method = method_path[0]
        path = method_path[1]
        version = method_path[2]
        body = request_lines[-1]
        print(f"request: {method} - {path} - {version}")
        give_access(method, path, body)

        # Close the client socket
        client_socket.close()

    except KeyboardInterrupt:
        print("\n--- SERVER SHUT DOWNED ---")
        break

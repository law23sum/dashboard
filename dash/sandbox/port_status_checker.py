import socket

def check_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(("127.0.0.1", port))
            return False  # If it binds successfully, the port is free
        except socket.error as e:
            return True   # If an error is raised, the port is likely in use

port = 4242  # Replace with your port number
if check_port(port):
    print(f"Port {port} is in use.")
else:
    print(f"Port {port} is free.")


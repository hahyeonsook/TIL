import socket
SERVER_NAME = "127.0.0.1"
SERVER_PORT = 12000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input("Input lowercase sentence:")
client_socket.sendto(message.encode(), (SERVER_NAME, SERVER_PORT))
modified_message, _ = client_socket.recvfrom(2048)
print(modified_message)
client_socket.close()

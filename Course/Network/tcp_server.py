import socket
SERVER_PORT = 12000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", SERVER_PORT))

server_socket.listen(1)
print("The server is ready to receive")

while True:
    connection_socket, _ = server_socket.accept()

    sentence = connection_socket.recv(1024)
    capitalized_sentence = sentence.upper()
    connection_socket.send(capitalized_sentence)
    connection_socket.close()

import socket

SERVER_NAME = "127.0.0.1"
SERVER_PORT = 12000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_NAME, SERVER_PORT))
sentence = input("Input lowercase sentence:")
client_socket.send(sentence.encode())
modified_sentence = client_socket.recv(1024)
print(f"From server: {modified_sentence}")
client_socket.close()

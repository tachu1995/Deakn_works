from socket import *

serverName = "127.0.0.1"
serverPort = 11500
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print("server Connected")

firstMessage = "Hello Server"
print(f"Client: {firstMessage}")
clientSocket.send(firstMessage.encode())
while True:
    serverResponse = clientSocket.recv(2048).decode("utf-8")
    print(f"Server: {serverResponse}")
    message = input("Client: ")
    clientSocket.send(message.encode())

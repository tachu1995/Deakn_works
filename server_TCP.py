from socket import *

serverPort = 11500
# creates a TCP socket at the server program
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("Server Online...")

while True:
    connectCl1Socket, clientAddress = serverSocket.accept()
    print("Server Connected")
    while True:
        message = connectCl1Socket.recv(2048)
        message = message.decode("utf-8")  # Decode the message as str
        print(f"Client: {message}")
        response = input("Server: ")
        connectCl1Socket.send(response.encode())

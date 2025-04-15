from socket import *
import json

# Create dictionary which will be used as DNS database
a_records = {
    "example.com": "192.168.1.1",  # example.com maps to 192.168.1.1
    "google.com": "8.8.8.8",  # google.com maps to 8.8.8.8
    "mydomain.com": "192.168.0.10",  # mydomain.com maps to 192.168.0.10
    "example.org": "203.0.113.1",  # example.org maps to 203.0.113.1
    "techsite.com": "198.51.100.20",  # techsite.com maps to 198.51.100.20
}

cname_records = {
    "www.example.com": "example.com",  # www.example.com is an alias for example.com
    "blog.example.com": "example.com",  # blog.example.com is an alias for example.com
    "shop.mydomain.com": "mydomain.com",  # shop.mydomain.com is an alias for mydomain.com
    "mail.google.com": "google.com",  # mail.google.com is an alias for google.com
    "cdn.example.org": "example.org",  # cdn.example.org is an alias for example.org
}

try:
    # Set ServerPort
    serverPort = 11500
    # Create socket as UDP and IPV4
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    # Bind socket and the server port
    serverSocket.bind(("", serverPort))
    # If these seccuess, print message
    print("Server Online.")
except:
    print("Server Failed To Initiate!")


# This is kind of unnessary but it keep the code clean\
def print_query(url):
    print(f"The server was asked to resolve a DNS request of URL: {url}")


while True:
    # Getting the message from the client, along with the clientAddress
    message, clientAddress = serverSocket.recvfrom(2048)
    url = message.decode(
        "utf-8"
    ).lower()  # Decode the message as str, and make it all lower case to match with the record
    print_query(url)

    # Process the in request URL from client
    data = {"url": url}
    if url in a_records:
        data["record"] = "A"
        data["result"] = a_records[url]

    elif url in cname_records:
        data["record"] = "CNAME"
        data["result"] = cname_records[url]
    else:
        data["record"] = "NXDOMAIN"
        data["result"] = None
    # Send the reponse back to the client via the client Address
    serverSocket.sendto(json.dumps(data).encode(), clientAddress)

from socket import *
import json

# Set Server Address and Server Port
serverName = "127.0.0.1"
serverPort = 11500


# Create a send message, which will return the reply response from the server
def dns_query(message):
    # Create A UDP socket with the server address and port, define this as IPV4
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    print("Sending Message to Server.")
    # Catch the response and the Address from the server
    reply, serverAddress = clientSocket.recvfrom(2048)
    # Decode the response and parse the JSON data
    reply = json.loads(reply.decode())
    # Close connection
    clientSocket.close()
    return reply


def print_respose(response):
    print("         ***********************")
    print(
        f"{dnsResponse["url"]}.           {dnsResponse["record"]}           {dnsResponse["result"]}"
    )
    print("         ***********************")


while True:
    print(
        "---------------------------------------------------------------------------------------"
    )
    url = input("Please Enter the URL you want to look up: ")

    dnsResponse = dns_query(url)

    while dnsResponse["record"] == "CNAME":
        print_respose(dnsResponse)
        print(
            f"The DNS query result for {dnsResponse["url"]} returned a CNAME Record, its Alias is {dnsResponse["result"]}"
        )
        answer = input("Do you want to send DNS query for the Alias? (Y/N): ")
        if answer.upper()[0] == "Y":
            dnsResponse = dns_query(dnsResponse["result"])
        else:
            break

    if dnsResponse["record"] == "A":
        print_respose(dnsResponse)
        print(
            f"The DNS query result for  {dnsResponse["url"]} returned a A Record, its IP is {dnsResponse["result"]}"
        )

    elif dnsResponse["record"] == "NXDOMAIN":
        print("DNS Server could not resolve your URL!")

    continueQuery = input("Do you want to look up another URL? (Y/N): ")
    if continueQuery.upper()[0] != "Y":
        print("Thank You, Goodbye!")
        break

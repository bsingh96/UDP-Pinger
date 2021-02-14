import random 

from socket import* 

serverSocket = socket(AF_INET, SOCK_DGRAM) #opening up the socket for udp transfer

serverPort = 50000 #setting the port number to 50000
serverSocket.bind(('127.0.0.1', serverPort)) # binding the socket to the ip and portnumber
print("The Server is ready to receive ( 127.0.0.1 )") # printing the server is ready message

# infinite loop to listen to recieve and encode the client message
while True:
    randomNumb = random.randint(1, 10) #using random functionality to assign
    # a random number between 1-10 
    message, clientAddress = serverSocket.recvfrom(2048) # specify the size of the packet to be sent
    newMessage = message.decode().upper() #decode the recieved message and change it to all uppercase
    if randomNumb >= 3: # if statement to check if the random numb > or = 3
        serverSocket.sendto(newMessage.encode(), clientAddress) # encodes the message and sents to back to client
    else: # if random number is less than 3 than the loop continues and falls out of the else statement
        continue

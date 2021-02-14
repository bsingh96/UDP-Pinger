import numpy
import datetime
from socket import *
from datetime import datetime
import time
clientSocket = socket(AF_INET, SOCK_DGRAM)#opening up the socket for udp transfer
clientSocket.settimeout(2) # setting timeout to 2s
count = 1 # declaring count variable and initializing it to 1
arr = [] # declaring an array to hold the rtt times of each ping
arrSum = 0 # declaring a varriable to keep track of all the rtt sums
try: 
    # try to send a message to the server
    while count <= 10: # while loop to make sure the client can only send 10 messages to the server
        message = ' ping from client  ' + str(count) # message variable declared and set to the message as required
        count += 1  # incrementing count by one each time the a message is sent
        try:
            cT = time.ctime() # getting the time at which message is sent
            currentTime = (time.time() * 1000) 
            clientSocket.sendto(message.encode(), ('127.0.0.1', 50000)) # sending message via udp transfer to the client
            newMessage, serverAddress = clientSocket.recvfrom(2048) # recieve the message back from the client in the specified byte size
            newTime = (time.time() * 1000) # getting the time at which the the message was recieved back
        except timeout: # if there is a timeout display the error
            print(' Request Timed Out ')
        else: # print the message recieved from the server
            RTT_arr = round((newTime - currentTime), 4) # calculate rtt using time recieved - time sent
            arr.append(RTT_arr) # append the rtt times into an array
            arrSum = arrSum + RTT_arr    # increment the rtt sum by each new calculated by each message sent
            time.sleep(1.5) # animation to print each message after 1.5 second
            print(str(newMessage.decode()) + " [ RTT: " + str(RTT_arr) + " ms ]" + ' [' + str(cT) + ']') # print and decode message , rtt , and time sent
            
 
finally: # print the ping statistics
    print('--------------------------------------------------')
    print('              Ping Statistics                     ')
    print('--------------------------------------------------')
    print("Minimum RTT : " + str(min(arr)) + " ms")
    print("Maximum RTT : " + str(max(arr)) + " ms")
    print("Average RTT : " + str((arrSum / len(arr))) + " ms")
    print("Standard Deviation of RTT : " + str(round(numpy.std(arr), 4)) + " ms")
    print("Packet Loss % : " + str((1 - (len(arr) / 10)) * 100) + " %")
    clientSocket.close()

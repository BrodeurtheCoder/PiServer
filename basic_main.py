host = "104.131.22.46" 
port = 2000

time.sleep(25)

while True:
testMessage = "" 
for i in range(16):
testMessage += str(randint(0,9))

	#Networking

s = socket.socket() # COnnects to a socket
s.connect((host, port)) # Connects to server
print "Sending message %s" %testMessage
    s.send(testMessage)                # Sends message to server
    print "Sent message successfully!" 
    s.close()                    # Closes connection to server
    print "Closing connection to server \n" 
    time.sleep(10)                    # Sleeps for n seconds before 
                        # sending again
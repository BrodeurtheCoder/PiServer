import socket, sys, time    # Import socket module
from random import randint

s = socket.socket()
host = "104.131.22.46"
port = 2000
testMessage = ""

for i in range(16):
	testMessage += str(randint(0,9))


s.connect((host, port))

# Do anything and send it below
s.send(testMessage)
print "Message sent successfully!"
s.close()
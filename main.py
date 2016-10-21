import socket, sys, time    # Import socket module

s = socket.socket()
host = "104.131.22.46"
port = 2000

testMessage = "Hello world!"

s.connect((host, port))

# Do anything and send it below
s.send(testMessage)
print "Message sent successfully!"
s.close()
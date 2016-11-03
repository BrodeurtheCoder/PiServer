import socket, sys, time #datetime, SDL_DS32131    # Import socket module
from random import randint

import bluetooth, threading, logging

host = "104.131.22.46"
portWi = 2000

def handler():
	print "Thread started for", child_node
	while True:
		data = client_sock.recv(1024)
		print "Controller node received", data, "from", child_node

		if data == "quit"
			return

server_sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)
portBlue = 0x1001
thread = []

server_sock.bind(("",portBlue))
server_sock.listen(1)
print "Server listening..."

time.sleep(10)		#need to get rid of this at some point

#startTime = datetime.datetime.utcnow()
#ds3231 = SDL_DS3231.SDL_DS3231(1, 0x68)
#ds3231.write_now()

#logging.basicConfig(Level = logging.DEBUG,
#	format='(%(threadName)-5s) %(message)s', )
###UPDATE CODE FROM BUFFER.PY TO THIS TO INTEGRATE ALL THE CODE###


while True:

	#testTimeMessage = [0,0]
	#currentTime = datetime.datetime.utcnow()
	#testTimeMessage[0] = currentTime
	testMessage = ""
	for i in range(8):
		testMessage += str(randint(0,9))

	client_sock, child_address = server_sock.accept()
	child_node = bluetooth.lookup_name(child_address[0])
	print "Server accepted connection from", child_node

	t = threading.Thread(name = child_node, target = handler)
	t.setDaemon(True)
	t.start()
	print "Thread started..."
	main_thread = threading.currentThread()

	for j in threading.enumerate():
        if j is not main_thread:
            print "Joining thread..."
            j.join()
            logging.debug("joined ", j.getName())
        if not threading.enumerate():
            break


	#testTimeMessage[1] = testMessage

	# Networking
	s = socket.socket() 				# Creates n

	# TODO: Implement failure check for connection failing
	s.connect((host, portWi))				# Connects to server

	#print "current time: \t" + currentTime
	#print "testMessage: %s" %testMessage
	#print "Sending testTimeMessage: " + testTimeMessage
	#s.send(testTimeMessage)
	#print "Sent message successfully!"
	#s.close()
	#print "Closing connection to server \n"
	#time.sleep(5)

	print "Sending message %s" %testMessage
	s.send(testMessage)					# Sends message to server
	print "Sent message successfully!"
	s.close()							# Closes connection to server
	print "Closing connection to server \n"
	time.sleep(5)						# Sleeps for n seconds before 
										# sending again



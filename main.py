import socket, sys, time #datetime, SDL_DS32131    # Import socket module
from random import randint

host = "104.131.22.46"
port = 2000

time.sleep(25)		#need to get rid of this at some point

#startTime = datetime.datetime.utcnow()
#ds3231 = SDL_DS3231.SDL_DS3231(1, 0x68)
#ds3231.write_now()


#server_sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)
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

	#testTimeMessage[1] = testMessage

	# Networking
	s = socket.socket() 				# Creates n

	# TODO: Implement failure check for connection failing
	s.connect((host, port))				# Connects to server

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



# real time clock control code for pi 3
# needs to initialize current time, send to all the nodes via bluetooth
# then check time of each of the data packest sent from nodes

import sys, time, datetime, SDL_DS3231

print "Testing code for real time control"

#print "starting time for system" + time.strftime(“%Y-%m-%d %H:%M:%S”)

startTime = datetime.datetime.utcnow()
ds3231 = SDL_DS3231.SDL_DS3231(1, 0x68)
ds3231.write_now()

while True:
	for i in range(10):
		currentTime = datetime.datetime.utcnow()
		changeInTime = currentTime - startTime

		print ""
		print "Pi time: \t" + time.strftime(“%Y-%m-%d %H:%M:%S”)
		print "DS3231 time: \t" + time.strftime(“%Y-%m-%d %H:%M:%S”)
		print "current time: ", currentTime
		print "change in time: ", changeInTime
		time.sleep(10)

# real time clock control code for pi 3
# needs to initialize current time, send to all the nodes via bluetooth
# then check time of each of the data packest sent from nodes

import sys, time, datetime, SDL_DS3231

for i in range(16):
	testMessage += str(randint(0,9))

print ""
print "Testing code for real time control"
print ""
print "starting time for system:" + time.strftime(“%Y-%m-%d %H:%M:%S”)

startTime = datetime.datetime.utcnow()
ds3231 = SDL_DS3231.SDL_DS3231(1, 0x68)
ds3231.write_now()

while True:

	currentTime = datetime.datetime.utcnow()
	changeInTime = currentTime - startTime

	print ""
	print "Pi time: \t", time.strftime(“%Y-%m-%d %H:%M:%S”)
	print "DS3231 time: \t", time.strftime(“%Y-%m-%d %H:%M:%S”)
	print "current time: ", currentTime
	print "change in time: ", changeInTime
	time.sleep(10)
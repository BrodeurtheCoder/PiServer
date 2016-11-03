# reliable data transfer with L2CAP reliable transport protocol - Server
import bluetooth  
import threading
import logging

def handler():      # function for each thread to use 

    print "Thread started for", child_node
    while True:
        data = client_sock.recv(1024)
        print "Server received", data, "from",child_node

        if data == "quit":
            return

server_sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)

# port must be an odd number between 0x1001 and 0x8FFF # server must be
# listening on the same port that the client is initiating a connection to port
portBlue = 0x1001
threads=[]

server_sock.bind(("",portBlue))
server_sock.listen(1)
print "Server listening..."

while True:
    client_sock,child_address = server_sock.accept()
    child_node = bluetooth.lookup_name(child_address[0])
    print "Server accepted connection from",child_node
    
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

client_sock.close()
server_sock.close()
t.stop()
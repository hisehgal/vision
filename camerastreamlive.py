import socket
import time
import sys
import picamera
from thread import *

## https://www.binarytides.com/python-socket-programming-tutorial/
## http://helloraspberrypi.blogspot.com/2015/04/stream-rpi-camera-module-video-to.html

## Connect to my_pi_address = 10.32.59.51
## On VLC >Media >Open Network Stream >Network >Network Protocol
## tcp/h264://my_pi_address:8000/

HOST = ''
PORT = 8001

response = "continue"
msg = ''

with picamera.PiCamera() as camera:
    camera.resolution = (1920,1080)
    camera.framerate = 30

    camera.annotate_text = "Cut Point"
    camera.annotate_background = picamera.Color('black')
    camera.awb_mode = 'auto'
    camera.exposure_mode = 'auto'
    camera.sharpness = 100

    server_socket = socket.socket()
    print('Socket created')

    try:
        server_socket.bind((HOST, PORT))
    except(socket.error, msg):
        print('Bind failed. Error Code: '+str(msg[0]) + ' Message ' + msg[1])
        sys.exit()
    print('Socket bind complete')

    server_socket.listen(10)
    print('Socket now listening')

#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
         
        #Receiving from client
        data = conn.recv(1024)
        reply = 'OK...' + data
        if not data: 
            break
     
        conn.sendall(reply)
     
    #came out of loop
    conn.close()
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = server_socket.accept()
    print(('Connected with ')+ addr[0] + ':' + str(addr[1]))
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
 
s.close()

##    
##    server_socket.bind(('0.0.0.0', 8000))
##    server_socket.listen(0)
##
##    connection = server_socket.accept()[0].makefile('wb')
##    try:
##        camera.start_recording(connection, format='h264')
##        while (response != "end"):
##                camera.wait_recording(5)
##                response = input("Type 'end' to stop stream.")
##                ## User needs to type end into the python 3.5.3 shell
##        camera.stop_recording()
##    finally:
##        connection.close()
##        server_socket.close()
##    sys.exit()

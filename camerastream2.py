import socket
import time
import sys
import picamera

## Connect to my_pi_address = 10.32.59.51
## On VLC >Media >Open Network Stream >Network >Network Protocol
## tcp/h264://my_pi_address:8000/

response = "continue"

with picamera.PiCamera() as camera:
    camera.resolution = (1920,1080)
    camera.framerate = 30

    camera.annotate_text = "Cut Point"
    camera.awb_mode = 'fluorescent'
    camera.exposure_mode = 'auto'
    camera.sharpness = 100
    camera.brightness = 55
    camera.contrast = 95

    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 8000))
    server_socket.listen(0)

    connection = server_socket.accept()[0].makefile('wb')
    try:
        camera.start_recording(connection, format='h264')
        while (response == "continue"):
                response = input("Type anything to stop stream.")
                ## User needs to type end into the python 3.5.3 shell
        camera.stop_recording()
    finally:
        connection.close()
        server_socket.close()
    sys.exit()

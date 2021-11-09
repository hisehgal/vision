import socket
import time
import picamera

## Connect to my_pi_address = 10.32.59.51
## On VLC >Media >Open Network Stream >Network >Network Protocol
## tcp/h264://my_pi_address:8000/

response = "Continue"

with picamera.PiCamera() as camera:
    camera.resolution = (1920,1080)
    camera.framerate = 30

    camera.annotate_text = "Cut Point"
    camera.awb_mode = 'auto'
    camera.exposure_mode = 'auto'
    camera.sharpness = 100

    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 8000))
    server_socket.listen(0)

    connection = server_socket.accept()[0].makefile('wb')
    try:
        camera.start_recording(connection, format='h264')
##        while (response != "end"):
##                camera.wait_recording(1)
##                response = input("Type 'end' to stop stream")
        camera.wait_recording(10)
        camera.stop_recording()
    finally:
        connection.close()
        server_socket.close()

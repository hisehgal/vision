from picamera import PiCamera
from picamera import PiCamera, Color
from time import sleep
import sys

camera = PiCamera()

##camera.resolution = (800,600)

camera.start_preview(fullscreen=False, window = (-270,-500,2592,1944))
camera.annotate_text = "Cut Point"
camera.annotate_text_size = 70 ##6 to 160 default 32
camera.annotate_background = Color('black')
camera.awb_mode = 'fluorescent' ##auto

##for i in range(100):
##    camera.annotate_text = "Brightness: %s" %i
##    camera.brightness = i
##    sleep(0.1)

camera.brightness = 48 ## 1 to 100, default 50
camera.contrast = 100  ## 1 to 100
camera.sharpness = 100
camera.exposure_mode = 'auto'
camera.image_effect = 'none'

##for effect in camera.EXPOSURE_MODES: ##AWB_MODES, IMAGE_EFFECTS, EXPOSURE_MODES
##    camera.exposure_mode = effect
##    camera.annotate_text = "exposure: %s" %effect
##    sleep(2)

response = 'continue'
while (response == 'continue'):
    response = input("Type anything to end the program.")
    
camera.stop_preview()
camera.close()
sys.exit()

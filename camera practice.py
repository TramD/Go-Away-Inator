########################################################################

# This program was used to test the camera and see how it works.

########################################################################

from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO

button = 19

GPIO.setmode(GPIO.BCM)

GPIO.setup(button, GPIO.IN, GPIO.PUD_DOWN)

camera = PiCamera()

try:
    while (True):
        if (GPIO.input(button) == GPIO.HIGH):
            camera.resolution = (250, 200)
            camera.start_preview()
            sleep(5)
            camera.capture('/home/pi/project/image.gif')
            camera.stop_preview()

except KeyboardInterrupt:
    # reset pins
    GPIO.cleanup()

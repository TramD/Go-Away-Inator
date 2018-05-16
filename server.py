###################################################################################

# This program is used on the Pi with the camera, and it will act as the server.
# This Pi will take a picture when the button is pressed and then listen for
# incoming connections. Then it will execute the function to send the image to the
# other Pi(client). When a button is chosen, the Pi will display the GUI from the
# ServerModule program for the chosen button.

###################################################################################


from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
import network
import ServerModule
import socket
import os

# set button pin number to 19
button = 19
# use the Broadcom pin mode
GPIO.setmode(GPIO.BCM)
# setup the input pin
GPIO.setup(button, GPIO.IN, GPIO.PUD_DOWN)
# set camera as a picamera
camera = PiCamera()

# Start Credit: The heard function was edited using the Server example from the following site as the base:
# http://blog.whaleygeek.co.uk/raspberry-pi-internet-of-things-demonstrator/
# function is called when server and client connect
def heard(phrase):

    # display the appropriate GUI for the chosen button
    # check if the phrase sent by client is "1" or "2"
    for a in phrase:
        # calls function from ServerModule program to display Button 1 response
        if (a == "1"):
            #print "Button 1" (Used for testing)
            response = ServerModule.runButton1()
        # calls function from ServerModule program to display Button 2 response    
        elif (a == "2"):
            #print "Button 2" (Used for testing)
            response = ServerModule.runButton2()

# End Credit

    # begins the heard function on the client
    network.say("START")

# Start Credit: The code to send the image file came from the RetrFile function from the following video:
# https://youtu.be/LJTaPaFGmM4?t=5m42s

    # sets the filename that it received from the client
    filename = network.peerHandle.recv(1024)
    
    # checks to see if file exists
    if (os.path.isfile(filename)):
        # send "EXISTS" and the size of the file
        network.peerHandle.send("EXISTS" + str(os.path.getsize(filename)))
        # wait for the response from client if it should start sending
        response = network.peerHandle.recv(1024)

        # if the client send "OK" begin sending file
        if (response[:2] == 'OK'):
            # open the file as read binary
            with open(filename, 'rb') as f:
                # read 1024 bytes of file
                bytesToSend = f.read(1024)
                # send the bytes to the client
                network.peerHandle.send(bytesToSend)
                # if file has more than 1024 bytes
                # read and send bytes until file has no more bytes
                while (bytesToSend != ""):
                    bytesToSend = f.read(1024)
                    network.peerHandle.send(bytesToSend)
    else:
        # send error message if file does not exist
        network.peerHandle.send("ERR ")
	
# End Credit
    
while (True):

        # if the button is pressed
        if (GPIO.input(button) == GPIO.HIGH):
            # set camera resolution
            camera.resolution = (500, 400)
            # show preview of image that will be captured
	    camera.start_preview()
	    # wait for 3 secs
            sleep(3)
            # take the picture and save it as a gif to the folder
	    camera.capture('/home/pi/Final/image.gif')
	    # close the preview window
	    camera.stop_preview()
	    
# Start Credit: The code to start the connection of the server came from Server example from the following site:
# http://blog.whaleygeek.co.uk/raspberry-pi-internet-of-things-demonstrator/
	
            # begin waiting for a connection
            # call heard function when it accepts connection from client
            print "waiting for connection"
            network.wait(whenHearCall=heard)
            print "connected"

            while network.isConnected():
                sleep(1)
                
            # when connection ends print message    
            print "connetion closed"

# End Credit
    

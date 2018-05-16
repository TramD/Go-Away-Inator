###################################################################################

# This program is used on the Pi that will act as the client. This Pi will connect
# with the server and wait to receive the image file. It will save the image
# and then pull up the GUI from the ClientModule program that will display the
# image and two buttons for the user. The ClientModule would send the server an
# indication of which button was pressed.

###################################################################################

import RPi.GPIO as GPIO
import time
import sys
import network
import ClientModule
import socket

# the server IP address is taken from the command line
SERVER_IP = sys.argv[1]
gotResponse = False

# function is called when server and client connect
def heard(phrase):

    # sets the name of the image file
    filename = "image.gif"
    
    # if filename does not equal quit
    if (filename != 'q'):
        # send filename to server
        network.peerHandle.send(filename)
        # wait for response from server if the file exists
        data = network.peerHandle.recv(1024)
        
        # if first six characters of data is "EXISTS", means file exists
        if (data[:6] == 'EXISTS'):
            # get the filesize from the rest of data
            filesize = long(data[6:])
            # indicate yes that you want the file
            message = "Y"

            # if message is "Y" ask server to send file
            if (message == 'Y'):
                # send "OK" to the server to start sending the file
                network.peerHandle.send("OK")
                # open a new file in write binary saved as image.gif
                f = open(filename, 'wb')
                # start receiving the data
                data = network.peerHandle.recv(1024)
                # total amount of data received
                totalRecv = len(data)
                # write data to the new file
                f.write(data)
                
                # if there's more than 1024 bytes of data, continue receiving
                while (totalRecv < filesize):
                    data = network.peerHandle.recv(1024)
                    totalRecv += len(data)
                    f.write(data)

                print ("Download Complete!")

                # close new file
                f.close()

        else:
            # print response if file does not exists in server
            print ("File Does Not Exist!")

    # calls the function that will display the GUI from the ClientModule program
    ClientGUI = ClientModule.run()

# connect to the server and call the heard function once connected    
while(True): 
    try:
        print "connecting to switch server"
        network.call(SERVER_IP, whenHearCall=heard)
        break
    except:
        print "refused"
        time.sleep(1)
print "connected"

while network.isConnected():
    gotResponse = False
    network.say("?")

    while network.isConnected() and not gotResponse:
        time.sleep(1)

# when connection ends print message
print "connection closed"





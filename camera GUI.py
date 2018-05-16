########################################################################

# This program was used to test setting up the GUI for the camera.

########################################################################

from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
from Tkinter import *


button = 19

GPIO.setmode(GPIO.BCM)

GPIO.setup(button, GPIO.IN, GPIO.PUD_DOWN)

camera = PiCamera()

class MainGUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

    def setupGUI(self):

        Grid.columnconfigure(window, 0, weight = 1)
        #for row in range(7):
        #    Grid.rowconfigure(self, row, weight=1)
        #for column in range(2):
        #    Grid.columnconfigure(self, column, weight=1)

        # set up the left of the GUI
        img = PhotoImage(file="image.gif")
        l1 = Label(self.master, image=img)
        l1.image = img
        l1.grid(row=0, column=0, rowspan=2, sticky=N+S+E+W)
        
        # set up top button on the right
        button = Button(self.master, text="Press this button",  command=lambda: self.process("Button 1"))
        button.grid(row=0, column=1, columnspan = 4, sticky=N+S+E+W)

        button = Button(self.master, text="Hello world", command=lambda: self.process("Button 2"))
        button.grid(row=1, column=1, columnspan = 4, sticky=N+S+E+W)

        # oganize the GUI
        #self.pack(fill=BOTH, expand=1)

    def process(self, button):
        if (button == "Button 1"):
            print "This is a test"
        elif (button == "Button 2"):
            print "This is a better test"
        
        
'''
try:
    while (True):
        if (GPIO.input(button) == GPIO.HIGH):
            camera.resolution = (400, 500)
            camera.start_preview()
            sleep(5)
            camera.capture('/home/pi/Desktop/image.jpg')
            camera.stop_preview()

except KeyboardInterrupt:
    # reset pins
    GPIO.cleanup()
'''

####################################################################
# default size of the GUI
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("The Go Away-inator")

p = MainGUI(window)

try:
    while (True):
        if (GPIO.input(button) == GPIO.HIGH):
            camera.resolution = (400, 400)
            camera.start_preview()
            sleep(3)
            camera.capture('/home/pi/project/image.gif')
            camera.stop_preview()
            p.setupGUI()
            window.mainloop()

except KeyboardInterrupt:
    # reset pins
    GPIO.cleanup()


############################################################################

# This program was able to take a picture using the camera, pull up the
# GUI with the picture and buttons, and pull up the response GUI depending
# on the button that was pressed. This only works on one Pi.

############################################################################

from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
from Tkinter import *

# the main GUI
class MainGUI(Frame):

    # the constructor    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

    # sets up the GUI
    def setupGUI(self):
        Grid.columnconfigure(window, 0, weight = 1)

        # set up the left screen of the GUI with the image captured on camera
        img = PhotoImage(file="image.gif")
        l1 = Label(self.master, image=img)
        l1.image = img
        l1.grid(row=0, column=0, rowspan=2, sticky=N+S+E+W)
        
        # set up top button on the right screen of the GUI
        button = Button(self.master, text="Press this button",  command=lambda: self.process("Button 1"))
        button.grid(row=0, column=1, columnspan = 4, sticky=N+S+E+W)

        # set up bottom button on the right screen of the GUI
        button = Button(self.master, text="No, press this button", command=lambda: self.process("Button 2"))
        button.grid(row=1, column=1, columnspan = 4, sticky=N+S+E+W)

    def process(self, button):
        # create a response to button 1 being pressed
        if (button == "Button 1"):
            print "This is a test"
            response = Tk()
            response.geometry("{}x{}".format(WIDTH,HEIGHT))
            response.title("Response Window")
            r = ResGUI(response)
            r.setupRes()
            response.mainloop()

        # create a response to button 2 being pressed            
        elif (button == "Button 2"):
            print "This is a better test"
            response = Tk()
            response.geometry("{}x{}".format(WIDTH,HEIGHT))
            response.title("Response Window")
            r = GUIRes(response)
            r.setupRes()
            response.mainloop()

# Set up the GUI for the response GUI
class ResGUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg="white")
        self.master = master
        
    def setupRes(self):
        display = Label(self.master, text="Swag money", anchor=S, bg="white", height=1, font=("TexGyreAdventor", 30))
        display.grid(row=3, column=0, columnspan=4, rowspan=7, sticky=N+S+E+W)


# Set up the GUI for the response GUI
class GUIRes(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg="white")
        self.master = master
        
    def setupRes(self):
        display = Label(self.master, text="swagger money", anchor=S, bg="white", height=1, font=("TexGyreAdventor", 30))
        display.grid(row=3, column=0, columnspan=4, rowspan=7, sticky=N+S+E+W)


  
        
button = 19

GPIO.setmode(GPIO.BCM)

GPIO.setup(button, GPIO.IN, GPIO.PUD_DOWN)

camera = PiCamera()

####################################################################

WIDTH=400
HEIGHT=400
# create the window
window = Tk()
window.title("The Go Away-inator")

p = MainGUI(window)

try:
    while (True):
        if (GPIO.input(button) == GPIO.HIGH):
            camera.resolution = (500, 400)
            camera.start_preview()
            sleep(3)
            camera.capture('/home/pi/project/image.gif')
            camera.stop_preview()
            p.setupGUI()
            window.mainloop()

except KeyboardInterrupt:
    # reset pins
    GPIO.cleanup()

####################################################################################

# This program is a module that sets up the GUI for the client Pi.
# The GUI will display the receieved image file on the left of the screen and
# two buttons on the right of the screen. After 10 secs, the GUI will close itself
# and the connection with the server will end. The buttons will send an indication
# to the server Pi of which button was pressed so that the approproate GUI will
# be displayed on the server Pi.

####################################################################################


from picamera import PiCamera
from time import sleep
from Tkinter import *
import RPi.GPIO as GPIO
import network

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
        button = Button(self.master, text="I'll be at the door shortly!",  command=lambda: self.process("Button 1"))
        button.grid(row=0, column=1, columnspan = 4, sticky=N+S+E+W)

        # set up bottom button on the right screen of the GUI
        button = Button(self.master, text="Sorry, No one is home, Go Away!", command=lambda: self.process("Button 2"))
        button.grid(row=1, column=1, columnspan = 4, sticky=N+S+E+W)

    def process(self, button):
        # "1" will be sent to the server to indicate that button 1 was pressed
        if (button == "Button 1"):
            #print "Button 1" (Used to test if the correct button was pressed)
            network.say("1")

        # "2" will be sent to the server to indicate that button 2 was pressed
        elif (button == "Button 2"):
            #print "Button 2" (Used to test if the correct button was pressed)
            network.say("2")

            
# displays the GUI 
def run():
    global window, WIDTH, HEIGHT
    
    WIDTH=400
    HEIGHT=400

    # create the window
    window = Tk()
    window.after(10000, lambda:window.destroy())
    window.title("The Go Away-inator")
    p = MainGUI(window)

    # display the GUI
    while (True):
        p.setupGUI()
        window.mainloop()

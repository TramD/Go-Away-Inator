###############################################################################

# This program is a module that sets up the response GUI for the server Pi.
# Depending on which button was pressed by the client Pi, the module would
# open the appropriate GUI for that button.

###############################################################################


from picamera import PiCamera
from time import sleep
from Tkinter import *
import RPi.GPIO as GPIO

# Set up the GUI as the response for button 1
class Button1(Frame):

    # the constructor
    # sets background to white and the window to fullscreen
    def __init__(self, master):
        Frame.__init__(self, master, bg="white")
        master.attributes("-fullscreen", True)
        self.master = master

    # sets up the GUI
    def setupRes(self):

        # display the text centered with a white background
        # font is "TexGyreAdventor" and fontsize is 50
        # pack so that it fills the entire screen
        display = Label(self.master, text="I'll be at the door shortly!",\
                        anchor=CENTER, bg="white", height=11,\
                        font=("TexGyreAdventor", 50))
        display.grid(row=3, column=0, columnspan=5, rowspan=8, sticky=N+S+E+W)
        display.pack(fill=BOTH)


# Set up the GUI as the response for button 2
class Button2(Frame):

    # the constructor
    # sets background to white and the window to fullscreen
    def __init__(self, master):
        Frame.__init__(self, master, bg="white")
        master.attributes("-fullscreen", True)
        self.master = master

    # sets up the GUI
    def setupRes(self):

        # display the text centered with a white background
        # font is "TexGyreAdventor" and fontsize is 50
        # pack so that it fills the entire screen
        display = Label(self.master, text="Sorry, No one is home.\n\nGo Away!",\
                        anchor=CENTER, bg="white", height=11,\
                        font=("TexGyreAdventor", 50))
        display.grid(row=3, column=0, columnspan=5, rowspan=8, sticky=N+S+E+W)
        display.pack(fill=BOTH)


# display the GUI for Button 1
def runButton1():
    
    # create the window
    response = Tk()
    response.after(5000, lambda: response.destroy()) 
    response.title("Response Window")
    r = Button1(response)

    # display the GUI
    while (True):
        r.setupRes()
        response.mainloop()
    
# display the GUI for Button 2    
def runButton2():

    # create the window
    response = Tk()
    response.after(5000, lambda: response.destroy()) 
    response.title("Response Window")
    r = Button2(response)

    # display the GUI
    while (True):
        r.setupRes()
        response.mainloop()
    


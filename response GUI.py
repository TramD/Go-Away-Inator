########################################################################

# This program was used to test setting up the response GUI for each of
# the buttons so that it displays a message when it is pressed.

########################################################################


from Tkinter import *

# Set up the GUI for the response GUI
class ResGUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg="white")
        self.setupGUI()
        
    def setupGUI(self):

        display = Label(self.master, text="Say something", anchor=S, bg="white", height=1, font=("TexGyreAdventor", 30))
        display.grid(row=3, column=0, columnspan=4, rowspan=7, sticky=N+S+E+W)

        #Grid.columnconfigure(response, 0, weight = 1)
        #Grid.rowconfigure(response, 0, weight = 1)
        for row in range(7):
            Grid.rowconfigure(self, row, weight=1)
        for column in range(2):
            Grid.columnconfigure(self, column, weight=1)

        # set up the left of the GUI
        
        #r1 = Label(self.master, text="No one is home")
        
        #r1.grid(row=2, column=1, rowspan=7, columnspan=2, sticky=N+S+E+W)

    def process(self, button):
        pass


WIDTH = 400
HEIGHT = 400
# create the response
response = Tk()
response.geometry("{}x{}".format(WIDTH, HEIGHT))
response.title("Response Window")

r = ResGUI(response)

response.mainloop()

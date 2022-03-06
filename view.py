from tkinter import *

class View:

    def __init__(self, screen):
        self.screen = screen
        
    
    def seeScreen(self):
        self.message = Label(self.screen, text = "hi")
        self.message.pack()

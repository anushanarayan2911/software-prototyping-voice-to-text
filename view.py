from tkinter import *

class View:

    def __init__(self, screen):
        self.screen = screen
        self.startButton = Button(self.screen, text = "Start")
        self.startButton.pack()
    
    def seeScreen(self):
        self.startButton.pack()

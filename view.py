from tkinter import *

class View:

    def __init__(self, screen):
        self.screen = screen
        self.startButton = Button(self.screen, text = "Start")
        self.startButton.pack()
    
    def displayInstructions(self, instruction):
        self.instructionsLabel = Label(self.screen, text = instruction)
        self.instructionsLabel.pack()


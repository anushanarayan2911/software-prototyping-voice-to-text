from email.mime import image
from tkinter import *
from PIL import Image

class View:

    def __init__(self, screen):
        self.screen = screen

        self.startButton = Button(self.screen, text = "Start")
        self.startButton.pack()

    def displayInstructions(self, instruction):
        self.instructionsLabel = Label(self.screen, text = instruction)
        self.instructionsLabel.pack()
    
    def displayImage(self, imageAddress):

        img = PhotoImage(file = imageAddress)

        self.imageLabel = Label(self.screen, image = img)
        self.imageLabel.photo = img
        self.imageLabel.pack()   
        


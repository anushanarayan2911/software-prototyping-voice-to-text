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
    
    def displayImage(self): 
        img = PhotoImage(file="shoes.png")

        scaleWidth = 1/2
        scaleHeight = 1/2
        img.zoom(10, 2)

        self.imageLabel = Label(self.screen, image = img)
        self.imageLabel.photo = img
        self.imageLabel.pack()   
        print("hi")
        


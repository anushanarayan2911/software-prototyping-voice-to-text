from model import Model
from view import View
from tkinter import *

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.startButton.bind("<Button>", self.getSpeech)

    def getSpeech(self, event):
        #speech = self.model.getSpeech()
        #self.view.displayInstructions(speech)
        self.view.displayImage()
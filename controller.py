from model import Model
from view import View
from data import Data
from tkinter import *

class Controller:
    def __init__(self, model, view, data):
        self.model = model
        self.view = view
        self.data = data
        self.view.startButton.bind("<Button>", self.getSpeech)

    def getSpeech(self, event):
        speech = self.model.getSpeech()
        self.view.displayInstructions(speech)
        imageItem = ""

        for item in self.data.dataset:
            if item in speech:
                imageItem = item

        imageAddress = imageItem + ".png"
        self.view.displayImage(imageAddress)
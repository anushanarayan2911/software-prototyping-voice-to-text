from model import Model
from view import View
from tkinter import *

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def getSpeech(self):
        self.model.getSpeech()
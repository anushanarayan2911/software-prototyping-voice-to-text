from model import Model

class Controller:
    def __init__(self, model):
        self.model = model

    def getSpeech(self):
        self.model.getSpeech()
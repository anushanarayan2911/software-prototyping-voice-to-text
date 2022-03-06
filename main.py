from model import Model
from controller import Controller

def main():
    
    model = Model()
    controller = Controller(model)
    controller.getSpeech()
    

if __name__ == "__main__":
    main()
from model import Model
from view import View
from controller import Controller
from data import Data
from tkinter import *

def main(): 
    
    screen = Tk()
    screen.title("Voice To Text")
    screen.geometry("500x500")
    
    model = Model()
    view = View(screen)
    data = Data()
    controller = Controller(model, view, data)
    screen.mainloop()
    

if __name__ == "__main__":
    main()
from PIL import Image, ImageTk
import tkinter as tk
from detail_window import DetailWindow

#La definimos en una clase aparte para mayor comodidad en las modificaciones
class Cell:
    def __init__(self, title, path, description):
        self.title = title
        self.path = path
        self.description = description
        self.load_and_resize_image()

    def load_and_resize_image(self):
        im_original = Image.open(self.path)
        im_modificada = im_original.resize((100,100), Image.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(im_modificada)
        return im_modificada


    
        

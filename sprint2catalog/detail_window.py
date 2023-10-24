import tkinter as tk
from PIL import Image, ImageTk

class DetailWindow:
    def __init__(self, root, title, path, description):
        self.root = root
        root.title("Información")
        
        #para q dentro de la ventana emergente se visualice el título
        self.title = tk.Label(root, text=title)
        self.title.pack()

        #para q dentro de la ventana emergente se visualice la descipción
        self.description = tk.Label(root, text=description) 
        self.description.pack()
        
        #para q dentro de la ventana emergente se visualice la imagen
        self.path = tk.Label(root, image=path) 
        self.path.pack()
        
        
        root.title(title)




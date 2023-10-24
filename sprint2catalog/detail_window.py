import tkinter as tk
from PIL import Image, ImageTk

class DetailWindow:
    def __init__(self, root, title, path, description):
        self.root = root
        
        #para que dentro de la ventana emergente se visualice el título
        self.title = tk.Label(root, text=title)
        self.title.pack()

        #para que dentro de la ventana emergente se visualice la descipción
        self.description = tk.Label(root, text=description) 
        self.description.pack()
        
        #para que dentro de la ventana emergente se visualice la imagen
        self.path = tk.Label(root, image=path) 
        self.path.pack()
        
        
        root.title(title)

        #Con estas líneas ajustamos la ventana al centro de la pantalla
        #En este caso, modificamos la x para que quede más en el medio
        x = (self.root.winfo_screenwidth() - 6*(self.root.winfo_reqwidth())) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}")




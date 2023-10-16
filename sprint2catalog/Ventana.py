import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from cell import Cell
from PIL import Image, ImageTk
from detail_window import DetailWindow



class MainWindow():
    image_references = []
    def on_button_clicked(self,cell):
        DetailWindow(cell)
        
    def __init__(self, root):
        root.title("MainWindow")

        #Inicializamos el listado de celdas:
        self.cells = [
            Cell("gatito", "C:\\msys64\\home\\Alumno\\DID\\sprint1Tkinter\\catalog\\data\\unedited\\gatito.jpg", "El gato doméstico (Felis silvestris catus), llamado más comúnmente gato, y de forma coloquial minino, michino, michi, micho, mizo, miz, morroño o morrongo, y algunos nombres más, es un mamífero carnívoro de la familia Felidae."),
            Cell("jirafita", "C:\\msys64\\home\\Alumno\\DID\\sprint1Tkinter\\catalog\\data\\unedited\\jirafita.jpg", "La jirafa (Giraffa camelopardalis) es una especie de mamífero artiodáctilo, de la familia Giraffidae propio de África. Es la más alta de todas las especies de animales terrestres existentes."),
            Cell("leoncito", "C:\\msys64\\home\\Alumno\\DID\\sprint1Tkinter\\catalog\\data\\unedited\\leoncito.jpg", "El león (Panthera leo) es un mamífero carnívoro de la familia de los félidos y una de las cinco especies del género Panthera. Los leones salvajes viven en poblaciones cada vez más dispersas."),
            Cell("patito", "C:\\msys64\\home\\Alumno\\DID\\sprint1Tkinter\\catalog\\data\\unedited\\patito.jpg", "Pato es el nombre común para ciertas aves de la familia Anatidae, principalmente de la subfamilia Anatinae y dentro de ella del género Anas."),
            Cell("quokka", "C:\\msys64\\home\\Alumno\\DID\\sprint1Tkinter\\catalog\\data\\unedited\\quokka.jpg", "El quokka (Setonix brachyurus, /kwɒkə/)es un pequeño Macropodidae del tamaño de un gato doméstico. Es el único miembro del género Setonix.")
        ]

        for i, cell in enumerate(self.cells):
            #Aquí transformamos las imágenes sin editar al formato deseado
            fotito = Image.open(cell.path)
            n_fotito = fotito.resize((100,100), Image.Resampling.LANCZOS)
            cell.image_tk = ImageTk.PhotoImage(n_fotito)


            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM) #compound nos indica como se va a posicionar la imagen con respecto al texto
            label.grid(row=i, column=0)#para meterlos en una columna, lo anterior era fila
            label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))#Este método escucha eventos sobre los widgets que estamos programando, para ver qué hacemos con él

    
                        

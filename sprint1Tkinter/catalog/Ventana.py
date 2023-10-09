from tkinter import Tk, ttk
from cell import Cell
from tkinter import messagebox 
import tkinter as tk

class MainWindow():
    
    def on_button_clicked(cell):
        message = "Has hecho click en la celda "+ cell.title
        messagebox.showinfo("Información" + message)

    def __init__(self, root):
        root.title("MainWindow")

        #Inicializamos el listado de celdas:
        self.cells = [
            Cell("gatito", "C:\\msys64\\home\\Alumno\\DID\\sprint1Tkinter\\catalog\\data\\edited\\gatito.jpg"),
            Cell("jirafita", "C:\\msys64\\home\\Alumno\\DID\\sprint1Tkinter\\catalog\\data\\edited\\jirafita.jpg"),
            Cell("leoncito", "C:\\msys64\\home\\Alumno\\DID\\sprint1Tkinter\\catalog\\data\\edited\\leoncito.jpg"),
            Cell("patito", "C:\\msys64\\home\\Alumno\\DID\\sprint1Tkinter\\catalog\\data\\edited\\patito.jpg"),
            Cell("quokka", "C:\\msys64\\home\\Alumno\\DID\\sprint1Tkinter\\catalog\\data\\edited\\quokka.jpg")
        ]

        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM) #compound nos indica como se va a posicionar la imagen con respecto al texto
            label.grid(row=i, column=0)#para meterlos en una columna, lo anterior era fila
            label.bind("Button-1", lambda event, cell = cell: self.on_button_clicked)#Este método escucha eventos sobre los widgets que estamos programando, para ver qué hacemos con él
                        

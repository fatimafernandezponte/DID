from tkinter import Tk, ttk
from cell import Cell
from tkinter import messagebox 
import tkinter as tk
from PIL import Image, ImageTk

class MainWindow():
    
    def on_button_clicked(cell):
        message = "Has hecho click en la celda "+ cell.title
        messagebox.showinfo("Información" + message)

    def __init__(self, root):
        root.title("MainWindow")

        #Inicializamos el listado de celdas:
        self.cells = [
            Cell("gatito", "C:\\msys64\\home\\Alumno\\DID\\sprint1Tkinter\\catalog\\data\\unedited\\gatito.jpg"),
            Cell("jirafita", "C:\\msys64\\home\\Alumno\\DID\\sprint1Tkinter\\catalog\\data\\unedited\\jirafita.jpg"),
            Cell("leoncito", "C:\\msys64\\home\\Alumno\\DID\\sprint1Tkinter\\catalog\\data\\unedited\\leoncito.jpg"),
            Cell("patito", "C:\\msys64\\home\\Alumno\\DID\\sprint1Tkinter\\catalog\\data\\unedited\\patito.jpg"),
            Cell("quokka", "C:\\msys64\\home\\Alumno\\DID\\sprint1Tkinter\\catalog\\data\\unedited\\quokka.jpg")
        ]

        for i, cell in enumerate(self.cells):
            #Aquí transformamos las imágenes sin editar al formato deseado
            fotito = Image.open(cell.path)
            n_fotito = fotito.resize((100,100),Image.Resampling.LANCZOS)

            cell.image_tk = ImageTk.PhotoImage(n_fotito)


            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM) #compound nos indica como se va a posicionar la imagen con respecto al texto
            label.grid(row=i, column=0)#para meterlos en una columna, lo anterior era fila
            label.bind("Button-1", lambda event, cell = cell: self.on_button_clicked)#Este método escucha eventos sobre los widgets que estamos programando, para ver qué hacemos con él
                        

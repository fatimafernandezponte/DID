import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO
from cell import Cell
from detail_window import DetailWindow
from tkinter import messagebox



class MainWindow():
    def on_button_clicked(self,cell):
        root = tk.Toplevel()
        detailWindow = DetailWindow(root, cell.title, cell.path, cell.description)

    #Lo utilizamos en  el menú
    def acerca_de_presionado(self):
            mensaje = "Fátima es una chica chulísima" #Este es el mensaje que se mostrará cuando clickes en "Acerca de"
            messagebox.showinfo("Acerca de la desarrolladora", mensaje) #Al usar una coma, lo primero será el nombre de la ventana y lo segundo, el mensaje que se mostrará en ella, el que creamos arriba 
    
    def __init__(self, root, json_data):
         self.root = root
         root.title("Listado")
         self.datos = [] #Creo una lista para guardar las celdas

         for dato in json_data:
            #Extraigo cada uno de los datos en sus respectivas variables
            nombre = dato.get("name")
            descripcion = dato.get("description")

            #Para descargar la imagen y no enviarla como una simple url hacemos esto
            url = dato.get("image_url")
            imagen = self.load_image_from_url(url)

            #Creo una celda para cada objeto(dato) y la incluyo en la lista
            self.datos.append(Cell(nombre,imagen,descripcion))
        
         for i, cell in enumerate(self.datos):
            label = tk.Label(root, image=cell.path, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0) 
            label.bind("<Button-1>", lambda event, celda = cell: self.on_button_clicked(celda))

        #Aquí creamos el menú
         barra_menus = tk.Menu() #Instanciamos que va a haber un menú
         menu_ayuda = tk.Menu(barra_menus, tearoff=False) #Elementos que aparecerán en el menú
         menu_ayuda.add_command (
             label = "Acerca de",
             command=self.acerca_de_presionado, #Créalo
         ) #Asignamos el valor y lo que va a hacer el elemento
         barra_menus.add_cascade(menu=menu_ayuda, label="Ayuda") #Nombramos el menú y le añadimos el elemento que acabamos de crear
         root.config(menu=barra_menus) #Con esto visualizamos el menú
    
        


        #Con estas líneas ajustamos la ventana al centro de la pantalla
         x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
         #En este caso, modificamos la y para que quede la altura más centrada
         y = (self.root.winfo_screenheight() - 3*(self.root.winfo_reqheight())) / 2
         self.root.geometry(f"+{int(x)}+{int(y)}")
            
    def load_image_from_url(self, url):
        response = requests.get(url)
        img_data = Image.open(BytesIO(response.content))
        img = ImageTk.PhotoImage(img_data)
        return img
    
    

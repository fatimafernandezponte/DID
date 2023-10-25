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
        

         #Creación de una scrollbar
         self.canvas = tk.Canvas(self.root)
         self.scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview) #Creamos la barra de desplazamiento y le proporcionamos una orientación
         self.scrollable_frame = tk.Frame(self.canvas) #Esto es el contenedor del canvas

         self.scrollable_frame.bind( #Con esto, cada vez que el frame cambie de tamaño, se actualiza la región de desplazamiento
             "<Configure>",
             lambda e: self.canvas.configure(
                 scrollregion=self.canvas.bbox("all")
             )
         )

         self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw") #Así colocamos el frame dentro del canvas
         self.canvas.configure(yscrollcommand=self.scrollbar.set) #Así hacemos que se actualice la barra de desplazamiento cuando  se desplaza el canvas

        #MODIFICADO EN EL 7 
         for cell in self.datos:
            self.add_item(cell)
                  
         self.canvas.grid(row=0, column=0, sticky="nsew") #Posiciona el canvas en la ventana principal y hace que se expanda con la ventana
         self.scrollbar.grid(row=0, column=1, sticky="ns") #Posiciona la barra de desplazamiento al lado del canvas, hace que se pueda expandir en vertical

         self.root.grid_rowconfigure(0, weight=1) #La fila va a pesar 1 y permite que se pueda redimensionar con la ventana
         self.root.grid_columnconfigure(0, weight=1) #Lo mismo que lo anterior pero con columna

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
         #Modificamos creando variables para que tenga un tamaño concreto para poder mostrar el scrollbar
         anchura=150
         altura=230
         self.root.geometry(f"{anchura}x{altura}")
         x = (self.root.winfo_screenwidth() - anchura)/2
         y = (self.root.winfo_screenheight() - altura)/2
         self.root.geometry(f"+{int(x)}+{int(y)}")

    #EJERCICIO 7. Este método nos permite que se visualicen las imágenes al mismo tiempo que las encapsula dentro del frame
    def add_item(self, cell):
        frame = tk.Frame(self.scrollable_frame)
        frame.pack(pady=10)

        label = tk.Label(frame, image=cell.path, text=cell.title, compound=tk.BOTTOM)
        label.grid(row=0, column=0) 
        label.bind("<Button-1>", lambda event, celda = cell: self.on_button_clicked(celda))
            
    def load_image_from_url(self, url):
        response = requests.get(url)
        img_data = Image.open(BytesIO(response.content))
        img = ImageTk.PhotoImage(img_data)
        return img
    
    
    
    

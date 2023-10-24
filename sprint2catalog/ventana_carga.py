import tkinter as tk
import threading
import requests
from Ventana import MainWindow

class LoadingWindow:
    def __init__(self, root):
        self.finished = False
        self.root = root
        self.root.title("Cargando...")
        self.root.geometry("170x120")
        self.root.resizable(False, False)

        self.label = tk.Label(self.root, text="Cargando datos...", font=("Arial", 14))
        self.label.pack(side=tk.TOP, pady=10)

        #Aquí creamos una variable bg
        label_bg_color = self.label.cget("bg")

        #Metemos el color de fondo en la variable bg para que no quede feo
        self.canvas = tk.Canvas(self.root, width=60, height=60, bg=label_bg_color)
        self.canvas.pack()

        self.progress = 0
        self.draw_progress_circle(self.progress)
        self.update_progress_circle()


        #hILO PARA LA PETICIÓN DE RED
        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()
        if self.thread.is_alive():
             self.check_thread()



    def draw_progress_circle(self, progress):
        self.canvas.delete("progress")
        angle = int(360 * (progress / 100))

        self.canvas.create_arc(10, 10, 35, 35, 
                               start=0, extent=angle, tags="progress", outline='green', width=4, style=tk.ARC)
    
    def update_progress_circle(self):
        #Aquí le decimos que tiene que completarse, a diferencia del ejemplo
        if self.progress < 90:
            self.progress += 10
        else:
            if self.progress > 89 and self.progress <=100:
                self.progress +=1
            else:
                self.progress = 0
            
        
        self.draw_progress_circle(self.progress)
        self.root.after(100, self.update_progress_circle)


    

    #Aquí enviamos el contenido del json a la nueva ventana
    def fetch_json_data(self):
        response = requests.get("https://raw.githubusercontent.com/fatimafernandezponte/DID/main/catalog.json")
        if response.status_code == 200:
            self.json_data = response.json()
            self.finished=True
            #Imprimimos el json para comprobar que se ha descargado
            #print(response.json())

            #Aquí hacemos que se cierre la ventana de carga
            self.root.quit()

    def check_thread(self):
            if self.finished:
                self.root.destroy()
                launch_main_window(self.json_data)
            else:
                self.root.after(100,self.check_thread)

    #Creamos aquí la nueva ventana
def launch_main_window(json_data):
        root =tk.Tk()
        app = MainWindow(root,json_data)
        root.mainloop()

    



        

        


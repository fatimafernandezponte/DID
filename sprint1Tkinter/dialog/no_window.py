import tkinter as tk

#Creamos la ventana que se mostrará si clickas no
def show_noWindow(self, no_root):
    self.no_root=no_root
    no_root.title("Casilla del no")
    self.frame=tk.Frame(self.no_root)
    self.frame.pack()

    self.label=tk.Label(self.frame, text="Pues debería apetecerte una tarta")
    self.label.pack()
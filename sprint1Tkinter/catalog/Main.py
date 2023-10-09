from tkinter import Tk
from Ventana import MainWindow

if __name__=="__main__":

    root = Tk()
    app = MainWindow(root) #La que acabamos de crear en el propio main
    root.mainloop() #Bucle de ejecución principal
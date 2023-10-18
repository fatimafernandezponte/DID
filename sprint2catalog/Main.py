from tkinter import Tk
from Ventana import MainWindow
from ventana_carga import LoadingWindow

if __name__=="__main__":
    root = Tk()
    app = LoadingWindow(root)
    root.mainloop()

    

    #app = MainWindow(root) #La que acabamos de crear en el propio main
    #root.mainloop() #Bucle de ejecución principal
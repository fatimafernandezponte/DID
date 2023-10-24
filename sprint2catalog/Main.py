from tkinter import Tk
from ventana_carga import LoadingWindow, launch_main_window

if __name__=="__main__":
    root = Tk()
    app = LoadingWindow(root)
    root.mainloop()

   # app = MainWindow(root) #La que acabamos de crear en el propio main
   # root.mainloop() #Bucle de ejecución principal
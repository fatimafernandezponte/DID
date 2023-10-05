from tkinter import Tk, ttk, Button
from yes_window import show_yesWindow
from no_window import show_noWindow

class MainWindow:
    def on_button1_click(self):
        yes_root=Tk()
        button1 = show_yesWindow(self,yes_root)
        yes_root.mainloop()
    def on_button2_click(self):
        no_root=Tk()
        button2 =show_noWindow(self,no_root)
        no_root.mainloop()

    def __init__(self, root):
        self.root = root
        root.title("La cuestión de la tarta")
        self.frame=ttk.Frame(self.root)
        self.frame.pack()

        self.label=ttk.Label(self.frame,text="¿Te apetece una tarta?")
        self.label.pack()


        self.button1 = ttk.Button(self.root, text="Sí", command = self.on_button1_click)
        self.button1.pack(side="left", fill="x", expand=True, anchor="nw")
        self.button2 = ttk.Button(self.root, text="No", command = self.on_button2_click)
        self.button2.pack(side="right", fill="x", expand=True, anchor="nw")
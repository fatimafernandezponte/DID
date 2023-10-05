import tkinter as tk


def show_yesWindow(self, yes_root):
    self.yes_root= yes_root
    yes_root.title("Casilla del sí")
    self.frame=tk.Frame(self.yes_root)
    self.frame.pack()

    self.label=tk.Label(self.frame, text="A mí también me apetece una tarta")
    self.label.pack()
    

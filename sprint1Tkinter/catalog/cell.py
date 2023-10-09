from PIL import ImageTk

#La definimos en una clase aparte para mayor comodidad en las modificaciones
class Cell:
    def __init__(self,title,path):
        self.title = title
        self.path = path
        self.image_tk = ImageTk.PhotoImage(file=self.path)
        

from tkinter import *
from collections import namedtuple
from PIL import Image, ImageTk

ImgSize = namedtuple('ImgSize',['X','Y'])

class Window(Frame):
    maxheight = 1050
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        with Image.open("static/tizen_remote.png") as load: 
            img_size = ImgSize._make(load.size)
            print("Image Size : x={},y={}".format(img_size.X,img_size.Y))
            scalefactor = self.maxheight/img_size.Y
            new_size = ImgSize(int(img_size.X * scalefactor) , int(img_size.Y * scalefactor))
            print("New Size = {}x{}".format(new_size.X,new_size.Y))
            load = load.resize((new_size.X,new_size.Y), Image.ANTIALIAS)
            self.geometry = new_size
            render = ImageTk.PhotoImage(load)
            img = Label(self, image=render)
            img.image = render
            img.place(x=0, y=0)
            


root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.geometry("{}x{}".format(app.geometry.X,app.geometry.Y))
root.mainloop()



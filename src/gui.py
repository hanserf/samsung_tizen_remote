from tkinter import *
from collections import namedtuple
from PIL import Image, ImageTk

ImgSize = namedtuple('ImgSize', ['X', 'Y'])


class Window(Frame):
    maxheight = 1000

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        with Image.open("static/tizen_remote.png") as load:
            img_size = ImgSize._make(load.size)
            print("Image Size : x={},y={}".format(img_size.X, img_size.Y))
            scalefactor = self.maxheight / img_size.Y
            new_size = ImgSize(int(img_size.X * scalefactor), int(img_size.Y * scalefactor))
            print("New Size = {}x{}".format(new_size.X, new_size.Y))
            load = load.resize((new_size.X, new_size.Y), Image.ANTIALIAS)
            self.geometry = new_size
            render = ImageTk.PhotoImage(load)
            img = Label(self, image=render)
            img.image = render
            img.place(x=0, y=0)
            self.my_image = render



def test():
    root = Tk()
    app = Window(root)
    root.wm_title("Tkinter window")
    root.geometry("{}x{}".format(app.geometry.X, app.geometry.Y))

    canvas = Canvas(master=root, height=1080, width=app.geometry.Y)
    canvas.bind("<Button-1>", button_click)
    # The above command means whenever <Button-1> (left mouse button) is clicked
    # within your canvas, the button_click function will be called.
    canvas.pack()
    canvas.create_image(app.geometry.X / 2, app.geometry.Y / 2, image=app.my_image)

    root.mainloop()


if __name__ == '__main__':
    test()


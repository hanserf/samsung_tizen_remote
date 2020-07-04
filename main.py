from tkinter import *
from collections import namedtuple
from PIL import Image, ImageTk

ImgSize = namedtuple('ImgSize',['X','Y'])

class Window(Frame):
    maxheight = 1000
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
            self.my_image = render

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        # (x1, y1) is the upper left point of the rectangle
        # (x2, y2) is the lower right point of the rectangle
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        return

    def contains(self, newx, newy):
        # Will return true if the point (newx, newy) lies within the rectangle.
        # False otherwise.
        return (self.x1 <= newx <= self.x2) and (self.y1 <= newy <= self.y2)

def button_click(event):
    # The location of the click is stored in event sent by tkinter
    # and can be accessed like:
    print("You clicked ({}, {})".format(event.x, event.y))

    ## Now that you're in here, you can determine if the user clicked
    ## inside one of your buttons. If they did, perform the action that
    ## you want. For example, I've created two rectangle objects which
    ## simulate the location of some.

    button1_rect = Rectangle( 100, 100, 200, 200 )
    button2_rect = Rectangle( 300, 300, 400, 400 )
    # Change the rectangles to reflect your own button locations.

    if button1_rect.contains(event.x, event.y):
        print("You clicked button number 1!")

    if button2_rect.contains(event.x, event.y):
        print("You clicked button number 2!")


    return


def main():
    root = Tk()
    app = Window(root)
    root.wm_title("Tkinter window")
    root.geometry("{}x{}".format(app.geometry.X, app.geometry.Y))

    canvas = Canvas(master=root, height=1080, width=app.geometry.Y)
    canvas.bind("<Button-1>", button_click)
    # The above command means whenever <Button-1> (left mouse button) is clicked
    # within your canvas, the button_click function will be called.
    canvas.pack()
    canvas.create_image(app.geometry.X/2,app.geometry.Y/2,image=app.my_image)

    root.mainloop()

if __name__ == '__main__':
    main()


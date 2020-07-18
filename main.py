from tkinter import *
import argparse
from src.gui import Window
from src.remote_jsonparser import RemoteJsonParser,JSONParseError,myRemote

parser = argparse.ArgumentParser(description='TizenRemote')
parser.add_argument('-ip','--ip_address', required=True, dest="ip", type=str, nargs=1, help="TV-IP address")
parser.add_argument('-if','--input_file', dest='input_file', type=str,default="static/keymap_samsung_tizen.json",nargs=1, help="Keymap file")
parser.add_argument('-v','--verbose', dest="verbose", action='store_true', help="Prints debug info")
dbg_print = False
args = vars(parser.parse_args())
if args['verbose']:
    dbg_print=True

remote = RemoteJsonParser(args['input_file'],debug_print=dbg_print)
keymap = myRemote(buttons=remote.myremote.buttons,rectangle=remote.myremote.rectangle)

def button_click(event):
    # The location of the click is stored in event sent by tkinter
    # and can be accessed like:
    if dbg_print:
        print("You clicked ({}, {})".format(event.x, event.y))
    ## Now that you're in here, you can determine if the user clicked
    ## inside one of your buttons. If they did, perform the action that
    ## you want. For example, I've created two rectangle objects which
    ## simulate the location of some.

    # Change the rectangles to reflect your own button locations.

    for cnt,btn in enumerate(keymap.rectangle):
        if btn.contains(event.x, event.y):
            print("You clicked button : {}".format(keymap.buttons[cnt]))

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
    if dbg_print:
        for cnt,btn in enumerate(keymap.rectangle):
            print("Button : {}".format(keymap.buttons[cnt]))
            btn.do_print()

    root.mainloop()

if __name__ == '__main__':
    main()

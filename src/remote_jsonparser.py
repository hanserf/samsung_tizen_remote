import json
from collections import namedtuple

RemoteOverlay = namedtuple("RemoteOverlay",["buttons","rectangle"])

class JSONParseError(Exception):
    """Raised when something goes bad in this module"""
    pass


class Rectangle:
    def __init__(self, center_x,center_y, width, height):
        # (x1, y1) is the upper left point of the rectangle
        # (x2, y2) is the lower right point of the rectangle
        self.x1 = int(center_x - width / 2)
        self.y1 = int(center_y - height / 2)
        self.x2 = int(center_x + width / 2)
        self.y2 = int(center_y + height / 2)
        return
    def do_print(self):
        print("[X1,Y1] = ({},{}), [X2,Y2] = ({},{})".format(self.x1,self.y1,self.x2,self.y2))

    def contains(self, newx, newy):
        # Will return true if the point (newx, newy) lies within the rectangle.
        # False otherwise.
        return (self.x1 <= newx <= self.x2) and (self.y1 <= newy <= self.y2)



class RemoteJsonParser():
    def __init__(self, path="static/keymap_samsung_tizen.json"):
        self.myremote = None
        try:
            with open(path, "r") as file:
                as_dict = json.load(file)
                self.button_pos = json.loads(json.dumps(as_dict["buttons_center"]))
                self.button_dims = json.loads(json.dumps(as_dict["button_dimensions"]))
        except Exception as msg:
            print("Could Not Open JSON file : {}".format(msg))
            raise JSONParseError
        self.__generate_remote()

    def __generate_remote(self):
        # Get keys of objects
        buttons = [*self.button_pos]
        # Get the dimension types used for physical layout
        rectangles = []
        for a_button in self.button_pos:
            btn_dims = self.button_dims[self.button_pos[a_button][2]]
            a_rect = Rectangle(center_x=self.button_pos[a_button][0],
                               center_y=self.button_pos[a_button][1],
                               width=btn_dims[0],
                               height=btn_dims[1])
            rectangles.append(a_rect)
        self.myremote = RemoteOverlay(buttons=buttons,rectangle=rectangles)

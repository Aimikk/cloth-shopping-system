from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg


class TextWithLabel:
    def __init__(self, master, text, x,y, data_type = "str",key_press_event= None):
        Label(master, text=text).place(x=x, y=y)
        match data_type:
            case "str":
                self.value = StringVar()
            case "int":
                self.value = IntVar()
            case "float":
                self.value = DoubleVar()
            case "bool":
                self.value = BooleanVar()
        text_box = Entry(master, textvariable=self.value)
        if key_press_event:
            text_box.bind("<KeyRelease>", key_press_event)
        text_box.place(x=x+80, y=y)
from tkinter import Tk
from tkinter import Canvas
from tkinter import Frame
from tkinter import Label
from tkinter import messagebox
from tkinter import Listbox
from tkinter import Button
from tkinter import SINGLE

from .utils import share_screen


class GUI:

    @classmethod
    def load(cls):
        window = Tk()
        canvas = Canvas(window, height=450, width=750)
        canvas.pack()
        frame_left = Frame(window, bg='#add8e6')
        frame_left.place(relx=0.05, rely=0.1, relwidth=0.4, relheight=0.8)
        frame_right = Frame(window, bg='#add8e6')
        frame_right.place(relx=0.55, rely=0.1, relwidth=0.4, relheight=0.8)
        return cls(window, frame_left, frame_right)

    def __init__(self, window, frame_left, frame_right):
        self.__window = window
        self.__frame_left = frame_left
        self.__frame_right = frame_right
        self.__create_left_frame_components()
        self.__create_right_frame_components()
        self.__window.mainloop()

    def __create_left_frame_components(self):
        label_branding = Label(
            self.__frame_left, bg='#add8e6', text="MAGNUS", font="Consolas 24")
        label_branding.pack(pady=30)

        label_info = Label(self.__frame_left, bg='#add8e6',
                           text="Local Screen Share Application", font="Consolas 12")
        label_info.pack()

        button_share = Button(
            self.__frame_left, text="Share Screen", command=share_screen)
        button_share.pack(pady=50)

    def __create_right_frame_components(self):
        label_available_hosts = Label(
            self.__frame_right, bg='#add8e6', text="Available Hosts", font="Consolas 12 bold")
        label_available_hosts.pack(pady=10)

        list_box = Listbox(self.__frame_right, bg='#add8e6',
                           selectmode=SINGLE, font="Consolas 12")
        list_items = ['192.168.1.20', '192.168.1.22', '192.168.1.54']
        # #list_items = network.available_hosts()
        for idx, item in enumerate(list_items):
            list_box.insert(idx, item)
        list_box.pack()

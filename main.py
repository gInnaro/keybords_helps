from serial.tools import list_ports
from threading import Thread
from tkinter import Tk, ttk, StringVar
from pystray import MenuItem as item
import pystray
import tkinter as tk
from PIL import Image
from key_jobs import Jobs
from button_block import Button_block as block_button
from color_menu import Color_menu


class Dekstops():
    def __init__(self):
        super().__init__()
        self.modes = False
        self.window = tk.Tk()
        self.window.title("Keyboard_ADD")
        self.image()
        self.window.iconbitmap(default="img/day/image.ico")
        self.window.maxsize(1400, 810)
        self.window.minsize(1400, 810)
        self.window.protocol('WM_DELETE_WINDOW', self.withdraw_window)
        self.fontExample = ("mr_CountryhouseG", 14)
        self.fontButton = ("mr_CountryhouseG", 18, "bold")
        self.frame1 = tk.Frame(self.window, width=300, height=810, bg=self.bg_left, borderwidth=2)
        self.frame1.pack(side='left', expand=True)
        self.frame1.option_add('*TCombobox*Listbox.font', self.fontExample)
        self.create_widgets_left()
        self.frame2 = tk.Frame(self.window, width=1100, height=810, background=self.bg_right)
        self.frame2.pack(side='right', expand=True)
        self.create_widgets_right()

    def quit_window(self, icon):
        icon.stop()
        self.window.destroy()

    def show_window(self, icon):
        icon.stop()
        self.window.after(0, self.window.deiconify)

    def withdraw_window(self):
        self.window.withdraw()
        menu = (item('Развернуть', self.show_window), item('Закрыть', self.quit_window))
        icon = pystray.Icon("Keyboard_ADD", self.image, "Keyboard_ADD", menu)
        icon.run()

    def image(self):
        self.image = Image.open("img/day/image.png")
        self.bg_left = '#e7e7e7'
        self.bg_right = '#FFFFFF'
        self.button_image = tk.PhotoImage(file='img/day/BTN_PIN1.png')
        self.conn = tk.PhotoImage(file='img/day/Conn.png')
        self.reconn = tk.PhotoImage(file='img/day/Re_conn.png')
        self.note1 = tk.PhotoImage(file="img/day/note_1.png")
        self.note2 = tk.PhotoImage(file="img/day/note_2.png")

    def frame_row_grid(self):
        self.frame1.grid_columnconfigure(0, minsize=148)
        self.frame1.grid_columnconfigure(1, minsize=148)
        self.frame1.grid_rowconfigure(0, minsize=55)
        self.frame1.grid_rowconfigure(1, minsize=55)
        self.frame1.grid_rowconfigure(2, minsize=160)
        self.frame1.grid_rowconfigure(3, minsize=160)
        self.frame1.grid_rowconfigure(4, minsize=160)
        self.frame1.grid_rowconfigure(5, minsize=160)
        self.frame1.grid_rowconfigure(6, minsize=40)

    def connect(self):
        com_ports = list_ports.comports()
        self.com_ports_list = []
        self.com_ports_list.append('')
        for i in range(len(com_ports)):
            self.com_ports_list.append(com_ports[i].device)
        self.combobox.configure(values=self.com_ports_list)

    def create_widgets_left(self):
        com_ports = list_ports.comports()
        self.com_ports_list = []
        self.com_ports_list.append('')
        for i in range(len(com_ports)):
            self.com_ports_list.append(com_ports[i].device)
        if self.com_ports_list == ['']:
            self.languages_var = StringVar(value='')
        else:
            self.languages_var = StringVar(value=com_ports[0].device)
        self.pixelVirtual = tk.PhotoImage(width=1, height=1)
        self.frame_row_grid()
        self.combobox = ttk.Combobox(self.frame1, textvariable=self.languages_var, font=12, width=12, height=100, state="readonly")
        self.connect()
        self.combobox.configure(font=("mr_CountryhouseG", 14))
        self.combobox.grid(row=0, column=0)
        self.status_ll1 = ttk.Label(self.frame1, background=self.bg_left, font=self.fontExample)
        self.status_ll1.grid(row=1, column=0)
        self.jobs = Jobs(self.status_ll1)
        self.btn_save = tk.Button(self.frame1, image=self.conn, height=40, width=120, border=0,
                             command=lambda: self.jobs.connect(self.combobox.get()))
        self.btn_save.grid(row=0, column=1)
        self.btn_upd = tk.Button(self.frame1, image=self.reconn, height=40, width=120, border=0,
                            command=self.connect)
        self.btn_upd.grid(row=1, column=1)
        self.btn1 = tk.Button(self.frame1, text="Подсветить кнопку #1", image=self.button_image, height=155, width=144, border=0, compound="c", font=self.fontButton, wraplength=120,
                         command=lambda: self.jobs.check_led('LED_1'))
        self.btn1.grid(row=2, column=0)
        self.btn2 = tk.Button(self.frame1, text="Подсветить кнопку #2", image=self.button_image, height=155, width=144, border=0, compound="c", font=self.fontButton, wraplength=120,
                         command=lambda: self.jobs.check_led('LED_2'))
        self.btn2.grid(row=2, column=1)
        self.btn3 = tk.Button(self.frame1, text="Подсветить кнопку #3", image=self.button_image, height=155, width=144, border=0, compound="c", font=self.fontButton, wraplength=120,
                         command=lambda: self.jobs.check_led('LED_3'))
        self.btn3.grid(row=3, column=0)
        self.btn4 = tk.Button(self.frame1, text="Подсветить кнопку #4", image=self.button_image, height=155, width=144, border=0, compound="c", font=self.fontButton, wraplength=120,
                         command=lambda: self.jobs.check_led('LED_4'))
        self.btn4.grid(row=3, column=1)
        self.btn5 = tk.Button(self.frame1, text="Подсветить кнопку #5", image=self.button_image, height=155, width=144, border=0, compound="c", font=self.fontButton, wraplength=120,
                         command=lambda: self.jobs.check_led('LED_5'))
        self.btn5.grid(row=4, column=0)
        self.btn6 = tk.Button(self.frame1, text="Подсветить кнопку #6", image=self.button_image, height=155, width=144, border=0, compound="c", font=self.fontButton, wraplength=120,
                         command=lambda: self.jobs.check_led('LED_6'))
        self.btn6.grid(row=4, column=1)
        self.btn7 = tk.Button(self.frame1, text="Подсветить кнопку #7", image=self.button_image, height=155, width=144, border=0, compound="c", font=self.fontButton, wraplength=120,
                         command=lambda: self.jobs.check_led('LED_7'))
        self.btn7.grid(row=5, column=0)
        self.btn8 = tk.Button(self.frame1, text="Подсветить кнопку #8", image=self.button_image, height=155, width=144, border=0, compound="c", font=self.fontButton, wraplength=120,
                         command=lambda: self.jobs.check_led('LED_8'))
        self.btn8.grid(row=5, column=1)

    def create_widgets_right(self):
        self.notebook = ttk.Notebook(self.frame2, width=1100, height=810)
        frame_right_1 = block_button(self.notebook)
        frame_right_1.configure(background=self.bg_right)
        frame_right_2 = Color_menu(self.notebook)
        frame_right_2.configure(background=self.bg_right)
        self.notebook.add(frame_right_1, image=self.note1)
        self.notebook.add(frame_right_2, image=self.note2)
        self.notebook.grid(row=0, column=0)

    def sends_clr(self, commands):
        self.jobs.sends_color(commands)

def start():
    program = Dekstops()
    program.window.mainloop()


if __name__ == '__main__':
    th1 = Thread(target=start, args=())
    th1.start()
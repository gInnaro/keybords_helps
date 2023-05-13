from tkinter import Tk, ttk, StringVar, colorchooser
import tkinter as tk
from db import btn_set
from key_jobs import Jobs

bg_label = "#ffffff"

class Color_menu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.fontExample = ("mr_CountryhouseG", 18, 'bold')
        self.parent = parent
        self.btn_set = btn_set('btn_setting.db')
        self.row_column()
        self.init_ui()
        self.images()
        self.indicator_label()
        self.save_button()


    def images(self):
        self.pixelVirtual = tk.PhotoImage(width=1, height=1)
        self.color_but = tk.PhotoImage(file='img/day/but_color.png')
        self.clr_label = tk.PhotoImage(file='img/day/Label.png')

    def row_column(self):
        self.grid_columnconfigure(0, minsize=320) # Колонна с текстом
        self.grid_columnconfigure(1, minsize=180) # Колонна с показом цвета
        self.grid_columnconfigure(2, minsize=180) # Колонна с кнопкой запуска палитры
        self.grid_columnconfigure(3, minsize=180) # Колонна с 3 кл. из комбинации
        self.grid_columnconfigure(4, minsize=145) # Колонна с кнопкой применить
        self.grid_columnconfigure(5, minsize=140) # Колонна со статусом применения
        for r in range(10):
            self.grid_rowconfigure(r, minsize=80)

    def init_ui(self):
        self.label1 = ttk.Label(self, text="Цвет нажатие Кнопки #1")
        self.label1.grid(row=0, column=0)
        self.label2 = ttk.Label(self, text="Цвет нажатие Кнопки #2")
        self.label2.grid(row=1, column=0)
        self.label3 = ttk.Label(self, text="Цвет нажатие Кнопки #3")
        self.label3.grid(row=2, column=0)
        self.label4 = ttk.Label(self, text="Цвет нажатие Кнопки #4")
        self.label4.grid(row=3, column=0)
        self.label5 = ttk.Label(self, text="Цвет нажатие Кнопки #5")
        self.label5.grid(row=4, column=0)
        self.label6 = ttk.Label(self, text="Цвет нажатие Кнопки #6")
        self.label6.grid(row=5, column=0)
        self.label7 = ttk.Label(self, text="Цвет нажатие Кнопки #7")
        self.label7.grid(row=6, column=0)
        self.label8 = ttk.Label(self, text="Цвет нажатие Кнопки #8")
        self.label8.grid(row=7, column=0)
        self.label9 = ttk.Label(self, text="Цвет для всех кнопок")
        self.label9.grid(row=8, column=0, sticky=tk.W, padx=25)
        
        for i in range(1,10):
            eval('self.label{}.configure(background=bg_label, font=self.fontExample)'.format(i))
        self.pack()

    def indicator_label(self):
        self.colorlabel1 = tk.Label(self, image=self.clr_label, background=self.btn_set.check_colors(1), height=63, width=93)
        self.colorlabel1.grid(row=0, column=1)

        self.colorlabel2 = tk.Label(self, image=self.clr_label, background=self.btn_set.check_colors(2), height=63, width=93)
        self.colorlabel2.grid(row=1, column=1)

        self.colorlabel3 = tk.Label(self, image=self.clr_label, background=self.btn_set.check_colors(3), height=63, width=93)
        self.colorlabel3.grid(row=2, column=1)

        self.colorlabel4 = tk.Label(self, image=self.clr_label, background=self.btn_set.check_colors(4), height=63, width=93)
        self.colorlabel4.grid(row=3, column=1)

        self.colorlabel5 = tk.Label(self, image=self.clr_label, background=self.btn_set.check_colors(5), height=63, width=93)
        self.colorlabel5.grid(row=4, column=1)

        self.colorlabel6 = tk.Label(self, image=self.clr_label, background=self.btn_set.check_colors(6), height=63, width=93)
        self.colorlabel6.grid(row=5, column=1)

        self.colorlabel7 = tk.Label(self, image=self.clr_label, background=self.btn_set.check_colors(7), height=63, width=93)
        self.colorlabel7.grid(row=6, column=1)

        self.colorlabel8 = tk.Label(self, image=self.clr_label, background=self.btn_set.check_colors(8), height=63, width=93)
        self.colorlabel8.grid(row=7, column=1)

        self.colorlabel9 = tk.Label(self, image=self.clr_label, height=63, width=93)
        self.colorlabel9.grid(row=8, column=1)

    def save_button(self):
        button1 = tk.Button(self, image=self.color_but, height=40, width=120, border=0,
                            command=lambda: self.colorSelect(1))
        button1.grid(row=0, column=2)
        button2 = tk.Button(self, image=self.color_but, height=40, width=120, border=0,
                            command=lambda: self.colorSelect(2))
        button2.grid(row=1, column=2)
        button3 = tk.Button(self, image=self.color_but, height=40, width=120, border=0,
                            command=lambda: self.colorSelect(3))
        button3.grid(row=2, column=2)
        button4 = tk.Button(self, image=self.color_but, height=40, width=120, border=0,
                            command=lambda: self.colorSelect(4))
        button4.grid(row=3, column=2)
        button5 = tk.Button(self, image=self.color_but, height=40, width=120, border=0,
                            command=lambda: self.colorSelect(5))
        button5.grid(row=4, column=2)
        button6 = tk.Button(self, image=self.color_but, height=40, width=120, border=0,
                            command=lambda: self.colorSelect(6))
        button6.grid(row=5, column=2)
        button7 = tk.Button(self, image=self.color_but, height=40, width=120, border=0,
                            command=lambda: self.colorSelect(7))
        button7.grid(row=6, column=2)
        button8 = tk.Button(self, image=self.color_but, height=40, width=120, border=0,
                            command=lambda: self.colorSelect(8))
        button8.grid(row=7, column=2)
        button_all = tk.Button(self, image=self.color_but, height=40, width=120, border=0,
                               command=lambda: self.colorSelect('all'))
        button_all.grid(row=8, column=2)

    def colorSelect(self, num):
        jobs = Jobs(self)
        user_color_arr = colorchooser.askcolor()
        if user_color_arr != (None, None):
            user_color_background = user_color_arr[1]
            r_clr, g_clr, b_clr = user_color_arr[0][0], user_color_arr[0][1], user_color_arr[0][2]
            if r_clr < 100:
                if r_clr < 10:
                    r_clr = f'00{r_clr}'
                else:
                    r_clr = f'0{r_clr}'
            if g_clr < 100:
                if g_clr < 10:
                    g_clr = f'00{g_clr}'
                else:
                    g_clr = f'0{g_clr}'
            if b_clr < 100:
                if b_clr < 10:
                    b_clr = f'00{b_clr}'
                else:
                    b_clr = f'0{b_clr}'
            if type(num) == int:
                self.btn_set.save_colors_db(num, user_color_background)
                label = eval('self.colorlabel{}'.format(int(num)))
                label["background"] = user_color_background
                sends_commands = f'clr{num}r{r_clr}g{g_clr}b{b_clr}$'
                jobs.sends_color(sends_commands)
            elif num == 'all':
                for n in range(1, 10):
                    label = eval('self.colorlabel{}'.format(n))
                    label["background"] = user_color_background
                for s in range(1, 9):
                    self.btn_set.save_colors_db(s, user_color_background)
                    sends_commands = f'clr{s}r{r_clr}g{g_clr}b{b_clr}$'
                    jobs.sends_color(sends_commands)
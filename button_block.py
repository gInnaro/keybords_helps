from tkinter import ttk, StringVar, font
import tkinter as tk
from libs_key import key_libs as lists
from db import btn_set


bg_label = "#ffffff"
libs = dict(lists())

class Button_block(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.btn_set = btn_set('btn_setting.db')
        self.row_column()
        self.generate_list()
        self.images()
        self.init_ui()

    def images(self):
        self.pixelVirtual = tk.PhotoImage(width=1, height=1)
        self.pixelbut_go = tk.PhotoImage(file='img/day/But_go.png')
        self.pixelbut_go_all = tk.PhotoImage(file='img/day/But_go_all.png')


    def row_column(self):
        self.grid_columnconfigure(0, minsize=380) # Колонна с текстом
        self.grid_columnconfigure(1, minsize=160) # Колонна с 1 кл. из комбинации
        self.grid_columnconfigure(2, minsize=160) # Колонна с 2 кл. из комбинации
        self.grid_columnconfigure(3, minsize=160) # Колонна с 3 кл. из комбинации
        self.grid_columnconfigure(4, minsize=130) # Колонна с кнопкой применить
        self.grid_columnconfigure(5, minsize=100) # Колонна со статусом применения
        for r in range(9):
            self.grid_rowconfigure(r, minsize=85)

    def generate_list(self):
        self.key_list = []
        libs = dict(lists())
        for key in libs:
            self.key_list.append(key)

    def init_ui(self):
        self.label1 = ttk.Label(self, text="Сочетание клавиш для Кнопки #1")
        self.label1.grid(row=0, column=0)
        self.label2 = ttk.Label(self, text="Сочетание клавиш для Кнопки #2")
        self.label2.grid(row=1, column=0)
        self.label3 = ttk.Label(self, text="Сочетание клавиш для Кнопки #3")
        self.label3.grid(row=2, column=0)
        self.label4 = ttk.Label(self, text="Сочетание клавиш для Кнопки #4")
        self.label4.grid(row=3, column=0)
        self.label5 = ttk.Label(self, text="Сочетание клавиш для Кнопки #5")
        self.label5.grid(row=4, column=0)
        self.label6 = ttk.Label(self, text="Сочетание клавиш для Кнопки #6")
        self.label6.grid(row=5, column=0)
        self.label7 = ttk.Label(self, text="Сочетание клавиш для Кнопки #7")
        self.label7.grid(row=6, column=0)
        self.label8 = ttk.Label(self, text="Сочетание клавиш для Кнопки #8")
        self.label8.grid(row=7, column=0)
        self.keyboard_shortcut()
        self.success_update()

        for i in range(1,9):
            eval('self.label{}.configure(background=bg_label, font=("mr_CountryhouseG", 18, "bold"))'.format(i))
        self.pack()

    def keyboard_shortcut(self):
        self.value11 = StringVar(value=self.btn_set.check_key_db(1, 1))
        self.key_box11 = ttk.Combobox(self, textvariable=self.value11, values=self.key_list, width=14, state="readonly")
        self.key_box11.grid(row=0, column=1)

        self.value21 = StringVar(value=self.btn_set.check_key_db(1, 2))
        self.key_box21 = ttk.Combobox(self, textvariable=self.value21, values=self.key_list, width=14, state="readonly")
        self.key_box21.grid(row=0, column=2)

        self.value31 = StringVar(value=self.btn_set.check_key_db(1, 3))
        self.key_box31 = ttk.Combobox(self, textvariable=self.value31, values=self.key_list, width=14, state="readonly")
        self.key_box31.grid(row=0, column=3)

        self.value12 = StringVar(value=self.btn_set.check_key_db(2, 1))
        self.key_box12 = ttk.Combobox(self, textvariable=self.value12, values=self.key_list, width=14, state="readonly")
        self.key_box12.grid(row=1, column=1)

        self.value22 = StringVar(value=self.btn_set.check_key_db(2, 2))
        self.key_box22 = ttk.Combobox(self, textvariable=self.value22, values=self.key_list, width=14, state="readonly")
        self.key_box22.grid(row=1, column=2)

        self.value32 = StringVar(value=self.btn_set.check_key_db(2, 3))
        self.key_box32 = ttk.Combobox(self, textvariable=self.value32, values=self.key_list, width=14, state="readonly")
        self.key_box32.grid(row=1, column=3)

        self.value13 = StringVar(value=self.btn_set.check_key_db(3, 1))
        self.key_box13 = ttk.Combobox(self, textvariable=self.value13, values=self.key_list, width=14, state="readonly")
        self.key_box13.grid(row=2, column=1)

        self.value23 = StringVar(value=self.btn_set.check_key_db(3, 2))
        self.key_box23 = ttk.Combobox(self, textvariable=self.value23, values=self.key_list, width=14, state="readonly")
        self.key_box23.grid(row=2, column=2)

        self.value33 = StringVar(value=self.btn_set.check_key_db(3, 3))
        self.key_box33 = ttk.Combobox(self, textvariable=self.value33, values=self.key_list, width=14, state="readonly")
        self.key_box33.grid(row=2, column=3)

        self.value14 = StringVar(value=self.btn_set.check_key_db(4, 1))
        self.key_box14 = ttk.Combobox(self, textvariable=self.value14, values=self.key_list, width=14, state="readonly")
        self.key_box14.grid(row=3, column=1)

        self.value24 = StringVar(value=self.btn_set.check_key_db(4, 2))
        self.key_box24 = ttk.Combobox(self, textvariable=self.value24, values=self.key_list, width=14, state="readonly")
        self.key_box24.grid(row=3, column=2)

        self.value34 = StringVar(value=self.btn_set.check_key_db(4, 3))
        self.key_box34 = ttk.Combobox(self, textvariable=self.value34, values=self.key_list, width=14, state="readonly")
        self.key_box34.grid(row=3, column=3)

        self.value15 = StringVar(value=self.btn_set.check_key_db(5, 1))
        self.key_box15 = ttk.Combobox(self, textvariable=self.value15, values=self.key_list, width=14, state="readonly")
        self.key_box15.grid(row=4, column=1)

        self.value25 = StringVar(value=self.btn_set.check_key_db(5, 2))
        self.key_box25 = ttk.Combobox(self, textvariable=self.value25, values=self.key_list, width=14, state="readonly")
        self.key_box25.grid(row=4, column=2)

        self.value35 = StringVar(value=self.btn_set.check_key_db(5, 3))
        self.key_box35 = ttk.Combobox(self, textvariable=self.value35, values=self.key_list, width=14, state="readonly")
        self.key_box35.grid(row=4, column=3)

        self.value16 = StringVar(value=self.btn_set.check_key_db(6, 1))
        self.key_box16 = ttk.Combobox(self, textvariable=self.value16, values=self.key_list, width=14, state="readonly")
        self.key_box16.grid(row=5, column=1)

        self.value26 = StringVar(value=self.btn_set.check_key_db(6, 2))
        self.key_box26 = ttk.Combobox(self, textvariable=self.value26, values=self.key_list, width=14, state="readonly")
        self.key_box26.grid(row=5, column=2)

        self.value36 = StringVar(value=self.btn_set.check_key_db(6, 3))
        self.key_box36 = ttk.Combobox(self, textvariable=self.value36, values=self.key_list, width=14, state="readonly")
        self.key_box36.grid(row=5, column=3)

        self.value17 = StringVar(value=self.btn_set.check_key_db(7, 1))
        self.key_box17 = ttk.Combobox(self, textvariable=self.value17, values=self.key_list, width=14, state="readonly")
        self.key_box17.grid(row=6, column=1)

        self.value27 = StringVar(value=self.btn_set.check_key_db(7, 2))
        self.key_box27 = ttk.Combobox(self,textvariable=self.value27, values=self.key_list, width=14, state="readonly")
        self.key_box27.grid(row=6, column=2)

        self.value37 = StringVar(value=self.btn_set.check_key_db(7, 3))
        self.key_box37 = ttk.Combobox(self,textvariable=self.value37, values=self.key_list, width=14, state="readonly")
        self.key_box37.grid(row=6, column=3)

        self.value18 = StringVar(value=self.btn_set.check_key_db(8, 1))
        self.key_box18 = ttk.Combobox(self,textvariable=self.value18, values=self.key_list, width=14, state="readonly")
        self.key_box18.grid(row=7, column=1)

        self.value28 = StringVar(value=self.btn_set.check_key_db(8, 2))
        self.key_box28 = ttk.Combobox(self,textvariable=self.value28, values=self.key_list, width=14, state="readonly")
        self.key_box28.grid(row=7, column=2)

        self.value38 = StringVar(value=self.btn_set.check_key_db(8, 3))
        self.key_box38 = ttk.Combobox(self,textvariable=self.value38, values=self.key_list, width=14, state="readonly")
        self.key_box38.grid(row=7, column=3)
        for c in range(1, 4):
            for r in range(1, 9):
                eval('self.key_box{}{}.configure(font=("mr_CountryhouseG", 14))'.format(c, r))

        self.save_button()
        self.pack()

    def save_button(self):

        btn1 = tk.Button(self, image=self.pixelbut_go, height=40, width=120, border=0,
                         command=lambda: self.click_button('btn1'))
        btn1.grid(row=0, column=4)
        btn2 = tk.Button(self, image=self.pixelbut_go, height=40, width=120, border=0,
                         command=lambda: self.click_button('btn2'))
        btn2.grid(row=1, column=4)
        btn3 = tk.Button(self, image=self.pixelbut_go, height=40, width=120, border=0,
                         command=lambda: self.click_button('btn3'))
        btn3.grid(row=2, column=4)
        btn4 = tk.Button(self, image=self.pixelbut_go, height=40, width=120, border=0,
                         command=lambda: self.click_button('btn4'))
        btn4.grid(row=3, column=4)
        btn5 = tk.Button(self, image=self.pixelbut_go, height=40, width=120, border=0,
                         command=lambda: self.click_button('btn5'))
        btn5.grid(row=4, column=4)
        btn6 = tk.Button(self, image=self.pixelbut_go, height=40, width=120, border=0,
                         command=lambda: self.click_button('btn6'))
        btn6.grid(row=5, column=4)
        btn7 = tk.Button(self, image=self.pixelbut_go, height=40, width=120, border=0,
                         command=lambda: self.click_button('btn7'))
        btn7.grid(row=6, column=4)
        btn8 = tk.Button(self, image=self.pixelbut_go, height=40, width=120, border=0,
                         command=lambda: self.click_button('btn8'))
        btn8.grid(row=7, column=4)
        btnall = tk.Button(self, image=self.pixelbut_go_all, height=40, width=240, border=0,
                         command=lambda: self.click_button('btnall'))
        btnall.grid(row=8, column=3, columnspan=2, sticky=tk.E, padx=12)

    def click_button(self, nums):
        if nums == 'btn1':
            var1, var2, var3 = libs[self.key_box11.get()], libs[self.key_box21.get()], libs[self.key_box31.get()]
            self.btn_set.edit_key('BTN_PIN_1', var1, var2, var3)
            self.status_label1['text'] = 'Изменено'
        if nums == 'btn2':
            var1, var2, var3 = libs[self.key_box12.get()], libs[self.key_box22.get()], libs[self.key_box32.get()]
            self.btn_set.edit_key('BTN_PIN_2', var1, var2, var3)
            self.status_label2['text'] = 'Изменено'
        if nums == 'btn3':
            var1, var2, var3 = libs[self.key_box13.get()], libs[self.key_box23.get()], libs[self.key_box33.get()]
            self.btn_set.edit_key('BTN_PIN_3', var1, var2, var3)
            self.status_label3['text'] = 'Изменено'
        if nums == 'btn4':
            var1, var2, var3 = libs[self.key_box14.get()], libs[self.key_box24.get()], libs[self.key_box34.get()]
            self.btn_set.edit_key('BTN_PIN_4', var1, var2, var3)
            self.status_label4['text'] = 'Изменено'
        if nums == 'btn5':
            var1, var2, var3 = libs[self.key_box15.get()], libs[self.key_box25.get()], libs[self.key_box35.get()]
            self.btn_set.edit_key('BTN_PIN_5', var1, var2, var3)
            self.status_labe5['text'] = 'Изменено'
        if nums == 'btn6':
            var1, var2, var3 = libs[self.key_box12.get()], libs[self.key_box26.get()], libs[self.key_box36.get()]
            self.btn_set.edit_key('BTN_PIN_6', var1, var2, var3)
            self.status_label6['text'] = 'Изменено'
        if nums == 'btn7':
            var1, var2, var3 = libs[self.key_box17.get()], libs[self.key_box27.get()], libs[self.key_box37.get()]
            self.btn_set.edit_key('BTN_PIN_7', var1, var2, var3)
            self.status_label7['text'] = 'Изменено'
        if nums == 'btn8':
            var1, var2, var3 = libs[self.key_box18.get()], libs[self.key_box28.get()], libs[self.key_box38.get()]
            self.btn_set.edit_key('BTN_PIN_8', var1, var2, var3)
            self.status_label8['text'] = 'Изменено'
        if nums == 'btnall':
            for i in range(1, 9):
                name = eval('"BTN_PIN_{}"'.format(i))
                var1 = eval('libs[self.key_box1{}.get()]'.format(i))
                var2 = eval('libs[self.key_box2{}.get()]'.format(i))
                var3 = eval('libs[self.key_box3{}.get()]'.format(i))
                eval('self.status_label{}'.format(i))['text'] = 'Изменено'
                self.btn_set.edit_key(name, var1, var2, var3)

    def success_update(self):
        self.status_label1 = ttk.Label(self)
        self.status_label1.grid(row=0, column=5)
        self.status_label2 = ttk.Label(self)
        self.status_label2.grid(row=1, column=5)
        self.status_label3 = ttk.Label(self)
        self.status_label3.grid(row=2, column=5)
        self.status_label4 = ttk.Label(self)
        self.status_label4.grid(row=3, column=5)
        self.status_label5 = ttk.Label(self)
        self.status_label5.grid(row=4, column=5)
        self.status_label6 = ttk.Label(self)
        self.status_label6.grid(row=5, column=5)
        self.status_label7 = ttk.Label(self)
        self.status_label7.grid(row=6, column=5)
        self.status_label8 = ttk.Label(self)
        self.status_label8.grid(row=7, column=5)

        for i in range(1,9):
            eval('self.status_label{}.configure(background=bg_label, font=14)'.format(i))
        self.pack()

        self.pack()

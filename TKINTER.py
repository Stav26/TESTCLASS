
from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('Сложение на Python')
root.geometry('400x300')


a = StringVar()
b = StringVar()

class Calculator:
    def calc(self, a, b):
        if '.' in a.get() or '.' in b.get():
            c = float(a.get()) + float(b.get())
            return c
        else:
            c = int(a.get()) + int(b.get())
            return c
cl = Calculator()

class Display:
    def display_calc(self):
        messagebox.showinfo("GUI Python", cl.calc(a, b))
pl = Display()

class Labeling:
    def label_func(self):
        alabel = Label(text="Введите цифру:")
        blabel = Label(text="Введите цифру:")

        alabel.grid(row=0, column=0, sticky="w")
        blabel.grid(row=1, column=0, sticky="w")
lb=Labeling()
lb.label_func()

class Entring:
    def entry_func(self):
        a_entry = Entry(textvariable=a)
        b_entry = Entry(textvariable=b)

        a_entry.grid(row=0, column=1, padx=5, pady=5)
        b_entry.grid(row=1, column=1, padx=5, pady=5)
en = Entring()
en.entry_func()

class Buttoning:
    def button_func(self):
        calc_button = Button(text="Нажми", command=pl.display_calc)
        calc_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")
bt = Buttoning()
bt.button_func()

root.mainloop()

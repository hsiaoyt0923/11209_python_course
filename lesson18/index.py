import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.geometry('400x250+300+300')
        self.title('Lines')
        self.configure(background='#F4A7B9')
    
class MyFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(background='#D0104C')
        self.pack(expand=1, fill='both')

def main():
    window = Window()
    myFrame = MyFrame(window)
    window.mainloop()

if __name__ == '__main__':
    main()
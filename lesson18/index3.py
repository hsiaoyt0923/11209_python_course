import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.geometry('400x250+300+300')
        self.title('Alignment')
        self.configure(background='#F4A7B9')
    
class MyFrame(ttk.LabelFrame):
    def __init__(self, master, title, **kwargs):
        super().__init__(master, text=title, **kwargs)
        self.alignment = tk.StringVar(value='left')
        ttk.Radiobutton(self, text='左邊', value='left', variable=self.alignment, command=self.selected).grid(row=0, column=0,padx=20)
        ttk.Radiobutton(self, text='中間', value='center', variable=self.alignment, command=self.selected).grid(row=0, column=1, padx=20)
        ttk.Radiobutton(self, text='右邊', value='right', variable=self.alignment, command=self.selected).grid(row=0, column=2, padx=20)
        self.pack()
    
    def selected(self):
        print(self.alignment.get())


def main():
    window = Window()
    myFrame = MyFrame(window, '對齊方式')
    window.mainloop()

if __name__ == '__main__':
    main()
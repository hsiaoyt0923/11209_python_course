import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title('Login Page')
    
class MyFrame(tk.LabelFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(expand=1, fill= 'both', padx=10, pady=10)
        #標題
        heading = ttk.Label(self, text='會員登入', font=('Helvetica', 20), foreground='red')
        heading.grid(row=0, column=0, columnspan=2)

        username_label = ttk.Label(self, text='使用者名稱:', font=('Helvetica', 12))
        username_label.grid(row=1, column=0, pady=10, padx=(10,1))  

        username_entry = ttk.Entry(self)    
        username_entry.grid(row=1, column=1, padx=(0,10))

        password_label = ttk.Label(self, text='密碼:', font=('Helvetica', 12))
        password_label.grid(row=2, column=0,sticky=tk.E, pady=10, padx=(10,1))

        password_entry = ttk.Entry(self, show='*')
        password_entry.grid(row=2, column=1, padx=(0,10))

        login_button = ttk.Button(self, text='登入')
        login_button.grid(row=3, column=1, sticky=tk.E, pady=10, padx=(0,10))

def main():
    window = Window()
    myFrame = MyFrame(window)
    window.mainloop()

if __name__ == '__main__':
    main()
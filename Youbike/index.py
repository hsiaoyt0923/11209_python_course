import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from threading import Timer
import datasource

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # try:
        #     datasource.update_sqlite_data()
        # except:
        #     messagebox.showerror('錯誤訊息', '網路不正常\n將關閉應用程式\n請稍後再試')
        #     self.destroy()





def main():
    def update_data(w:Window):
        datasource.update_sqlite_data()
        window.after(5*1000,update_data,w)
    window = Window()
    window.title('台北市Youbike2.0')
    window.geometry('600x300')
    print('做事')
    window.resizable(width=False, height=False)
    update_data(window)
    window.mainloop()

if __name__ == '__main__':
    main()
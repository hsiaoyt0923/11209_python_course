import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from threading import Timer
import datasource

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            datasource.update_sqlite_data()
        except:
            messagebox.showerror('錯誤訊息', '網路不正常\n將關閉應用程式\n請稍後再試')
            self.destroy()

timer = None
def update_data():
    print('做事')
    global timer
    timer = Timer(20, update_data)
    timer.start()
    

def on_closing(w:Window) -> None:
    print('關閉視窗')
    timer.cancel()
    w.destroy()
    

def main():
    window = Window()
    window.title('台北市Youbike2.0')
    window.geometry('600x300')
    update_data()
    window.resizable(width=False, height=False)
    window.protocol("WM_DELETE_WINDOW",lambda :on_closing(window))  
    window.mainloop()

if __name__ == '__main__':
    main()
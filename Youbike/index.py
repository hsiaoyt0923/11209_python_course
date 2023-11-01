import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datasource

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        topFrame = tk.Frame(self, relief=tk.GROOVE, borderwidth=1)
        tk.Label(topFrame, text='台北市youbike即時資訊', font=('arial', 20), bg='#33A6B8', fg='#000', padx=10, pady=10).pack()
        topFrame.pack(pady=30)

        bottomFrame = tk.Frame(self)
        bottomFrame.pack(pady=30)


        # print(datasource.lastest_datetime_data())


def main():
    # def update_data(w:Window):
    #     datasource.update_sqlite_data()
    #     window.after(60*1000,update_data,w)
    window = Window()
    window.title('台北市Youbike2.0')
    window.geometry('600x300')
    window.resizable(width=False, height=False)
    # update_data(window)
    window.mainloop()

if __name__ == '__main__':
    main()
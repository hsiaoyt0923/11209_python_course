import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from youbikeTreeview import YoubikeTreeview
import datasource

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        topFrame = tk.Frame(self, relief=tk.GROOVE, borderwidth=1)
        tk.Label(topFrame, text='台北市youbike即時資訊', font=('arial', 20), bg='#33A6B8', fg='#000', padx=30, pady=30).pack(padx=30, pady=30)
        topFrame.pack(pady=30)

        middleFrame = tk.Frame(self)
        tk.Label(middleFrame, text='站點名稱查詢:', font=('微軟正黑體', 32)).grid(row=0, sticky=tk.W)
        tk.Entry(middleFrame, width=32, font=('微軟正黑體', 32)).grid(row=0, column=1, sticky=tk.W) 
 
        
        bottomFrame = tk.Frame(self)
        scrollbar = ttk.Scrollbar(bottomFrame, orient='vertical')
        scrollbar.pack(side='right', fill='y')
        self.youbikeTreeview = YoubikeTreeview(bottomFrame, show='headings', columns=('sna','mday','sarea','ar','tot','sbi','bemp'), yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.youbikeTreeview.yview)
        self.youbikeTreeview.pack()
        bottomFrame.pack(pady=30)

        
        


def main():
    def update_data(w:Window):
        datasource.update_sqlite_data()
        latest_data = datasource.lastest_datetime_data()
        w.youbikeTreeview.update_content(latest_data)
        w.after(3*60*1000,update_data,w)
        
    window = Window()
    window.title('台北市Youbike2.0')
    update_data(window)
    window.mainloop()

if __name__ == '__main__':
    main()
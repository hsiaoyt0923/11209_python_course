import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from youbikeTreeview import YoubikeTreeview
import datasource

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        #------------------------建立介面------------------------
        topFrame = tk.Frame(self, relief=tk.GROOVE, borderwidth=1)
        tk.Label(topFrame, text='台北市youbike即時資訊',
                font=('arial', 36),
                bg='#DAC9A6',
                fg='#000',
                padx=30,
                pady=30).pack(padx=30, pady=30)
        topFrame.pack(pady=30)

        #------------------------建立搜尋條------------------------
        middleFrame = tk.Frame(self)
        tk.Label(middleFrame, text='站點名稱:',
                font=('微軟正黑體', 24)).grid(row=0, sticky=tk.W)
        self.keyin = tk.StringVar()
        self.entry = tk.Entry(middleFrame, width=24,
                            font=('微軟正黑體', 24),
                            textvariable=self.keyin)
        self.entry.bind("<KeyRelease>", self.search_item)
        self.entry.grid(row=0, column=1)
        

        # tk.Button(middleFrame,
        #         text='搜尋',
        #         state='active',
        #         font=('微軟正黑體', 24),
        #         command=self.search_item).grid(row=1, column=0, columnspan = 2)
        
        middleFrame.pack()
        
        #------------------------建立Treeview、Scrollbar------------------------
        bottomFrame = tk.Frame(self)
        scrollbar = ttk.Scrollbar(bottomFrame, orient='vertical')
        scrollbar.pack(side='right', fill='y')
        self.youbikeTreeview = YoubikeTreeview(bottomFrame,
                                               show='headings',
                                               columns=('sna','mday','sarea','ar','tot','sbi','bemp'),
                                               yscrollcommand=scrollbar.set,
                                               height = 20)
        scrollbar.configure(command=self.youbikeTreeview.yview)
        self.youbikeTreeview.pack()
        bottomFrame.pack(padx=20,
                         pady=20)
    
    #------------------------建立與搜尋按鈕連動的function:search_item()------------------------
    def search_item(self, event):
        item = self.keyin.get() 
        search_data = datasource.search_sitename(item)
        self.youbikeTreeview.update_content(search_data)
      
        
def main():
    def update_data(w:Window):
        datasource.update_sqlite_data()
        latest_data = datasource.lastest_datetime_data()
        w.youbikeTreeview.update_content(latest_data)
        w.after(5*60*1000,update_data,w)
    
    
        
    window = Window()
    window.title('台北市Youbike2.0')
    update_data(window)
    window.mainloop()

if __name__ == '__main__':
    main()
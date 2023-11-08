import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import Dialog

class YoubikeTreeview(ttk.Treeview):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
    #---設定欄位名稱--------------------------
        self.heading('sna',text='站點名稱')
        self.heading('mday',text='更新時間')
        self.heading('sarea',text='行政區')
        self.heading('ar',text='站點地址')
        self.heading('tot',text='總車輛數')
        self.heading('sbi',text='可借數量')
        self.heading('bemp',text='可還數量')

    #---設定欄位寬度--------------------------
        self.column('sna', width=270)
        self.column('mday', width=150)
        self.column('sarea', width=50)
        self.column('ar', width=300)
        self.column('tot', width=60)
        self.column('sbi', width=60)
        self.column('bemp', width=60)

    #---設定點擊事件--------------------------
        self.bind('<ButtonRelease-1>', self.selected_item)
    
    def update_content(self, site_data):
        for i in self.get_children():
            self.delete(i)
        for site in site_data:
            self.insert('','end',values=site)
    
    def selected_item(self, event):
        selectedItem = self.focus()
        data_dict = self.item(selectedItem)
        data_list = data_dict['values']
        title=data_list[0]
        detail = ShowDetail(self.parent, data=data_list, title=title)


class ShowDetail(Dialog):
    def __init__(self, parent, data, **kwargs):
        self.sna = data[0]
        self.mday = data[1]
        self.sarea = data[2]
        self.ar = data[3]
        self.tot = data[4]
        self.sbi = data[5]
        self.bemp = data[6]
        super().__init__(parent, **kwargs)


    def body(self, master):
        '''create dialog body.

        return widget that should have initial focus.
        This method should be overridden, and is called
        by the __init__ method.
        '''
        mainFrame = tk.Frame(master)
        tk.Label(mainFrame, text='站點名稱:').grid(row=0, column=0, sticky='w')
        tk.Label(mainFrame, text='更新時間:').grid(row=1, column=0, sticky='w')
        tk.Label(mainFrame, text='行政區:').grid(row=2, column=0, sticky='w')
        tk.Label(mainFrame, text='站點地址:').grid(row=3, column=0, sticky='w')
        tk.Label(mainFrame, text='總數量:').grid(row=4, column=0, sticky='w')
        tk.Label(mainFrame, text='可借數量:').grid(row=5, column=0, sticky='w')
        tk.Label(mainFrame, text='可還數量:').grid(row=6, column=0, sticky='w')
        tk.Label(mainFrame, text=self.sna, width='30', anchor='w').grid(row=0, column=1, sticky='w')
        tk.Label(mainFrame, text=self.mday, width='30', anchor='w').grid(row=1, column=1, sticky='w')
        tk.Label(mainFrame, text=self.sarea, width='30', anchor='w').grid(row=2, column=1, sticky='w')
        tk.Label(mainFrame, text=self.ar, width='30', anchor='w').grid(row=3, column=1, sticky='w')
        tk.Label(mainFrame, text=self.tot, width='30', anchor='w').grid(row=4, column=1, sticky='w')
        tk.Label(mainFrame, text=self.sbi, width='30', anchor='w').grid(row=5, column=1, sticky='w')
        tk.Label(mainFrame, text=self.bemp, width='30', anchor='w').grid(row=6, column=1, sticky='w')
        
        mainFrame.pack()

    def buttonbox(self):
        '''add standard button box.

        override if you do not want the standard buttons
        '''

        box = tk.Frame(self)

        w = tk.Button(box, text="確認", width=10, command=self.ok, default='active')
        w.pack(padx=5, pady=20)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

    
        

from tkinter import ttk

class YoubikeTreeview(ttk.Treeview):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
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
    
    def update_content(self, site_data):
        for i in self.get_children():
            self.delete(i)
        for site in site_data:
            self.insert('','end',values=site)
    
        

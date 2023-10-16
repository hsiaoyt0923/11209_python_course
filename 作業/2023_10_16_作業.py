import tkinter as tk
from tkinter import ttk
import csv

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title('個股資訊')

        self.tree = ttk.Treeview(self,columns=['#1','#2','#3','#4','#5','#6'], show='headings')
        self.tree.pack()
        self.tree.heading('#1', text='日期')
        self.tree.heading('#2', text='開盤價')
        self.tree.heading('#3', text='盤中最高價')
        self.tree.heading('#4', text='盤中最低價')
        self.tree.heading('#5', text='收盤價')
        self.tree.heading('#6', text='成交量')
    



def main():
    window = Window()
    window.mainloop()

if __name__ == '__main__':
    main()
    with open('台積電.csv','r',encoding='UTF-8') as file:
        csvReader = csv.reader(file)
        next(csvReader)
        list_csvReader = list(csvReader)
        for row in list_csvReader:
            
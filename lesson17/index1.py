import dataSource
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title('教學範例')
               
        firstFrame = tk.Frame(self, background='#E87A90')
        firstFrame.pack()        
        label = tk.Label(firstFrame, text='Hello, tkinter!', font=('Helvetica','20'))
        label.pack(padx=20, pady=20)

        secondFrame = tk.Frame(self, background='#F8C3CD')
        secondFrame.pack(expand=True, fill= 'x')
        choices = dataSource.cityNames()
        choicevar = tk.StringVar(value=choices)
        self.listbox = tk.Listbox(secondFrame, listvariable = choicevar, width=12)
        self.listbox.bind('<<ListboxSelect>>', self.user_selected)
        self.listbox.pack(pady=20)

        resultFrame = tk.Frame(self)
        resultFrame.pack()
        self.yearVar = tk.StringVar()
        self.cityVar = tk.StringVar()
        self.populationVar = tk.StringVar()
        self.areaVar = tk.StringVar()
        self.densityVar = tk.StringVar()
        tk.Label(resultFrame, text='年度').grid(column=0, row=0, sticky='E')
        tk.Label(resultFrame, text='地區').grid(column=0, row=1, sticky='E')
        tk.Label(resultFrame, text='人口數').grid(column=0, row=2, sticky='E')
        tk.Label(resultFrame, text='土地面積').grid(column=0, row=3, sticky='E')
        tk.Label(resultFrame, text='人口密度').grid(column=0, row=4, sticky='E')
        tk.Label(resultFrame, textvariable=self.yearVar).grid(column=1, row=0, sticky='W')
        tk.Label(resultFrame, textvariable=self.cityVar).grid(column=1, row=1, sticky='W')
        tk.Label(resultFrame, textvariable=self.populationVar).grid(column=1, row=2, sticky='W')
        tk.Label(resultFrame, textvariable=self.areaVar).grid(column=1, row=3, sticky='W')
        tk.Label(resultFrame, textvariable=self.densityVar).grid(column=1, row=4, sticky='W')

    def user_selected(self, event):
        selectedIndex = self.listbox.curselection()[0]
        cityName = self.listbox.get(selectedIndex)
        datalist = dataSource.Names(cityName)
        self.yearVar.set(datalist[0])
        self.cityVar.set(datalist[1])
        self.populationVar.set(datalist[2])
        self.areaVar.set(datalist[3])
        self.densityVar.set(datalist[4])

def main():
    window = Window()
    window.mainloop()

if __name__ == '__main__':
    main()
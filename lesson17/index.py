import tkinter as tk


def main():
    window = tk.Tk()
    window.title('這是我的第一個視窗')
    label = tk.Label(window, text='Hello, tkinter!', font=('Helvetica','40'))
    label.pack(padx=60,pady=60)
    window.mainloop()

if __name__ == '__main__':
    main()
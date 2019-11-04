import tkinter as tk

root = tk.Tk()

menubar = tk.Menu(root)
menu = tk.Menu(menubar, title='Menu')

root.config(menu=menubar)
root.mainloop()
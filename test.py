import tkinter as tk

root = tk.Tk()

root.geometry("1024x1024")
root.title("test")

cell = tk.Frame(root, width=40, height= 40, bg="white")

cell.grid(row=1, column=1)

root.mainloop()
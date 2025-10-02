import tkinter as tk;

class Cell:
    def __init__(self, root, text="", row=1, column=1, size=40, bgcolor="#FFFFFF", color="#000000"):
        self.root = root
        self.text = text
        self.row = row
        self.column = column
        self.size = size
        self.bgcolor = bgcolor
        self.color = color
    
    def render(self):
        bg = tk.Frame(self.root, width= self.size, height=self.size, bg=self.bgcolor)
        bg.grid(row=self.row, column= self.column)

        text = tk.Label(bg, text= self.text, fg=self.color, bg= self.bgcolor, font= ("Arial", 10))
        text.pack(expand= True)     

'''root = tk.Tk()

for i in range(0, 8):
    for j in range(0, 8):
        fg, bg = "", ""
        if (i % 2 == 0 and j % 2 == 0):
            fg = "#000000"
            bg = "#ffffff"
        else:
            fg = "#ffffff"
            bg = "#000000"

        cell = Cell(root=root, text=str((i, j)), row=j, column=i, bgcolor= bg, color= fg) 
        cell.render()

root.mainloop()'''

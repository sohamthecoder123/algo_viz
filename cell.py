"""
This file stores the Cell class, the basic elementary unit of a CellArray
"""

#imports
import tkinter as tk

#Cell class
class Cell:
    #constructor with default values
    # NOTE: @soham, since the signature got bulky, using kwargs for styling parameters
    def __init__(self, root, text="", row=1, column=1, **kwargs):
        self.root = root #the root of our cell in the tkinter sense
        self.text = text #the text of our cell
        self.row = row #the row number of our cell as it is going to be in a grid
        self.column = column #the column number of our cell
        self.size = kwargs.get('size', 40)
        self.bg_color = kwargs.get('bg_color', "#FFFFFF")
        self.color = kwargs.get('color', "#000000")
        self.font = kwargs.get('font', ('Arial', 18))

    #rendering function
    def render(self):
        #set up the background
        bg = tk.Frame(self.root, width= self.size, height=self.size, bg=self.bg_color)
        bg.grid(row=self.row, column= self.column) #set it to grid
        bg.grid_propagate(False) #don't propagate down (ie, don't let the size of the text determine the size of the cell)

        #the text
        text = tk.Label(bg, text= self.text, fg=self.color, bg= self.bg_color, font=self.font)
        text.place(relx=0.5,  rely=0.5, anchor="center")#place it at the center


#test code (commented out)
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

'''
This file stores the Cell class, the basic elementary unit of a CellArray
'''

#imports
import tkinter as tk;

#Cell class
class Cell:

    #constructor with default values
    def __init__(self, root, text="", row=1, column=1, size=40, bgcolor="#FFFFFF", color="#000000"):

        self.root = root #the root of our cell in the tkinter sense
        self.text = text #the text of our cell
        self.row = row #the row number of our cell as it is going to be in a grid
        self.column = column #the column number of our cell
        self.size = size #the size (width = height as our cell is a square) of our cell
        self.bgcolor = bgcolor #the background color of our cell, Default = white
        self.color = color #the color of the text. Default = black
    

    #rendering function
    def render(self):

        #set up the background
        bg = tk.Frame(self.root, width= self.size, height=self.size, bg=self.bgcolor)
        bg.grid(row=self.row, column= self.column) #set it to grid
        bg.grid_propagate(False) #don't propagate down (ie, don't let the size of the text determine the size of the cell)

        #the text
        text = tk.Label(bg, text= self.text, fg=self.color, bg= self.bgcolor, font= ("Arial", 10))
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

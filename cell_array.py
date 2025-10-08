'''
This file contains the CellArray object which I plan to use to display the list
'''

#imports
import cell
import tkinter as tk;
import time

#CellArray class
class CellArray:

    #constructor 
    def __init__(self, root, array:list[cell.Cell] = [], bgColor:str = "white", textColor:str = "black", size:int = 40, font=('Arial', 18)):
        self.root = root #root 
        self.array = array #array is the list on which the CellArray is built on
        self.bgColor = bgColor #the background color of the cell
        self.textColor = textColor #the color of the text
        self.size = size #size of the cells
        self.font = font #the font
        self.bg = None #reference to the background

    #rendering
    def render(self):
        #set up background
        if self.bg is None:
            self.bg = tk.Frame(self.root)
            self.bg.grid(row=1, column=0, columnspan=len(self.array)) #make background horizontal

        #render each individual element of the array as a cell, one after the other
        for i in range(len(self.array)):
            cell_i = cell.Cell(root= self.bg, text= str(self.array[i]), row=1, column=(i+1), bgcolor=self.bgColor, color=self.textColor, size=self.size, font=self.font) #create the cell
            cell_i.render() #render the cell

    #updating
    def update(self, array):
        self.array = array #reset the array
        #print(self.array) #debugging

        #destroy existing children
        for child_cell in self.bg.winfo_children():
            child_cell.destroy()

        self.root.after(10, self.render()) #render it again after a short delay to prevent the jitter when the objects are deleted from becoming noticeable

#test code          
'''l1 = [1, 2, 3, 4]
l2 = [5, 6, 7]

root = tk.Tk()

cellArray = CellArray(root= root, array= l1, bgColor="blue", textColor="red", size="100", font=('Broadway', 12))
cellArray.render()

nextButton = tk.Button(root, text= "Next", command= lambda: cellArray.update(l2))
nextButton.grid(row=2, column=2, pady=10)

root.mainloop()
'''
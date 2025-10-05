'''
This file contains the CellArray object which I plan to use to display the list
'''

#imports
import cell
import tkinter as tk;

#CellArray class
class CellArray:

    #constructor 
    def __init__(self, root, array:list[cell.Cell] = [], bgColor:str = "white", textColor:str = "black", size:int = 40, font=('Arial', 18)):

        self.root = root #root 
        self.array = array #array is the list on which the CellArray is built on
        self.bgColor = bgColor #the background color of the cell
        self.textColor = textColor #the color of the text
        self.size = size #size of the cells
        self.font = font

    #rendering
    def render(self):
        #set up background
        bg = tk.Frame(self.root)
        bg.grid(row=1, column=len(self.array)) #make background horizontal

        #render each individual element of the array as a cell, one after the other
        for i in range(len(self.array)):
            cell_i = cell.Cell(root= bg, text= str(self.array[i]), row=1, column=(i+1), bgcolor=self.bgColor, color=self.textColor, size=self.size, font=self.font) #create the cell
            cell_i.render() #render the cell

#test code          
'''l1 = [1, 2, 3, 4]

root = tk.Tk()

cellArray = CellArray(root= root, array= l1, bgColor="blue", textColor="red", size="100", font=('Broadway', 12))
cellArray.render()

root.mainloop()
'''
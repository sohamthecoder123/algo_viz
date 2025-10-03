'''
This file contains the CellArray object which I plan to use to display the list
'''

#imports
import cell
import tkinter as tk;

#CellArray class
class CellArray:

    #constructor 
    def __init__(self, root, array):

        self.root = root #root 
        self.array = array #array is the list on which the CellArray is built on

    #rendering
    def render(self):
        #set up background
        bg = tk.Frame(self.root, bg="white")
        bg.grid(row=1, column=len(self.array)) #make background horizontal

        #render each individual element of the array as a cell, one after the other
        for i in range(len(self.array)):
            cell_i = cell.Cell(root= bg, text= str(self.array[i]), row=1, column=(i+1)) #create the cell
            cell_i.render() #render the cell

#test code          
'''
l1 = [1, 2, 3, 4]

root = tk.Tk()

cellArray = CellArray(root= root, array= l1)
cellArray.render()

root.mainloop()'''
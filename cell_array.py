"""
This file contains the CellArray object which I plan to use to display the list
"""

#imports
import cell
import tkinter as tk

#CellArray class
class CellArray:
    #constructor
    # NOTE: @soham, The signature gets too bulky, hence using kwargs for styling parameters.
    def __init__(self, root, array, **kwargs) -> None:
        self.root = root #root 
        self.array = None if array is None else array #array is the list on which the CellArray is built on
        # NOTE: @soham, this kind of parsing kwargs is helpful when you do not explicitly want to use
        # each kwargs parameter frequently, it helps passing the whole kwargs to other functions (Cell in this case).
        self.cell_params = {
            "size": kwargs.get("size", 40),
            "bg_color": kwargs.get("bgColor", "white"),
            "text_color": kwargs.get("textColor", "black"),
            "font": kwargs.get("font", ('Arial', 18))
        }
        self.bg = None #reference to the background

    #rendering
    def render(self) -> None:
        #set up background
        if self.bg is None:
            self.bg = tk.Frame(self.root)
            self.bg.grid(row=1, column=0, columnspan=len(self.array)) #make background horizontal

        #render each individual element of the array as a cell, one after the other
        for i in range(len(self.array)):
            cell_i = cell.Cell(root= self.bg, text= str(self.array[i]), row=1, column=(i+1), **self.cell_params) #create the cell
            cell_i.render() #render the cell

        self.update(low=0, mid=None, high=len(self.array)-1)

    # NOTE: @soham, read about public vs. private vs. protected methods.
    def _add_pointer(self, text, col):
        # Helper to create the pointers above the cells
        lbl = tk.Label(self.bg, text=text, font=("Arial", 12, "bold"), fg="red")
        lbl.grid(row=0, column=col)

    #updating
    def update(self, low, mid, high): # @soham, instead of resetting the array, change location of pointers
        # self.array = array #reset the array
        #print(self.array) #debugging

        #destroy existing children
        for child_cell in self.bg.winfo_children():
            child_cell.destroy()

        #self.root.after(10000000000, self.render) #render it again after a short delay to prevent the jitter when the objects are deleted from becoming noticeable

        for i in range(len(self.array)):
            current_style = self.cell_params.copy()
            if i == mid:
                current_style['bg_color'] = "yellow"
            elif low <= i <= high:
                pass
            else:
                current_style['bg_color'] = "lightgray"

            # Rendering pointers
            if i == low:
                self._add_pointer("L", i)
            elif i == high:
                self._add_pointer("H", i)
            if i == mid:
                self._add_pointer("M", i)

            # Rendering Cell
            c = cell.Cell(root= self.bg, text= str(self.array[i]), row=1, column=i, **current_style)
            c.render()

            # Rendering Index Numbers
            idx_label = tk.Label(self.bg, text=str(i), font=("Arial", 10))
            idx_label.grid(row=2, column=i)

'''#test code          
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7]

root = tk.Tk()

cellArray = CellArray(root= root, array= l1, bgColor="blue", textColor="red", size="100", font=('Broadway', 12))
cellArray.render()

nextButton = tk.Button(root, text= "Next", command= lambda: cellArray.update(l2))
nextButton.grid(row=1, column= len(cellArray.array) + 1)

root.mainloop()

'''
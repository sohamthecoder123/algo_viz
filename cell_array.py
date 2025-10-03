import cell
import tkinter as tk;

class CellArray: 
    def __init__(self, root, array):
        self.root = root
        self.array = array

    def render(self):
        bg = tk.Frame(self.root, bg="white")
        bg.grid(row=1, column=len(self.array))

        for i in range(len(self.array)):
            cell_i = cell.Cell(root= bg, text= str(self.array[i]), row=1, column=(i+1))
            cell_i.render()
            
'''
l1 = [1, 2, 3, 4]

root = tk.Tk()

cellArray = CellArray(root= root, array= l1)
cellArray.render()

root.mainloop()'''
import tkinter as tk #ignore for now
from cell_array import CellArray

'''
main file

Currently I haven't integrated it w/ tkinter - Soham
'''

root = tk.Tk()
root.geometry("1024x1024")
root.title("Algorithm Visualizer")

label = tk.Label(root, text="Binary Search Visualizer", font=('Arial', 18))
label.pack(padx = 20, pady = 20)

array_test = [1, 2, 3, 4, 5, 6, 7, 8, 9] #array on which the bs algo is to be run

value = 5 #the value being searched for 

i = 0 #index/no of steps

#some vars for visualization
limit_reached = False
is_found = False

#low and high fingers
#low = 0
#high = len(array)

def binary_search_step(array: list[int], value: int):
    print("Hello")
    low = 0
    high = len(array) - 1
    mid = (low + high)//2 #calculate mid value

    mid_value = array[mid]

    if mid_value < value: 
        low = mid + 1
    elif mid_value > value:
        high = mid - 1

    return array[low:high]


#frame for the array
array_frame = tk.Frame(root)

cells = CellArray(root= array_frame, array= array_test)
cells.render()

array_frame.pack()

button_frame = tk.Frame(root)

def btnFunction():
    global array_test
    new_array = binary_search_step(array_test, value)
    array_test = new_array
    cells.update(array_test)

nextButton = tk.Button(root, text= "Next", command= lambda: btnFunction())

nextButton.pack()

button_frame.pack()


'''
#the while loop
while True:
    i += 1 #increment i by 1
    print("Step: ", i) #print current step no.

    mid = (low + high)//2 #calculate mid value

    limited_array = array[low:high] #the array in which we are searching now
    print("Array in question: ", limited_array) #print it

    mid_value = array[mid] #the value of the middle element

    #print stuff about the position, etc.
    print("Position of value: ", mid)
    print("Value to be checked: ", mid_value)

    #handles bst logic
    if mid_value == value:
        limit_reached = True #we have reached the correct value
        is_found = True #we have found it
    elif mid_value < value: 
        low = mid + 1 #clearly our term must be to the right of the middle value then
        print("mid < val")
    else:
        high = mid - 1 #clearly our term must be to the left of the middle value then
        print("mid > val")

    #stop condition
    if low >= high:
        limit_reached = True

    #stop and print the no of steps and whether the value was found or not
    if limit_reached:
        print("No of steps: ", i)
        print("Was found: ", is_found)
        break
    
'''


root.mainloop() #ignore for now
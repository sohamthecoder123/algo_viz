import tkinter as tk
from cell_array import CellArray

'''
main file
'''

root = tk.Tk()
root.geometry("1024x600") # 1024 height is too much, and who likes a square window anyway?
root.title("Algorithm Visualizer")

label = tk.Label(root, text="Binary Search Visualizer", font=('Arial', 18))
label.pack(padx = 20, pady = 20)

array_test = [1, 2, 3, 4, 5, 6, 7, 8, 9] #array on which the bs algo is to be run

value = 2 #the value being searched for 

i = 0 #index/no of steps

#some vars for visualization
search_finished = False
is_found = False

#low and high fingers
low = 0
mid = None
high = len(array_test)-1

def binary_search_step(array: list[int], value: int):
    global low, high, search_finished, is_found, mid

    if search_finished: return
    elif mid is None:
        mid = mid = (low + high)//2
        cells.update(low=low, mid=mid, high=high)
        return

    mid = (low + high)//2 #calculate mid value
    mid_value = array[mid]

    cells.update(low=low, mid=mid, high=high)

    if mid_value == value:
        is_found = True
        search_finished = True
        nextButton.config(text="Found!", state="disabled")
    elif low >= high:
        search_finished = True
        nextButton.config(text="Not Found", state="disabled")
    elif mid_value < value:
        low = mid + 1
    else: # mid_value > value:
        high = mid - 1

    # NOTE: @soham, do not return a new array. The array should remain the same,
    # and only the position of pointers should change
    # return array[low:high]


#frame for the array
array_frame = tk.Frame(root)

cells = CellArray(
    root= array_frame,
    array= array_test,
    size=50,
    bg_color="#FFF",
    text_color="#000",
    font=('Arial', 18)
)
cells.render()

array_frame.pack()

button_frame = tk.Frame(root)

def btnFunction():
    global low, mid, high, array_test, value
    binary_search_step(array_test, value)
    cells.update(low=low, mid=mid, high=high)

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
        search_finished = True #we have reached the correct value
        is_found = True #we have found it
    elif mid_value < value: 
        low = mid + 1 #clearly our term must be to the right of the middle value then
        print("mid < val")
    else:
        high = mid - 1 #clearly our term must be to the left of the middle value then
        print("mid > val")

    #stop condition
    if low >= high:
        search_finished = True

    #stop and print the no of steps and whether the value was found or not
    if search_finished:
        print("No of steps: ", i)
        print("Was found: ", is_found)
        break
    
'''


root.mainloop() 
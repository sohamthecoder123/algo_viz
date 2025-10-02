import tkinter as tk

'''
file = open("binary_search.algo", "r")

lines = file.readlines()

state = ""

for i in lines:
    if i.startswith("-input"):
        state = "input"

    elif i.startswith("-init"):
        state = "init"

    elif i.startswith("-process"):
        state = "process"

    elif i.startswith("-output"):
        state = "output"

    match state:
        case "input":



file.close()

'''

root = tk.Tk()
root.geometry("1024x1024")
root.title("Algorithm Visualizer")

label = tk.Label(root, text="Binary Search Visualizer", font=('Arial', 18))
label.pack(padx = 20, pady = 20)

array = [1, 3, 4, 19, 23, 45, 67]

value = 3

i = 0

limit_reached = False
is_found = False

low = 0
high = len(array)

array_frame = tk.Frame(root)


while True:
    i += 1
    print("Step: ", i)

    mid = (low + high)//2

    limited_array = array[low:high]
    print("Array in question: ", limited_array)

    mid_value = array[mid]

    print("Position of value: ", mid)
    print("Value to be checked: ", mid_value)

    if mid_value == value:
        limit_reached = True
        is_found = True
    elif mid_value < value:
        low = mid + 1
        print("mid < val")
    else:
        high = mid - 1
        print("mid > val")

    if low >= high:
        limit_reached = True

    if limit_reached:
        print("No of steps: ", i)
        print("Was found: ", is_found)
        break

root.mainloop()

'''
tree = ET.parse("factorial.xml")
root = tree.getroot()

setup_xml = root[0]
input_xml = setup_xml[0]

input = {}

for j in input_xml:
    i = j.attrib
    
    name = i['name']
    type = i['type']

    if(type == "int"):
        return_dict = {name: 0}
        input.update(return_dict)

init_state_xml = setup_xml[1]

for j in init_state_xml:
    i = j.attrib
    name = i['name']
    type = i['type']
    value = j.text

def setup(n: int) -> list:
    return [n, 1]

def update(state: list) -> bool:
    if state[0] <= 1:
        return False
    state[1] *= state[0]
    state[0] -= 1
    return True

def answer(state: list) -> int:
    return state[1]

f = mapcode.algorithm(setup, update, answer)

print(f(5))
'''

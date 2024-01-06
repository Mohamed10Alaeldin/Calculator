from tkinter import *
win = Tk() 
win.geometry("365x475+600+200")
win.title("Calculator")
# <------ BUTTONS COMMANDS -------->

# whenever insertion button is clicked
def btn_click(item):
    global expression
    expression = input_text.get()
    if expression in ("0","Invalid" ) :
        expression = item
    else:
        expression += item
    input_text.set(expression)
    
# clear the text display 
def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("0")

# Erase one Character from the right
def delete():
    expression = input_text.get()
    if expression and expression not in ("0", "Invalid") and len(expression) > 1:
        input_text.set(expression[:-1])
    else:
        input_text.set("0")

def bt_equal():
    global expression
    expression = input_text.get()
    # check if the expression is valid or not
    try:
        result = str(eval(expression)) # convert the expression string to result
        input_text.set(result) # print the result on input_text
    except:
        input_text.set("Invalid")
    expression = ""

# when the user clicks on Return key (Enter <--)
def Enter_key_pressed(event):
    bt_equal() # redirected to equals function
    
# ------------- initialize --------------
win.bind('<Return>', Enter_key_pressed) # if the user clicks the enter key on keyboard
input_text = StringVar() # used to get the instance of input field
expression = ""
input_text.set("0")

input_frame = Frame(win, width=312, height=50,bg="#EBE4D1", bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=0)
input_frame.pack()
 
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#EBE4D1", bd=0,justify=RIGHT, cursor = "hand2") 
input_field.pack(pady=40,padx=10) #increase the height of input field 

btns_frame = Frame(win, width=312, height=272.5, bg="#D2CBB8")
btns_frame.pack()

# first row
clear = Button(btns_frame, text = "C", fg = "blue", width = 10, height = 3, bd = 0, cursor = "hand2", command = bt_clear).grid(row = 0, column = 0, padx = 2, pady = 2)

mod = Button(btns_frame, text = "%", fg = "#000", width = 10, height = 3, bd = 0, cursor = "hand2", command = lambda: btn_click("%")).grid(row = 0, column = 1, padx = 2, pady = 2)

remove = Button(btns_frame, text = "Del", fg = "#000", width = 10, height = 3, bd = 0, cursor = "hand2", command = delete).grid(row = 0, column = 2, padx = 2, pady = 2)
 
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 2, pady = 2)
 
# second row
seven = Button(btns_frame, text = "7", fg = "#000", width = 10, height = 3, bd = 0, cursor = "hand2", command = lambda: btn_click("7")).grid(row = 1, column = 0, padx = 2, pady = 2)
 
eight = Button(btns_frame, text = "8", fg = "#000", width = 10, height = 3, bd = 0, cursor = "hand2", command = lambda: btn_click("8")).grid(row = 1, column = 1, padx = 2, pady = 2)
 
nine = Button(btns_frame, text = "9", fg = "#000", width = 10, height = 3, bd = 0, cursor = "hand2", command = lambda: btn_click("9")).grid(row = 1, column = 2, padx = 2, pady = 2)
 
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 2, pady = 2)
 
# third row
four = Button(btns_frame, text = "4", fg = "#000", width = 10, height = 3, bd = 0, cursor = "hand2", command = lambda: btn_click("4")).grid(row = 2, column = 0, padx = 2, pady = 2)
 
five = Button(btns_frame, text = "5", fg = "#000", width = 10, height = 3, bd = 0, cursor = "hand2", command = lambda: btn_click("5")).grid(row = 2, column = 1, padx = 2, pady = 2)
 
six = Button(btns_frame, text = "6", fg = "#000", width = 10, height = 3, bd = 0, cursor = "hand2", command = lambda: btn_click("6")).grid(row = 2, column = 2, padx = 2, pady = 2)
 
minus = Button(btns_frame, text = "-", fg = "#000", width = 10, height = 3, bd = 0, cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 2, pady = 2)
 
# fourth row
one = Button(btns_frame, text = "1", fg = "#000", width = 10, height = 3, bd = 0, cursor = "hand2", command = lambda: btn_click("1")).grid(row = 3, column = 0, padx = 2, pady = 2)
 
two = Button(btns_frame, text = "2", fg = "#000", width = 10, height = 3, bd = 0, cursor = "hand2", command = lambda: btn_click("2")).grid(row = 3, column = 1, padx = 2, pady = 2)
 
three = Button(btns_frame, text = "3", fg = "#000", width = 10, height = 3, bd = 0, cursor = "hand2", command = lambda: btn_click("3")).grid(row = 3, column = 2, padx = 2, pady = 2)
 
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 2, pady = 2)
 
# fifth row
two_zeros = Button(btns_frame, text = "00", fg = "#000", width = 10, height = 3, bd = 0, cursor = "hand2", command = lambda: btn_click("00")).grid(row = 4, column = 0, padx = 2, pady = 2)

zero = Button(btns_frame, text = "0", fg = "#000", width = 10, height = 3, bd = 0, cursor = "hand2", command = lambda: btn_click("0")).grid(row = 4, column = 1, padx = 2, pady = 2)
 
point = Button(btns_frame, text = ".", fg = "#000", width = 10, height = 3, bd = 0, cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 2, pady = 2)

equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "orange", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 2, pady = 2)
 
win.mainloop() # start the GUI
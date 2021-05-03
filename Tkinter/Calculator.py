# In the name of ALLAH
# I'm theove46

# import Tkinter module
from tkinter import *

tk = Tk()
tk.title("V Calculator")

# Display string
display = StringVar()

# Buttons row body 
def button_body(source, side):
    bdy = Frame(source, bd=3, bg="gray10", )
    bdy.pack(side=side, expand =YES, fill =BOTH)
    return bdy

# Button
def button(source, side, text, bg, command):
    bt = Button(source, text=text, bd=0, bg=bg, fg="white", height=2, font = ("Verdana", 14), command=command) 
    bt.pack(side=side, expand = YES, fill=BOTH)
    return bt

# Press C / full display clear
def clr():
    button(val, LEFT, text, "firebrick1", lambda show=display, q=text: show.set(''))

# Press dl/ right char delete
def delt():
    button(val, LEFT, text, "brown1", lambda show=display, q=text: show.set(show.get()[:-1]))

# Press digits
def digit(text):
        button(val, LEFT, text, "gray5", lambda show=display, q=text: show.set(show.get()+q))

# Press operations
def opr(text):
        button(val, LEFT, text, "gray5", lambda show=display, q=text: show.set(show.get()+q))


# Press equal
def eql():
    eq = Button(val, text="=", bg="dodger blue", fg="white", bd=0, height=2, font = ("Verdana", 14), command=None) 
    eq.pack(side=LEFT, expand = YES, fill=BOTH)
    eq.bind('<ButtonRelease-1>', lambda e, show=display: calc(show), '+')
    
# Calculate equal
def calc(display):
    try: display.set(eval(display.get()))
    except: display.set("math error")


# Display screen
Entry(tk, bd=0, bg="gray10", fg="gray80", font = ("Verdana", 20), relief=RIDGE, textvariable=display,
justify='right', width=18).pack(side=TOP, expand=YES, fill=BOTH, ipady=40)


# Buttons placing
for button_line in ( ["c", "dl", "//", "/"],
             ["7", "8", "9", "*"], 
             ["4", "5", "6", "-"],
             ["1", "2", "3", "+"],
             [".", "0", "%", "="]):
    val = button_body(tk, TOP)
    for text in button_line:
        if(text=="c"): clr()
        elif(text=="dl"): delt()
        elif(text=="="): eql()
        elif(text=="+" or text=="-" or text=="*" or text=="/" or text=="//" or text=="%"): opr(text)
        elif(text=="." or text=="0" or text=="1" or text=="2" or text=="3" or text=="4" or text=="5" 
            or text=="6" or text=="7" or text=="8" or text=="9"): digit(text)

# main loop
tk.mainloop()

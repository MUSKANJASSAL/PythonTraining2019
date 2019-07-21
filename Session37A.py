from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="purple")
button1.pack()
button2.pack()
button3.pack()
button4.pack()

# ----------------------------------------------------- #
# Fitting Widgets in your Layout #

one = Label(root, text="One", bg="red", fg="white")
one.pack()
two = Label(root, text="Two", bg="green", fg="black")
two.pack(fill=X)
three = Label(root, text="Three", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y)

# ----------------------------------------------------- #
# GRID LAYOUT #

# label1 = Label(root, text="Name", sticky=E)             North|South|East|West
# label2 = Label(root, text="Password", sticky=E)
# entry1 = Entry(root)
# entry2 = Entry(root)
#
# label1.grid(row=0)
# label2.grid(row=1)
#
# entry1.grid(row=0, column=1)
# entry2.grid(row=1, column=1)
# c = Checkbutton(root, text="Keep me logged in!!")
# c.grid(columnspan=2)
# Never mix grid and pack in the same master window. Tkinter will happily spend the rest of your lifetime
# trying to negotiate a solution that both managers are happy with. Instead of waiting, kill the application,
# and take another look at your code. A common mistake is to use the wrong parent for some of the widgets.

# ----------------------------------------------------- #
# Binding Functions to Layouts #
def printName():
# def printName(event):
    print("Hello, My name is Muskan")

button = Button(root, text="Print my name", command=printName)
# button = Button(root, text="Print my name")
# button.bind("<Button>",printName)
button.pack()

# ----------------------------------------------------- #
# Mouse Click Events #

def leftClick(event):
    print("LEFT")

def middleClick(event):
    print("MIDDLE")

def rightClick(event):
    print("RIGHT")

frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", leftClick())
frame.bind("<Button-2>", middleClick())
frame.bind("<Button-3>", rightClick())
frame.pack()

root.mainloop()
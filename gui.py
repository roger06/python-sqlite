from tkinter import *

root = Tk()

myLabel = Label(root, text="This will remove unwanted cookies")
myLabel2 = Label(root, text="But only from FireFox")

myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=2)

# myLabel.pack()



root.mainloop()


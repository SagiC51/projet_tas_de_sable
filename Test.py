from tkinter import *

gui = Tk()
frame1 = Frame(gui)
frame1.pack()

frame2 = Frame(gui)
frame2.pack(side = BOTTOM)

btn1 = Button(frame1, text="Valider", bg="green")
btn1.pack(side = LEFT)

btn2 = Button(frame1, text="Anuller", bg="red")
btn2.pack(side = LEFT)

label = Label(frame2, text="Welcome To WayToLearnX!")
label.pack(side = BOTTOM)

gui.mainloop()
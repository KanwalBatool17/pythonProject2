from tkinter import *
import random

root = Tk()
root.title("Dice Simulator")
root.geometry("600x500")
root.maxsize(550, 400)
root.minsize(400, 450)

label_1 = Label(root, font=("times",300, 'bold'), text = " ")


def Roll_dice():

    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684','\u2685']
    label_1.configure(text =random.choices(dice))
    label_1.pack()


Button_1 = Button(root, text="Dice Roll", font=(" bold", 25),bg="green",fg="white", command = Roll_dice)
Button_1.pack(side = TOP)

root.mainloop()
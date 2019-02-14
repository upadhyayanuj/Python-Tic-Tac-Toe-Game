import os
import time
print("*********************************")
print("* X & O Design by Anuj Upadhyay *")
print("* Player 1 [X] ---- Player 2 [O]*")
print("*********************************")
print()

p1 = input("Enter Player 1 Name : ")
p2 = input("Enter Player 2 Name : ")
print("Please wait....")
time.sleep(0.5)
os.system('cls')
from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("X and 0 By Anuj Upadhyay")
click = True
def checkwin(buttons):
    global click,p1,p2
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True

    if(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
        button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
        button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
        button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or
        button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
        button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
        button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
        button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
        tkinter.messagebox.showinfo("Winner '"+p1+"'", "Congrats '"+p1+"' You won the Game ")
        tk.destroy()
        print(p1,"Won the Game")
    elif(button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
        button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
        button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
        button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" or
        button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
        button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
        button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
        button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):
        tkinter.messagebox.showinfo("Winner '"+p2+"'", "Congrats '"+p2+"', You won the game ")
        tk.destroy()
        print(p2,"Won the Game")
    elif(button1["text"] != " " and button2["text"] != " " and button3["text"] != " " and
        button4["text"] != " " and button5["text"] != " " and button6["text"] != " " and
        button7["text"] != " " and button8["text"] != " " and button9["text"]!= " " and
        button3["text"] != " " and button5["text"] != " " and button7["text"] != " " and
        button1["text"] != " " and button5["text"] != " " and button9["text"] != " " and
        button1["text"] != " " and button4["text"] != " " and button7["text"] != " " and
        button2["text"] != " " and button5["text"] != " " and button8["text"] != " " and
        button3["text"] != " " and button6["text"] != " " and button9["text"] != " "):
        tkinter.messagebox.showinfo("No Winner", "Game Draw")
        tk.destroy()
        print("No winner,Game Draw")
buttons = StringVar()

button1 = Button(tk,bg = "red", text = " ", font = ("Times 26 bold"), height = 3, width = 6, command = lambda:checkwin(button1))
button1.grid(row = 1, column = 0, sticky = S+N+E+W)

button2 = Button(tk, bg = "blue", text = " ", font = ("Times 26 bold"), height = 3, width = 6, command = lambda:checkwin(button2))
button2.grid(row = 1, column = 1, sticky = S+N+E+W)

button3 = Button(tk, bg = "aqua", text = " ", font = ("Times 26 bold"), height = 3, width = 6, command = lambda:checkwin(button3))
button3.grid(row = 1, column = 2, sticky = S+N+E+W)

button4 = Button(tk, bg = "yellow", text = " ", font = ("Times 26 bold"), height = 3, width = 6, command = lambda:checkwin(button4))
button4.grid(row = 2, column = 0, sticky = S+N+E+W)

button5 = Button(tk, bg = "green", text = " ", font = ("Times 26 bold"), height = 3, width = 6, command = lambda:checkwin(button5))
button5.grid(row = 2, column = 1, sticky = S+N+E+W)

button6 = Button(tk, bg = "orange", text = " ", font = ("Times 26 bold"), height = 3, width = 6, command = lambda:checkwin(button6))
button6.grid(row = 2, column = 2, sticky = S+N+E+W)

button7 = Button(tk, bg = "pink", text = " ", font = ("Times 26 bold"), height = 3, width = 6, command = lambda:checkwin(button7))
button7.grid(row = 3, column = 0, sticky = S+N+E+W)

button8 = Button(tk, bg = "light green", text = " ", font = ("Times 26 bold"), height = 3, width = 6, command = lambda:checkwin(button8))
button8.grid(row = 3, column = 1, sticky = S+N+E+W)

button9 = Button(tk, bg = "gray", text = " ", font = ("Times 26 bold"), height = 3, width = 6, command = lambda:checkwin(button9))
button9.grid(row = 3, column = 2, sticky = S+N+E+W)

tk.mainloop()

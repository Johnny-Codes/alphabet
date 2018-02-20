from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import random

### 1 = addition, 2 = subtraction
operators = [1, 2]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
"t", "u", "v", "w", "x", "y", "z"]

win = ["Good work! Let's go again.", "Way to go. Your hard work is paying off!", "Good attention for detail!"]
oops = ["Opps. Keep trying! You'll get it next time.", "That's not right but nice try! Keep working at it."]


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("Learning is fun!")
        # Style().configure("TFrame", background="#333")
        self.pack(fill=BOTH, expand=1)

        mathButton = Button(self, text="Numbers", command=self.math)
        letterButton = Button(self, text="Letters", command=self.alphafun)

        mathButton.place(x=50, y=250)
        letterButton.place(x=250, y=250)

    def alphafun(self):
        ### Need to figure out how to clear the screen/previous iteration ###
        ### without destroy()ing the buttons from init_window ###
        ### tried delete(), pack_forget(), and others, but it deletes everything
        ### from init_window which I don't want deleted. I just want
        ### the stuff below deleted when it reruns.

        ### This is good, displays a random letter and text to screen
        self.x = random.choice(alphabet)
        text = Label(self, text=f"Type this letter: {self.x}")
        text.pack()

        ### Creating user input.
        self.user_input = StringVar()
        prompt = ttk.Entry(width=14, textvariable=self.user_input)
        prompt.place(x=150, y=200)

        ### Creates the submit button to run alphacheck()
        submitButton = Button(self, text="Submit", command=self.alphacheck)
        submitButton.place(x=255, y=200)

    def alphacheck(self):

        Label(self, text=f"Is {self.x} the same as {self.user_input.get()}?").pack()

        if self.user_input.get() == self.x:
            text = Label(self, text=f"\n{random.choice(win)}")
            text.pack()
            self.alphafun()
        else:
            text = Label(self, text=f"\n{random.choice(oops)}")
            text.pack()
            self.alphafun()

    def math(self):
        self.a = random.randint(1, 5)
        self.b = random.randint(1, 5)
        self.c = random.choice(operators)

        if self.c == 1:
            self.d = self.a + self.b

            Label(self, text=f"\nWhat is {self.a} + {self.b}?").pack()
            self.math_input = IntVar()
            prompt = ttk.Entry(width=14, textvariable=self.math_input)
            prompt.place(x=150, y=200)

            submitButton = Button(self, text="Submit", command=self.checkAddition)
            submitButton.place(x=255, y=200)

        if self.c == 2:
            ### don't want negative numbers for an answer
            ### you can delete this layer if/else statement...
            ### if you want negative numbers as answers
            if self.a >= self.b:
                self.d = self.a - self.b

                Label(self, text=f"\nWhat is {self.a} - {self.b}?").pack()
                self.math_input2 = IntVar()
                prompt = ttk.Entry(width=14, textvariable=self.math_input2)
                prompt.place(x=150, y=200)

                submitButton = Button(self, text="Submit", command=self.checkSubtraction)
                submitButton.place(x=255, y=200)
            ### delete below here if you want negative answers
            else:
                self.d = self.b - self.a

                Label(self, text=f"\nWhat is {self.b} - {self.a}?").pack()
                self.math_input3 = IntVar()
                prompt = ttk.Entry(width=14, textvariable=self.math_input3)
                prompt.place(x=150, y=200)

                submitButton = Button(self, text="Submit", command=self.checkSubtraction)
                submitButton.place(x=255, y=200)

    def checkAddition(self):
        if self.d == self.math_input.get():
            Label(self, text=f"\n{random.choice(win)}").pack()
            self.math()
        else:
            Label(self, text=f"\n{random.choice(oops)}").pack()
            Label(self, text=f"\nThe correct answer is {self.d}").pack()
            self.math()

    def checkSubtraction(self):
        if self.a >= self.b:
            if self.d == self.math_input2.get():
                text = Label(self, text=f"\n{random.choice(win)}")
                text.pack()
                self.math()
            else:
                text = Label(self, text=f"\n{random.choice(oops)}")
                text.pack()
                self.math()
        else:
            if self.d == self.math_input3.get():
                text = Label(self, text=f"\n{random.choice(win)}")
                text.pack()
                self.math()
            else:
                text = Label(self, text=f"\n{random.choice(oops)}")
                text.pack()
                self.math()

root = Tk()
root.geometry("400x300")

app = Window(root)
root.mainloop()

from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import random

### 1 = addition, 2 = subtraction
operators = [1, 2]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
"t", "u", "v", "w", "x", "y", "z"]

win = ["Good work! Let's go again.", "Way to go. Your hard work is paying off!", "Good attention for detail!",
       "You're awesome", "Good job!"]
oops = ["Opps. Keep trying! You'll get it next time.", "That's not right but nice try! Keep working at it."]


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("Learning is fun!")
        Style().configure("TFrame", background="#93F")
        self.pack(fill=BOTH, expand=1)

        mathButton = Button(self, text="Numbers", command=self.math)
        letterButton = Button(self, text="Letters", command=self.alphafun)

        mathButton.place(x=50, y=250)
        letterButton.place(x=250, y=250)

        ### The question label
        self.label_question = Label(self, text = '')
        self.label_question.place(x=150, y=0)
        self.label_question.pack()
        self.label_question.configure(font=("Courier", 16), background='#93F')

        ### The answer label
        self.label_answer = Label(self, text='')
        self.label_answer.place(x=150, y=50)
        self.label_answer.pack()
        self.label_answer.configure(font=("Courier", 10), background='#93F')

        ### The correct answer counter label
        self.correct_answers = 0
        self.label_counter = Label(self, text=f"\nCorrect answers: {self.correct_answers}")
        self.label_counter.pack()
        self.label_counter.configure(font=("Courier", 12), background="#93F")

    def alphafun(self):
        ### This is good, displays a random letter and text to screen
        self.x = random.choice(alphabet)
        self.label_question.configure(text=f"Type this letter: {self.x}")

        ### Creating user input.
        self.user_input = StringVar()
        prompt = ttk.Entry(width=14, textvariable=self.user_input)
        prompt.place(x=150, y=200)

        ### Creates the submit button to run alphacheck()
        submitButton = Button(self, text="Submit", command=self.alphacheck)
        submitButton.place(x=255, y=200)

    def alphacheck(self):

        if self.user_input.get() == self.x:
            self.label_answer.configure(text = f"\n{random.choice(win)}")
            self.correct_answers += 1
            self.label_counter.configure(text=f"Correct answers: {self.correct_answers}")
            self.alphafun()
        else:
            self.label_answer.configure(text = f"\n{random.choice(oops)}")
            self.alphafun()

    def math(self):
        self.a = random.randint(1, 5)
        self.b = random.randint(1, 5)
        self.c = random.choice(operators)

        if self.c == 1:
            self.d = self.a + self.b

            self.label_question.configure(text=f"What is {self.a} + {self.b}?")
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

                self.label_question.configure(text=f"What is {self.a} - {self.b}?")
                self.math_input2 = IntVar()
                prompt = ttk.Entry(width=14, textvariable=self.math_input2)
                prompt.place(x=150, y=200)
                submitButton = Button(self, text="Submit", command=self.checkSubtraction)
                submitButton.place(x=255, y=200)
            ### delete below here if you want negative answers
            else:
                self.d = self.b - self.a

                self.label_question.configure(text=f"What is {self.b} - {self.a}?")
                self.math_input3 = IntVar()
                prompt = ttk.Entry(width=14, textvariable=self.math_input3)
                prompt.place(x=150, y=200)
                submitButton = Button(self, text="Submit", command=self.checkSubtraction)
                submitButton.place(x=255, y=200)

    def checkAddition(self):
        if self.d == self.math_input.get():
            self.label_answer.configure(text=f"\n{random.choice(win)}")
            self.correct_answers += 1
            self.label_counter.configure(text=f"Correct answers: {self.correct_answers}")
            self.math()
        else:
            self.label_answer.configure(text=f"\n{random.choice(oops)}\nThe correct answer is {self.d}")
            self.math()

    def checkSubtraction(self):
        if self.a >= self.b:
            if self.d == self.math_input2.get():
                self.label_answer.configure(text=f"\n{random.choice(win)}")
                self.correct_answers += 1
                self.label_counter.configure(text=f"Correct answers: {self.correct_answers}")
                self.math()
            else:
                self.label_answer.configure(text=f"\n{random.choice(oops)}\nThe correct answer is {self.d}")
                self.math()
        else:
            if self.d == self.math_input3.get():
                self.label_answer.configure(text=f"\n{random.choice(win)}")
                self.correct_answers += 1
                self.label_counter.configure(text=f"Correct answers: {self.correct_answers}")
                self.math()
            else:
                self.label_answer.configure(text=f"\n{random.choice(oops)}\nThe correct answer is {self.d}")
                self.math()

root = Tk()
root.geometry("400x300")

app = Window(root)
root.mainloop()

### Resources ###
### http://zetcode.com/gui/tkinter/layout/
### https://pythonprogramming.net/tkinter-adding-text-images/?completed=/tkinter-menu-bar-tutorial/
### http://www.tkdocs.com/tutorial/widgets.html

import random

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
"t", "u", "v", "w", "x", "y", "z"]

numbers = [1, 2, 3, 4, 5]

# 1 = addition, 2 = subtraction
operators = [1, 2]

win = ["Good work! Let's go again.", "Way to go. Your hard work is paying off!", "Good attention for detail!"]

oops = ["Opps. Keep trying! You'll get it next time.", "That's not right but nice try! Keep working at it."]

def rand_let():
    x = random.choice(alphabet)
    print(f"\n{x}")
    y = input("\nType the above letter\n>>> ")
    if y == x:
        print(f"\n{random.choice(win)}")
        rand_let()
    elif y == "quit":
        start()
    else:
        print(f"\n{random.choice(oops)}")
        rand_let()

def rand_num():
    a = random.choice(numbers)
    b = random.choice(numbers)
    c = random.choice(operators)
    if c == 1:
        d = a + b
        print(f"\nWhat is {a} + {b}?")
        while True:
            try:
                x = int(input("\n>>> "))
                break
            except ValueError:
                print("\nThat's no number! Try again")
                print(f"\nWhat is {a} + {b}?")
            except KeyboardInterrupt:
                start()
        if d == x:
            print(f"\n{random.choice(win)}")
            rand_num()
        else:
            print(f"\n{random.choice(oops)}")
            print("The correct answer is", d)
            rand_num()
    if c == 2:
        # don't want negative numbers for an answer
        # you can delete this layer if/else statement...
        # if you want negative numbers as answers
        if a >= b:
            d = a - b
            print(f"\nWhat is {a} - {b}?")
            while True:
                try:
                    x = int(input("\n>>> "))
                    break
                except ValueError:
                    print("\nThat's no number! Try again")
                    print(f"\nWhat is {a} - {b}?")
            if d == x:
                print(f"\n{random.choice(win)}")
                rand_num()
            else:
                print(f"\n{random.choice(oops)}")
                print("The correct answer is", d)
                rand_num()
        # delete below here if you want negative answers
        else:
            print("b > a")
            print(f"\nWhat is {b} - {a}?")
            while True:
                try:
                    x = int(input("\n>>> "))
                    break
                except ValueError:
                    print("\nThat's no number! Try again")
                    print(f"\nWhat is {b} - {a}?")
            if d == x:
                print(f"\n{random.choice(win)}")
                rand_num()
            else:
                print(f"\n{random.choice(oops)}")
                print("The correct answer is", d)
                rand_num()

def start():
    x = int(input(("Do you want to play with letters or numbers\nPress 1 for letters and 2 for numbers\n>>> ")))
    if x == 1:
        rand_let()
    elif x == 2:
        rand_num()
    else:
        start()


start()

#tkinter or wxPython? GUI this so it looks good

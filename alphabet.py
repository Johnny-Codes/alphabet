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
        x = int(input("\n>>> "))
        if d == x:
            print(f"\n{random.choice(win)}")
            rand_num()
        else:
            print(f"\n{random.choice(oops)}")
            print("The correct answer is", d)
            rand_num()
    if c == 2:
        # don't want negative numbers for an answer
        # you can delete this second layer if statement...
        # if you want negative numbers as answers
        if a >= b:
            d = a - b
            print(f"\nWhat is {a} - {b}?")
            x = int(input("\n>>> "))
            if d == x:
                print(f"\n{random.choice(win)}")
                rand_num()
            elif ValueError in d:
                pass
            else:
                print(f"\n{random.choice(oops)}")
                print("The correct answer is", d)
                rand_num()
        else:
            d = b - a
            print(f"\nWhat is {b} - {a}?")
            x = int(input("\n>>> "))
            if d == x:
                print(f"\n{random.choice(win)}")
                rand_num()
            elif ValueError in d:
                pass
            else:
                print(f"\n{random.choice(oops)}")
                print("The correct answer is", d)
                rand_num()

def start():
    x = int(input(("Do you want to play with letters or numbers\nPress 1 for letters and 2 for numbers")))
    if x == 1:
        rand_let()
    else:
        rand_num()


start()
#rand_let()
#rand_num()





### Practice Code Below ###
#print(random.choice(alphabet))
#tkinter? GUI this shit so it looks good

# AlphaGUI.py

1 MAR 18: Changed font size, changed font to Comic Sans, and got rid of unnecessary text. Also added a counter to track correct answers for positive feedback.

21 FEB 18: Fixed the below issue. Added a counter to keep track of correct answers. Thinking about adding images or something with the Pillow module (most likely). Like, instead of just correct answers, maybe put a picture of an ice cream cone for each correct answer, I don't know. 

20 FEB 18: Got the game into tkinter for a GUI. Learned a lot. Need to find out how to clear contents in the frame without deleting the buttons. Possible solution is creating a new frame for the alphabet game and the math game but I don't quite understand it at the moment. Maybe add another class that runs it?

# Alphabet.py

Typing/alphabet game with a little bit of math

# What I learned:

tkinter, gui layouts

This was my attempt at a first project without researching answers. For the most part, I didn't, just needed a reminder of the import random and code that goes with it.

Lots of practice with Try/Exception. Really the only thing I had to look up and play with so that typing strings as an answer in the math excercises wouldn't break with the ValueError.

# To do:

[X] I really want to put this in a GUI as this was an exercise for me, but also a game for teaching my young kiddo. I think a good looking GUI will keep her interest more than looking at PowerShell. Leaning towards using wxPython.

[] I don't like tkinter's GUI, so I'm going to use Kivy and turn it into an app also. This is probably where future updates will go.

Hopefully I can keep this evolving as she gets older, adding dictionaries for word games, bigger numbers and adding multiplication and division.

# File: hello2.py

from Tkinter import *

class bidder:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.spades = Button(frame, text="Spades", command=self.say_spades)
        self.spades.pack(side=LEFT)

        self.clubs = Button(frame, text="Clubs", command=self.say_clubs)
        self.clubs.pack(side=LEFT)

        self.hearts = Button(frame, text="Hearts", command=self.say_hearts)
        self.hearts.pack(side=LEFT)

        self.diamonds = Button(frame, text="Diamonds", command=self.say_diamonds)
        self.diamonds.pack(side=LEFT)

        self._pass = Button(frame, text="Pass", command=self.say_pass)
        self._pass.pack(side=LEFT)

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

    def say_diamonds(self):
        print "D"

    def say_hearts(self):
        print "H"

    def say_spades(self):
        print "S"

    def say_clubs(self):
        print "C"

    def say_pass(self):
        print "P"

root = Tk()

app = bidder(root)

root.mainloop()


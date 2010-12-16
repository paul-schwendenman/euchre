# using Tkinter to display a hand of 5 random card images
# each time you click the canvas
# (images are in GIF format for Tkinter to display properly)
 
from Tkinter import *
import random
import basics

A = basics.card("A","C") 
B = basics.card("9","C")
C = basics.card("K","H")
D = basics.card("J","D")
E = basics.card("J","H")

 
root = Tk()
root.title("Click me!")
 
def create_cards():
    """
    create a list of 24 cards
    suit: club=C, diamond=D, heart=H spade=S
    rank: jack=J, queen=Q, king=K, numbers=1,9,10
    ace of spade would be SA, 9 of heart would be H9 and so on ...
    """
    return [ suit + rank for suit in "CDHS" for rank in list("9JQKA")+["10"] ]
 
def shuffle_cards(card_list):
    """random shuffle a list of cards"""
    # make a copy of the original list
    card_list1 = card_list[:]
    random.shuffle(card_list1)
    return card_list1
 
def pick_5cards(card_list):
    """pick five cards from the shuffled list"""
    return card_list[:5]
 
def create_images():
    """create all card images as a card_name:image_object dictionary"""
    card_list = create_cards()
    image_dict = {}
    for card in card_list:
        # all images have filenames the match the card_list names + extension
        image_dict[card] = PhotoImage(file=image_dir+card+".gif")
        #print image_dir+card+".gif" # test
    return image_dict
 
def next_hand(event):
    """create the card list, shuffle, pick five cards and display them"""
    card_list = create_cards()
    card_list = shuffle_cards(card_list)
    card_list = pick_5cards(card_list)
    root.title(card_list) # test
     
    # now display the card images at the proper location on the canvas
    x = 10
    y = 10
    for card in card_list:
        #print card, x, y # test
        canvas1.create_image(x, y, image=image_dict[card], anchor=NW)
        # calculate each NW corner x, y
        x += 15
#get the bid

# change this to the directory your card GIFs are in
image_dir = "~/expanded-euchre/pics/"
 
# load a sample card to get the size
photo1 = PhotoImage(file=image_dir+"C2.gif")
     
 
# load a sample card to get the size
photo1 = PhotoImage(file=image_dir+"C2.gif")
 
# make canvas 5 times the width of a card + 100
width1 = 5 * photo1.width() + 100
height1 = photo1.height() + 20
canvas1 = Canvas(width=width1, height=height1)
canvas1.pack()
 
# now load all card images into a dictionary
image_dict = create_images()
#print image_dict # test
 
class player():
    def bidder(self, master):
        def say_diamonds():
            self.bid = "D"
            self.bid_frame.pack_forget()

        def say_hearts():
            self.bid = "H"
            self.bid_frame.pack_forget()
            
        def say_spades():
            self.bid = "S"
            self.bid_frame.pack_forget()

        def say_clubs():
            self.bid = "C"
            self.bid_frame.pack_forget()

        def say_pass():
            self.bid = "P"
            self.bid_frame.pack_forget()

        self.bid_frame = Frame(master)
        self.bid_frame.pack()

        self.spades = Button(self.bid_frame, text="Spades", command="return 'C'")
        self.spades.pack(side=LEFT)

        self.clubs = Button(self.bid_frame, text="Clubs", command=say_clubs)
        self.clubs.pack(side=LEFT)

        self.hearts = Button(self.bid_frame, text="Hearts", command=say_hearts)
        self.hearts.pack(side=LEFT)

        self.diamonds = Button(self.bid_frame, text="Diamonds", command=say_diamonds)
        self.diamonds.pack(side=LEFT)

        self._pass = Button(self.bid_frame, text="Pass", command=say_pass)
        self._pass.pack(side=LEFT)

        self.button = Button(self.bid_frame, text="QUIT", fg="red", command=self.bid_frame.quit)
        self.button.pack(side=LEFT)

    def player(self, master):
        def say_1():
            self.play = "1"
            self.play_frame.pack_forget()

        def say_2():
            self.play = "2"
            self.play_frame.pack_forget()

        def say_3():
            self.play = "3"
            self.play_frame.pack_forget()

        def say_4():
            self.play = "4"
            self.play_frame.pack_forget()

        def say_5():
            self.play = "5"
            self.play_frame.pack_forget()

        def say_6():
            self.play = "6"
            self.play_frame.pack_forget()

        self.play_frame = Frame(master)
        self.play_frame.pack()

        self.buttons = [0]*6
        commands = [say_1, say_2, say_3, say_4, say_5, say_6]
        for index, _card in enumerate(self.cards):
            self.buttons[index] = Button(self.play_frame, text = "Card"+str(index), image=image_dict[_card.suit + _card.rank], command=commands[index])
            self.buttons[index].pack(side=LEFT)


# bind left mouse click on canvas to next_hand display
canvas1.bind('<Button-1>', next_hand)

# Make me a label
w = Label(root, text='Hello')
w.pack()

# Make me a row of buttons
p = player()
p.cards = [A,B,C,D,E]
p.bidder(root)

p.player(root)
     
print p.bid_frame.pack_slaves()
print p.play_frame.pack_slaves()
print root.pack_slaves()

root.mainloop()

bid = p.bid
play = p.play
print bid, play
# pack a top and a bottom frame
# put played cards in top frame. pack them on each side
# put msg/input on the bottom frame
# put sizes on the frame?


from Tkinter import *
import random
import basics

 
def Pass():
    pass

class player_tk():
    def __init__(self):
        # change this to the directory your card GIFs are in
        self.image_dir = "~/expanded-euchre/pics/"
        self.photo1 = PhotoImage(file=self.image_dir+"C2.gif")
        

        # now load all card images into a dictionary
        self.create_images()
        #print image_dict # test

    def display(self, top_card = None, trump = None, played_cards = 0, cards = [], msg = "", error = "", players = 0, dealer = None, team = []):
        pass

    #def ask(self, top_card = None, trump = None, played_cards = [], cards = [], msg = "", error = "", team = [99,99], players = [], dealer = None, secret = 0):
    def ask(self, top_card = None, trump = None, played_cards = [], cards = [], msg = "", error = "", team = [99,99], players = [], dealer = None, secret = 0):
        # in top: played_cards, top_card, score? (team)

        self.top_frame = Frame(master)
        self.top_frame.pack(side=TOP)

        self.bottom_frame = Frame(master)
        self.bottom_frame.pack(side=BOTTOM)
        # in bottom: cards / msg / input / error /
        self.msg = Label(bottom_frame, text = msg)
        self.show_score(bottom_frame, team)
        
        if (msg[:7] == "The win"): # Results
            self.show_played(self.top_frame, played_cards, dealer)

        elif (msg[-6:] == "play? "): # Play
            self.show_played(self.top_frame, played_cards, dealer)
            self.trump = Label(bottom_frame, text = trump)
            self.show_cards(bottom_frame)

        elif (msg[-4:] == "up? "):#Bid
            self.show_card(top_card, self.top_frame, relief=FLAT)
            self.show_cards(bottom_frame)
            self.show_yesno(self.bottom_frame, top_card)

        elif (msg[-6:] == "Pass? "): # Bid
            self.show_cards(bottom_frame)
            self.show_bid(self.bottom_frame)

        elif (msg[:5] == "Order"): # Pick it Up
            self.show_played(self.top_frame, played_cards, dealer)
            self.trump = Label(bottom_frame, text = trump)
            self.show_cards(bottom_frame)

        else: # Bad
            print "|%s|" % msg
            raise Exception("Should have called one of those ^")

        if error:
            tkMessageBox.showerror("Error", error)


    def show_score(self, master, scores):
        frame = Frame(master)
        frame.pack(side.RIGHT)
        teams = ["Your Team: ", "Other Team: "]
        
        for index, score in enumerate(scores):
            label = Label(frame, text = teams[index] + str(score))
            
            
    def show_played(self, master, played_cards, dealer, side=TOP):
        labels = ["3:", "P:", "1:", "U:"]
        if dealer:
            labels[dealer] = "*" + labels[dealer] + "*"
        played_frame = Frame(master)
        played_frame.pack(side = side)
        rows = [1,0,1,2]
        columns = [2,1,0,1]
        dummys = 4 * [basics.card()]
        played_cards.reverse()
#        for index, _card in enumerate(played_cards):
        for index, _card in enumerate((played_cards + dummys)[:4]):
            self.show_card(_card, played_frame, text=labels[index], relief = FLAT, grid = (rows[index],columns[index]))                
        
 
    def create_images(self):
        """create all card images as a card_name:image_object dictionary"""
        card_list = [ suit + rank for suit in basics.suits[1:] for rank in basics.ranks[1:] ]
        card_list += ["NoneNone"]
        self.image_dict = {}
        for card in card_list:
            # all images have filenames the match the card_list names + extension
            self.image_dict[card] = PhotoImage(file=self.image_dir+card+".gif")
            #print image_dir+card+".gif" # test
    def show_suits(self, master):

        self.bid_frame = Frame(master)
        self.bid_frame.pack()

        self.spades = Button(self.bid_frame, text="Spades", command=say_spades)
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

    def show_yesno(self, master, top_card):

        say_yes = {"S" : say_spades, "C" : say_clubs, "H" : say_hearts, "D" : say_diamonds,}[top_card.suit]

        self.bid_frame = Frame(master)
        self.bid_frame.pack()

        self.yes = Button(self.bid_frame, text="Spades", command=say_yes)
        self.yes.pack(side=LEFT)

        self.no = Button(self.bid_frame, text="No", command=say_pass)
        self.no.pack(side=LEFT)

        self.hearts = Button(self.bid_frame, text="Hearts", command=say_hearts)
        self.hearts.pack(side=LEFT)

        self.diamonds = Button(self.bid_frame, text="Diamonds", command=say_diamonds)
        self.diamonds.pack(side=LEFT)

        self._pass = Button(self.bid_frame, text="Pass", command=say_pass)
        self._pass.pack(side=LEFT)

        self.button = Button(self.bid_frame, text="QUIT", fg="red", command=self.bid_frame.quit)
        self.button.pack(side=LEFT)

    def show_cards(self, master, side=TOP):
        self.play_frame = Frame(master)
        self.play_frame.pack(side = side)

        commands = [self.say_1, self.say_2, self.say_3, self.say_4, self.say_5, self.say_6]
        for index, _card in enumerate(self.cards):
            self.show_card(_card, self.play_frame, func = commands[index])                

    def show_card(self, _card, master, text = "", func = Pass, side=LEFT, relief=RAISED, grid = None):
        frame = Frame(master)
        if text:
            label = Label(frame, text = text) 
            label.pack(side=LEFT)

        button = Button(frame, text = str(_card), image=self.image_dict[str(_card.suit) + str(_card.rank)], command=func, relief=relief)
        button.pack(side=LEFT)
        
        if grid:
            row, column = grid
            frame.grid(row = row, column = column)
        else:
            frame.pack(side=side)
        return button

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
    def say_1(self):
        self.play = "1"
        self.play_frame.pack_forget()

    def say_2(self):
        self.play = "2"
        self.play_frame.pack_forget()

    def say_3(self):
        self.play = "3"
        self.play_frame.pack_forget()

    def say_4(self):
        self.play = "4"
        self.play_frame.pack_forget()

    def say_5(self):
        self.play = "5"
        self.play_frame.pack_forget()

    def say_6(self):
        self.play = "6"
        self.play_frame.pack_forget()
 
# Make me a row of buttons
#p.bidder(root)

#p.show_card(A, root, side=TOP, relief=FLAT)

     
#print p.bid_frame.pack_slaves()
#print p.play_frame.pack_slaves()
#print root.pack_slaves()

if __name__ == "__main__":
    root = Tk()
    root.title("Euchre")

    p = player_tk()
    p.cards = [A,B,C,D,E]

    root.mainloop()


class extras():
    def __init__():
        # bind left mouse click on canvas to next_hand display
        canvas1.bind('<Button-1>', next_hand)

        # Make me a label
        w = Label(root, text='Hello')
        w.pack()
        # make canvas 5 times the width of a card + 100
        width1 = 5 * photo1.width() + 100
        height1 = photo1.height() + 20
        canvas1 = Canvas(width=width1, height=height1)
        canvas1.pack()
        # load a sample card to get the size

     
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


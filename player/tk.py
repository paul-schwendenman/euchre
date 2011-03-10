# pack a top and a bottom frame
# put played cards in top frame. pack them on each side
# put msg/input on the bottom frame
# put sizes on the frame?


from Tkinter import *
import random
import basics
from client import player_client

 
def Pass():
    pass

class player_tk(player_client):
    def __init__(self, master):
        #Setup the Keybindings

        master.bind('<space>', self.say_next)
        master.bind('<Return>', self.say_next)
        master.bind('q', self.say_quit)
        master.bind('1', self.say_1)
        master.bind('2', self.say_2)
        master.bind('3', self.say_3)
        master.bind('4', self.say_4)
        master.bind('5', self.say_5)
        master.bind('6', self.say_6)
        master.bind('y', self.say_yes)
        master.bind('n', self.say_pass)
        master.bind('p', self.say_pass)
        master.bind('s', self.say_spades)
        master.bind('d', self.say_diamonds)
        master.bind('h', self.say_hearts)
        master.bind('c', self.say_clubs)
        
        

        # change this to the directory your card GIFs are in
        self.image_dir = "~/expanded-euchre/pics/"
        self.photo1 = PhotoImage(file=self.image_dir+"C2.gif")
        
        self.master  = master        
        
        # now load all card images into a dictionary
        self.create_images()
        #print image_dict # test
        
        player_client.__init__(self, None)

    def display(self, top_card = None, trump = None, played_cards = 0, cards = [], msg = "", error = "", players = 0, dealer = None, team = []):
        pass

    def ask(self, top_card = None, trump = None, played_cards = basics.trick(), cards = [], msg = "", error = "", team = [99,99], players = [], dealer = None, secret = 0, quit = 0):
    #def ask(self, data):
        # in top: played_cards, top_card, score? (team)
        master = self.master
        self.cards = cards
        self.top_frame = Frame(master)
        self.top_frame.pack(side=TOP)

        self.bottom_frame = Frame(master)
        self.bottom_frame.pack(side=BOTTOM)
        # in bottom: cards / msg / input / error /
        self.msg = Label(self.bottom_frame, text = msg)
        self.msg.pack()
        self.show_score(self.top_frame, team)

        if (msg[:7] == "The win"): # Results
            played_cards._shift(-1, destructive=1)
            self.show_played(self.top_frame, played_cards, dealer)
            self.show_next(self.bottom_frame)
        elif (msg[-6:] == "play? "): # Play
            self.show_played(self.top_frame, played_cards, dealer)
            self.show_trump(self.bottom_frame, trump)
            self.show_cards(self.bottom_frame)

        elif (msg[-4:] == "up? "):#Bid
            self.show_played(self.top_frame, played_cards, dealer)
            self.show_card(top_card, self.top_frame, text = "Top Card: ", relief=FLAT)
            self.show_cards(self.bottom_frame)
            self.show_yesno(self.bottom_frame, top_card)

        elif (msg[-6:] == "Pass? "): # Bid
            self.show_played(self.top_frame, played_cards, dealer)
            self.show_cards(self.bottom_frame)
            self.show_bid(self.bottom_frame)

        elif (msg[-9:] == "discard? "): # Pick it Up
            trump = top_card.suit
            self.show_played(self.top_frame, played_cards, dealer)
            self.show_trump(self.bottom_frame, trump)
            self.show_cards(self.bottom_frame)

        elif (1): #someone bid. points scored, and game over?
            #import tkMessageBox
            self.hide_score()
            self.show_next(self.bottom_frame)
            #tkMessageBox.showinfo("Info", msg)
            #self.say("")
            
        else: # Bad
            print "|%s|" % msg
            raise Exception("Should have called one of those ^")

        if error:
            import tkMessageBox
            tkMessageBox.showerror("Error", error)

    def show_trump(self, master, trump):
        self.trump = Label(master, text = "Trump: " + str(trump))
        self.trump.pack()


    def show_score(self, master, scores):
        self.score = Frame(master)
        self.score.pack(side=RIGHT)
        teams = ["Your Team: ", "Other Team: "]
        
        for index, score in enumerate(scores):
            label = Label(self.score, text = teams[index] + str(score))
            label.pack()
    def hide_score(self):
        self.score.pack_forget()        
            
    def show_played(self, master, played_cards, dealer, side=TOP):
        labels = ["U:", "1:", "P:", "3:"]
        labels[dealer] = "*" + labels[dealer] + "*"
        labels.reverse()
        played_frame = Frame(master)
        played_frame.pack(side = side)
        rows = [1,0,1,2]
        columns = [2,1,0,1]
        dummys = 4 * [basics.card()]
        played_cards.cards.reverse()
#        for index, _card in enumerate(played_cards):
        for index, _card in enumerate((played_cards.cards + dummys)[:4]):
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

    def show_bid(self, master):

        self.bid_frame = Frame(master)
        self.bid_frame.pack()

        self.spades = Button(self.bid_frame, text="Spades", command=self.say_spades)
        self.spades.pack(side=LEFT)

        self.clubs = Button(self.bid_frame, text="Clubs", command=self.say_clubs)
        self.clubs.pack(side=LEFT)

        self.hearts = Button(self.bid_frame, text="Hearts", command=self.say_hearts)
        self.hearts.pack(side=LEFT)

        self.diamonds = Button(self.bid_frame, text="Diamonds", command=self.say_diamonds)
        self.diamonds.pack(side=LEFT)

        self._pass = Button(self.bid_frame, text="Pass", command=self.say_pass)
        self._pass.pack(side=LEFT)

        self.button = Button(self.bid_frame, text="QUIT", fg="red", command=self.say_quit)
        self.button.pack(side=LEFT)

    def show_yesno(self, master, top_card):

        #self.say_yes = {"S" : self.say_spades, "C" : self.say_clubs, "H" : self.say_hearts, "D" : self.say_diamonds,}[top_card.suit]

        self.bid_frame = Frame(master)
        self.bid_frame.pack()

        self.yes = Button(self.bid_frame, text="Yes", command=self.say_yes)
        self.yes.pack(side=LEFT)

        self.no = Button(self.bid_frame, text="No", command=self.say_pass)
        self.no.pack(side=LEFT)

        self.button = Button(self.bid_frame, text="QUIT", fg="red", command=self.say_quit)
        self.button.pack(side=LEFT)

    def show_cards(self, master, side=TOP):
        self.play_frame = Frame(master)
        self.play_frame.pack(side = side)
        label = Label(self.play_frame, text = "Your cards: ")
        label.pack(side=LEFT)
        commands = [self.say_1, self.say_2, self.say_3, self.say_4, self.say_5, self.say_6]
        for index, _card in enumerate(self.cards):
            self.show_card(_card, self.play_frame, func = commands[index])                

    def show_next(self, master):
        frame = Frame(master)

        button = Button(frame, text = "Next", command=self.say_next)
        button.pack(side=LEFT)
        
        frame.pack()
        return button

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

    def say(self, result):
        self.send(result) 
        self.bid = result
        #self.bid_frame.quit
        self.top_frame.pack_forget()
        self.bottom_frame.pack_forget()
        root.quit()
        
    def say_quit(self, *args):
        self.bid = "Q"
        self.say("Q")
        self.client_socket.close()
        self.quit = 1

    def say_next(self, *args):
        self.bid = ""
        self.say("")

    def say_diamonds(self, *args):
        self.bid = "D"
        self.bid_frame.pack_forget()
        self.say("D")

    def say_hearts(self, *args):
        self.bid = "H"
        self.bid_frame.pack_forget()
        self.say("H")
        
    def say_spades(self, *args):
        self.bid = "S"
        self.bid_frame.pack_forget()
        self.say("S")

    def say_clubs(self, *args):
        self.bid = "C"
        self.bid_frame.pack_forget()
        self.say("C")

    def say_pass(self, *args):
        self.bid = "P"
        self.bid_frame.pack_forget()
        self.say("P")

    def say_yes(self, *args):
        self.bid = "Y"
        self.bid_frame.pack_forget()
        self.say("Y")


    def say_1(self, *args):
        self.play = "1"
        self.play_frame.pack_forget()
        self.say("1")

    def say_2(self, *args):
        self.play = "2"
        self.play_frame.pack_forget()
        self.say("2")

    def say_3(self, *args):
        self.play = "3"
        self.play_frame.pack_forget()
        self.say("3")

    def say_4(self, *args):
        self.play = "4"
        self.play_frame.pack_forget()
        self.say("4")

    def say_5(self, *args):
        self.play = "5"
        self.play_frame.pack_forget()
        self.say("5")

    def say_6(self, *args):
        self.play = "6"
        self.play_frame.pack_forget()
        self.say("6")
 
    
# Make me a row of buttons
#p.bidder(root)

#p.show_card(A, root, side=TOP, relief=FLAT)

     
#print p.bid_frame.pack_slaves()
#print p.play_frame.pack_slaves()
#print root.pack_slaves()

if __name__ == "__main__":
    root = Tk()
    root.title("Euchre")

    p = player_tk(root)
    data = {}
    data["quit"] = 0
    p.quit = 0

    while not data["quit"] and not p.quit:
        data = p.recv()
        p.ask(**data)
        root.mainloop()
else:
    print __name__        
print hi
print __name__
# ** debug mode **
#    from cPickle import load, dump
#    with open("data", "r") as f:
#        data = load(f)

#    p.ask(**data)
    
#    root.mainloop()


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


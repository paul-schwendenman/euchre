from player import *

class player_test(player):
    """A simple test player is inherited from player, is interactive. No "graphics" """
    def ask(self, top_card = None, trump = None, played_cards = 0, cards = [], msg = "", error = "", players = 0, dealer = None, team = [], secret = 0):
        if (team):
            print "Score: ", team
        if (trump):
            print "Trump is: ", trump
        if (top_card): 
            print "the top card is", top_card
        if (dealer): 
            print "the dealer is", dealer + 0
        if (played_cards):
            print "Cards played so far:", played_cards
        elif (played_cards != 0):
            print "Cards played so far: None"
        print "Your hand", self.index + 0, "\033[1D :" , self
        print "                ",
        for i in range(len(self.cards)):
            print i + 1, "       ",
        print
        if error:
            print error
        output = (raw_input(msg) + " ").upper()[0]

        print "\033[2J \033[0;0H",
        return output



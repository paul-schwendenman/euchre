from player import *

class player_test(player):
    """A simple test player is inherited from player, is interactive. No "graphics" """
    def display(self, top_card = None, trump = None, played_cards = [], cards = [], msg = "", error = "", players = 0, dealer = None):
        if (trump):
            print "Trump is: ", trump
        if (top_card): 
            print "the top card is", top_card
        if (dealer): 
            print "the dealer is", dealer + 0
        if (len(played_cards)):
            print "Cards played so far:", played_cards
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



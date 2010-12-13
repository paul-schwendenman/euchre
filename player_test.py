import "player"

class player_test(player):
    """A simple test player is inherited from player, is interactive. No "graphics" """
    def display(self, top_card = None, trump = None, played_cards = [], cards = [], msg = "", error = "", players = 0):
        print "Your hand", self.index + 0, "\033[1D:" , self
        for i in range(len(self.cards)):
            print "        ",  i + 1,
        if (trump):
            print "Trump is: ", trump
        if (top_card): 
            print "the top card is", top_card
        if (dealer): 
            print "the dealer is", dealer + 0
        if (not len(played_cards)):
            print "Cards played so far:", played_cards
        print "     ",

        card = (raw_input(msg) + " ").upper()[0]

        print "\033[2J\033d[0;0H",
        return output



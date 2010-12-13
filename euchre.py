import curses

#shuffle
#set scores to zero
##deal cards
##bidding
##lead
##follow suit
##else 
###trump
###throw off



        


class table:
    """Class for the table, has players.
    Needs to handle: leader, dealer, points etc."""
    def __init__(self):
        pass

    def start(self, game):
        """begins a game by adding players"""
        self.game = game
        num_players = 0
        self.players = []
        self.players = [player(), comp(), comp(), comp(), ] 
#        self.players = [testPlayer(), comp(), comp(), comp(), ] 
#        self.players = [player(), player(), player(), player(), ] 
#        self.players = [player(), comp(), player(), comp(), ] 
#        self.players = [comp(), comp(), comp(), comp(), ] 
        for each_player in self.players:
            each_player.set_table(self)
            each_player.tricks_taken = 0
        self.players[0].name = "Paul"
        self.players[1].name = "Phil"
        self.players[2].name = "Sierra"
        self.players[3].name = "Julia"
    def __str__():
        pass
    def _shift(self, n, destructive = 0):
        n = n % len(self.players)
        tail = self.players[n:]
        self.players[n:] = []
        tail.extend(self.players)
        if destructive:
            self.players = tail
        else:
            return tail
        
    
class game:
    """Class for each hand in a game, meaning all the stuff needed to play for one hand."""
    def __init__(self):
        pass


    def start(self, table):
        """Starts up the deck and deals"""
        self.table = table
        bid = ""
        dealer = random.randrange(0,4)
        self.table._shift(self.dealer, 1)
        players = table.players
        self.deck = deck()
        self.deck.populate()
        self.deck.cards = self.deck.bubble_sort()
        self.deck.shuffle()
        self.deck.deal(players, self.dealer)

        for each_player in players:
            each_player.index = players.index(each_player)
            each_player.cards = each_player.bubble_sort()

    def bid(self, players):
        """Handles bidding for all players"""
        top_card = self.deck.cards[0]
        bid, index = self.get_bid(players, top_card)
        return (bid, index)
    def play(self, players, bid = 'S'):
        """Handles the card play given a bid"""
        team = 0
        trump = bid
        del bid
        #print "trump:\t\t", trump, "\ndealer:\t\t", self.dealer
        for each_player in players:
            each_player.cards = each_player.bubble_sort(trump)
        leader = self.dealer + 1
#        del self.dealer
        tricks = 5 * [trick()] #tricks = [trick(), trick(), trick(), trick(), trick(),]
        for _trick in tricks:
            #for index, player in enumurate(players):
            for index in range(0, 4):
                #print index
                play_this_card = players[((leader + index) % 4)].get_play(trump, _trick)
                players[((leader + index) % 4)].give(play_this_card, _trick)
                #print "this ", play_this_card
            #print
            winner = _trick.best_card(trump)
            players[winner.owner].tricks_taken += 1 
            #This is a print statement used for debugging
            for _player in players:
                _player.results(winner, leader, _trick)
            
            leader = winner.owner
            if (leader % 2):
                team -= 1
            else:
                team += 1
            
#        for _trick in tricks:
            while (len(_trick.cards) > 0):      
                _trick.give(_trick.cards[0], self.deck)
        return team

    def get_bid(self, players, top_card):
        """Handles the bid recovery for all players"""
        for index in range(1, 5):
            bid = players[((self.dealer + index) % 4)].bid(top_card, self.dealer)
            if self.good_bid(bid):
                players[self.dealer].pick_it_up(top_card)
                return (bid, index)
        for index in range(1, 5):
            bid = players[((self.dealer + index) % 4)].bid()
            if self.good_bid(bid):
                return (bid, index)
        return (bid, index)

    def good_bid(self, bid):
        """tests to see if the bid is "Good" """
        if (bid == "S" or bid == "C" or bid == "H" or bid == "D"):
            return 1
        else:
            return 0



class euchre:
    """Highest level class creates a game for play"""
    def __init__(self):
        """Sets up and starts a game."""
        self.table = table()
        
        index = 0
        self.game = game()
        self.game.team = [0, 0]
        team = self.game.team
        self.game.dealer = 0
        while(team[0] < 10 and team[1] < 10):
            self.table.start(self.game)
            self.game.start(self.table)
            (mybid, index) = self.game.bid(self.table.players)
            if (mybid == "P"):
                continue
            print "mybid, index", mybid, index
            result = self.game.play(self.table.players, mybid)            
            #result = self.bid.play(self.table.players)
            if (result == 5):
                team[(index + 1) % 2] += 2
                print "Team %c gains 2" % (['A', 'B'][index % 2])
            elif (result > 0):
                team[(index + 1) % 2] +=1
                print "Team %c gains 1" % (['A', 'B'][index % 2])
            elif (result < 0):
                team[(index + 0) % 2] +=2
                print "Team %c euchred. Team %c gains 2" % ((['A', 'B'][(index) % 2]),(['A', 'B'][(index + 1) % 2]))
            else:
                raise IndexError
            self.table._shift(1)
            self.game.dealer += 1
            self.game.dealer %= 4
        if (team[0] > 10):
            print "Team A wins!... 0, 2"
        else:
            print "Team A wins!... 1, 3"

                
                 

def main():
    euchre()

if __name__ == "__main__":
    main()


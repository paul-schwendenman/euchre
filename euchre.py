#!/usr/bin/python

import random
import basics
import player.curses_
import player.test
import player.server
import comp.comp
import logger

#from basics import deck
#from player.curses_ import *
#from player.test import *
#from player.server import *
#from comp.comp import comp as comp
#from logger import log

log = logger.log
comp = comp.comp
player_server = player.server.player_server
player_curses = player.curses_.player_curses
open_socket = player.server.open_socket
deck = basics.deck
trick = basics.trick

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
    def __init__(self, port = 5000):
        self.setup_socket(port)
        self.players = []
        self.players = [player_server(self.server_socket), comp(), comp(), comp(), ] 
#        self.players = [player_server(self.server_socket), comp(), player_server(self.server_socket), comp(), ] 
#        self.players = [player_server(self.server_socket), comp(), player_curses(), comp(), ] 
#        self.players = [player_curses(), comp(), player_curses(), comp(), ] 
#        self.players = [player_curses(), comp(), comp(), comp(), ] 
#        self.players = [player_test(), comp(), comp(), comp(), ] 
#        self.players = [player(), player(), player(), player(), ] 
#        self.players = [player(), comp(), comp(), comp(), ] 
#        self.players = [player(), comp(), player(), comp(), ] 
#        self.players = [comp(), comp(), comp(), comp(), ] 
        self.players[0].name = "Paul"
        self.players[1].name = "Phil"
        self.players[2].name = "Sierra"
        self.players[3].name = "Julia"

    def setup_socket(self, port):
        if port == 5000:
            self.server_socket = open_socket(port)
            port = 3000
            client = self.server_socket.accept()
            client[0].send(str(port))
            client[0].close()
        self.server_socket = open_socket(port)

    def start(self, game):
        """begins a game by adding players"""
        self.game = game

        num_players = 0
        for each_player in self.players:
            each_player.tricks_taken = 0
            each_player.clear()

    def global_message(self, msg, quit, players = []):	
        for _player_ in self.players:
            if _player_ != players:
                _player_.msg(msg, quit)
            elif quit:
                _player_.msg(msg, quit)
            
    def __str__(self):
        return str([player.__class__ for player in self.players])

    def _split(self, n):
        return self.players[:n], self.players[n:]

    def _shift(self, n, destructive = 0):
        b, a = self._split(n)
        c = a + b

        if destructive:
            self.players = c
        else:
            return c
    def quit(self, msg = ''):
        if msg:
            self.global_message(msg, 1)
        try:
            self.server_socket.close()
        except:
            pass
        exit()
            
    
class game:
    """Class for each hand in a game, meaning all the stuff needed to play for one hand."""
    def __init__(self):
        self.deck = deck()
        #dealer = random.randrange(0,4)
        #self.table._shift(self.dealer, 1)
        pass


    def start(self, table):
        """Starts up the deck and deals"""
        self.table = table
        bid = ""

#        players = self.table.players
#        self.deck = basics.deck()
        self.deck.populate()
        self.deck.cards = self.deck.bubble_sort()
        self.deck.shuffle()

        self.deck.deal(self.table.players, self.dealer)
        log("kitty: ", self.deck)
        for index, each_player in enumerate(self.table.players):
            each_player.index = index
            each_player.cards = each_player.bubble_sort()
            log(index, ": ", each_player)

    def bid(self):
        """Handles bidding for all players"""
        top_card = self.deck.cards[0]
        log("top card: ",top_card)
        for index in range(1, 5):
            bid = self.table.players[((self.dealer + index) % 4)].bid(top_card, self.dealer, self.table.players, self.team)
            log("I, ", self.dealer + index, "-", bid)
            if self.good_bid(bid):
                self.table.global_message(str(index) + ' ordered up ' + str(top_card) + '. So trump is '  + bid, 0 , self.table.players[index % 4])
                self.table.players[self.dealer].pick_it_up(top_card, self.dealer, self.team)
                return (bid, index)
        for index in range(1, 5):
            bid = self.table.players[((self.dealer + index) % 4)].bid(team = self.team)
            log("I, ", self.dealer + index, "-", bid)

            if self.good_bid(bid):
                self.table.global_message(str(index) + ' called ' + str(bid) + ' trump\n', 0 , self.table.players[index % 4])
                return (bid, index)

        return (bid, index)
    def play(self, trump, bidder):
        """Handles the card play given a bid"""
        team = 0
        for each_player in self.table.players:
            each_player.cards = each_player.bubble_sort(trump)
        leader = self.dealer + 1
#        del self.dealer
        #tricks = 5 * [trick()] 
        tricks = [trick(), trick(), trick(), trick(), trick(),]
        for _trick in tricks:
            #for index, player in enumurate(self.table.players):
            for index in range(0, 4):
                #print index
                play_this_card = self.table.players[((leader + index) % 4)].play(trump, _trick, self.dealer, self.team, self.table.players)
                log((leader + index) % 4, ":\t", play_this_card)
                self.table.players[((leader + index) % 4)].give(play_this_card, _trick)
                #print "this ", play_this_card
            #print
            winner = _trick.best_card(trump)
            self.table.players[winner.owner].tricks_taken += 1 
            log(winner.owner, ":\t", self.table.players[winner.owner].tricks_taken)
            for _player_ in self.table.players:
                _player_.results(winner, leader, _trick, self.team, self.table.players, self.dealer)
            
            leader = winner.owner
            if ((bidder + leader) % 2):
                team -= 1
            else:
                team += 1
            
        for _trick in tricks:
            _trick.clear()
        return team

    def good_bid(self, bid):
        """tests to see if the bid is "Good" """
        if (bid == "S" or bid == "C" or bid == "H" or bid == "D"):
            return 1
        else:
            return 0
    def score(self, result, bidder, team):
        if (result == 5):
            #You took them all! Take two.
            team[(bidder + 0) % 2] += 2
            #print "Team %c gains 2" % (['A', 'B'][bidder % 2])
            log("Team %s gains 2" % (['A...0,2', 'B...1,3'][bidder % 2]))
            self.table.global_message("Team %s gains 2" % (['A...0,2', 'B...1,3'][bidder % 2]), 0)

        elif (result > 0):
            #Made the bid
            team[(bidder + 0) % 2] +=1
            #print "Team %c gains 1" % (['A', 'B'][bidder % 2])
            log("Team %s gains 1" % (['A...0,2', 'B...1,3'][bidder % 2]))
            self.table.global_message("Team %s gains 1" % (['A...0,2', 'B...1,3'][bidder % 2]), 0)
        elif (result < 0):
            #Other team won give them two.
            team[(bidder + 1) % 2] +=2
            #print "Team %c euchred. Team %c gains 2" % ((['A', 'B'][(bidder) % 2]),(['A', 'B'][(bidder + 1) % 2]))
            log("Team %s euchred. Team %s gains 2" % ((['A...0,2', 'B...1,3'][(bidder) % 2]),(['A...0,2', 'B...1,3'][(bidder + 1) % 2])))
            self.table.global_message("Team %s euchred. Team %s gains 2" % ((['A...0,2', 'B...1,3'][(bidder) % 2]),(['A...0,2', 'B...1,3'][(bidder + 1) % 2])), 0)
        else:
            raise IndexError
        return team


class euchre:
    """Highest level class creates a game for play"""
    def __init__(self, port):
        """Sets up and starts a game."""
        global quit

        self.table = table(port)
        quit = self.table.quit
        
        index = 0
        self.game = game()
        self.game.team = [0, 0]
        team = self.game.team
        self.game.dealer = 0
        log("********* New Game *****************")
        redeals = 0
        while(team[0] < 10 and team[1] < 10):
            #keep playing until someone gets ten points.
            self.table.start(self.game)
            self.game.start(self.table)
            (thebid, bidder) = self.game.bid()
            # adjust the bidder for the dealer. do earlier?
            bidder = (bidder + self.game.dealer) % 4
            log("Bid: ", thebid, " Bidder:", bidder)
            log("Dealer: ", self.game.dealer)
            if (thebid == "P"):
                redeals += 1
                continue
#            print "Redeals: ", redeals
            redeals = 0
            
            result = self.game.play(thebid, bidder)            

            log("Result:\t", result)
            
            team = self.game.score(result, bidder, team)
            
            log("Score:", team)
            self.game.dealer += 1
            self.game.dealer %= 4
        if (team[0] > 10):
            msg = "Team A wins!... 0, 2"
        else:
            msg ="Team B wins!... 1, 3"
        print msg 
        log(msg)
        self.table.global_message(msg, 1)
def quit():
    print "should have been over written"
    exit()

def main(port):
    print "running euchre"
    a  = euchre(port)
    print "game over"

if __name__ == "__main__":
    port = 5000
    main(port)


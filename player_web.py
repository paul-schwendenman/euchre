#!/usr/bin/env python

import basics
from player_client import *

class player_web(player_client):
    def __init__(self):
        self.image_dir = "pics/"
        self.create_images()
        
        #self.open_socket()
        
    def ask(self, top_card = None, trump = None, played_cards = basics.trick(), cards = [], msg = "", error = "", team = [99,99], players = [], dealer = None, secret = 0, quit = 0):
    #def ask(self, data):
        # in top: played_cards, top_card, score? (team)
        self.cards = cards

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

        else: # Bad
            print "|%s|" % msg
            raise Exception("Should have called one of those ^")

        if error:
            import tkMessageBox
            tkMessageBox.showerror("Error", error)


    def callback(self):
        pass
    def create_images(self):
        """create all card images as a card_name:image_object dictionary"""
        card_list = [ suit + rank for suit in basics.suits[1:] for rank in basics.ranks[1:] ]
        card_list += ["NoneNone"]
        self.image_dict = {}
        for card in card_list:
            # all images have filenames the match the card_list names + extension
            self.image_dict[card] = self.image_dir+card+".gif"
            #print image_dir+card+".gif" # test

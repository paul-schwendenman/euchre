import "comp"

class comp_if(comp):
    """Comp_if is inherited from comp and picks the cards different, everything else the same."""
    
    def get_play_ai(self, trump, played_cards):
        """AI play rewritten without try...except"""
        index = 0
        this = player()
        this.set_hand(played_cards)
        if (len(played_cards.cards) > 0):
            if (len(self.search(played_cards.cards[0].suit)) > 0):
                cards = self.search(played_cards.cards[0].suit)
                for card in cards:
                    print card,
                print
                this.bubble_sort(trump)
                index = len(cards) - 1
                for card in cards:
                    if (card.value(trump) > played_cards.cards[0].value(trump)):
                        index = cards.index(card)
            elif(len(self.search(trump)) > 0):
                cards = self.search(trump)
                this.bubble_sort(trump)
                index = len(cards) - 1
                for card in cards:
                    if (card.value(trump) > played_cards.cards[0].value(trump)):
                        index = cards.index(card)
            else:
                pass
#                index = random.randrange(0, len(self.cards) - 1)
        else:
            cards = self.cards
            if ((cards[0].value(trump)) > 27):
                index = 0
            else:
                for card in cards:
                    if card.value(trump) < 20:
                        index = cards.index(card)
                        break
         
        # This print is for debugging        
        print "(" , self.index, ": " , self.cards[index] , ")", self
        return self.cards[index]


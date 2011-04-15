from comp import *

class comp_try(comp):
    """Comp_try is inherited from comp and picks the cards different, everything else the same."""
    
    def ai(self, trump, played_cards):
        """AI version of play using try...except"""
        results = hand()
        try:
            print """Try to follow suit"""
            results.cards = self.search(suit = played_cards.cards[0].suit)
            print results
            if ((((ranks.index(trump) + ranks.index(played_cards.cards[0].suit)) % 2) == 0) and (trump != played_cards.cards[0].suit)):
                for card in results.cards:
                    if(card.rank == "J"):
                        results.remove(card(played_cards.cards[0].suit, "J"))
            results.bubble_sort()
            if (len(results.cards) != 1):
                index = random.randrange(0, len(results.cards) - 1)
                index = self.cards.index(results.cards[index])                    
            else:
                index = 0
        except IndexError:
            print """This is the first player of trick aka the Leader"""        
            try:
                print """What should I lead?"""
                if (self.cards[0].value(trump) == 28):
                    index = 0
                else:
                    print """Don't have the right"""
                    for card in self.cards:
                        if (card.value(trump) < 20):
                            print """Highest non-trump"""
                            index = self.cards.index(card)
                            break
                        else:
                            print """All trump???"""
                            index = 0
#                index = random.randrange(0, len(self.cards) - 1)
            except ValueError:
                print """This is the last trick"""
                index = 0
        except ValueError:
            print """Can't follow suit (not leader)"""
            try:
                results.cards = self.search(suit = trump)
                print results
                results.bubble_sort()
                if (len(results.cards > 1)):
                    index = random.randrange(0, len(results.cards) - 1)
                else:
                    index = 0
            except ValueError:
                print """No trump... through smallest card"""
                cards = self.search(rank = self.cards[len(self.cards) - 1].rank)
                try:
                    print """More than one?"""
                    index = random.randrange(0, len(cards) - 1)
                except ValueError:
                    print """The first (and only) one"""
                    index = 0
                finally:
                    print """Reassign index from "cards" to self.cards"""
                    index = self.cards.index(cards[index])                    
            except:
                print """This is the last trick"""
                index = 0
        else:
            pass
        finally:
            pass
        print "(" , self.index, ": " , self.cards[index] , ")", self
        
        return self.cards[index]


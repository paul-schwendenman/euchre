from basics import *

a = card("A","C")
b = card("10","S")
c = card("J","H")
d = card("9","C")
e = card("Q","D")
f = card("J","D")

aa = trick()
bb = trick()
cc = trick()
dd = trick()
ee = trick()


aa.cards = [a,b,c,d]
bb.cards = [a,f,c,e]

class both(deck, trick):
  pass

aaa = both()
bbb = both()

aaa.populate()
#aaa.shuffle()



for rank in ranks:
  bbb.cards = aaa._higher(rank)
  print rank, ": ", bbb
  print
  
  
  
# _suits works.
# _trump suceeded.
# _notTrump also suceeded
# _higher fails... "A" < "K" < "Q" do it by rank.index() not string value
# _lower also fails





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

cc.cards = [d,c,c,c]

aa.cards = [a,b,c,d]
bb.cards = [a,f,c,e]

class both(deck, trick):
  pass

aaa = both()
bbb = both()

aaa.populate()

for i in range(0,10):
  aaa.shuffle()
  bbb.cards = aaa.cards[:4]
  print bbb
  for suit in suits[1:]:
    z = bbb.best_card(suit)
    y = bbb.old_bestcard(suit)
    if z != y:
      print suit, z, y

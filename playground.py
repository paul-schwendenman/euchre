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

aaa.populate()
aaa.shuffle()




#!/usr/bin/python

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

def ask(dealer):
  dealer %= 4
  if dealer == 0:
    print " x \nx x\n D "
  elif dealer == 1:
    print " x \nD x\n x "
  elif dealer == 2:
    print " D \nx x\n x "
  elif dealer == 3:
    print " x \nx D\n x "

for i in range(0, 4):
  for j in range(i + 1, i + 5):
#    if (i+2) % 4 == j % 4:
      print "dealer", i, "you", j % 4
      dealer = i - j
      ask (dealer)


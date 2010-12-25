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
dd.cards = ["a","b","c","d"]

print aa

print a

from pickle import dumps, loads

aaa = dumps(a)
print loads(aaa)

qqq = dumps(aa)
cc = loads(qqq)
print cc
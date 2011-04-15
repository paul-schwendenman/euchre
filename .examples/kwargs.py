class nothing():
    def this(self, **blah):
        print blah["this"], blah

g = nothing()
a = {"this" : 0, "that" :1}
b = {"this" : 12, "that" :1}
g.this(**a)
g.this(**b)
this = "peas   "
that = "carrots"
g.this(this=this,that=that)
g.this(**locals())


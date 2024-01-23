class oranges:
    def flavor (self):
        print ("oranges are sweet like Kevin")
    def shape (self):
        print ("oranges are round shape")
    def color (self):
        print ("oranges are orange")

class cherry:
    def flavor (self):
        print ("cherry is sweet")
    def shape (self):
        print ("cherry is small")
    def color (self):
        print ("cherries are red")

class lemon:
    def flavor (self):
        print ("lemon is sour")
    def shape (self):
        print ("lemon is round")
    def color (self):
        print ("lemon is yellow")
def color(fruit):
    fruit.color()



orangeobj = oranges ()
cherryobj = cherry ()
lemonobj = lemon ()
color(orangeobj)
color(cherryobj)
color(lemonobj)

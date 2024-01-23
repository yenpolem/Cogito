class oranges:
    def flavor (self):
        print ("oranges are sweet")

    def shape (self):
        print ("oranges are round shape")

class cherry:
    def flavor (self):
        print ("cherry is sweet")
    def shape (self):
        print ("cherry is small")

class lemon:
    def flavor (self):
        print ("lemon is sour")
    def shape (self):
        print ("lemon is round")
def shape(fruit):
    fruit.shape()



orangeobj = oranges ()
cherryobj = cherry ()
lemonobj = lemon ()
shape(orangeobj)
shape(cherryobj)
shape(lemonobj)

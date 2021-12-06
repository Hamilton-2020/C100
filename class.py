class Scrunchie(object):
    def __init__(self, color, size, material):
        self.color= color
        self.size=size
        self.material=material

    def changeColor(self,newColor):
        self.color=newColor
        print("The color has been changed to "+self.color)

newScrunchie=Scrunchie("red", "large", "velvet")

newScrunchie.changeColor("purple")

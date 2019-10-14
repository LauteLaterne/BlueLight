class Zahl:

    def __init__(self, wert):
        self.__x = wert

    def __getX(self):
        return self.__x

    def __setX(self, wert):
        if wert > 100:
            self.__x = 100
        else:
            self.__x = wert

    x = property(__getX, __setX)


zahl1 = Zahl(10)
print (zahl1.x)

zahl1.x = 13333
print (zahl1.x)

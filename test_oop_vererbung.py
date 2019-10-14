class RiegelBasis:

    name = "Riegelbasis"
    
    def __init__(self, mg_ho, mg_bu):
        self.__MengeHonig = mg_ho
        self.__MengeButter = mg_bu

    def __str__(self):
        zutaten = "\n" + "Basisrezept zum Backen für die " + RiegelBasis.name + " mit den Zutaten:"
        zutaten += "\n" + "  Honig " +  str(self.__MengeHonig) + " gr"
        zutaten += "\n" + "  Butter " +  str(self.__MengeButter) + " gr"
        return zutaten

    def Backen():
        pass
            

class KraftRiegel(RiegelBasis):

    name = "Kraftriegel"

    def __init__(self, mg_ho, mg_bu, mg_haf, mg_dingepu, mg_man, mg_has):
        RiegelBasis.__init__(self, mg_ho, mg_bu)
        self.__MengeHafer = mg_haf
        self.__MengeDinkelGepuf = mg_dingepu
        self.__MengeMandeln = mg_man
        self.__MengeHasselnuss = mg_has

    def __str__(self):
        zutaten = RiegelBasis.__str__(self)
        zutaten += "\n" + "für den " + KraftRiegel.name + " kommen folgende Zutaten hinzu:"
        zutaten += "\n" + "  Hafer " +  str(self.__MengeHafer) + " gr"
        zutaten += "\n" + "  Dinkel " +  str(self.__MengeDinkelGepuf) + " gr"
        zutaten += "\n" + "  Mandeln " +  str(self.__MengeMandeln) + " gr"
        zutaten += "\n" + "  Hasselnuss " +  str(self.__MengeHasselnuss) + " gr"
        return zutaten

   
riegel1 = RiegelBasis(200, 50)
print(riegel1)

riegel2 = KraftRiegel(1, 2, 3, 4, 5, 6)
print(riegel2)

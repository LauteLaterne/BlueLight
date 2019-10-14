# Übung: Programm zum Definieren einer neuen Klasse in einem Programm
# Die Klasse soll einem Vermieter ermöglichen den Wohnungsbestand zu verwalten.
# Dazu soll eine Klasse definiert werden.
# Wohnungseigenschaften: Stadt, Postleitzahl, Strasse, Hausnummer, Anzahl Zimmer, Gesamtfläche.
# Die Klasse soll Methoden haben, um die Werte auszulesen und zu verändern --> dafür die Standardschleifen verwenden
# Step 2: Methoden schreiben
# Step3: Im Hauptprogramm Schleife einfügen zum Ändern der Werte von Objektattributen
# Step 4: Dann eine Klassenvariable einfügen zum "Zählen" der erzeugten Objekte

class Wohnung:
    """Erstellt die Klasse Wohnung für eine Hausverwaltung"""

    anzahl = 0

    def __init__(self, std, plz, strna, hnr, az, gf, m):
        """Definiert die Attribute der Klasse Wohnung"""
        
        """*Stadt (string): Stadt, in der sich die Wohnung befindet
            *PostLZ (string): Postleitzahl der Stadt
            *Strasse (string): Strasse, in der sich die Wohnung befindet
            *Hausnummer (string): Hausnummer der Strasse, in der sich die Wohnung befindet
            *Zimmeranzahl (integer): Anzahl der Zimmer in der Wohnung
            *Wohnfläche (float): Wohnfläche in der Wohnung in qm
            *AktuelleMiete(float): Aktueller Mietpreis für die Wohnfläche ohne Nebenkosten"""
        
        self.__Stadt = std
        self.__PostLZ = plz
        self.__Strasse = strna
        self.__Hausnummer = hnr
        self.__Zimmeranzahl = az
        self.__Wohnfläche = gf
        self.__Miete = m
        Wohnung.anzahl += 1

    def getStadt(self):
            """Gibt die Stadt der Wohnung aus"""
            return self.__Stadt

    def getStrasse(self):
            """Gibt die Strasse der Wohnung aus"""
            return self.__Strasse

    def getMiete(self):
            """Gibt die Stadt der Wohnung aus"""
            return self.__Miete

    def setMiete(self, miete_neu):
            """Ändert die Miete der Wohnung"""
            self.__Miete = miete_neu

    def __del__(self):
        """Löscht das Objekt Wohnung"""
        Wohnung.anzahl -= 1
        print("Ein Objekt Wohnung wurde gelöscht")
        print("In der Liste sind noch %d Wohnungen enthalten" %Wohnung.anzahl)

           
class PremiumWohnung(Wohnung):
    """Erstellt eine untergeordnete Klasse PremiumWohnung abgeleitet von der Klasse Wohnung"""

    anzahl = 0

    def __init__(self, std, plz, strna, hnr, az, gf, m, stellp):
        """Definiert die Attribute der untergeordneten Klasse PremiumWohnung"""
        
        """*Stadt (string): Stadt, in der sich die Wohnung befindet
            *PostLZ (string): Postleitzahl der Stadt
            *Strasse (string): Strasse, in der sich die Wohnung befindet
            *Hausnummer (string): Hausnummer der Strasse, in der sich die Wohnung befindet
            *Zimmeranzahl (integer): Anzahl der Zimmer in der Wohnung
            *Wohnfläche (float): Wohnfläche in der Wohnung in qm
            *AktuelleMiete(float): Aktueller Mietpreis für die Wohnfläche ohne Nebenkosten
                    *Stellplatz (bool): Hat die Wohnung einen Stellplatz für ein Fahrzeug?"""

        Wohnung.__init__(self, std, plz, strna, hnr, az, gf, m)
        self.__Stellplatz = stellp
        PremiumWohnung.anzahl += 1

    def getStellplatz(self):
        """Gibt aus, ob ein Stellplatz vorhanden ist"""
        return self.__Stellplatz

    def __del__(self):
        """Löscht das Objekt PremiumWohnung"""
        PremiumWohnung.anzahl -= 1
        print("Ein Objekt PremiumWohnung wurde gelöscht")
        print("In der Liste sind noch %d PremiumWohnungen enthalten" %PremiumWohnung.anzahl)


# Start Hauptprogramm
# Erzeugen von Objekten aus der Klasse Wohnung
print("Anzahl Objekte Wohnung:", Wohnung.anzahl)
wohnung1 = Wohnung("Gilching", "82205", "Andechserstrasse", "8a", 3, 72.2, 1003)
print("Anzahl Objekte Wohnung:", Wohnung.anzahl)
wohnung2 = Wohnung("München", "80993", "Paula-Ludwig-Weg", "8", 4, 85, 0)
print("Anzahl Objekte Wohnung:", Wohnung.anzahl)
wohnung3 = Wohnung("München", "81541", "Edelweißstraße", "3", 2, 59, 703)
print("Anzahl Objekte Wohnung:", Wohnung.anzahl)
wohnung4 = Wohnung("Gilching", "82205", "St. Vitusstraße", "15", 6, 180, 0)

print(wohnung1.getStadt())
print(wohnung1.getStrasse())
print(wohnung1.getMiete())
wohnung1.setMiete(1100)
print(wohnung1.getMiete())
print(Wohnung.anzahl)
print(wohnung4.anzahl)

# Erzeugen von Objekten aus der Klasse PremiumWohnung
premwohnung1 = PremiumWohnung("Gilching", "82205", "Schützenweg", "5", 3, 84, 1100, True)
print("Anzahl Objekte PremiumWohnung:", PremiumWohnung.anzahl)
print(premwohnung1.getStrasse())
print(premwohnung1.getStellplatz())


# Um Werte in dem Objekt Wohnung zu ändern, eine Eingabeschleife aus dem vorherigen Programm einbauen...

aktion = "ja"
start= ""
print("\n", "*** Willst Du die Miete einer BESTIMMTEN Wohnung ändern?  ***")
start = input("Zum Starten gebe 'ja' ein: ")
print("")

if start == "ja":
    while aktion == "ja":    
        print("TESTAUSGABE WIEDERHOLUNGSSCHLEIFE")
        aktion = input("Wenn Du das wiederholen möchtest gebe 'ja' ein: ")
        print("")
    else:
        print("\n", "ENDE ÄNDERN DER MIETE !! ")

print ("\n", "--> ENDE Programm", "\n")






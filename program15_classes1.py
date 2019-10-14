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
        """Stadt (string
            PostLZ (string)
            Strasse (string)
            Hausnummer (string)
            Zimmernzahl (integer)
            Gesamtfläche (float)
            AktuelleMiete(float)"""
        
        Wohnung.anzahl += 1
        self.__ObjektNr = Wohnung.anzahl
        self.__Stadt = std
        self.__PostLZ = plz
        self.__Strasse = strna
        self.__Hausnummer = hnr
        self.__Zimmeranzahl = az
        self.__Gesamtfläche = gf
        self.__Miete = m
                
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

    def __str__(self):
        return "\n" + "Von der Klasse <Wohnung> existieren jetzt " + str(Wohnung.anzahl) + " Objekte." + "\n"

    def __repr__(self):
        return "\n" + "Mit der eingebauten Funktion 'repr()' können Sie Informationen zu einem Objekt abrufen"\
               "\n" + "z.B. die Miete von Wohnung #" + str(self.__ObjektNr)  + " beträgt aktuell "\
               + str(self.__Miete) + " EURO" + "\n"

    def __del__(self):
        """Löscht das Objekt Wohnung"""
        Wohnung.anzahl -= 1
        print("Ein Objekt Wohnung wurde gelöscht")
        print("In der Liste sind noch %d Wohnungen enthalten" %Wohnung.anzahl)
           

# Start Hauptprogramm
# Erzeugen der Objekte aus der Klasse
print(Wohnung.anzahl)
wohnung1 = Wohnung("Gilching", "82205", "Andechserstrasse", "8a", 3, 72.2, 1003)
print(Wohnung.anzahl)
wohnung2 = Wohnung("München", "80993", "Paula-Ludwig-Weg", "8", 4, 85, 0)
print(Wohnung.anzahl)
wohnung3 = Wohnung("München", "81541", "Edelweißstraße", "3", 2, 59, 703)
print(Wohnung.anzahl)
wohnung4 = Wohnung("Gilching", "82205", "St. Vitusstraße", "15", 6, 180, 0)
print(Wohnung.anzahl)

print(wohnung4)
print(repr(wohnung3))

print(wohnung1.getStadt())
print(wohnung1.getStrasse())
print(wohnung1.getMiete())
wohnung1.setMiete(1100)
print(wohnung1.getMiete())

print(Wohnung.anzahl)
print(wohnung4.anzahl)

wohnung1
listeWohnungen = [wohnung1, wohnung2, wohnung3, wohnung4]
listeWohnungen[0]


# Um die Werte in einem Wohnung-Objekt zu ändern, eine Eingabeschleife aus dem vorherigen Programm einbauen...

aktion = "ja"
start= ""
print("\n", "*** Willst Du die Miete einer BESTIMMTEN Wohnung ändern?  ***")
start = input("Zum Starten gebe 'ja' ein: ")
print("")

if start == "ja":
    while aktion == "ja":    
        print("TESTAUSGABE WIEDERHOLUNGSSCHLEIFE  --> Ändern der Miete (noch) nicht programmiert" + "\n")
        aktion = input("Wenn Du das wiederholen möchtest gebe 'ja' ein: ")
        print("")
    else:
        print("\n", "ENDE ÄNDERN DER MIETE !! ")

print ("\n", "--> ENDE Programm", "\n")






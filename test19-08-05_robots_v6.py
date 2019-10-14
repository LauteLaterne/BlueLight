#Übungen von python-kurs.eu zu OOP - Übungen zu Klassen, Instanzen. Klassenvariablen/Klassenmethoden vs. Instanzattribute

class Roboter:
    
    anzahl = 0
    
    def __init__(self, name, baujahr):
        self.name = name
        self.baujahr = baujahr
        Roboter.anzahl += 1
        # anstatt "Roboter.anzahl" ist auch die allgemeinere Bezeichnung "type(self).anzahl" möglich --> führt zum gleichen Wert --> diese ist besser bei Vererbung der 
        print("Methode  '__init__'  wurde ausgeführt.")
        print("Roboter Nr. " + str(Roboter.anzahl) + " mit dem Namen <" + self.name + "> wurde erzeugt.")

    def __del__(self):
        print("Die Instanz Nr. " + str(Roboter.anzahl) + " der Klasse 'Roboter' mit dem Namen <" + str(self.name) + "> wurde GELÖSCHT")   
        Roboter.anzahl -= 1
       
    def SageHallo(self):
        print("Ich sage: WELCOME to the PLEASUREDOME!")

    def SetNewName(self, name):
        self.name = name

    def SetNewBaujahr(self, baujahr):
        self.baujahr = baujahr

    def GetName(self):
        print("\n")
        print("Mein Name ist " + self.name + " und mein Baujahr ist " + self.baujahr + ".")

    @staticmethod
    def GetAnzahlRoboter():
        return Roboter.anzahl
        
    
print("\n")

r1 = Roboter("HAL3000", "1968")
r2 = Roboter("Marvin", "1978")
r3 = r2

print("\n")
print("Das built-in-Attribut '__name__' ist hat den Wert: " + __name__)
print("r1 == r2:", r1 == r2)
print("r3 == r2:", r3 == r2)

print("Dictionary von Objekt r1:", r1.__dict__)
print("Dictionary von Objekt r2:", r2.__dict__)

r1.SetNewName("Gertrud7000")
r1.SetNewBaujahr("2042")

r1.SageHallo()
r1.GetName()
print(Roboter.GetAnzahlRoboter())
print(r1.GetAnzahlRoboter())

print("Dictionary von Objekt r1:", r1.__dict__)
print("Dictionary von Objekt r2:", r2.__dict__)

print(r1.name)

for rob in [r1,r3]:
    del rob

del r3

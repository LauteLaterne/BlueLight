class Roboter:

    def SageHallo(self):
        print("Ich sage: BULLSHIT!")

    def SetName(self, name):
        self.name = name

    def SetBaujahr(self, baujahr):
        self.baujahr = baujahr

    def GetName(self):
        print("Mein Name ist " + self.name + " und mein Baujahr ist " + self.baujahr + ".")

r1 = Roboter()
r2 = Roboter()

r3 = r2

print("__name__:", __name__)

print(r1 == r2)
print(r3 == r2)

r1.name = "HAL3000"
r1.baujahr = "1968"

r2.name = "Marvin"
r2.baujahr = "1978"

print(r1.__dict__)
print(r2.__dict__)

r1.SetName("Gertrud7000")
r1.SetBaujahr("2042")

r1.SageHallo()
r1.GetName()

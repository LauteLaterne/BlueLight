#Erste Übungsaufgabe Kapitel 7.5

fahrzeug1 = dict(fahrzeugtyp="Oldtimer-Auto", hersteller="Ford", modell="Fiesta", Kaufjahr=1989, Preis=500, Farbe="rot")
fahrzeug2 = dict(fahrzeugtyp="Auto", hersteller="Skoda", modell="Octavia", Kaufjahr=2012, Preis=20200, Farbe="silbergrau")
fahrzeug3 = dict(fahrzeugtyp="Rennrad", hersteller="Canyon", modell="Ultimate SLX", Kaufjahr=2013, Preis=3300, Farbe="stealth")

# flotte=[fahrzeug1, fahrzeug2, fahrzeug3] --> nicht verwendet

print("\n", "Das ist die aktuelle Flotte:", "\n")
print("Fahrzeug 1:  TYP=", fahrzeug1["fahrzeugtyp"], ", Preis=", fahrzeug1["Preis"], "EUR")
print("Fahrzeug 2:  TYP=", fahrzeug2["fahrzeugtyp"], ", Preis=", fahrzeug2["Preis"], "EUR")
print("Fahrzeug 3:  TYP=", fahrzeug3["fahrzeugtyp"], ", Preis=", fahrzeug3["Preis"], "EUR", "\n")

maxpreis = eval(input("Gebe den maximalen Preis für DEIN Wunschfahrzeug in Euro ein: "))
print("\n", "Für den maximalen Preis von", maxpreis, "EUR suchen wir jetzt Dein Traumfahrzeug!", "\n")

if maxpreis >= fahrzeug1["Preis"]:
  print("ACHTUNG --> Dein Traumauto:  TYP=", fahrzeug1["fahrzeugtyp"], ", Preis=", fahrzeug1["Preis"], "EUR")
  
if maxpreis >= fahrzeug2["Preis"]:
  print("ACHTUNG --> Dein Traumauto:  TYP=", fahrzeug2["fahrzeugtyp"], ", Preis=", fahrzeug2["Preis"], "EUR")

if maxpreis >= fahrzeug3["Preis"]:
  print("ACHTUNG --> Dein Traumauto:  TYP=", fahrzeug3["fahrzeugtyp"], ", Preis=", fahrzeug3["Preis"], "EUR")
  
if (maxpreis < fahrzeug1["Preis"] and maxpreis < fahrzeug2["Preis"] and maxpreis < fahrzeug3["Preis"]):
   print("\n", "Für so WENIG Euro haben wir leider kein Fahrzeug für DICH!", "\n")

print ("\n", "CODE ENDE", "\n")
